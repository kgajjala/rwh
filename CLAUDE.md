# CLAUDE.md — kg-invest-wiki Schema (v2)

This is the instruction file for the LLM agent that maintains this wiki.
**Read this file at the start of every session before making any changes to `wiki/`, `raw/`, or `outputs/`.**

---

## What This Wiki Is

A personal, position-agnostic investment knowledge base maintained by an LLM agent.
It accumulates and compounds knowledge from primary sources over time so that every
session starts from the latest synthesis, not a blank page.

- **Owner**: Karthik G
- **Started**: April 2026
- **Schema version**: v2 (April 2026)
- **Model**: Karpathy LLM Wiki pattern, adapted

### What this wiki is *not*
- It is **not** a portfolio tracker. It does not record what the owner holds.
- It does **not** prescribe position sizing, tranche %, or portfolio allocation.
- It does **not** invent numbers. Every figure traces to a primary source or is
  explicitly tagged `[Estimate]` / `[Analyst consensus]` / `[Management guidance]`.

---

## Directory Layout

```
kg-invest-wiki/
├── CLAUDE.md                     ← This file. Read before every session.
├── README.md
├── raw/                          ← Immutable source material. NEVER modify.
│   ├── [TICKER]/                 ← Per-ticker raw store (created on first ingest)
│   │   ├── filings/              ← 10-K, 10-Q, 8-K, DEF 14A
│   │   ├── transcripts/          ← Earnings call transcripts
│   │   ├── press-releases/       ← Earnings + corporate announcements
│   │   ├── investor-day/         ← Slide decks, conference presentations
│   │   └── analyst-reports/      ← User-uploaded PDFs from research firms
│   ├── clippings/                ← General articles, not ticker-specific
│   └── analyses/                 ← Legacy folder — pre-v2 imports (read-only)
├── wiki/                         ← LLM-owned. Write and maintain everything here.
│   ├── index.md                  ← Master catalog. Updated on every ingest.
│   ├── log.md                    ← Append-only event log. Never delete entries.
│   ├── watchlist.md              ← Cross-ticker attractiveness ranking (no allocation)
│   ├── tickers/
│   │   └── [TICKER]/
│   │       ├── [TICKER].md       ← Single consolidated wiki page (overview + 15 sections + financial tables, all in one)
│   │       └── changelog.md      ← Append-only per-ticker event log
│   └── frameworks/               ← Cross-ticker analytical frameworks
│       ├── bait.md
│       ├── moneyball.md
│       └── asset-types.md
└── outputs/                      ← Generated reports.
    ├── [TICKER]/
    │   └── [TICKER]_initial_analysis_YYYY-MM-DD.md   ← Polished first-run report
    └── weekly/
        └── YYYY-MM-DD_weekly_summary.md              ← Friday cross-ticker rollup
```

---

## Core Rules

1. **Never modify `raw/`**. It is the immutable source of truth. Add, never edit.
2. **Position-agnostic**. The wiki analyzes the *company*, not the owner's holdings.
   Recommendations are framed conditionally: what action a non-holder should consider
   vs. what a holder should consider, when they diverge.
3. **No portfolio sizing**. Do not write tranche %, position %, target allocation,
   or stock/options split anywhere in the wiki. Price-level entry/exit *valuation*
   ranges (e.g., "attractive below $140") are allowed — those are valuation, not sizing.
4. **Always update `index.md`** when adding or substantially changing a wiki page.
5. **Always append to `log.md`** with a timestamped entry for every session action.
   Never delete or rewrite existing entries.
6. **Source from primary sources**: SEC filings, earnings releases, official IR
   pages, transcripts, conference materials. Anything not from primary sources must
   be tagged `[Estimate]`, `[Analyst consensus]`, `[Management guidance]`, or
   `[Source: <name>, <date>]`.
7. **Live price always verified first**: Before any valuation work, fetch from
   `https://finance.yahoo.com/quote/[TICKER]`. If unavailable, fall back to web search
   (CNBC, Google Finance, MarketWatch). Never trust a search-snippet price; click through.
8. **`changelog.md` is the action layer**: After every wiki update, write a changelog
   entry stating Thesis Status (Strengthened / Weakened / Unchanged) and a recommended
   action verb (Initiate / Add / Reduce / Exit / Hold / Avoid).
9. **Quiet weeks still log**. If a weekly run finds no material events for a ticker,
   write a `[YYYY-MM-DD] — No Material Events` changelog entry with a price /
   short-interest / analyst-consensus snapshot. This becomes the next week's baseline.
