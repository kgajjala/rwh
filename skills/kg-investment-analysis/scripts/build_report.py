#!/usr/bin/env python3
"""Build the v7 report: one Markdown file = decision front matter + deep dive (kg-investment-analysis v7).

Usage:  python3 -I build_report.py REPORT_DIR [--check] [--html]

REPORT_DIR holds:
  report.md        the essay: Markdown plus directives on their own line (below)
  data.json        meta, verdict, call, tests, updates, tables, charts, sources, vars
  model_out.json   written by model.py
  updates/*.md     dated update notes (Modes B/C), listed in data.json "updates"
  series/*.json    total-return series written by prices.py
Writes:
  the report at meta.report_path (default ../TICKER.md): header, Verdict, The Call, the three
  tests, the latest update with its scorecard, then the deep dive and its appendix, in
  GitHub-flavored Markdown with no HTML;
  charts as static SVG images in REPORT_DIR/charts/, referenced from the Markdown;
  --html  also writes an optional interactive page (TICKER-deep-dive.html) for publishing.

Directives (one per line):
  ::toc                      contents line linking the ## chapters (GitHub heading anchors)
  ::updates                  placeholder; the latest update renders in the front matter
  ::tests                    a pointer to the tests in the front matter
  ::table ID                 data.json tables[ID] as a GFM table, with its note
  ::chart ID                 data.json charts[ID] (type "line" or "bar100") as an SVG image plus a data table
  ::model_build CASE         segment build table for one model case (bold cells are inputs)
  ::scenarios                scenario and diagnostic table from model_out.json
  ::sources                  data.json "sources"
  ::disclaimer               placeholder; the fixed footer closes the file
Tokens: [[name]] in prose, tables, notes, tests and the call are filled from the model and
data.json "vars": price, yield, pw_ev, pw_return, entry, rr, trim, avoid, breakeven_bear,
implied_bear, hurdle, "<Case>.value|return|eps|eps0|cagr|pe|prob",
"<Diagnostic>.value|eps|cagr|pe|return", "testN.pw_ev|pw_return|entry|verb" (from a test's "shift").
--check  reports unresolved tokens and missing ids, and exits non-zero if any.
Standard library only.
"""
import json, os, re, sys, glob, html

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "assets", "page.html")
PROBLEMS = []

# ---------- formatting ----------
def pct(x, d=1): return "n/a" if x is None else f"{x*100:.{d}f}%"
def odds(x): return "n/a" if x is None else (">100%" if x > 1 else "<0%" if x < 0 else f"{x*100:.0f}%")
def money(x, d=0): return f"${x:,.{d}f}"

def build_vars(data, mo):
    v = {}
    m = data["meta"]
    v["price"] = money(m["price"], 2); v["ticker"] = m["ticker"]; v["company"] = m["company"]
    if mo:
        v["yield"] = pct(mo["yield"]); s = mo.get("summary", {})
        if s:
            v.update({"pw_ev": money(s["pw_ev"]), "pw_return": pct(s["pw_return"]), "entry": money(s["entry"]),
                      "hurdle": pct(s["hurdle"], 0), "rr": "n/m" if s.get("rr") is None else f"{s['rr']:.1f}:1",
                      "breakeven_bear": odds(s.get("breakeven_bear")), "implied_bear": odds(s.get("implied_bear")),
                      "trim": f"{money(s['pw_ev'])}–{money(s['trim_high'])}" if s.get("trim_high") else "—",
                      "avoid": f"≥{money(s['avoid'])}" if s.get("avoid") else "—"})
        for group in ("cases", "diagnostics"):
            for name, c in mo.get(group, {}).items():
                if "rows" not in c: continue
                v[f"{name}.value"] = money(c["value"]); v[f"{name}.return"] = pct(c["return"])
                v[f"{name}.eps"] = money(c["rows"]["eps"][-1], 2); v[f"{name}.eps0"] = money(c["rows"]["eps"][0], 2)
                v[f"{name}.cagr"] = pct(c["eps_cagr"]); v[f"{name}.pe"] = f"{c['inputs']['pe']:.1f}×".replace(".0×", "×")
                if c.get("prob"): v[f"{name}.prob"] = pct(c["prob"], 0)
    if mo and mo.get("summary"):
        s = mo["summary"]; yrs = mo["years"]; spot = mo["spot"]; y = mo["yield"]
        for i, t in enumerate(data.get("tests", []), 1):
            sh = t.get("shift")
            if not sh: continue
            vals = {n: c["value"] for n, c in mo["cases"].items()}
            probs = {n: c["prob"] for n, c in mo["cases"].items() if c.get("prob")}
            if "from" in sh:
                probs[sh["from"]] -= sh["points"]; probs[sh["to"]] += sh["points"]
            if "value" in sh: vals[sh["case"]] = sh["value"]
            if "eps" in sh: vals[sh["case"]] = sh["eps"] * mo["cases"][sh["case"]]["inputs"]["pe"]
            pw = sum(vals[n] * p for n, p in probs.items())
            ret = (pw / spot) ** (1 / yrs) - 1 + y; ent = pw / (1 + s["hurdle"] - y) ** yrs
            v[f"test{i}.pw_ev"] = money(pw); v[f"test{i}.pw_return"] = pct(ret); v[f"test{i}.entry"] = money(ent)
            v[f"test{i}.verb"] = "Initiate" if ret >= s["hurdle"] and spot <= ent else "Watch"
    v.update({k: str(x) for k, x in data.get("vars", {}).items()})
    return v

