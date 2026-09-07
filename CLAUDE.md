# CLAUDE.md — kg-invest-wiki Schema (v5.0)

Operating manual for the LLM agent that maintains this wiki. **Read before touching `wiki/` or `raw/`.**

---

## 1. What This Wiki Is

A personal, position-agnostic investment knowledge base. Knowledge compounds from primary sources so every session starts from the latest synthesis, not a blank page.

**Owner**: Karthik G · **Started**: April 2026 · **Schema**: v5.0
**Lens**: a 5–10-year holder who wants the *business* to compound at a teens rate. The hurdle is **13%/yr total return on the probability-weighted case** (R8). Re-rating is upside, never the thesis; momentum, sentiment and technicals are context, never the reason to act.

**The deliverable is a decision.** `wiki/tickers/[TICKER]/[TICKER].md` answers one question — *what should someone do about this stock, and what would change that answer* — and is kept current in place. Everything on the page either supports that decision or does not belong.

**Schema v5.0 is mandatory for all new work.** Every Workflow A ingest and every Workflow B incremental — including a single post-earnings update to a page still written in v3 or v4 — produces the v5 page shape in §4. There is no older path; if you are writing to a page, you are writing v5.

**Migration is opportunistic, never bulk.** An older page migrates to v5 the next time a material event touches it, as part of that update — one page at a time, paid for by work you were doing anyway. Never run a mass migration, and never rewrite a page just to change its format. A quiet week does not migrate a page (it does not touch `[TICKER].md` at all). Until a page is touched, its older layout stands and is correct. Mixed v3/v4/v5 pages are the expected steady state for months; `git log` is the record of which is which.

**Not**: a portfolio tracker (never records holdings) · position sizing of any kind (price-level *valuation* ranges are fine; tranche/allocation/%-of-portfolio are not) · invented numbers (every figure traces to a primary source or carries `[Estimate]` / `[Analyst consensus]` / `[Management guidance]` / `[Derived]`).

---

## 2. Directory Layout