10. **Always push to `origin` after every commit**. Local commits are not the
    source of truth — the remote is. After any `git commit` (schema change,
    ingest, weekly run, manual update), immediately run `git push`. If the push
    fails, log the failure in `log.md` and surface it to the user.
11. **One wiki page per ticker**. The per-ticker folder contains exactly two
    files: `[TICKER].md` (the single consolidated wiki page covering business
    overview, all 15 thesis sections, and embedded financial tables) and
    `changelog.md` (append-only event log). Do not create separate
    `overview.md`, `thesis.md`, or `financials.md` files. If legacy v1 files
    exist, fold them into `[TICKER].md` and delete them on first re-ingest.

---

## Investment Framework — 15-Section Thesis Structure

Every ticker's `thesis.md` follows this structure:

| # | Section | Purpose |
|---|---------|---------|
| 1 | Why Does This Company Exist? + Pivotal Investment Question | Founding insight + the one question the thesis turns on |
| 2 | Annual Financial Metrics | 4–6 year trend + recent quarters |
| 3 | Geographic Revenue Mix | Region table + forward-looking shifts |
| 4 | Revenue Mix & Business Model | Revenue streams, unit economics, business-model evolution |
| 5 | Competitive Moat | Wide / Narrow / None + sources + vulnerabilities |
| 6 | Management & Leadership | CEO/CFO assessment + capital allocation track record |
| 7 | Strategic Growth Initiatives | The growth vectors that justify forward multiples |
| 8 | Key Risks | Impact × Probability table |
| 9 | Industry-Specific Macro Analysis | TAM, structural dynamics, regulatory environment |
| 10 | Valuation & Comparable Analysis | Multiples, peer set, "fair price" range |
| 11 | **Catalyst & Sentiment Tracker** | **(NEW)** Analyst ratings, short interest, options skew, insider activity, recent news, upcoming events |
| 12 | BAIT Framework | Behavioral / Analytical / Informational / Technical lenses |
| 13 | Bull / Bear / Base Cases | Scenario price targets with explicit probabilities summing to 100% |
| 14 | Probability-Weighted Expected Value | PW EV vs. current price; horizon stated |
| 15 | **Recommendation & Bottom Line** | **(REVISED)** Action verb (Initiate / Add / Reduce / Exit / Hold / Avoid), price-level rationale, thesis-break triggers, next review trigger |

### Section 11 — Catalyst & Sentiment Tracker (detail)

This is the surface that drives weekly incrementals. Standardized fields:

- **Live price + 52-week range + % from high/low** (with date stamp)
- **Analyst consensus**: rating breakdown (Buy/Hold/Sell counts), median target,
  high/low. Note any rating changes since last update with firm name + direction.
- **Short interest**: % of float, days-to-cover, week-over-week and month-over-month delta.
  Flag any sustained increase >10% MoM.
- **Options skew (optional)**: 30-day put/call ratio, IV percentile if material.
- **Insider activity (last 90 days)**: net buy/sell, notable transactions
  (>$1M or executive officers / directors). Source: OpenInsider or equivalent + SEC Form 4.
- **Recent corporate news (last 90 days)**: bullet list, each tagged
  `[YYYY-MM-DD] [Event Type] — [one-line summary] [Source: ...]`
- **Upcoming catalysts**: earnings date, shareholder meeting, FDA/regulatory date,
  product launch, contract decision — anything date-anchored.

### Section 15 — Recommendation & Bottom Line (detail)

Required structure:

```
**Thesis in one sentence**: [Single sentence stating the central thesis]

**For a non-holder**: [Initiate / Watch / Avoid] — [price-level rationale]
**For a current holder**: [Add / Hold / Reduce / Exit] — [price-level rationale]

**Attractive entry zone**: [$X – $Y] (rationale: [valuation logic])
**Trim zone**: [$X – $Y] (rationale: [valuation logic])
**Exit / avoid zone**: [$X – $Y] (rationale: [valuation logic])

**Thesis-break triggers** (would force re-rating, possibly to Exit / Avoid):
- [Specific quantified trigger 1]
- [Specific quantified trigger 2]
- ...

**Next review trigger**: [Specific event or date]
```

---

## BAIT Framework (Mauboussin)

Section 12 of every thesis. Four lenses:

- **B — Behavioral**: Identifiable sentiment / fear driving mispricing? Empirically
  supported by operating data, or narrative-only?