def subst(s, V):
    def r(mt):
        k = mt.group(1).strip()
        if k in V: return V[k]
        PROBLEMS.append(f"unresolved token [[{k}]]"); return mt.group(0)
    return re.sub(r"\[\[([^\]]+)\]\]", r, s)

# ---------- minimal Markdown ----------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"~~(.+?)~~", r"<s>\1</s>", s)
    return s

def md_blocks(text, render_directive):
    out = []; para = []; lines = text.split("\n"); i = 0
    def flush():
        if para: out.append("<p>" + inline(" ".join(x.strip() for x in para)) + "</p>"); para.clear()
    while i < len(lines):
        ln = lines[i]; st = ln.strip()
        if not st: flush(); i += 1; continue
        if st.startswith("<!--"):
            flush()
            while i < len(lines) and "-->" not in lines[i]: i += 1
            i += 1; continue
        if st.startswith("::"):
            flush(); out.append(render_directive(st[2:].strip())); i += 1; continue
        m = re.match(r"^(#{1,3})\s+(.*?)(?:\s*\{#([\w-]+)\})?\s*$", st)
        if m:
            flush(); lvl = len(m.group(1)); ident = f' id="{m.group(3)}"' if m.group(3) else ""
            out.append(f"<h{lvl}{ident}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if st.startswith(">"):
            flush(); q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip()); i += 1
            cite = ""
            if q and (q[-1].startswith("— ") or q[-1].startswith("-- ")):
                cite = f"<cite>{inline(q.pop()[2:].strip())}</cite>"
            body = "".join(f"<p>{inline(p)}</p>" for p in q if p.strip())
            out.append(f"<blockquote>{body}{cite}</blockquote>"); continue
        if re.match(r"^(-|\*|\d+\.)\s+", st):
            flush(); ordered = bool(re.match(r"^\d+\.", st)); items = []
            while i < len(lines) and re.match(r"^\s*(-|\*|\d+\.)\s+", lines[i]):
                items.append(re.sub(r"^\s*(-|\*|\d+\.)\s+", "", lines[i])); i += 1
                while i < len(lines) and lines[i].startswith("   ") and lines[i].strip() and not re.match(r"^\s*(-|\*|\d+\.)\s+", lines[i]):
                    items[-1] += " " + lines[i].strip(); i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>"); continue
        para.append(ln); i += 1
    flush()
    return "\n".join(out)

# ---------- tables ----------
def cell(c):
    if isinstance(c, dict):
        cls = f' class="{c["cls"]}"' if c.get("cls") else ""
        return f"<td{cls}>{inline(str(c.get('v','')))}</td>"
    return f"<td>{inline(str(c))}</td>"

def table_html(t):
    cols = t["columns"]
    head = "<thead><tr>" + "".join(
        f'<th class="wrap">{inline(c[1:])}</th>' if str(c).startswith("~") else f"<th>{inline(str(c))}</th>" for c in cols) + "</tr></thead>"
    body = []
    for r in t["rows"]:
        if isinstance(r, dict): cells, cls = r["cells"], r.get("cls", "")
        else: cells, cls = r, ""
        wraps = [str(c).startswith("~") for c in cols]
        tds = []
        for j, c in enumerate(cells):
            if j < len(wraps) and wraps[j] and not isinstance(c, dict): c = {"v": c, "cls": "wrap"}
            tds.append(cell(c))
        body.append((f'<tr class="{cls}">' if cls else "<tr>") + "".join(tds) + "</tr>")
    return f'<table>{head}<tbody>{"".join(body)}</tbody></table>'

def figure(inner, note):
    n = f'<p class="note">{inline(note)}</p>' if note else ""
    return f'<div class="wide">{inner}{n}</div>'