```
rwh/
├── CLAUDE.md                  ← this file
├── README.md                  ← ticker table (§8)
├── raw/[TICKER]/              ← immutable. NEVER modify. Store extracted text, not binaries.
│   ├── filings/ transcripts/ press-releases/
│   ├── shareholder-letters/ appearances/ investor-day/ analyst-reports/
│   └── ../clippings/          ← non-ticker-specific
└── wiki/
    ├── index.md               ← catalog (§8)
    ├── watchlist.md           ← attractiveness ranking (§8)
    ├── tickers/[TICKER]/
    │   ├── [TICKER].md        ← the deliverable
    │   └── changelog.md       ← append-only event log
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
- Every fact has exactly one home. Elsewhere it is **referenced in a clause**, never re-explained. Canonical homes: price/range → header · driver tree, ROIC, quality rows → §1 · growth levers and runway → §2 · moat mechanism, trend, customer → §3 · capital allocation, incentives, credibility, Outsider grade → §4 · multiples, scenarios, PW EV, return decomposition, hurdle, R/R → §5 · sentiment, analysts, insiders, short interest → §7 · the argument → The Call.
- **Synthesis, not transcription.** A verbatim quote must earn its place — use one only where paraphrase would weaken it. Never a chronological table of source extracts where 2–3 sentences would do.
- **No schema mechanics on the page.** No references to this file, no "corrected from" / "prior framing" / "previously we said". Git is the audit trail.
- **Budget: ≤1,500 words of prose** for a full page, **≤250 words** for a changelog entry — both measured on prose only, **excluding tables and source lists** (a page's Sources section, a changelog's Trigger/Sources block). Citing sources properly must never cost you budget. The v5 additions (driver tree, growth levers, promises ledger, return decomposition) are **tables and one-line fields by design** so that depth does not cost prose. Below ~1,200 a page starts losing the evidence that makes its argument credible; below ~250 a changelog starts dropping metrics a later reader needs. A table with one meaningful row is a sentence.
- **Closing audit, required**: scan for any thesis-carrying *claim* — a figure, a rate, a named risk, a valuation multiple — appearing more than twice, and collapse the extras to a reference. Proper nouns are exempt: naming an initiative, a segment or a person in three places is not duplication, **restating what it proves is**.

**R8 — Valuation: one 5-year forward lens, one hurdle.**
- §5 scenarios always use a 5-year terminal horizon; Bull/Base/Bear probabilities sum to 100%. Optionality that is not in the core business (a new segment, a stake, an unlaunched product) is **valued as its own line** — probability × value — so the core case can be read without it.
- **PW EV is the sole anchor, and its annualized total return is the gate.** `PW return/yr = (PW EV ÷ spot)^(1/5) − 1 + dividend yield`. **Initiate requires PW return/yr ≥ 13%.** Below it the non-holder verb is Watch (or Avoid), whatever the R/R says.
- **Entry derives from the hurdle, not from a margin-of-safety guess**: `Entry = PW EV ÷ (1 + 0.13 − yield)^5`. Trim = PW EV → Bull · Avoid = ≥ Bull.
- **Report the return in three parts** (→ [`compounding.md`](wiki/frameworks/compounding.md)): FCF- or EPS-per-share growth + shareholder yield (dividend + net buyback) ± multiple change. The first two are the **compounding rate at a flat multiple**; state it on its own line, and say plainly how much of the PW return is re-rating. A thesis whose return is mostly re-rating is a Watch, not an Initiate.
- **Price-implied expectations, one line**: what growth, for how long, does spot require at a stated discount rate. **Base-rate check, one line**: where the Bull growth rate sits in the reference class for this company's size (table in `compounding.md`). **Year-ten sentence**: is the business still growing at year ten, or is the terminal multiple doing the work.
- **One R/R figure**, cited identically everywhere: (Bull % upside) ÷ (Bear % downside) vs. spot.
- Analyst targets, rating changes, short interest, technical levels and 12–18-month re-rating math are *inputs to probabilities and context in §7*. **None of them may be cited as the reason for a verb or a zone.**

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
| 1 Business | §1, §2, §3 | Founding insight, segment definitions, unit of value, customer |
| **1A Risk Factors** | **§6** | Verbatim language for the highest-impact few; flag *new* vs. prior year |
| **7 MD&A** | **§1, §2, §3** | Segment drivers, volume vs. price/mix, competitive dynamics, macro sensitivity |
| 7A Market Risk | §6 | Quantified rate/FX/commodity sensitivities |
| 8 Statements & Notes | §1, §4 | Segment data, invested capital, contingencies, debt, leases, share count |
| 15 / DEF 14A | §4 | **Incentive metrics and weightings**, board, insider ownership |

EDGAR HTML > IR PDF > analyst summaries. The **[SEC XBRL company-facts API](https://data.sec.gov/api/xbrl/companyfacts/CIK[##########].json)** is the fastest reliable source for multi-year series, including the balance-sheet items that build invested capital — prefer it over parsing HTML tables. Workflow B diffs Item 1A year-over-year; new risks get a `[NEW in FY[N] 10-K]` tag.

**R11 — Risk materiality filter.** §6 covers risks material to the *decision*, not every Item 1A line.
- **Drop** boilerplate: "revenue could fluctuate", generic cyber, generic key-personnel, generic third-party reliance.
- **Keep** only risks meeting ≥1 test: (a) materially worse here than for peers; (b) **not priced in** — say so explicitly; (c) tied to a quantified thesis-break trigger the page commits to monitor; (d) tied to a specific large discretionary bet with an uncertain outcome.
- Multi-year risk evolution is 2–3 sentences of prose, never a table.

**R12 — Outsiders lens.** §4 carries a one-line grade per [`outsiders.md`](wiki/frameworks/outsiders.md), anchored on countercyclical buyback discipline. Vocabulary: `Outsider · Outsider-leaning · Reinvestor · Steward (not Outsider) · Anti-Outsider`. One sentence of evidence. Surface it to the Verdict **only on a material capital-allocation event** (buyback authorization/execution, dividend init/raise/cut, M&A, large debt action). Keep the ticker's row in `outsiders.md` in sync.

**R13 — One page per ticker; changelog is the event log.** The folder holds exactly `[TICKER].md` and `changelog.md`. Every material update writes a changelog entry stating **Thesis Status** (Strengthened / Weakened / Unchanged), the **scorecard** (each prior "Wrong About" test resolved Pass / Fail / Pending, §13), and an **action verb** (Initiate / Add / Hold / Trim / Exit / Watch / Avoid — *Trim* and *Reduce* are the same action; prefer *Trim*, matching the §5 zone name). Cross-ticker and schema-only events live in **commit messages**, not in any wiki file.

**R14 — Active / Paused.** Header carries `**Status**: Active` or `**Status**: Paused — since YYYY-MM-DD`. README, `index.md` and `watchlist.md` mirror it; Workflow B skips Paused entirely. Quiet ≠ paused: an Active quiet week still logs; a Paused ticker writes nothing.

**R15 — Style.** Emoji carry meaning, never decoration: 🟢 bullish/add · 🔴 bearish/exit · 🟡 neutral/hold · ⚠️ material risk · ✅ resolved (pair with `~~strikethrough~~`) · 📅 dated catalyst · 💰 capital allocation · 🎯 price zone. **Bold** only punchlines and thesis-carrying numbers — if half a paragraph is bold, none of it is. Tables run time in columns, metrics in rows.

**R16 — Ground truth: the business is understood from the unit up.** *(new in v5.0 — see [`compounding.md`](wiki/frameworks/compounding.md) for the method)*
- **Driver tree (§1)** — name the unit of value (a store, a subscriber, a trip, a case, a GWh, a policy), then build revenue and profit from it: units × revenue per unit × contribution per unit → segment profit → consolidated → per share. The unit and its per-unit metrics are fixed per asset type in [`asset-types.md`](wiki/frameworks/asset-types.md). Growth is split into *more units* and *more per unit*.
- **Reinvestment economics (§1)** — invested capital, ROIC, **incremental ROIC over three years**, reinvestment rate, and the organic growth those two imply (ROIIC × reinvestment rate). These rows are what a compounder thesis rests on; a page without them is not making one. Say how invested capital was built (equity + debt + leases − cash, or operating assets − operating liabilities) and tag it `[Derived]`.
- **Quality and survivability rows (§1)** — SBC as % of revenue, FCF conversion, net debt/EBITDA, interest coverage, nearest maturity wall. A decade-long hold must survive a recession; the page says whether it can.
- **Growth levers (§2)** — one table, fixed lever list: market growth · share gain · price and mix · attach / new products · new geographies · M&A · margin · share count. For each: current contribution, runway in years, evidence, management's stated intent, and stage (proven / scaling / option). Options are also valued in §5. Adjacency test (Zook): a new bet must share customers, costs or capabilities with the core, or it is diversification and is graded as such.
- **Customer block (§3)** — who buys, the job the product does, retention or repeat rate, the last price increase and what volume did, CAC and LTV where disclosed. Mauboussin's customer economics apply wherever the unit is a customer.
- **Moat mechanism and trend (§3)** — name the mechanism from the [7 Powers](wiki/frameworks/powers.md) vocabulary, call the trend (widening / stable / narrowing) with the evidence, and state who in the value chain captures the margin and whether that is shifting.
- **Incentives, credibility, promises (§4)** — one line on what the CEO is paid for (metrics and weights from the proxy), a guidance grade over the last eight to twelve quarters (`Consistent beater · Mixed · Misser`, with the one number that decides it), and a **promises ledger**: a three-row table of what letters or investor days three to five years back committed to, and what happened.

---

## 4. The Page

Eight sections. The front matter *is* the deliverable; the sections exist to support it.

```markdown
# TICKER — Company Name

