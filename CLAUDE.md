# CLAUDE.md — kg-invest-wiki Schema (v7.0)

Operating manual for the LLM agent that maintains this wiki. **Read before touching `wiki/` or `raw/`.**

---

## 1. What This Wiki Is

A personal, position-agnostic investment knowledge base. Knowledge compounds from primary sources so every session starts from the latest synthesis, not a blank page.

**Owner**: Karthik G · **Started**: April 2026 · **Schema**: v7.0
**Lens**: a 5–10-year holder who wants the *business* to compound at a teens rate. The hurdle is **13%/yr total return on the probability-weighted case** (R8). Re-rating is upside, never the thesis; momentum, sentiment and technicals are context, never the reason to act.

**The deliverable is a decision, argued as a deep dive.** Each ticker has a long-form **deep dive**: an essay in the style of MBI Deep Dives that starts from the history, argues the debate that decides the stock from management's own words and the numbers, and ends in a verdict. It is built by the `kg-investment-analysis` skill (v7.0, `skills/kg-investment-analysis/`) from source files in `wiki/tickers/[TICKER]/report/` into **one Markdown file, `[TICKER].md`**. Its front matter states what to do about the stock, at what prices, and what would change that answer; the deep dive below it makes the argument. Everything in it either supports that decision or does not belong.

**Schema v7.0 is mandatory for all new work.** Every Workflow A ingest produces a v7 report. Every Workflow B update to a ticker that already has one adds an update note and rebuilds it.

**Migration is opportunistic, never bulk.** A v3/v5/v6 page migrates to v7 the next time a *material event* touches it: that update is done as a v7 full deep dive (Workflow A shape) instead of a page edit. Never run a mass migration, and never rewrite a page just to change its format. A quiet week migrates nothing. Mixed v3–v7 pages are the expected steady state for months; `git log` records which is which.

**Not**: a portfolio tracker (never records holdings) · position sizing of any kind (price-level *valuation* ranges are fine; tranche/allocation/%-of-portfolio are not) · invented numbers (every figure traces to a primary source or carries `[Estimate]` / `[Analyst consensus]` / `[Management guidance]` / `[Derived]`).

---

## 2. Directory Layout

```
rwh/
├── CLAUDE.md                  ← this file
├── README.md                  ← ticker table (§8)
├── skills/kg-investment-analysis/   ← the skill: SKILL.md, references/, scripts/, assets/, examples/
├── raw/[TICKER]/              ← immutable. NEVER modify. Store extracted text, not binaries.
│   ├── filings/ transcripts/ press-releases/
│   ├── shareholder-letters/ appearances/ investor-day/ analyst-reports/
│   └── ../clippings/          ← non-ticker-specific
└── wiki/
    ├── index.md               ← catalog (§8)
    ├── watchlist.md           ← attractiveness ranking (§8)
    ├── insights/              ← cross-ticker studies; pre-v7 standalone deep dives
    ├── tickers/[TICKER]/
    │   ├── [TICKER].md        ← the report: generated Markdown in v7 (front matter + deep dive), hand-written in v3–v6
    │   ├── changelog.md       ← append-only event log
    │   └── report/            ← v7 sources (report.md, data.json, model.json, model_out.json,
    │                             updates/, series/) and charts/*.svg referenced by [TICKER].md
    └── frameworks/            ← compounding.md, powers.md, bait.md, moneyball.md, asset-types.md, outsiders.md
```

---

## 3. Core Rules

**R1 — `raw/` is immutable.** Add, never edit. Store extracted `.txt`, not multi-MB PDFs; link the public URL for the original.

**R2 — Position-agnostic.** Analyze the company, not the owner's holdings. Recommendations split non-holder / holder only where they diverge.

**R3 — No sizing.** No tranche %, position %, allocation, or stock/options split, anywhere.