# ---------- model tables ----------
def model_build(mo, case):
    c = mo["cases"].get(case) or mo["diagnostics"].get(case)
    if not c: PROBLEMS.append(f"model case {case} missing"); return ""
    r = c["rows"]; inp = c["inputs"]; fy = mo.get("fy_prefix", "FY"); names = mo.get("segment_names", {})
    years = [f"{fy}{y}E" for y in r["year"]]
    act = mo.get("actual")
    cols = ["$ Billion"] + ([f"{fy}{act['year']}A"] if act else []) + years
    pc = lambda x: pct(x)
    rows = []
    def g(l, i): return l[i] / l[i - 1] - 1
    for s in mo["segments"]:
        seg = r["seg"][s]; a = act["segments"].get(s) if act else None
        lab = names.get(s, s)
        rows.append({"cells": [f"**{lab} revenue**"] + ([f"{a['rev']:.1f}"] if a else []) + [f"{v:.1f}" for v in seg["rev"]], "cls": "grp"})
        rows.append({"cells": ["YoY growth"] + (["—"] if a else []) + [pc(g(seg["rev"], 1)) if a is None else pc(seg["rev"][0] / a["rev"] - 1)]
                     + [{"v": pc(g(seg["rev"], i)), "cls": "in"} for i in range(1, len(seg["rev"]))], "cls": "sub"})
        rows.append({"cells": ["Operating margin"] + ([pc(a["op"] / a["rev"])] if a else [])
                     + [({"v": pc(m), "cls": "in"} if i == len(seg["margin"]) - 1 else pc(m)) for i, m in enumerate(seg["margin"])], "cls": "sub"})
        rows.append({"cells": ["Operating profit"] + ([f"{a['op']:.2f}"] if a else []) + [f"{v:.2f}" for v in seg["op"]], "cls": "sub"})
    if act and "corp" in act: corp_a = [f"({-act['corp']:.2f})"]
    else: corp_a = ["—"] if act else []
    rows.append(["Corporate and other"] + corp_a + [f"({-v:.2f})" for v in r["corp"]])
    tot_a = sum(x["rev"] for x in act["segments"].values()) if act else None
    op_a = (sum(x["op"] for x in act["segments"].values()) + act.get("corp", 0)) if act else None
    rows.append({"cells": ["Total revenue"] + ([f"{tot_a:.1f}"] if act else []) + [f"{v:.1f}" for v in r["rev"]], "cls": "tot"})
    rows.append({"cells": ["Operating profit"] + ([f"{op_a:.2f}"] if act else []) + [f"{v:.2f}" for v in r["op"]], "cls": "tot"})
    rows.append({"cells": ["Operating margin"] + ([pc(op_a / tot_a)] if act else []) + [pc(v) for v in r["opm"]], "cls": "sub"})
    rows.append(["Net income"] + ([f"{act['ni']:.2f}"] if act and "ni" in act else (["—"] if act else [])) + [f"{v:.2f}" for v in r["ni"]])
    rows.append(["Diluted shares (B)"] + ([f"{act['shares']:.3f}"] if act and "shares" in act else (["—"] if act else [])) + [f"{v:.3f}" for v in r["shares"]])
    lab = mo.get("eps_label", "EPS")
    rows.append({"cells": [lab] + ([money(act["eps"], 2)] if act and "eps" in act else (["—"] if act else [])) + [money(v, 2) for v in r["eps"]], "cls": "tot"})
    rows.append({"cells": ["YoY growth"] + ([ "—"] if act else []) + [(pc(r["eps"][0] / act["eps"] - 1) if act and "eps" in act else "—")] + [pc(g(r["eps"], i)) for i in range(1, len(r["eps"]))], "cls": "sub"})
    return {"columns": cols, "rows": rows}

def scenarios(mo, spec):
    cols = ["Case", "Prob."] + [f"{mo.get('segment_names', {}).get(s, s)} growth / margin" for s in spec.get("segments_shown", mo["segments"])] + \
           [f"{mo.get('eps_label','EPS')} {mo.get('fy_prefix','FY')}{mo['cases'][next(iter(mo['cases']))]['rows']['year'][-1]}", "EPS CAGR", "Exit P/E", "Value", "Return/yr"]
    rows = []
    order = list(mo["cases"].items()) + [(k, v) for k, v in mo["diagnostics"].items() if "rows" in v]
    for name, c in order:
        inp = c["inputs"]; label = c.get("label", name)
        rows.append([f"**{label}**", pct(c["prob"], 0) if c.get("prob") else "—"] +
                    [f"{inp['segments'][s]['g']*100:+.1f}% / {inp['segments'][s]['m']*100:.1f}%" for s in spec.get("segments_shown", mo["segments"])] +
                    [money(c["rows"]["eps"][-1], 2), pct(c["eps_cagr"]), f"{inp['pe']:.1f}×", money(c["value"]), pct(c["return"])])
    s = mo.get("summary")
    if s:
        rows.append({"cells": ["Probability-weighted", "100%"] + [""] * len(spec.get("segments_shown", mo["segments"])) + ["", "", "", money(s["pw_ev"]), pct(s["pw_return"])], "cls": "tot"})
    return {"columns": cols, "rows": rows}

