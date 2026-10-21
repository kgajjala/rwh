#!/usr/bin/env python3
"""Segment model for the deep-dive report (kg-investment-analysis v7).

Usage:  python3 -I model.py report/model.json  [report/model_out.json]

Reads a model spec (see assets/model.example.json), projects each case from the base
year to the terminal year, and writes model_out.json with:
  - per-case rows (segment revenue, margin, operating profit; corporate; totals; EPS)
  - per-case terminal value and annual return  (value/spot)^(1/years) - 1 + yield
  - PW EV, PW return, hurdle-derived entry, R/R, break-even and price-implied Bear odds
  - diagnostic cases solved by bisection: the inputs that return exactly a target rate
    (e.g. "Priced-in" at the discount rate, "Hurdle" at 13%) at a fixed exit multiple
  - owner earnings per share (SBC treated as a real cost), net share change from gross
    dilution and buybacks, implied perpetual growth per case (terminal-growth check against
    the risk-free rate), optionality lines added to PW EV, compounding at a flat multiple and
    the re-rating share, and the probability-fragile flag.
Spec keys (all optional unless noted): base.sbc_pct (SBC % of revenue), base.eps_excludes_sbc,
base.oe_conversion (owner earnings ÷ net income before the SBC adjustment, default 1.0);
case.sbc_pct (terminal), case.dilution and case.buyback (% of shares per year; net change =
dilution − buyback, else case.share_change), case.basis ("eps" or "owner": which per-share
figure the exit multiple applies to), case.value_override (for P/TBV or sum-of-the-parts
values computed outside the engine), case.story, case.tier; spec.risk_free; spec.optionality
[{"name","prob","value"}].
Standard library only.
"""
import json, sys, copy

def project(spec, case):
    b = spec["base"]; segs = list(b["segments"].keys())
    years = list(range(b["year"], spec["last_year"] + 1)); n = len(years) - 1
    rows = {"year": years, "seg": {s: {"rev": [], "margin": [], "op": []} for s in segs},
            "corp": [], "rev": [], "op": [], "opm": [], "ni": [], "shares": [], "eps": [],
            "sbc": [], "owner_ni": [], "owner_eps": [], "share_change": []}
    rev = {s: b["segments"][s]["rev"] for s in segs}
    shares = b["shares"]; other = b.get("other", 0.0)
    corp0 = b.get("corp_pct", 0.0); corp1 = case.get("corp_pct", corp0)
    tax0 = b.get("tax", 0.21); tax1 = case.get("tax", tax0)
    sbc0 = b.get("sbc_pct", 0.0); sbc1 = case.get("sbc_pct", sbc0); conv = b.get("oe_conversion", 1.0)
    excl = b.get("eps_excludes_sbc", False)
    if "dilution" in case or "buyback" in case:
        net_change = case.get("dilution", 0.0) - case.get("buyback", 0.0)
    else:
        net_change = case.get("share_change", 0.0)
    for i, y in enumerate(years):
        f = 0 if n == 0 else i / n
        tot = 0.0; op = 0.0
        for s in segs:
            if i > 0:
                rev[s] *= 1 + case["segments"][s]["g"]
            m0 = b["segments"][s]["margin"]; m1 = case["segments"][s]["m"]
            m = m0 + (m1 - m0) * f
            o = rev[s] * m
            rows["seg"][s]["rev"].append(rev[s]); rows["seg"][s]["margin"].append(m); rows["seg"][s]["op"].append(o)
            tot += rev[s]; op += o
        cp = corp0 + (corp1 - corp0) * f
        corp = -cp * tot; op += corp
        if i > 0:
            shares *= 1 + net_change
            other *= 1 + spec.get("other_growth", 0.0)
        tax = tax0 + (tax1 - tax0) * f
        ni = (op + other) * (1 - tax)
        sbc = (sbc0 + (sbc1 - sbc0) * f) * tot
        owner_ni = ni * conv - (sbc * (1 - tax) if excl else 0.0)   # SBC is a real cost: deduct it when EPS excludes it
        for k, v in (("corp", corp), ("rev", tot), ("op", op), ("opm", op / tot), ("ni", ni), ("shares", shares), ("eps", ni / shares),
                     ("sbc", sbc), ("owner_ni", owner_ni), ("owner_eps", owner_ni / shares), ("share_change", 0.0 if i == 0 else net_change)):
            rows[k].append(v)
    return rows