- **A — Analytical**: What is consensus missing? What does a rigorous model yield
  vs. price?
- **I — Informational**: Primary data (transcript, filing, conference) underappreciated
  because most investors rely on summaries?
- **T — Technical**: Converging mechanical catalysts — index inclusion, short squeeze,
  buyback acceleration, options expiry, institutional flow.

**BAIT Verdict**: Triple or quadruple overlap = highest-conviction signal.
Always rate each lens Strong / Moderate / Weak with a one-paragraph justification.
Full detail in `wiki/frameworks/bait.md`.

---

## Moneyball Probability Scoring

Section 13 / 14 of every thesis. All scenario price targets carry explicit
probabilities summing to 100%.

Example: Bull $X (30%) + Base $Y (50%) + Bear $Z (20%) = weighted EV of $W.
Use this to compute expected return vs. current price, with horizon stated.

Full detail in `wiki/frameworks/moneyball.md`.

---

## Asset Type Rules

| Type | Key Metrics | Valuation Primary |
|------|-------------|-------------------|
| Capital-light platform (BKNG, SHOP) | GBV, take rate, room nights, GMV | FCF yield, EV/EBITDA |
| Three-sided marketplace (DASH) | GOV, orders, MAU, take rate, ad attach | EV/EBITDA, EV/GOV |
| Franchise royalty (WING) | SSS, AUV, unit count, royalty rate | EV/EBITDA |
| Financial / brokerage (SCHW) | NII, NIM, AUM, NNA | P/TBV, P/E |
| Pharma / biotech (LLY) | Revenue by drug, pipeline milestones | P/E, EV/Sales |
| Managed care (UNH) | MLR, membership, premium yield | P/E, P/FCF |
| Mortgage / housing (RKT) | Origination volume, recapture, gain-on-sale | P/TBV, EV/EBITDA |
| Consumer staples (PG) | Organic sales growth, volume vs. price, FX | P/E, dividend yield |

Full detail in `wiki/frameworks/asset-types.md`.

---

## Workflow A — First-Run Ingest (Mode A: Full Analysis)

Triggered by: "ingest [TICKER]" or "build wiki page for [TICKER]".

### Step 1 — Pre-flight
1. Read this `CLAUDE.md`.
2. Read the `kg-investment-analysis` skill SKILL.md if not already loaded.
3. Check whether `wiki/tickers/[TICKER]/` already exists. If yes, this is not a
   first-run — switch to Workflow B instead.

### Step 2 — Fetch standard raw set
Create `raw/[TICKER]/` and populate with:
- **Latest 10-K** (most recent annual filing) → `filings/`
- **Last 4 quarterly earnings transcripts** → `transcripts/`
- **Last 4 quarterly earnings press releases** → `press-releases/`
- **All 8-K filings in last 12 months** → `filings/`
- **Most recent DEF 14A (proxy statement)** → `filings/`
- **Latest investor day or annual conference deck**, if available → `investor-day/`
- **Any user-supplied PDFs** → `analyst-reports/` (user-managed)

Source preference: SEC EDGAR > company IR site > major aggregator.
Do not fabricate filings. If something is unavailable, log the gap and move on.

### Step 3 — Verify live data
- Live price from Yahoo Finance (fallback: CNBC, Google Finance via web search)
- 52-week range, market cap, EV, latest float
- Current short interest (aggregator)
- Current analyst consensus (rating breakdown, median target)
- Recent insider activity (last 90 days, aggregator + SEC Form 4 spot check)

### Step 4 — Synthesize the 15 sections
Compile from the raw set, not from prior media summaries. Cite primary source for
every material claim. Tag estimates explicitly.

### Step 5 — Write wiki files
- `wiki/tickers/[TICKER]/[TICKER].md` — single consolidated wiki page. Required structure:
  1. **Header block** — ticker, company name, last-updated date, schema version
  2. **Business Overview** (1–2 paragraphs: what the company does, brands, revenue streams)
  3. **Moat Assessment** (Wide / Narrow / None + sources + vulnerabilities)
  4. **Pivotal Investment Question** (the one question the thesis turns on)
  5. **Key Stats Snapshot** (price, market cap, EV, FY revenue, FCF, key operating metrics)
  6. **Sections 1–15** of the 15-section thesis structure (financial tables embedded inline in Sections 2, 3, 10, 14 — do not duplicate elsewhere)