# ---------- page pieces ----------
def header(data, V):
    m = data["meta"]; vd = data["verdict"]
    kick = [f"Deep Dive · {m['ticker']}", m["date_long"], f"Price {V['price']} ({m['price_note']})"]
    tiles = vd.get("tiles") or [
        {"label": "Verdict", "value": vd["non_holder"]["verb"]},
        {"label": "Entry for 13%/yr", "value": "≤ [[entry]]"},
        {"label": f"PW value ({m.get('terminal_label','5-yr')})", "value": "[[pw_ev]]"},
        {"label": "PW return/yr", "value": "[[pw_return]]"},
        {"label": "Price implies", "value": vd.get("price_implies", "—")},
        {"label": "Next", "value": vd.get("next", "—")}]
    t = "".join(f'<div><b>{inline(subst(x["label"],V))}</b><span>{inline(subst(x["value"],V))}</span></div>' for x in tiles)
    return (f'<header class="mast"><div class="kicker">{"".join(f"<span>{inline(k)}</span>" for k in kick)}</div>'
            f'<h1>{inline(m["title"])}</h1><p class="dek">{inline(subst(m["dek"],V))}</p><div class="verdict">{t}</div></header>')

def render_updates(data, rdir, V):
    ups = sorted(data.get("updates", []), key=lambda u: u["date"], reverse=True)
    if not ups: return ""
    parts = []
    for k, u in enumerate(ups):
        p = os.path.join(rdir, u["file"])
        if not os.path.exists(p): PROBLEMS.append(f"update file missing: {u['file']}"); continue
        body = md_blocks(subst(open(p).read(), V), lambda d: "")
        sc = ""
        if u.get("scorecard"):
            sc = '<ul class="score">' + "".join(
                f'<li><span class="res {x["result"]}">{ {"pass":"✅ Pass","fail":"🔴 Fail","pending":"🟡 Pending"}[x["result"]] }</span>'
                f'<span>{inline(subst(x["test"],V))} — {inline(subst(x["evidence"],V))}</span></li>' for x in u["scorecard"]) + "</ul>"
        inner = f'<div class="when">Update · {u["date"]}</div><h3>{inline(u["title"])}</h3>{sc}{body}'
        if k == 0: parts.append(f'<section class="update" id="latest-update">{inner}</section>')
        else: parts.append(f'<details class="older"><summary>Earlier update · {u["date"]} · {inline(u["title"])}</summary>{inner}</details>')
    return parts[0] + (f'<div class="update">{"".join(parts[1:])}</div>' if len(parts) > 1 else "")

def build_html(rdir, data, mo, V):
    raw = re.sub(r"<!--.*?-->", "", open(os.path.join(rdir, "report.md")).read(), flags=re.S)
    text = subst(raw, V)
    charts = {}
    heads = re.findall(r"^##\s+(.*?)\s*\{#([\w-]+)\}\s*$", text, flags=re.M)
    def directive(d):
        parts = d.split(None, 1); name = parts[0]; arg = parts[1].strip() if len(parts) > 1 else ""
        if name == "toc":
            return '<nav class="toc" aria-label="Sections">' + "".join(f'<a href="#{i}">{inline(re.sub(r"[*_]","",h))}</a>' for h, i in heads) + "</nav>"
        if name == "updates": return render_updates(data, rdir, V)
        if name == "tests":
            return '<ol class="tests">' + "".join(
                f'<li><strong>{inline(subst(t["claim"],V))}</strong> Test: {inline(subst(t["test"],V))} <strong>If Fail →</strong> {inline(subst(t["if_fail"],V))}</li>'
                for t in data["tests"]) + "</ol>"
        if name == "table":
            t = data["tables"].get(arg)
            if not t: PROBLEMS.append(f"table {arg} missing"); return ""
            t = json.loads(subst(json.dumps(t, ensure_ascii=False), V))
            return figure(f'<div class="frame">{table_html(t)}</div>', t.get("note"))
        if name == "chart":
            c = data["charts"].get(arg)
            if not c: PROBLEMS.append(f"chart {arg} missing"); return ""
            c = dict(c)
            if "file" in c:
                f = json.load(open(os.path.join(rdir, c["file"])))
                for k in ("dates", "order", "names", "series"): c.setdefault(k, f[k])
                if "names" in data["charts"][arg]: c["names"] = {**f["names"], **data["charts"][arg]["names"]}
            charts[arg] = {k: v for k, v in c.items() if k not in ("note", "aria", "file")}
            return (f'<div class="wide" data-chart="{arg}"><div class="legend"></div>'
                    f'<div class="chart" role="img" aria-label="{html.escape(c.get("aria", arg))}"></div>'
                    f'<p class="note">{inline(subst(c.get("note",""),V))}</p>'
                    f'<details><summary>Show the numbers</summary><div class="frame"><table></table></div></details></div>')
        if name == "model_build":
            if not mo: PROBLEMS.append("model_out.json missing"); return ""
            mb = data.get("model_build", {})
            return figure(f'<div class="frame">{table_html(model_build(mo, arg))}</div>', subst(mb.get("note", ""), V))
        if name == "scenarios":
            if not mo: PROBLEMS.append("model_out.json missing"); return ""
            sc = data.get("scenarios", {})
            return figure(f'<div class="frame">{table_html(scenarios(mo, sc))}</div>', subst(sc.get("note", ""), V))
        if name == "sources":
            return '<p class="sources">' + " · ".join(f'<a href="{s["url"]}">{inline(s["label"])}</a>' if s.get("url") else inline(s["label"]) for s in data.get("sources", [])) + "</p>"
        if name == "disclaimer":
            return ('<p class="disclaimer">This is analysis, not personal investment advice, and it does not size positions. Figures trace to the filings, '
                    'releases and transcripts linked in the text, or are labelled as estimates. The model is a simplified segment build and its assumptions are judgments. '
                    f'Prices as of {inline(data["meta"]["price_note"])}. Charts and tables built with Claude from the sources cited.</p>')
        PROBLEMS.append(f"unknown directive ::{name}"); return ""
    body = md_blocks(text, directive)
    m = data["meta"]
    page = open(TEMPLATE).read()
    acc = m.get("accent", {"light": "#1a4f9e", "dark": "#86b6ef"})
    page = (page.replace("{{TITLE}}", html.escape(m["title"])).replace("{{ACCENT_LIGHT}}", acc["light"]).replace("{{ACCENT_DARK}}", acc["dark"])
                .replace("{{HEADER}}", header(data, V)).replace("{{BODY}}", body)
                .replace("{{CHARTS_JSON}}", json.dumps(charts, separators=(",", ":"), ensure_ascii=False)))
    out = os.path.join(rdir, m.get("html_name", f"{m['ticker']}-deep-dive.html"))
    open(out, "w").write(page)
    print(f"wrote optional HTML page {out} ({os.path.getsize(out)//1024} KB)")