> **Schema** v5.0 · **Updated** YYYY-MM-DD · **Status** Active
> **Price** $X.XX verified <date, time> ([Yahoo](url)) · 52-wk $L–$H · Nth %ile · ±X% from high
> **Type** <one-line asset class> · **Stage** <early growth / scaling / mature compounder / mature ex-growth / turnaround / declining>

## Verdict
<One sentence. The whole call — what this is and what to do.>

🟢 **Non-holder: <verb>** · 🟡 **Holder: <verb>**

| PW EV | PW return/yr | Compounding/yr | R/R | Entry | Trim | Avoid | <primary multiple> | Yield | BAIT | Moat | Next |
|---|---|---|---|---|---|---|---|---|---|---|---|
(one row — PW return/yr carries "(≥13%)" or "(<13%)"; Compounding/yr is the flat-multiple rate from §5)

**Breaks if**: <the single most load-bearing fact — if this goes, the thesis goes.>

## The Call
≤200 words. What the market has priced, what it has wrong, and the one number that
proves it. This is the ONLY place the argument is made — sections 1–8 supply evidence,
they do not re-argue.

## What I'd Have To Be Wrong About
Exactly 3 bullets. Each is a *disconfirming test*: what I would look for, where it
would show up, and by when. Not a hazard list — that is §6. Tests resolved in the last
window are marked ✅ Pass / 🔴 Fail / 🟡 Pending in the changelog scorecard, then replaced.

