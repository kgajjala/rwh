#!/usr/bin/env python3
"""Segment model for the deep-dive report (kg-investment-analysis v7).

Usage:  python3 -I model.py report/model.json  [report/model_out.json]

Reads a model spec (see assets/model.example.json), projects each case from the base
year to the terminal year, and writes model_out.json with:
  - per-case rows (segment revenue, margin, operating profit; corporate; totals; EPS)
  - per-case terminal value and annual return  (value/spot)^(1/years) - 1 + yield
  - PW EV, PW return, hurdle-derived entry, R/R, break-even and price-implied Bear odds
  - diagnostic cases solved by bisection: the inputs that return exactly a target rate
    (e.g. "Priced-in" at the discount rate, "Hurdle" at 13%) at a fixed exit multiple.
Standard library only.
"""
import json, sys, copy

def project(spec, case):
    b = spec["base"]; segs = list(b["segments"].keys())
    years = list(range(b["year"], spec["last_year"] + 1)); n = len(years) - 1
    rows = {"year": years, "seg": {s: {"rev": [], "margin": [], "op": []} for s in segs},
            "corp": [], "rev": [], "op": [], "opm": [], "ni": [], "shares": [], "eps": []}
    rev = {s: b["segments"][s]["rev"] for s in segs}
    shares = b["shares"]; other = b.get("other", 0.0)
    corp0 = b.get("corp_pct", 0.0); corp1 = case.get("corp_pct", corp0)
    tax0 = b.get("tax", 0.21); tax1 = case.get("tax", tax0)
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
            shares *= 1 + case.get("share_change", 0.0)
            other *= 1 + spec.get("other_growth", 0.0)
        tax = tax0 + (tax1 - tax0) * f
        ni = (op + other) * (1 - tax)
        for k, v in (("corp", corp), ("rev", tot), ("op", op), ("opm", op / tot), ("ni", ni), ("shares", shares), ("eps", ni / shares)):
            rows[k].append(v)
    return rows

def evaluate(spec, case):
    r = project(spec, case)
    yrs = spec["last_year"] - spec["base"]["year"]
    value = r["eps"][-1] * case["pe"]
    spot = spec["spot"]; yld = spec.get("dps", 0.0) / spot
    ret = (value / spot) ** (1 / yrs) - 1 + yld
    cagr = (r["eps"][-1] / r["eps"][0]) ** (1 / yrs) - 1
    return r, value, ret, cagr

def interp(a, b, lam):
    out = copy.deepcopy(a)
    for s in a["segments"]:
        for k in ("g", "m"):
            out["segments"][s][k] = a["segments"][s][k] + (b["segments"][s][k] - a["segments"][s][k]) * lam
    for k in ("corp_pct", "share_change", "tax"):
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
                              "prob": c.get("prob"), "role": c.get("role")}
        if c.get("role"): roles[c["role"]] = name
    for name, d in spec.get("diagnostics", {}).items():
        res = solve(spec, d)
        if res is None:
            out["diagnostics"][name] = {"error": "target return not reachable along the path", **d}; continue
        lam, c = res
        r, v, ret, cagr = evaluate(spec, c)
        out["diagnostics"][name] = {"rows": r, "value": v, "return": ret, "eps_cagr": cagr, "inputs": c,
                                    "lambda": lam, "target_return": d["target_return"], "pe": d["pe"], "path": d["path"],
                                    "label": d.get("label", name)}
    probs = [(n, c["prob"]) for n, c in out["cases"].items() if c["prob"]]
    tp = sum(p for _, p in probs)
    if probs and abs(tp - 1) > 1e-6:
        sys.exit(f"probabilities sum to {tp:.3f}, not 1")
    if probs:
        pw = sum(out["cases"][n]["value"] * p for n, p in probs)
        pw_ret = (pw / spot) ** (1 / yrs) - 1 + yld
        entry = pw / (1 + h - yld) ** yrs
        s = {"pw_ev": pw, "pw_return": pw_ret, "entry": entry, "hurdle": h, "discount_rate": r_disc,
             "trim_low": pw}
        if {"bull", "base", "bear"} <= set(roles):
            bu, ba, be = (out["cases"][roles[k]] for k in ("bull", "base", "bear"))
            s["trim_high"] = bu["value"]; s["avoid"] = bu["value"]
            s["rr"] = (bu["value"] / spot - 1) / (1 - be["value"] / spot) if be["value"] < spot else None
            pb, pa = bu["prob"], ba["prob"]
            vnb = (pb * bu["value"] + pa * ba["value"]) / (pb + pa)
            def odds(rate):
                need = spot * (1 + rate - yld) ** yrs
                if vnb == be["value"]: return None
                return (vnb - need) / (vnb - be["value"])
            s["breakeven_bear"] = odds(h); s["implied_bear"] = odds(r_disc); s["vnb"] = vnb
            s["bear_prob"] = be["prob"]
        out["summary"] = s
    json.dump(out, open(dst, "w"), indent=1)
    for n, c in out["cases"].items():
        print(f"{n:22s} EPS {c['rows']['eps'][0]:.2f} → {c['rows']['eps'][-1]:.2f} ({c['eps_cagr']:+.1%}/yr)  value {c['value']:.1f}  return {c['return']:.1%}")
    for n, d in out["diagnostics"].items():
        if "error" in d: print(f"{n:22s} {d['error']}"); continue
        print(f"{n:22s} EPS → {d['rows']['eps'][-1]:.2f} ({d['eps_cagr']:+.1%}/yr) at {d['pe']}×  value {d['value']:.1f}  return {d['return']:.1%}  λ={d['lambda']:.2f}")
    if "summary" in out:
        s = out["summary"]; fmt = lambda x: "n/a" if x is None else (">100%" if x > 1 else "<0%" if x < 0 else f"{x:.0%}")
        print(f"PW EV {s['pw_ev']:.1f}  PW return {s['pw_return']:.1%}  entry {s['entry']:.1f}  R/R {s.get('rr') or 0:.1f}  "
              f"break-even Bear {fmt(s.get('breakeven_bear'))}  price-implied Bear {fmt(s.get('implied_bear'))}")

if __name__ == "__main__":
    main()