# =====================================================================================
# Markdown report (the v7 output): one [TICKER].md = decision front matter + deep dive
# =====================================================================================
SLOT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]   # reference categorical palette, fixed order
INK2 = "#6f6e69"; GRID = "#8a8a8a"; FONT = "system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

def gh_slug(text):
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    s = re.sub(r"[*_`~]", "", s).strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.U)
    return s.replace(" ", "-")

def md_cell(c, cls_row=""):
    v = str(c.get("v", "")) if isinstance(c, dict) else str(c)
    cls = c.get("cls", "") if isinstance(c, dict) else ""
    if "in" in cls.split() and v and not v.startswith("**"): v = f"**{v}**"
    return v.replace("|", "\\|").replace("\n", " ")

def md_table(t):
    cols = [str(c)[1:] if str(c).startswith("~") else str(c) for c in t["columns"]]
    L = ["| " + " | ".join(c.replace("|", "\\|") for c in cols) + " |", "|" + "---|" * len(cols)]
    for r in t["rows"]:
        cells, cls = (r["cells"], r.get("cls", "")) if isinstance(r, dict) else (r, "")
        out = [md_cell(c) for c in cells]
        if cls == "sub" and out: out[0] = "\u2003" + out[0]
        if cls == "tot" and out and not out[0].startswith("**"): out[0] = f"**{out[0]}**"
        out += [""] * (len(cols) - len(out))
        L.append("| " + " | ".join(out) + " |")
    return "\n".join(L)

def md_note(n): return f"\n\n*{n.strip()}*" if n and n.strip() else ""

def esc_x(s): return html.escape(str(s), quote=True)

def nice_ticks(lo, hi, n=6):
    import math
    span = (hi - lo) or 1; raw = span / n; mag = 10 ** math.floor(math.log10(raw))
    step = next((s * mag for s in (1, 2, 2.5, 5, 10) if span / (s * mag) <= n), 10 * mag)
    v = math.floor(lo / step) * step; out = []
    while v <= hi + 1e-9: out.append(round(v, 2)); v += step
    if out[-1] < hi: out.append(round(out[-1] + step, 2))
    return out