## 1. Business & Numbers      ← driver tree · five-year table incl. ROIC + quality rows · recent quarters
## 2. Growth Levers           ← one table (R16) + optionality named
## 3. Moat, Customer & Competition
## 4. Management & Capital    ← incentives · credibility grade · promises ledger · Outsider grade · letters/appearances
## 5. Scenarios → PW EV       ← one table + return decomposition + implied expectations + base rate + year ten
## 6. Risks & Triggers        ← one table
## 7. Catalysts & Sentiment
## 8. Sources
```

**Section notes**

- **§1** — Lead with what changed, not what is. **Driver tree table** first (unit · count · revenue/unit · contribution/unit · return or payback per unit · growth from units vs. per unit). Then the five-year table with the R16 rows added to the P&L and cash rows: invested capital, ROIC, 3-yr ROIIC, reinvestment rate, SBC %, FCF conversion, net debt/EBITDA, interest coverage. Then recent quarters and segment detail. Where a per-unit figure is not disclosed, write `n/d` and name the proxy you used.
- **§2** — The **Growth Levers table** (R16) and two or three sentences on which lever carries the Base case and which the Bull. Name what is optional and point to its §5 line. Nothing here re-argues The Call.
- **§3** — a four-row **moat read table** (`Read | Call | Evidence`: Mechanism in 7 Powers terms · Trend, widening / stable / narrowing, with the number · Profit pool, who in the chain captures the margin and the direction · Customer, R16), then the rating in one sentence. Then the competitor table: direct competitors with market share and a one-line threat read each; how *this* company differs and the evidence. Structurally unique businesses get a line, not a table. Industry structure and TAM live here.
- **§4** — **Incentives** line · **Guidance grade** · **Promises ledger** (three rows) · CEO/CFO read · capital-allocation record and Outsider grade (R12) · letters/appearances synthesis (R9), quotes attributed to venue. State explicitly when a window had no appearances.
- **§5** — **One scenario table**: scenario, 5-yr target, probability, contribution, the driving assumption. PW EV is the sum. Below it a **return-math table**, one row each in this order: **PW return/yr vs. the 13% hurdle** · **Compounding at a flat multiple** (growth + yield, and the re-rating share) · **Optionality** (probability × value, so the core reads without it) · **Price-implied expectations** · **Base rate for the Bull growth rate** · **Year ten** · **R/R**. Multiples and the peer read sit above the scenario table as its anchor.
- **§6** — **One table**: `Risk | Impact | Prob | Priced in? | Would break the thesis if…`. Front-matter bullets state the *test*; this table states the *hazard and odds* — different objects, no restatement.
- **§7** — Analyst consensus + rating changes in **one or two lines**; short interest with delta in one line; insider activity (last 90 days, Form 4 verified); window events and upcoming catalysts as **dated tables**; **management appearances** sit in §4 (R9). Move delivered items to `✅ Delivered`. Nothing in this section moves a verb (R8).
- **BAIT** is one cell in the Verdict table (`Triple (B+A+T)`). Justify a lens in §7 only where the rating is non-obvious. It is a scoring overlay, not a section; the Technical lens is informational and never load-bearing.

---

## 5. Frameworks

- **Compounding** — driver tree, ROIIC × reinvestment, return decomposition, hurdle-derived entry, price-implied expectations, growth-lever taxonomy, lifecycle stages, base-rate tables. → [`compounding.md`](wiki/frameworks/compounding.md)
- **7 Powers** (Helmer) — moat mechanism vocabulary, moat trend, profit-pool read, customer block. → [`powers.md`](wiki/frameworks/powers.md)
- **BAIT** (Mauboussin) — Behavioral / Analytical / Informational / Technical, each Strong / Moderate / Weak. Triple+ overlap = highest conviction. → [`bait.md`](wiki/frameworks/bait.md)
- **Moneyball** — 5-year terminal scenarios; PW EV per R8. → [`moneyball.md`](wiki/frameworks/moneyball.md)
- **Asset Types** — per-asset-class unit of value, per-unit metrics, valuation primary, and the ticker map. → [`asset-types.md`](wiki/frameworks/asset-types.md)
- **Outsiders** (Thorndike) — five tests, R12. → [`outsiders.md`](wiki/frameworks/outsiders.md)

---

## 6. Workflow A — First-Run Ingest

Trigger: *"ingest [TICKER]"* / *"add [TICKER]"* / *"build a page for [TICKER]"*. If the folder exists, switch to Workflow B.

1. **Verify the date** (R6) and **the live price** (R4).
2. **Fetch the raw set** into `raw/[TICKER]/` — 5 annual 10-Ks · last 4 quarterly transcripts and press releases · 12 months of 8-Ks · latest DEF 14A (incentive metrics are required, R16) · 5 years of letters (R9) · 12 months of appearances plus scheduled forward dates (R9) · latest investor-day deck · user-supplied PDFs. Log gaps; never fabricate. Store extracted text (R1).
3. **Pull the numbers** — SEC XBRL company facts for the multi-year series and the invested-capital components (R10, R16); then 52-wk range, market cap, EV, net debt, operating leases, float, short interest, analyst consensus, 90-day insider activity from Form 4 XML. Classify the asset type and unit of value from `asset-types.md`; add a row there if the type is new.
4. **Synthesize the page** per §4, applying R7–R12 and R16.
5. **Write** `[TICKER].md` + a `changelog.md` initial entry. Delete any legacy `overview.md` / `thesis.md` / `financials.md`.
6. **Run the closing audit** (R7) — duplication scan and word budget.
7. **Update the cross-file layer** (§8) — including the `index.md` Summary cell with its verb and fresh upside/downside pair, and the `Updated` date in the same edit. Then **commit and push** (§9).

## 7. Workflow B — Incremental Update

Trigger: *"weekly update"* / *"update [TICKER]"*.

1. **Baseline** — read `**Status**:`. Paused → skip entirely. Active → baseline is the latest changelog entry date; the lookback window is everything since.
2. **Scan** the Meaningful Events list (§11) across IR (including the events calendar), SEC EDGAR, the earnings calendar, the appearance sweep (R9), analyst actions, short interest, Form 4s, and news.
3. **Score the standing tests first.** Before touching the page, resolve each of the three "Wrong About" tests against the window's evidence — Pass / Fail / Pending — and record it in the changelog scorecard (§13). A failed test forces a scenario or verb change or an explicit sentence saying why not. Then write the replacement test.
4. **Material events** → fetch new raw material, then refresh **only what moved**:

   | Always | On the right trigger |
   |---|---|
   | §1 on earnings (new quarter row, roll TTM, refresh the driver tree and ROIC rows) | §2 — on a new lever, a lever that stalled, or a stage change |
   | §5 — re-verify multiples, scenarios, PW EV, PW return vs. hurdle, entry, R/R | §3 — only on a moat-altering event, a customer-metric disclosure, or a true strategic pivot |
   | §6 — mark resolved risks `~~struck~~ DE-RISKED [date]`, add new under R11 | §4 — on management change, capital allocation, a new proxy, a new letter or a material appearance |
   | §7 — price, consensus, insiders, news, upcoming | |
   | **Verdict** — thesis, verbs, zones, "Breaks if" | |

   §3 rarely moves on a single earnings print. Do not touch a section the news did not touch.
5. **Quiet week** → write only a `[YYYY-MM-DD] — No Material Events` changelog entry with a price / short-interest / consensus snapshot. **Do not modify `[TICKER].md` and do not bump any dates.**
6. **Changelog** entry mirroring the sections refreshed, ≤250 words (R7). Then §8 — re-derive the `index.md` Summary against the new price and scenario set, since both the verb and the upside/downside pair move whenever §5 or the price does — and §9.

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
   - Write it as `PW EV $204: +49% up / −27% down`. Both legs come from the §5 scenario set, so they always reconcile to that page's R/R (R8) without restating it.

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

**Resume** — a multi-quarter pause spans earnings, analyst clusters and macro events; reconstruct them, don't just re-price. Scan the full window (all 10-Q/10-K, earnings and transcripts, 8-Ks, the full analyst-action record noting clusters, current short interest / insiders / consensus, plus management, M&A, regulatory and capital-allocation events). Apply the Workflow B refresh; §7 enumerates each earnings print in order before settling on the current state. Set Active, bump Updated, append a `## [date] — Resumed (Catch-Up)` entry, update cross-files, commit `RESUME`.