def evaluate(spec, case):
    r = project(spec, case)
    yrs = spec["last_year"] - spec["base"]["year"]
    per = r["owner_eps"] if case.get("basis") == "owner" else r["eps"]
    value = case["value_override"] if "value_override" in case else per[-1] * case["pe"]
    spot = spec["spot"]; yld = spec.get("dps", 0.0) / spot
    ret = (value / spot) ** (1 / yrs) - 1 + yld
    cagr = (per[-1] / per[0]) ** (1 / yrs) - 1 if per[0] > 0 and per[-1] > 0 else None
    return r, value, ret, cagr

def implied_g(spec, value, owner_eps_terminal):
    """Terminal-growth check (valuation.md section 3): g = (M·r − 1) ÷ (M + 1), M = value ÷ owner EPS."""
    if owner_eps_terminal <= 0: return None
    M = value / owner_eps_terminal; r = spec.get("discount_rate", 0.09)
    return (M * r - 1) / (M + 1)

def interp(a, b, lam):
    out = copy.deepcopy(a)
    for s in a["segments"]:
        for k in ("g", "m"):
            out["segments"][s][k] = a["segments"][s][k] + (b["segments"][s][k] - a["segments"][s][k]) * lam
    for k in ("corp_pct", "share_change", "tax", "sbc_pct", "dilution", "buyback"):
        if k in a or k in b:
            va = a.get(k, b.get(k, 0.0)); vb = b.get(k, a.get(k, 0.0))
            out[k] = va + (vb - va) * lam
    return out

def solve(spec, d):
    a = spec["cases"][d["path"][0]]; b = spec["cases"][d["path"][1]]
    def ret_at(lam):
        c = interp(a, b, lam); c["pe"] = d["pe"]
        return evaluate(spec, c)[2], c
    lo, hi = -2.0, 4.0
    rlo, _ = ret_at(lo); rhi, _ = ret_at(hi)
    if not (rlo <= d["target_return"] <= rhi):
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if ret_at(mid)[0] < d["target_return"]: lo = mid
        else: hi = mid
    lam = (lo + hi) / 2
    return lam, ret_at(lam)[1]