def svg_line(c):
    W, H = 760, 380; m = dict(l=48, r=120, t=46, b=34)
    D = c["dates"]; n = len(D); order = c["order"]; S = c["series"]; names = c.get("names", {})
    allv = [v for k in order for v in S[k]] + ([c["baseline"]] if c.get("baseline") is not None else [])
    ticks = c.get("yTicks") or nice_ticks(min(allv), max(allv))
    if min(allv) < ticks[0] or max(allv) > ticks[-1]:            # data outside the requested ticks: widen to fit
        ticks = nice_ticks(min(min(allv), ticks[0]), max(max(allv), ticks[-1]))
    lo, hi = ticks[0], ticks[-1]
    X = lambda i: m["l"] + (W - m["l"] - m["r"]) * i / (n - 1)
    Y = lambda v: m["t"] + (H - m["t"] - m["b"]) * (1 - (v - lo) / (hi - lo))
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}" font-size="12">']
    if c.get("title"): o.append(f'<title>{esc_x(c["title"])}</title>')
    o.append(f'<defs><clipPath id="plot"><rect x="{m["l"]}" y="{m["t"]-6}" width="{W-m["l"]-m["r"]+6}" height="{H-m["t"]-m["b"]+12}"/></clipPath></defs>')
    x0 = m["l"]
    for i, k in enumerate(order):                                    # legend row
        o.append(f'<rect x="{x0}" y="12" width="14" height="3" rx="1.5" fill="{SLOT[i]}"/>')
        o.append(f'<text x="{x0+20}" y="17" fill="{INK2}">{esc_x(names.get(k, k))}</text>')
        x0 += 28 + 7.2 * len(names.get(k, k))
    for v in ticks:
        base = c.get("baseline") is not None and abs(v - c["baseline"]) < 1e-9
        o.append(f'<line x1="{m["l"]}" x2="{W-m["r"]}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{GRID}" stroke-opacity="{0.6 if base else 0.25}" stroke-width="1"/>')
        o.append(f'<text x="{m["l"]-8}" y="{Y(v)+4:.1f}" text-anchor="end" fill="{INK2}">{v:g}</text>')
    seen = set(); yrs = sorted({d[:4] for d in D}); step = 2 if len(yrs) > 9 else 1
    for i, d in enumerate(D):
        yr = d[:4]
        if i == 0:
            o.append(f'<text x="{X(0):.1f}" y="{H-10}" text-anchor="start" fill="{INK2}">{esc_x(d[:7])}</text>'); seen.add(yr); continue
        if yr not in seen and int(yr) % step == 0 and X(i) > X(0) + 60 and X(i) < W - m["r"] - 16:
            o.append(f'<text x="{X(i):.1f}" y="{H-10}" text-anchor="middle" fill="{INK2}">{yr}</text>')
        seen.add(yr)
    ends = []
    for i, k in enumerate(order):
        pts = " ".join(f"{X(j):.1f},{Y(v):.1f}" for j, v in enumerate(S[k]))
        o.append(f'<polyline clip-path="url(#plot)" points="{pts}" fill="none" stroke="{SLOT[i]}" stroke-width="{2.5 if i == 0 else 2}" stroke-linejoin="round" stroke-linecap="round"/>')
        o.append(f'<circle cx="{X(n-1):.1f}" cy="{Y(S[k][-1]):.1f}" r="4" fill="{SLOT[i]}"/>')
        ends.append([Y(S[k][-1]), k, S[k][-1]])
    ends.sort()
    for j in range(1, len(ends)):
        if ends[j][0] - ends[j-1][0] < 15: ends[j][0] = ends[j-1][0] + 15
    for y, k, v in ends:
        o.append(f'<text x="{X(n-1)+9:.1f}" y="{y+4:.1f}" fill="{INK2}">{esc_x(names.get(k, k))} {v:.0f}</text>')
    o.append("</svg>")
    return "\n".join(o)

def svg_bar100(c):
    W = 760; rowH, gap = 24, 18; m = dict(l=96, r=12, t=40, b=26)
    H = m["t"] + len(c["rows"]) * rowH + (len(c["rows"]) - 1) * gap + m["b"]
    X = lambda f: m["l"] + (W - m["l"] - m["r"]) * f
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}" font-size="12">']
    x0 = m["l"]
    for i, k in enumerate(c["keys"]):
        o.append(f'<rect x="{x0}" y="10" width="12" height="12" rx="3" fill="{SLOT[i]}"/>')
        o.append(f'<text x="{x0+18}" y="20" fill="{INK2}">{esc_x(k)}</text>'); x0 += 30 + 7.2 * len(k)
    for f in (0, .25, .5, .75, 1):
        o.append(f'<line x1="{X(f):.1f}" x2="{X(f):.1f}" y1="{m["t"]-4}" y2="{H-m["b"]}" stroke="{GRID}" stroke-opacity="0.25"/>')
        anc = "start" if f == 0 else "end" if f == 1 else "middle"
        o.append(f'<text x="{X(f):.1f}" y="{H-8}" text-anchor="{anc}" fill="{INK2}">{int(f*100)}%</text>')
    for ri, r in enumerate(c["rows"]):
        tot = sum(r["values"]); y = m["t"] + ri * (rowH + gap); acc = 0
        o.append(f'<text x="{m["l"]-10}" y="{y+rowH/2+4:.1f}" text-anchor="end" fill="{INK2}">{esc_x(r["label"])}</text>')
        for i, v in enumerate(r["values"]):
            a, b = X(acc / tot) + (1 if i else 0), X((acc + v) / tot) - (1 if i < len(r["values"]) - 1 else 0); acc += v
            o.append(f'<rect x="{a:.1f}" y="{y}" width="{max(0.5,b-a):.1f}" height="{rowH}" fill="{SLOT[i]}"/>')
            if b - a > 44:
                tc = "#ffffff" if i < 2 else "#1a1a19"
                o.append(f'<text x="{(a+b)/2:.1f}" y="{y+rowH/2+4:.1f}" text-anchor="middle" fill="{tc}" font-weight="600">{v/tot*100:.0f}%</text>')
    o.append("</svg>")
    return "\n".join(o)