- `wiki/tickers/[TICKER]/changelog.md` — initial entry "v2 Initial Ingest"

If legacy `overview.md`, `thesis.md`, `financials.md` files exist for this
ticker, delete them as part of this step. The single `[TICKER].md` file
replaces all three.

### Step 6 — Generate polished report
Write a single consolidated MD report combining overview + thesis + financials
to: `outputs/[TICKER]/[TICKER]_initial_analysis_YYYY-MM-DD.md`

### Step 7 — Update cross-cutting files
- `wiki/index.md` — add row, refresh ticker summary, refresh last-updated date.
  Ticker column links to `tickers/[TICKER]/[TICKER].md` (the single wiki page).
- `wiki/watchlist.md` — add row in attractiveness ranking
- `wiki/log.md` — append entries for INGEST, UPDATE, REPORT actions

### Step 8 — Commit and push
- `git add` all changed files (raw additions, wiki page, changelog, index, watchlist, log, outputs)
- `git commit` with message `INGEST [TICKER]: v2 initial ingest — [one-line headline]`
- `git push origin <branch>` — never leave the commit local-only

---

## Workflow B — Weekly Incremental (Mode B)

Triggered by: scheduled task every **Friday evening**, OR manual command
"weekly update" / "update [TICKER]".

### Step 1 — Determine baseline
For each ticker in `wiki/tickers/`:
- Read the latest entry in `wiki/tickers/[TICKER]/changelog.md`.
- The baseline is the date of that entry. The lookback window is
  **everything that has happened since that date**.

### Step 2 — Scan for meaningful events (lookback window)
Check for any event from the **Meaningful Events List** below. Sources:
- Company IR page (press releases, 8-K filings)
- SEC EDGAR (any filings since baseline)
- Earnings calendar (was there an earnings event in window?)
- Analyst rating changes (primary research firm releases or aggregator)
- Short interest aggregator (any material delta)
- Insider activity aggregator (any new Form 4 transactions)
- News search for ticker for window

### Step 3a — If material events exist
1. Fetch and store the new raw material under `raw/[TICKER]/<subfolder>/`.
2. Update the affected sections of `[TICKER].md` (the single wiki page).
   Typical update surface: Section 2 financial tables, Section 11 Catalyst &
   Sentiment Tracker, Section 13/14 scenarios + PW EV if targets shifted.
3. Update Section 15 (Recommendation) if the action verb or price-zone
   thresholds moved.
4. Append a `changelog.md` entry using the standard format below.
5. Update `wiki/index.md` last-updated date.
6. Update `wiki/watchlist.md` ranking if attractiveness changed.

### Step 3b — If no material events (quiet week)
1. Write a `[YYYY-MM-DD] — No Material Events` changelog entry containing a
   snapshot: live price, 52-wk range %, short interest %, analyst consensus
   median target, any minor news headlines reviewed and dismissed.
2. This entry sets the new baseline. Do not modify `[TICKER].md`.

### Step 4 — Write the weekly cross-ticker summary
After all tickers are processed, write:
`outputs/weekly/YYYY-MM-DD_weekly_summary.md`

Required content:
- Header: date, ticker count, count with material events vs. quiet
- Per-ticker section with: action verb (if changed), one-line "what happened",
  price delta vs. last week, recommendation delta if any, source links
- Cross-ticker macro callouts (rate moves, sector rotations) where relevant
- Upcoming catalysts in the next 1–2 weeks

### Step 5 — Log
- Append all per-ticker actions to `wiki/log.md`.
- Append a final `WEEKLY` entry summarizing the run.

### Step 6 — Commit and push
- `git add` all changed files
- `git commit` with message `WEEKLY YYYY-MM-DD: [N] events / [M] quiet — [one-line headline]`
- `git push origin <branch>`

---

## Meaningful Events List (extensible)

Trigger a wiki update when any of the following occur during the lookback window:

- **Earnings**: 10-Q / 10-K filing, earnings press release, earnings call transcript
- **Shareholder meeting**: annual meeting, special meeting, proxy vote outcomes
- **Strategic announcements**: new product launch, market entry, market exit,
  divestiture, asset sale, restructuring
- **M&A**: acquisition announcement / close, merger, joint venture, strategic partnership
- **Capital allocation changes**: buyback authorization or execution update,
  dividend initiation / increase / cut / suspension, debt issuance, equity issuance