**R4 — Primary sources, verified.** SEC filings, earnings releases, IR pages, transcripts. Non-primary content carries a tag (R above). **Verify live price before any valuation work** — [Yahoo Finance](https://finance.yahoo.com/quote/) first, then CNBC / Google Finance / MarketWatch. Never trust a search snippet; click through. Same for any number that moves the decision.

**R5 — Every source is a real Markdown link.** `[Human-readable label](url-or-relative-path)`, pointing at the *specific* document. Relative path when stored locally, absolute when public. Unresolvable → append `[link pending]`. Never a bare `[Source: …]` tag.

**R6 — Date discipline.** Run `date -u +%Y-%m-%d` before writing any date-stamped artifact. Never infer today's date from context or file contents.

**R7 — State once.**
- Every fact has exactly one home in the deep dive. Elsewhere it is **referenced in a clause**, never re-explained. Canonical homes:
  - price, range, verdict, zones → `data.json` (rendered in the front matter);
  - the argument → The Call (`data.json`) and the debate chapters;
  - segment economics → Business Overview;
  - driver tree, five-year record with ROIC and quality rows, growth levers, moat table, risks, catalysts → the Appendix;
  - capital allocation, incentives, credibility, Outsider grade → Management, Capital Allocation and Incentives;
  - scenarios, PW EV, return decomposition, hurdle, R/R, Priced-in and Hurdle cases → Valuation;
  - sentiment, analysts, insiders, short interest → the update note or the Appendix.
- **Model numbers go through tokens.** Any figure the model produces is written as a `[[token]]` in prose, tables and the front matter, so it is stated once and cannot drift.
- **Quote where it earns its place.** Management's own words carry the debate chapters, at length where paraphrase would weaken them, always attributed to person, venue and date. Never a chronological table of source extracts where 2–3 sentences would do.
- **No schema mechanics in the report.** No references to this file, no "corrected from" / "prior framing" / "previously we said". Git is the audit trail.
- **Budget — a guardrail against sprawl, not a hard cap.** Prose only, excluding tables, block quotes, the Appendix and source lists:
  - **~4,000–7,000 words** for a full deep dive;
  - **600–1,200 words** for a Mode B update note, **200–500** for Mode C;
  - **~250 words** for a changelog entry.
  - The front matter is generated and has no budget of its own.
  - When a draft runs long, compress before deleting: collapse a restated claim to a reference, drop a second example, cut a quote that paraphrase would carry. Overshooting by 10–15% to keep load-bearing evidence is correct; cutting evidence to hit the number is not.
- **Closing audit, required**: scan the prose for any thesis-carrying *claim* — a figure, a rate, a named risk, a valuation multiple — appearing more than twice, and collapse the extras to a reference. Proper nouns are exempt. Then run `build_report.py --check`; it must be clean.

**R8 — Valuation: one 5-year forward lens, one hurdle.**
- Scenarios always use a 5-year terminal horizon; Bull/Base/Bear probabilities sum to 100%. Optionality that is not in the core business (a new segment, a stake, an unlaunched product) is **valued as its own line** — probability × value — so the core case can be read without it.
- **PW EV is the sole anchor, and its annualized total return is the gate.** `PW return/yr = (PW EV ÷ spot)^(1/5) − 1 + dividend yield`. **Initiate requires PW return/yr ≥ 13%.** Below it the non-holder verb is Watch (or Avoid), whatever the R/R says.
- **Entry derives from the hurdle, not from a margin-of-safety guess**: `Entry = PW EV ÷ (1 + 0.13 − yield)^5`. Trim = PW EV → Bull · Avoid = ≥ Bull.
- **Report the return in three parts** (→ [`compounding.md`](wiki/frameworks/compounding.md)): FCF- or EPS-per-share growth + shareholder yield (dividend + net buyback) ± multiple change. The first two are the **compounding rate at a flat multiple**; state it on its own line, and say plainly how much of the PW return is re-rating. A thesis whose return is mostly re-rating is a Watch, not an Initiate.
- **Price-implied expectations, one line**: what growth, for how long, does spot require at a stated discount rate. **Base-rate check, one line**: where the Bull growth rate sits in the reference class for this company's size (table in `compounding.md`). **Year-ten sentence**: is the business still growing at year ten, or is the terminal multiple doing the work.
- **One R/R figure**, cited identically everywhere: (Bull % upside) ÷ (Bear % downside) vs. spot.
- Analyst targets, rating changes, short interest, technical levels and 12–18-month re-rating math are *inputs to probabilities and context* (update notes and the Appendix). **None of them may be cited as the reason for a verb or a zone.**

**R9 — Management primary sources: letters *and* appearances.**
Management speaks off-script at conferences, on CNBC/Bloomberg, on podcasts, and discloses strategy and pricing detail that never reaches the press release.
- **Letters** — 5 fiscal years. Pattern A (standalone annual): 5. Pattern B (quarterly letters): 5× Q4 + 3 most recent, min 8. Pattern C (no standalone): chairman's letter in the annual report or DEF 14A; if neither exists, log the gap. Store as `shareholder-letters/YYYY_letter.txt` by fiscal year covered.
- **Appearances — sweep every ingest and every Workflow B window**, in order: (a) IR events/calendar page — also confirms *upcoming* appearances; (b) earnings-day CEO/CFO media hit, which routinely reframes the print; (c) podcasts / non-financial shows, where CEOs are least guarded; (d) conference transcripts. Fetch the transcript or a substantive write-up, never a headline. Store as `appearances/YYYY-MM-DD_<venue>_<who>.txt`.
- When an IR prepared-remarks PDF won't parse, cross-check **two independent transcripts plus one trade-press write-up** — secondary transcripts truncate, and pricing/product/partnership detail is what they drop.
- Attribute every quote to *where* it was said. An off-script claim carries different weight than a scripted one.
- **If a window genuinely had no appearances, say so.** An unstated absence is indistinguishable from an unchecked one.

**R10 — 10-K MD&A and Risk Factors are required.** Last 5 fiscal years on first ingest.

| 10-K Item | Lands in | Extract |
|---|---|---|
| 1 Business | Overview, debates, Appendix | Founding insight, segment definitions, unit of value, customer |
| **1A Risk Factors** | **Risks table (Appendix)** | Verbatim language for the highest-impact few; flag *new* vs. prior year |
| **7 MD&A** | **Overview, debates, Appendix** | Segment drivers, volume vs. price/mix, competitive dynamics, macro sensitivity |
| 7A Market Risk | Risks table | Quantified rate/FX/commodity sensitivities |
| 8 Statements & Notes | Appendix, Management | Segment data, invested capital, contingencies, debt, leases, share count |
| 15 / DEF 14A | Management (incentive table) | **Incentive metrics and weightings**, board, insider ownership |

EDGAR HTML > IR PDF > analyst summaries. The **[SEC XBRL company-facts API](https://data.sec.gov/api/xbrl/companyfacts/CIK[##########].json)** is the fastest reliable source for multi-year series, including the balance-sheet items that build invested capital — prefer it over parsing HTML tables. Workflow B diffs Item 1A year-over-year; new risks get a `[NEW in FY[N] 10-K]` tag.

**R11 — Risk materiality filter.** The risks table (Appendix) and the debate chapters cover risks material to the *decision*, not every Item 1A line.
- **Drop** boilerplate: "revenue could fluctuate", generic cyber, generic key-personnel, generic third-party reliance.
- **Keep** only risks meeting ≥1 test: (a) materially worse here than for peers; (b) **not priced in** — say so explicitly; (c) tied to a quantified thesis-break trigger the page commits to monitor; (d) tied to a specific large discretionary bet with an uncertain outcome.
- Multi-year risk evolution is 2–3 sentences of prose, never a table.

**R12 — Outsiders lens.** The Management chapter carries a one-line grade per [`outsiders.md`](wiki/frameworks/outsiders.md), anchored on countercyclical buyback discipline. Vocabulary: `Outsider · Outsider-leaning · Reinvestor · Steward (not Outsider) · Anti-Outsider`. One sentence of evidence. Surface it to the Verdict **only on a material capital-allocation event** (buyback authorization/execution, dividend init/raise/cut, M&A, large debt action). Keep the ticker's row in `outsiders.md` in sync.

**R13 — One report per ticker; changelog is the event log.** The folder holds `[TICKER].md`, `changelog.md` and, from v7, `report/`. Every material update writes a changelog entry stating:
- **Thesis Status** (Strengthened / Weakened / Unchanged);
- the **scorecard** (each prior "Wrong About" test resolved Pass / Fail / Pending, §13; in v7 the same scorecard is stored in `data.json` and rendered in the update note);
- an **action verb** (Initiate / Add / Hold / Trim / Exit / Watch / Avoid). *Trim* and *Reduce* are the same action; prefer *Trim*, matching the zone name.

Cross-ticker and schema-only events live in **commit messages**, not in any wiki file.

**R14 — Active / Paused.** Header carries `**Status**: Active` or `**Status**: Paused — since YYYY-MM-DD`. README, `index.md` and `watchlist.md` mirror it; Workflow B skips Paused entirely. Quiet ≠ paused: an Active quiet week still logs; a Paused ticker writes nothing.

**R15 — Style.** The deep dive follows `skills/kg-investment-analysis/references/deep-dive-style.md`: first person, plain words, concrete numbers, fair to management, no emoji in the essay. On the decision card and in changelogs, emoji carry meaning, never decoration: 🟢 bullish/add · 🔴 bearish/exit · 🟡 neutral/hold · ⚠️ material risk · ✅ resolved (pair with `~~strikethrough~~`) · 📅 dated catalyst · 💰 capital allocation · 🎯 price zone. **Bold** only punchlines and thesis-carrying numbers. Tables run time in columns, metrics in rows.

**R16 — Ground truth: the business is understood from the unit up.** *(see [`compounding.md`](wiki/frameworks/compounding.md) for the method; in v7 these tables live in the deep dive's Appendix and are argued in its chapters)*
- **Driver tree** — name the unit of value (a store, a subscriber, a trip, a case, a GWh, a policy), then build revenue and profit from it: units × revenue per unit × contribution per unit → segment profit → consolidated → per share. The unit and its per-unit metrics are fixed per asset type in [`asset-types.md`](wiki/frameworks/asset-types.md). Growth is split into *more units* and *more per unit*.
- **Reinvestment economics** — invested capital, ROIC, **incremental ROIC over three years**, reinvestment rate, and the organic growth those two imply (ROIIC × reinvestment rate). These rows are what a compounder thesis rests on; a page without them is not making one. Say how invested capital was built (equity + debt + leases − cash, or operating assets − operating liabilities) and tag it `[Derived]`.
- **Quality and survivability rows** — SBC as % of revenue, FCF conversion, net debt/EBITDA, interest coverage, nearest maturity wall. A decade-long hold must survive a recession; the page says whether it can.
- **Growth levers** — one table, fixed lever list: market growth · share gain · price and mix · attach / new products · new geographies · M&A · margin · share count. For each: current contribution, runway in years, evidence, management's stated intent, and stage (proven / scaling / option). Options are also valued in the Valuation chapter. Adjacency test (Zook): a new bet must share customers, costs or capabilities with the core, or it is diversification and is graded as such.
- **Customer block** — who buys, the job the product does, retention or repeat rate, the last price increase and what volume did, CAC and LTV where disclosed. Mauboussin's customer economics apply wherever the unit is a customer.
- **Moat mechanism and trend** — name the mechanism from the [7 Powers](wiki/frameworks/powers.md) vocabulary, call the trend (widening / stable / narrowing) with the evidence, and state who in the value chain captures the margin and whether that is shifting.
- **Incentives, credibility, promises** — one line on what the CEO is paid for (metrics and weights from the proxy), a guidance grade over the last eight to twelve quarters (`Consistent beater · Mixed · Misser`, with the one number that decides it), and a **promises ledger**: a three-row table of what letters or investor days three to five years back committed to, and what happened.

---

## 4. The Report

A v7 report is **one Markdown file, `[TICKER].md`**, built from the sources in `wiki/tickers/[TICKER]/report/` (GitHub-flavored Markdown, no HTML; charts are SVG images in `report/charts/`). Never hand-edit it; edit the sources and rebuild. In order:

1. **Front matter** (generated):
   - the header (schema, updated, status, verified price, 52-week range, type, stage, flags);
   - the Verdict (one sentence, two verbs, the one-row table `PW EV | PW return/yr | Compounding/yr | R/R | Entry | Trim | Avoid | multiple | Yield | BAIT | Moat | Next`, **Breaks if**);
   - The Call (~200 words);
   - What I'd Have To Be Wrong About (exactly three kill criteria with pre-committed, model-computed consequences);
   - the latest update with its scorecard, and links to earlier updates.
2. **Deep Dive: [title]**, chapters in order:
   1. an untitled opening (a dated moment, the stock against the business, the question);
   2. Business Overview;
   3. the key debate (management's narrative, then the holes, then an illustrative unit-economics table, then rings of profit);
   4. the second debate;
   5. Management, Capital Allocation and Incentives;
   6. Valuation and Model Assumptions;
   7. Final Words;
   8. Appendix: The Numbers;
   9. Sources.

The skill's `references/deep-dive-style.md` is authoritative for structure, devices, voice, charts and update notes. Its section 4 maps every required item (R8–R12, R16) to its home. Tests resolved in a window are scored in the update and the changelog, then replaced. An optional interactive page (`--html`) may be published for sharing; the Markdown file remains the report.

**Legacy pages** (v3–v6) keep their eight-section layout until their next material event (§1).

---

## 5. Frameworks

- **Compounding** — driver tree, ROIIC × reinvestment, return decomposition, hurdle-derived entry, price-implied expectations, growth-lever taxonomy, lifecycle stages, base-rate tables. → [`compounding.md`](wiki/frameworks/compounding.md)
- **7 Powers** (Helmer) — moat mechanism vocabulary, moat trend, profit-pool read, customer block. → [`powers.md`](wiki/frameworks/powers.md)
- **BAIT** (Mauboussin) — Behavioral / Analytical / Informational / Technical, each Strong / Moderate / Weak. Triple+ overlap = highest conviction. → [`bait.md`](wiki/frameworks/bait.md)
- **Moneyball** — 5-year terminal scenarios; PW EV per R8. → [`moneyball.md`](wiki/frameworks/moneyball.md)
- **Asset Types** — per-asset-class unit of value, per-unit metrics, valuation primary, and the ticker map. → [`asset-types.md`](wiki/frameworks/asset-types.md)
- **Outsiders** (Thorndike) — five tests, R12. → [`outsiders.md`](wiki/frameworks/outsiders.md)

---

## 6. Workflow A — First-Run Ingest (or v7 migration)

Trigger: *"ingest [TICKER]"* / *"add [TICKER]"* / *"build a page for [TICKER]"*, or the first material event on a pre-v7 page. If a v7 `report/` folder exists, switch to Workflow B.

1. **Verify the date** (R6) and **the live price** (R4).
2. **Fetch the raw set** into `raw/[TICKER]/`:
   - 5 annual 10-Ks;
   - the last 4 quarterly transcripts and press releases;
   - 12 months of 8-Ks;
   - the latest DEF 14A (incentive metrics are required, R16);
   - 5 years of letters (R9);
   - 12 months of appearances plus scheduled forward dates (R9);
   - the latest investor-day deck;
   - user-supplied PDFs.

   Log gaps; never fabricate. Store extracted text (R1).
3. **Pull the numbers**:
   - `scripts/xbrl.py` for the multi-year series and invested-capital components (R10, R16);
   - `scripts/prices.py` for the total-return charts;
   - the 52-week range, market cap, EV, net debt, leases, float, short interest, consensus, and 90 days of Form 4 XML.

   Classify the asset type from `asset-types.md`, adding a row if the type is new.
4. **Write the report** per the skill: grade before valuing, run the premortem, build `model.json` and run `model.py`, then write `report.md` + `data.json` in the deep-dive style (§4), applying R7–R12 and R16.
5. **Build and check**: `build_report.py report --check`, then build. This writes `[TICKER].md` and the chart SVGs. Read the result once and fix what you see. Write the `changelog.md` initial entry. Delete any legacy `overview.md` / `thesis.md` / `financials.md`.
6. **Run the closing audit** (R7).
7. **Update the cross-file layer** (§8), including the `index.md` Summary cell with its verb and fresh upside/downside pair, and the `Updated` date in the same edit. Then **commit and push** (§9).

## 7. Workflow B — Incremental Update

Trigger: *"weekly update"* / *"update [TICKER]"*.

1. **Baseline** — read `**Status**:`. Paused → skip entirely. Active → baseline is the latest changelog entry date; the lookback window is everything since.
2. **Scan** the Meaningful Events list (§11) across IR (including the events calendar), SEC EDGAR, the earnings calendar, the appearance sweep (R9), analyst actions, short interest, Form 4s, and news.
3. **Score the standing tests first.** Before touching the page, resolve each of the three "Wrong About" tests against the window's evidence — Pass / Fail / Pending — and record it in the changelog scorecard (§13). A failed test forces a scenario or verb change or an explicit sentence saying why not. Then write the replacement test.
4. **Material events, v7 ticker** → fetch new raw material, then:
   - write the **update note** (`report/updates/YYYY-MM-DD.md`, Mode B or C per the skill) and record its scorecard in `data.json`;
   - refresh the data that moved: new quarter rows in the tables, the Appendix five-year record when a fiscal year closes, `model.json` spot (and inputs only where evidence moved them) → `model.py`, plus `meta`, `verdict`, `call` and any replaced tests;
   - edit body prose the news made false, in place;
   - rebuild with `--check` and read the result once.

   **Material event on a pre-v7 page** → migrate: do the update as a v7 full deep dive (Workflow A steps 3–6), with the event as its first update note.

   Do not touch chapters the news did not touch. The key-debate and moat chapters rarely move on a single print.
5. **Quiet week** → write only a `[YYYY-MM-DD] — No Material Events` changelog entry with a price / short-interest / consensus snapshot. **Do not rebuild the report or modify `[TICKER].md`, and do not bump any dates.**
6. **Changelog** entry (~250 words, R7) recording what changed and why. Then §8: re-derive the `index.md` Summary against the new price and scenario set, since both the verb and the upside/downside pair move whenever the model or the price does. Then §9.

## 8. Cross-File Layer

Three files summarize the ticker set. **Each carries only what is unique to it** — the same sentence must not appear in two of them. All history lives in commit messages (R13), never as append-only prose.

| File | Carries | Hard cap |
|---|---|---|
| `README.md` | `Ticker \| Status \| Updated \| Punchline`, alphabetical; `*N tickers.*` counter below | **Punchline ≤ 30 words** — the verdict and the one number behind it |
| `wiki/index.md` | `Ticker \| Status \| Company \| Moat \| Conviction \| Updated \| Summary` + a price/BAIT/recommendation table + pending data gaps. **Summary format below.** | **Summary ≤ 40 words.** No "last refresh" narrative — a bare `*Last updated: YYYY-MM-DD*` line only |
| `wiki/watchlist.md` | Attractiveness ranking: `Rank \| Ticker \| Conviction \| BAIT \| PW EV vs. price \| Recommendation \| Next catalyst` + price-target table + earnings calendar + macro watch items. Active only; Paused in a footer | **Ranking cell ≤ 40 words.** No header changelog |

### The `index.md` Summary cell

The one place a reader can scan the whole book and see, per ticker, *what to do and what it is worth*. Three parts, in this order, ≤40 words total:

1. **The action verb**, leading — 🟢 Initiate / Add · 🟡 Hold / Watch · 🔴 Trim / Exit / Avoid. Where non-holder and holder diverge, give both (`Initiate / Hold-Add`).
2. **One or two lines on the opportunity** — what the setup is, in plain words. Not a metrics dump.
3. **Upside and downside**, always as a pair and always defined the same way:
   - **Upside** = **PW EV vs. spot** — what the probability-weighted case is worth from here.
   - **Downside** = **Bear case vs. spot** — what it costs if the thesis fails.
   - Write it as `PW EV $204: +49% up / −27% down`. Both legs come from the model's scenario set, so they always reconcile to the report's R/R (R8) without restating it.

**These percentages are point-in-time and go stale as the price moves.** That is expected and disclosed by the `Updated` column in the same row — which is why the two must never drift apart. Refresh the Summary, the percentages and the `Updated` date **in the same edit**, on every Workflow A ingest and every Workflow B incremental that touches the page. **A quiet week refreshes none of them** — it does not touch `[TICKER].md`, so the row keeps its old date and its old numbers, correctly labelled as of that date.

⚠️ **The v3 failure mode this replaces**: the same ~400-word block written three times, plus `index.md` accreting a single 4,000-word "last refresh" line. If a reader needs the full story, they open the ticker page. These three files are indexes, not summaries.

## 9. Commit & Push

`git commit` with a subject naming the ticker and the finding, then **`git push origin main` — always** (R13). Surface push failures to the user.

- Ingest: `INGEST [TICKER]: <headline finding>`
- Update: `WEEKLY YYYY-MM-DD: [N] events / [M] quiet — <headline>`
- Pause/resume: `PAUSE [TICKER]: <reason>` / `RESUME [TICKER]: catch-up over [N] days — <headline>`
- Schema: `SCHEMA: vX.Y — <what changed and why>`

The commit body is where rationale, migration history and cross-ticker context live.

## 10. Workflow C — Pause / Resume

**Pause** — verify Active, get the date (R6), set the header, append a changelog entry with the reason and last baseline, update the three cross-files (README/index Status → Paused, watchlist → Paused footer; do **not** bump Updated), commit `PAUSE`.

**Resume** — a multi-quarter pause spans earnings, analyst clusters and macro events; reconstruct them, don't just re-price. Scan the full window (all 10-Q/10-K, earnings and transcripts, 8-Ks, the full analyst-action record noting clusters, current short interest / insiders / consensus, plus management, M&A, regulatory and capital-allocation events). Apply the Workflow B refresh; the resume update note enumerates each earnings print in order before settling on the current state. Set Active, bump Updated, append a `## [date] — Resumed (Catch-Up)` entry, update cross-files, commit `RESUME`.

---

## 11. Meaningful Events

Earnings (10-Q/10-K, release, transcript) · annual shareholder letter · **material C-suite appearance** (R9 — material when it discloses strategy, pricing, product, partnership or competitive detail not in the filings, or reframes a print) · shareholder meeting and proxy outcomes (a changed incentive metric is material, R16) · strategic announcements (launch, market entry/exit, divestiture, restructuring) · M&A and JVs · capital allocation (buyback, dividend, debt, equity issuance) · a disclosed customer metric (retention, cohort, CAC, unit economics) · analyst rating changes (**a cluster of ≥3 firms in a week gets special attention**) · short interest >10% MoM or a sustained 3-week trend · insider Form 4 >$1M, any cluster, or a CEO/CFO sale into a decline · major regulatory action · material litigation · CEO/CFO/COO or board changes · credit rating actions.

Extensible — add types when encountered.

## 12. Data Sources

| Data | Primary | Fallback |
|---|---|---|
| Live price | [Yahoo Finance](https://finance.yahoo.com/quote/) | CNBC, Google Finance, MarketWatch |
| Filings | SEC EDGAR (HTML; `curl` with a UA header — `www.sec.gov` blocks undeclared tools, `data.sec.gov` does not; fall back to the web fetcher or the IR-hosted PDF) | Company IR |
| Multi-year financials, invested capital | **SEC XBRL company-facts API** (`scripts/xbrl.py`) | 10-K tables |
| Total-return price history (charts) | Yahoo chart API via `scripts/prices.py` (dividend-adjusted) | StockAnalysis history |
| Transcripts | IR prepared remarks, Motley Fool, Seeking Alpha | Investing.com, AlphaStreet, Benzinga — cross-check ≥2 (R9) |
| Appearances | IR events page, conference transcripts | CNBC/Bloomberg, podcast notes, trade press |
| Incentive design | **DEF 14A CD&A** | IR-hosted proxy PDF; log the gap if neither parses |
| Guidance history | Company releases (guide vs. delivered) | MarketBeat / StockAnalysis beat-miss tables `[Analyst consensus]` |
| Base rates | [`compounding.md`](wiki/frameworks/compounding.md) table (Mauboussin, Credit Suisse HOLT 1950–2015) | — |
| Analyst ratings | Research-firm releases | User PDFs in `analyst-reports/`, TipRanks, StockAnalysis |
| Short interest | Fintel, ChartExchange, NASDAQ | FINRA twice-monthly |
| Insiders | **SEC Form 4 XML direct** | OpenInsider, SecForm4 |
| Options | CBOE, Yahoo chain | Barchart |

## 13. changelog.md Format

Append-only, newest first. **Record what changed and why — never restate the thesis; the page carries that.**

```markdown
## [YYYY-MM-DD] — <Event type>

**Trigger**: <what caused this; link the primary source>
**Sources**: <files in raw/ or URLs>

### Scorecard
- <prior test 1, in a clause> — ✅ Pass / 🔴 Fail / 🟡 Pending — <the number that decided it>
- <prior test 2> — …
- <prior test 3> — …

### Changed
- <metric or thesis element — direction and magnitude, one bullet each>

### Status
- **Thesis**: Strengthened / Weakened / Unchanged
- **PW EV**: $X → $Y · **PW return/yr**: A% → B% (hurdle 13%) · **R/R**: A → B · **BAIT**: <delta if any>
- **Verbs**: non-holder <verb> · holder <verb>

**Next trigger**: <event or date>
```

Quiet week:

```markdown
## [YYYY-MM-DD] — No Material Events

**Window**: <baseline> → <today>
**Snapshot**: price $X (±Y%) · 52-wk %ile · short interest A% (±B% MoM) · consensus $C
**Dismissed**: <headlines scanned and why they don't matter>

**Recommendation**: Unchanged. **Next trigger**: <default or specific>.
```

## 14. Parallelization

- Workflow A fetch: optional fan-out of 3–4 agents split by source type; one synthesizer reads the aggregate.
- Weekly across N tickers: one agent per Active ticker, dispatched in a single message.
- **Within a ticker: single agent.** Valuation depends on the risks, which depend on the economics; chapter-level parallelism costs more in merge than it saves.
- **Never parallel-write** `README.md`, `index.md` or `watchlist.md`.
- Only spawn agents when the user asks for them.

## 15. Schema Co-Evolution

This file **does not grow by default.** R7 applies to it as much as to a ticker page.

1. **Find the home first.** Edit where the concept already lives. A new rule only when no home exists.
2. **Replace, don't append.** A change that adds lines deletes the lines it supersedes in the same commit.
3. **Rationale goes in the commit message**, never as residue in the text.
4. **Apply on next material touch** (§1). Never backfill untouched pages, and never bulk-migrate — git is the record.
5. **Consolidate when rules sprawl.** Bump the major version and rewrite rather than patch.

`git log --oneline CLAUDE.md` · `git log -p CLAUDE.md` · `git blame CLAUDE.md`