def chart_md(arg, c, rdir, rel_report, V):
    os.makedirs(os.path.join(rdir, "charts"), exist_ok=True)
    svg = svg_line(c) if c["type"] == "line" else svg_bar100(c)
    open(os.path.join(rdir, "charts", f"{arg}.svg"), "w").write(svg)
    alt = c.get("aria", arg).replace("[", "(").replace("]", ")")
    out = f"![{alt}]({rel_report}/charts/{arg}.svg)" + md_note(subst(c.get("note", ""), V))
    if c["type"] == "line":                                           # compact data table under the chart
        D = c["dates"]; n = len(D); k = max(1, round(n / 6)); idx = sorted(set(list(range(0, n, k)) + [n - 1]))
        t = {"columns": ["Date"] + [c.get("names", {}).get(s, s) for s in c["order"]],
             "rows": [[D[i]] + [f"{c['series'][s][i]:.0f}" for s in c["order"]] for i in idx]}
    else:
        t = {"columns": ["Period"] + c["keys"] + [f"Total{(' (' + c['unit'] + ')') if c.get('unit') else ''}"],
             "rows": [[r["label"]] + [f"{v:,.0f} ({v/sum(r['values'])*100:.0f}%)" for v in r["values"]] + [f"{sum(r['values']):,.0f}"] for r in c["rows"]]}
    return out + "\n\n" + md_table(t)

def load_chart(data, rdir, arg):
    c = data["charts"].get(arg)
    if not c: PROBLEMS.append(f"chart {arg} missing"); return None
    c = dict(c)
    if "file" in c:
        f = json.load(open(os.path.join(rdir, c["file"])))
        for k in ("dates", "order", "series"): c.setdefault(k, f[k])
        c["names"] = {**f.get("names", {}), **data["charts"][arg].get("names", {})}
    return c

def essay_md(data, mo, V, rdir, rel_report):
    raw = re.sub(r"<!--.*?-->", "", open(os.path.join(rdir, "report.md")).read(), flags=re.S)
    text = subst(raw, V)
    heads = [h for h in re.findall(r"^##\s+(.*?)(?:\s*\{#[\w-]+\})?\s*$", text, flags=re.M)]
    out = []
    for ln in text.split("\n"):
        st = ln.strip()
        hm = re.match(r"^(#{1,3})\s+(.*?)(?:\s*\{#[\w-]+\})?\s*$", st)
        if hm:                                                        # demote one level under "## Deep Dive"
            out.append("#" * (len(hm.group(1)) + 1) + " " + hm.group(2)); continue
        if not st.startswith("::"): out.append(ln); continue
        parts = st[2:].split(None, 1); name = parts[0]; arg = parts[1].strip() if len(parts) > 1 else ""
        if name == "toc":
            out.append("**Contents**: " + " · ".join(f"[{re.sub(r'[*_]','',h)}](#{gh_slug(h)})" for h in heads))
        elif name in ("updates", "disclaimer"):
            pass                                                      # updates sit in the front matter; footer is fixed
        elif name == "tests":
            out.append("*The three tests, with their pre-committed consequences, are listed at the top of this report under [What I'd Have To Be Wrong About](#what-id-have-to-be-wrong-about).*")
        elif name == "table":
            t = data["tables"].get(arg)
            if not t: PROBLEMS.append(f"table {arg} missing"); continue
            t = json.loads(subst(json.dumps(t, ensure_ascii=False), V))
            out.append(md_table(t) + md_note(t.get("note")))
        elif name == "chart":
            c = load_chart(data, rdir, arg)
            if c: out.append(chart_md(arg, c, rdir, rel_report, V))
        elif name == "model_build":
            if not mo: PROBLEMS.append("model_out.json missing"); continue
            out.append(md_table(model_build(mo, arg)) + md_note(subst(data.get("model_build", {}).get("note", ""), V) + " Bold cells are model inputs."))
        elif name == "scenarios":
            if not mo: PROBLEMS.append("model_out.json missing"); continue
            sc = data.get("scenarios", {})
            out.append(md_table(scenarios(mo, sc)) + md_note(subst(sc.get("note", ""), V)))
        elif name == "sources":
            out.append(" · ".join(f"[{s['label']}]({s['url']})" if s.get("url") else s["label"] for s in data.get("sources", [])))
        else:
            PROBLEMS.append(f"unknown directive ::{name}")
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()