- **Analyst rating changes**: any upgrade / downgrade / initiation / target revision
  from a primary research firm. Pay extra attention to clusters (3+ firms in a week).
- **Short interest delta**: >10% MoM change, OR sustained 3-week trend in either direction
- **Insider activity**: any Form 4 transaction >$1M, OR any cluster of buys/sells,
  OR any unusual pattern (CEO/CFO sell into a decline, etc.)
- **Major regulatory action**: agency investigation, fine, ruling, new rule
  affecting the business model, antitrust action
- **Litigation**: material lawsuit filed, settlement, judgment
- **Management changes**: CEO/CFO/COO appointment or departure, board changes
- **Credit / rating agency actions**: rating change from S&P / Moody's / Fitch

This list is extensible — add new event types over time. Update this section
when a new event type is added.

---

## Data Source Priority

| Data Type | Primary | Fallback |
|-----------|---------|----------|
| Live price | Yahoo Finance (`finance.yahoo.com/quote/[TICKER]`) | CNBC, Google Finance, MarketWatch (via web search) |
| Filings | SEC EDGAR | Company IR site |
| Transcripts | Company IR site, Motley Fool, Seeking Alpha | Yahoo Finance transcripts |
| Press releases | Company IR site, BusinessWire, PRNewswire | Web search |
| Analyst ratings | Primary research firm releases | User-uploaded PDFs in `raw/[TICKER]/analyst-reports/`, aggregator (TipRanks / Yahoo) |
| Short interest | Aggregator (Fintel, ChartExchange, NASDAQ) | FINRA twice-monthly data |
| Insider activity | OpenInsider or equivalent aggregator | SEC EDGAR Form 4 direct |
| Options data | CBOE, Yahoo options chain | Barchart |

---

## changelog.md Format (Per Ticker)

Append-only. Most recent entry first.

### Standard event entry

```markdown
## [YYYY-MM-DD] — [Event Type: Earnings Q[X] / Strategic Announcement / Analyst Action / Insider Cluster / etc.]

**Trigger**: [What caused this update; cite primary source filename or URL]
**Sources reviewed**: [List of files in raw/ or URLs read]

### What Changed
- [Specific metric or thesis element that changed]
- [Direction and magnitude of change]

### Thesis Status
- **Overall**: Strengthened / Weakened / Unchanged
- **BAIT delta**: [Any change in B/A/I/T signals]
- **Price target delta**: Bull $X → $Y | Base $X → $Y | Bear $X → $Y
- **Catalyst & Sentiment delta**: [Short interest, analyst, insider, options changes]

### Recommendation
- **For a non-holder**: Initiate / Watch / Avoid — [rationale]
- **For a current holder**: Add / Hold / Reduce / Exit — [rationale]

**Next review trigger**: [Specific event or date]
```

### Quiet-week entry

```markdown
## [YYYY-MM-DD] — No Material Events

**Lookback window**: [Prior baseline date] → [today]
**Sources scanned**: IR page, SEC EDGAR, analyst feed, short-interest, insider feed, news search

### Snapshot
- Price: $X (Δ vs. last entry: ±Y%)
- 52-wk range: $L – $H (% from high: ±Z%)
- Short interest: A% of float (Δ MoM: ±B%)
- Analyst consensus: median target $C (Δ: ±D%)
- Recent news scanned and dismissed: [bullet list, one-line each]

**Recommendation**: Unchanged.
**Next review trigger**: Next Friday (default), or [specific upcoming catalyst].
```

---

## log.md Format

Each entry starts with a fixed prefix for grep / Unix parseability:

```
LOG [YYYY-MM-DD HH:MM] [ACTION] [SCOPE] — [description]
```

ACTION verbs (extend as needed):
- `INIT` — wiki initialization
- `INGEST` — first-run ingest of a new ticker (Workflow A)
- `UPDATE` — wiki file modification
- `WEEKLY` — Friday-evening weekly run summary
- `LINT` — schema / consistency lint pass
- `FETCH` — raw material fetch
- `PRICE` — live price verification
- `REPORT` — polished output report generation
- `SCHEMA` — change to CLAUDE.md itself
- `PUSH` — `git push` to origin (record success or failure)
- `DELETE` — file deletion