def main():
    src = sys.argv[1]; dst = sys.argv[2] if len(sys.argv) > 2 else src.replace("model.json", "model_out.json")
    spec = json.load(open(src))
    spot = spec["spot"]; yld = spec.get("dps", 0.0) / spot
    yrs = spec["last_year"] - spec["base"]["year"]
    h = spec.get("hurdle", 0.13); r_disc = spec.get("discount_rate", 0.09)
    out = {"spot": spot, "yield": yld, "years": yrs, "segments": list(spec["base"]["segments"].keys()),
           "segment_names": spec.get("segment_names", {}), "eps_label": spec.get("eps_label", "EPS"),
           "fy_prefix": spec.get("fy_prefix", "FY"), "actual": spec.get("actual"), "cases": {}, "diagnostics": {}}
    roles = {}
    for name, c in spec["cases"].items():
        r, v, ret, cagr = evaluate(spec, c)
        out["cases"][name] = {"rows": r, "value": v, "return": ret, "eps_cagr": cagr, "inputs": c,
                              "prob": c.get("prob"), "role": c.get("role"), "story": c.get("story"), "tier": c.get("tier"),
                              "basis": c.get("basis", "eps"), "implied_g": implied_g(spec, v, r["owner_eps"][-1])}
        if c.get("role"): roles[c["role"]] = name
    for name, d in spec.get("diagnostics", {}).items():
        res = solve(spec, d)
        if res is None:
            out["diagnostics"][name] = {"error": "target return not reachable along the path", **d}; continue
        lam, c = res
        r, v, ret, cagr = evaluate(spec, c)
        out["diagnostics"][name] = {"rows": r, "value": v, "return": ret, "eps_cagr": cagr, "inputs": c,
                                    "implied_g": implied_g(spec, v, r["owner_eps"][-1]), "basis": c.get("basis", "eps"),
                                    "lambda": lam, "target_return": d["target_return"], "pe": d["pe"], "path": d["path"],
                                    "label": d.get("label", name)}
    probs = [(n, c["prob"]) for n, c in out["cases"].items() if c["prob"]]
    tp = sum(p for _, p in probs)
    if probs and abs(tp - 1) > 1e-6:
        sys.exit(f"probabilities sum to {tp:.3f}, not 1")
    if probs:
        core_pw = sum(out["cases"][n]["value"] * p for n, p in probs)
        opts = spec.get("optionality", [])
        opt_value = sum(o["prob"] * o["value"] for o in opts)
        pw = core_pw + opt_value
        pw_ret = (pw / spot) ** (1 / yrs) - 1 + yld
        entry = pw / (1 + h - yld) ** yrs
        s = {"pw_ev": pw, "pw_return": pw_ret, "entry": entry, "hurdle": h, "discount_rate": r_disc,
             "trim_low": pw, "core_pw_ev": core_pw, "optionality": opts, "optionality_value": opt_value,
             "risk_free": spec.get("risk_free")}
        g_flags = [n for n, c in out["cases"].items() if c["implied_g"] is not None and spec.get("risk_free") is not None and c["implied_g"] > spec["risk_free"]]
        s["g_above_risk_free"] = g_flags
        if {"bull", "base", "bear"} <= set(roles):
            bu, ba, be = (out["cases"][roles[k]] for k in ("bull", "base", "bear"))
            s["trim_high"] = bu["value"]; s["avoid"] = bu["value"]
            s["rr"] = (bu["value"] / spot - 1) / (1 - be["value"] / spot) if be["value"] < spot < bu["value"] else None
            pb, pa = bu["prob"], ba["prob"]
            vnb = (pb * bu["value"] + pa * ba["value"]) / (pb + pa)
            def odds(rate):
                need = spot * (1 + rate - yld) ** yrs
                if vnb == be["value"]: return None
                return (vnb - need) / (vnb - be["value"])
            s["breakeven_bear"] = odds(h); s["implied_bear"] = odds(r_disc); s["vnb"] = vnb
            s["bear_prob"] = be["prob"]
            s["fragile"] = s["breakeven_bear"] is not None and abs(s["breakeven_bear"] - be["prob"]) <= 0.10
            if ba["eps_cagr"] is not None:
                comp = ba["eps_cagr"] + yld
                s["compounding"] = comp                                  # per-share growth (buybacks inside it) + dividend yield
                s["rerating"] = ba["return"] - comp                      # what the Base gets from the multiple moving
                s["rerating_share"] = (s["rerating"] / ba["return"]) if ba["return"] else None
        out["summary"] = s
    json.dump(out, open(dst, "w"), indent=1)
    for n, c in out["cases"].items():
        g = "n/a" if c["implied_g"] is None else f"{c['implied_g']:.1%}"
        cg = "n/a" if c["eps_cagr"] is None else f"{c['eps_cagr']:+.1%}"
        print(f"{n:22s} EPS {c['rows']['eps'][0]:.2f} → {c['rows']['eps'][-1]:.2f}, owner EPS → {c['rows']['owner_eps'][-1]:.2f} ({cg}/yr on {c['basis']})  value {c['value']:.1f}  return {c['return']:.1%}  implied g {g}")
    for n, d in out["diagnostics"].items():
        if "error" in d: print(f"{n:22s} {d['error']}"); continue
        cg = "n/a" if d["eps_cagr"] is None else f"{d['eps_cagr']:+.1%}"
        print(f"{n:22s} EPS → {d['rows']['eps'][-1]:.2f} ({cg}/yr) at {d['pe']}×  value {d['value']:.1f}  return {d['return']:.1%}  λ={d['lambda']:.2f}")
    if "summary" in out:
        s = out["summary"]; fmt = lambda x: "n/a" if x is None else (">100%" if x > 1 else "<0%" if x < 0 else f"{x:.0%}")
        print(f"PW EV {s['pw_ev']:.1f}  PW return {s['pw_return']:.1%}  entry {s['entry']:.1f}  R/R {('n/m' if s.get('rr') is None else format(s['rr'], '.1f'))}  "
              f"break-even Bear {fmt(s.get('breakeven_bear'))}  price-implied Bear {fmt(s.get('implied_bear'))}")
        if s.get("compounding") is not None:
            print(f"Compounding at a flat multiple {s['compounding']:.1%}; re-rating {s['rerating']:+.1%} of the Base return"
                  + (f" ({s['rerating_share']:.0%})" if s.get('rerating_share') is not None else ""))
        if s.get("optionality_value"): print(f"Optionality adds {s['optionality_value']:.1f} to PW EV (core {s['core_pw_ev']:.1f})")
        if s.get("fragile"): print("PROBABILITY-FRAGILE: break-even Bear odds within 10 points of the assigned Bear probability")
        if s.get("g_above_risk_free"): print("TERMINAL-GROWTH FLAG: implied perpetual growth above the risk-free rate in", s["g_above_risk_free"])

if __name__ == "__main__":
    main()