def front_matter(data, mo, V, rdir, rel_report):
    m = data["meta"]; vd = data["verdict"]; s = (mo or {}).get("summary", {})
    lo, hi = m["range52"]; pctl = round((m["price"] - lo) / (hi - lo) * 100) if hi > lo else 0
    ordn = lambda n: f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n % 10,'th')}"
    chg = (m["price"] / hi - 1) * 100; chg_s = f"{'+' if chg >= 0 else '−'}{abs(chg):.1f}%"
    flags = f" · **Cyclical** {m['cyclical']} · **Competence** {m['competence']}" + (" · 🔁 **High-ROIIC compounder** (no Trim zone)" if m.get("compounder") else "")
    pub = f" · [published page]({m['artifact_url']})" if m.get("artifact_url") else ""
    L = [f"# {m['ticker']} — {m['company']}", "",
         f"> **Schema** v7.0 · **Updated** {m['date']} · **Status** {m.get('status','Active')}",
         f"> **Price** {V['price']} verified {m['price_note']} ([Yahoo]({m.get('price_url','https://finance.yahoo.com/quote/'+m['ticker']+'/')})) · 52-wk ${lo:,.2f}–${hi:,.2f} · {ordn(pctl)} %ile · {chg_s} from high",
         f"> **Type** {m['type']} · **Stage** {m['stage']}{flags}{pub}", "",
         "## Verdict", "", f"**{subst(vd['sentence'],V)}**", "",
         f"{vd['non_holder']['emoji']} **Non-holder: {subst(vd['non_holder']['verb'],V)}** · {vd['holder']['emoji']} **Holder: {subst(vd['holder']['verb'],V)}**", "",
         f"| PW EV | PW return/yr | Compounding/yr | R/R | Entry | Trim | Avoid | {vd['multiple_label']} | Yield | BAIT | Moat | Next |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|",
         f"| **{V.get('pw_ev','—')}** | **{V.get('pw_return','—')} ({'≥' if s and s['pw_return']>=s['hurdle'] else '<'}13%)** | {subst(vd.get('compounding','—'),V)} | {V.get('rr','—')} | ≤{V.get('entry','—')} | "
         f"{'—' if m.get('compounder') else V.get('trim','—')} | {V.get('avoid','—')} | {subst(vd['multiple'],V)} | {V.get('yield','—')} | {vd['bait']} | {vd['moat']} | 📅 {vd['next']} |", "",
         f"**Breaks if**: {subst(vd['breaks_if'],V)}", "",
         "## The Call", "", subst(data["call"], V).strip(), "",
         "## What I'd Have To Be Wrong About", ""]
    for i, t in enumerate(data["tests"], 1):
        L.append(f"{i}. **{subst(t['claim'],V)}** Test: {subst(t['test'],V)} **If Fail →** {subst(t['if_fail'],V)}")
    ups = sorted(data.get("updates", []), key=lambda u: u["date"], reverse=True)
    if ups:
        u = ups[0]; p = os.path.join(rdir, u["file"])
        L += ["", f"## Latest update: {u['date']} · {u['title']}", ""]
        if u.get("scorecard"):
            icon = {"pass": "✅ Pass", "fail": "🔴 Fail", "pending": "🟡 Pending"}
            L += [f"- {subst(x['test'],V)} — {icon[x['result']]} — {subst(x['evidence'],V)}" for x in u["scorecard"]] + [""]
        if os.path.exists(p): L.append(subst(re.sub(r"<!--.*?-->", "", open(p).read(), flags=re.S), V).strip())
        else: PROBLEMS.append(f"update file missing: {u['file']}")
        if len(ups) > 1:
            L += ["", "**Earlier updates**: " + " · ".join(f"[{x['date']} · {x['title']}]({rel_report}/{x['file']})" for x in ups[1:])]
    return "\n".join(L)

def build(rdir, check=False, want_html=False):
    data = json.load(open(os.path.join(rdir, "data.json")))
    mo_p = os.path.join(rdir, "model_out.json"); mo = json.load(open(mo_p)) if os.path.exists(mo_p) else None
    V = build_vars(data, mo); m = data["meta"]
    out = os.path.normpath(os.path.join(rdir, m.get("report_path", m.get("card_path", f"../{m['ticker']}.md"))))
    rel_report = os.path.relpath(os.path.abspath(rdir), os.path.dirname(os.path.abspath(out)))
    fm = front_matter(data, mo, V, rdir, rel_report)
    essay = essay_md(data, mo, V, rdir, rel_report)
    doc = (fm + "\n\n---\n\n" + f"## Deep Dive: {m['title']}\n\n*{subst(m['dek'],V)}*\n\n" + essay +
           "\n\n---\n\n*Analysis, not personal investment advice. Every figure traces to a linked primary source or carries a tag "
           "([Estimate], [Analyst consensus], [Management guidance], [Derived]). No position sizing by design. Built from "
           f"[{rel_report}/]({rel_report}/) by kg-investment-analysis v7; edit the sources there, not this file.*\n")
    if check:
        for p in PROBLEMS: print("PROBLEM:", p)
        sys.exit(1 if PROBLEMS else 0)
    for p in PROBLEMS: print("PROBLEM:", p)
    open(out, "w").write(doc)
    prose = re.sub(r"^\|.*\|$", "", essay, flags=re.M)
    print(f"wrote {out} (~{len(prose.split())} words of essay prose excl. tables; {len(doc.split())} words total)")
    if want_html:
        build_html(rdir, data, mo, V)

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    build(a[0], check="--check" in sys.argv, want_html="--html" in sys.argv)