Examples:
```
LOG 2026-04-24 22:00 SCHEMA ALL — Migrated CLAUDE.md to v2 (position-agnostic, weekly cron, removed sizing).
LOG 2026-04-24 22:30 INGEST DASH — Fetched 10-K, last 4 transcripts + press releases, recent 8-Ks, DEF 14A.
LOG 2026-04-24 22:45 PRICE DASH — Live price verified at $X via Yahoo Finance.
LOG 2026-04-24 23:30 UPDATE DASH — Wrote DASH.md (single consolidated page) + changelog.md.
LOG 2026-04-24 23:35 REPORT DASH — Generated outputs/DASH/DASH_initial_analysis_2026-04-24.md.
LOG 2026-04-24 23:40 UPDATE index.md, watchlist.md — Refreshed for DASH.
LOG 2026-04-24 23:45 PUSH origin main — Pushed schema + DASH ingest commits.
LOG 2026-04-25 18:00 WEEKLY ALL — 9 tickers scanned. 2 with material events (DASH earnings, RKT analyst cluster). 7 quiet. Summary in outputs/weekly/2026-04-25_weekly_summary.md.
LOG 2026-04-25 18:05 PUSH origin main — Pushed weekly run.
```

---

## index.md Maintenance

Required columns (no allocation column):

| Ticker | Company | Moat | Conviction | Last Updated | Status |

The Ticker column links to `tickers/[TICKER]/[TICKER].md` (the single
consolidated wiki page).

Plus a Ticker Summary table:

| Ticker | Price | vs. 52-wk High | FCF Yield | P/E Fwd | BAIT | Recommendation (non-holder / holder) |

Plus a Pending Data Gaps table.

Update on every ingest or substantive change. Refresh "last full index refresh"
date at the bottom.

---

## watchlist.md Maintenance

Pure attractiveness ranking. **No portfolio allocation, no target %, no form (stock/options) splits.**

Required columns:

| Rank | Ticker | Conviction | BAIT Overlap | Asymmetry (PW EV vs. price) | Recommendation (non-holder / holder) | Next Catalyst |

Plus the Price Targets Summary (Probability-Weighted) table — kept, since it's
pure analysis.

Plus the Earnings Calendar & Key Watch Events table — kept.

Plus Cross-Portfolio Macro Watch Items — kept.

**Removed in v2**: "Portfolio Allocation Summary" table. Do not re-introduce it.

---

## Schema Co-Evolution

This file (`CLAUDE.md`) is meant to evolve. When a new framework is added, a new
ticker type is encountered, or a new update operation is needed:

1. **Update this file first.**
2. **Then apply the change to wiki content.**
3. **Commit with a descriptive message** (`SCHEMA: [what changed and why]`).
4. **Append a `LOG ... SCHEMA ALL ...` entry** to `wiki/log.md`.
5. **Push to `origin`** and append a `LOG ... PUSH ALL ...` entry.

Version history is tracked via Git. v2 is current. Major changes bump the
version (v3, v4, ...). Minor edits within a version are fine without bump.

### v2 changelog (April 2026)
- Removed all portfolio sizing language and `frameworks/position-sizing.md`.
- Wiki is now position-agnostic. Recommendations split into non-holder / holder framings.
- Section 11 changed from "Position Building Strategy" → "Catalyst & Sentiment Tracker".
- Section 15 renamed to "Recommendation & Bottom Line" with explicit action verbs:
  Initiate / Add / Reduce / Exit / Hold / Avoid.
- Added Workflow A (first-run) and Workflow B (Friday weekly cron) as primary operating modes.
- Added per-ticker `raw/[TICKER]/` structure with standard fetch set.
- Added `outputs/[TICKER]/[TICKER]_initial_analysis_YYYY-MM-DD.md` and
  `outputs/weekly/YYYY-MM-DD_weekly_summary.md` deliverables.
- Added Meaningful Events List (extensible).
- Codified data source priority table.
- Codified changelog entry format for both event-driven and quiet-week updates.

### v2.1 changelog (April 2026 — same-day refinement)
- **Consolidated per-ticker wiki from 4 files into 2.** Per-ticker folder now
  contains exactly `[TICKER].md` (single page: business overview + 15 sections +
  embedded financial tables) and `changelog.md`. Eliminates the prior
  duplication of business description and financial metrics across `overview.md`,
  `thesis.md`, and `financials.md`. Legacy v1 files are deleted on first
  re-ingest under Workflow A.
- **Always push to origin after every commit.** Added as Core Rule #10.
  Workflow A and B now have explicit Commit-and-Push steps. New `PUSH` ACTION
  verb in `log.md` tracks success/failure. Schema Co-Evolution gains a step 5
  for pushing schema commits.