---

## 11. Meaningful Events

Earnings (10-Q/10-K, release, transcript) · annual shareholder letter · **material C-suite appearance** (R9 — material when it discloses strategy, pricing, product, partnership or competitive detail not in the filings, or reframes a print) · shareholder meeting and proxy outcomes (a changed incentive metric is material, R16) · strategic announcements (launch, market entry/exit, divestiture, restructuring) · M&A and JVs · capital allocation (buyback, dividend, debt, equity issuance) · a disclosed customer metric (retention, cohort, CAC, unit economics) · analyst rating changes (**a cluster of ≥3 firms in a week gets special attention**) · short interest >10% MoM or a sustained 3-week trend · insider Form 4 >$1M, any cluster, or a CEO/CFO sale into a decline · major regulatory action · material litigation · CEO/CFO/COO or board changes · credit rating actions.

Extensible — add types when encountered.

## 12. Data Sources

| Data | Primary | Fallback |
|---|---|---|
| Live price | [Yahoo Finance](https://finance.yahoo.com/quote/) | CNBC, Google Finance, MarketWatch |
| Filings | SEC EDGAR (HTML; `curl` with a UA header — `www.sec.gov` blocks undeclared tools, `data.sec.gov` does not; fall back to the web fetcher or the IR-hosted PDF) | Company IR |
| Multi-year financials, invested capital | **SEC XBRL company-facts API** | 10-K tables |
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
- **Within a ticker: single agent.** §5 depends on §6 depends on §1 — section-level parallelism costs more in merge than it saves.
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
