# CLAUDE.md — kg-invest-wiki Schema (v2.12)

Instruction file for the LLM agent that maintains this wiki. **Read this file at the start of every session before modifying `wiki/`, `raw/`, or `outputs/`.**

---

## What This Wiki Is

A personal, position-agnostic investment knowledge base maintained by an LLM agent. Knowledge compounds from primary sources so every session starts from the latest synthesis, not a blank page.

- **Owner**: Karthik G
- **Started**: April 2026
- **Schema version**: v2.12 (April 2026)
- **Model**: Karpathy LLM Wiki pattern, adapted

### What this wiki is *not*
- It is **not** a portfolio tracker. It does not record what the owner holds.
- It does **not** prescribe position sizing, tranche %, or portfolio allocation.
- It does **not** invent numbers. Every figure traces to a primary source or is tagged `[Estimate]` / `[Analyst consensus]` / `[Management guidance]`.

---

## Directory Layout

```
kg-invest-wiki/
├── CLAUDE.md                     ← This file. Read before every session.
├── README.md                     ← Top-level ticker table (per Rule #14).
├── raw/                          ← Immutable source material. NEVER modify.
│   ├── [TICKER]/
│   │   ├── filings/              ← 10-K, 10-Q, 8-K, DEF 14A
│   │   ├── transcripts/          ← Earnings call transcripts
│   │   ├── press-releases/       ← Earnings + corporate announcements
│   │   ├── shareholder-letters/  ← CEO/founder letters (last 5 yrs + new on incremental)
│   │   ├── investor-day/         ← Slide decks, conference presentations
│   │   └── analyst-reports/      ← User-uploaded PDFs
│   └── clippings/                ← General articles, not ticker-specific
├── wiki/                         ← LLM-owned. Write and maintain everything here.
│   ├── index.md                  ← Master catalog.
│   ├── summaries.md              ← Reverse-chronological weekly-summary index.
│   ├── watchlist.md              ← Cross-ticker attractiveness ranking (no allocation).
│   ├── tickers/[TICKER]/
│   │   ├── [TICKER].md           ← Single consolidated wiki page.
│   │   └── changelog.md          ← Append-only per-ticker event log.
│   └── frameworks/               ← bait.md, moneyball.md, asset-types.md
└── outputs/
    ├── [TICKER]/[TICKER]_initial_analysis_YYYY-MM-DD.md
    └── weekly/YYYY-MM-DD_weekly_summary.md
```

---

## Core Rules

1. **Never modify `raw/`**. Immutable source of truth. Add, never edit.
2. **Position-agnostic**. Analyze the *company*, not the owner's holdings. Recommendations split into non-holder / holder framings when they diverge.
3. **No portfolio sizing**. No tranche %, position %, target allocation, or stock/options split anywhere. Price-level *valuation* ranges (e.g., "attractive below $140") are allowed — those are valuation, not sizing.
4. **Always update `index.md`** when adding or substantially changing a wiki page.
5. **Per-ticker `changelog.md` is the only event log**. The session-wide `wiki/log.md` was retired in v2.10. Material actions live in the relevant ticker's `changelog.md`; cross-ticker / schema-only events live in commit messages.
6. **Source from primary sources**: SEC filings, earnings releases, official IR pages, transcripts, conference materials. Non-primary content must be tagged `[Estimate]`, `[Analyst consensus]`, `[Management guidance]`, or `[Source: <name>, <date>]`.
7. **Live price always verified first**: Fetch from `https://finance.yahoo.com/quote/[TICKER]` before any valuation work. Fall back to CNBC / Google Finance / MarketWatch via web search. Never trust a search-snippet price; click through.
8. **`changelog.md` is the action layer**: Every wiki update writes a changelog entry stating Thesis Status (Strengthened / Weakened / Unchanged) and an action verb (Initiate / Add / Reduce / Exit / Hold / Avoid).
9. **Quiet weeks still log**. A weekly run with no material events writes a `[YYYY-MM-DD] — No Material Events` changelog entry with a price / short-interest / analyst-consensus snapshot. This becomes the next week's baseline.
10. **Always push to `origin` after every commit**. The remote is the source of truth. Surface push failures to the user (and to the affected ticker's `changelog.md` if mid-Workflow-B).
11. **One wiki page per ticker**. Per-ticker folder contains exactly two files: `[TICKER].md` (consolidated page: header + Summary + Business Overview + Pivotal Question + Key Stats + Sections 1–13) and `changelog.md`. Never create separate `overview.md` / `thesis.md` / `financials.md`; fold legacy files into `[TICKER].md` on first re-ingest.
12. **Date discipline**. Before writing any date-stamped artifact (Last Updated, changelog title, output filename, weekly summary filename), the agent MUST run `date -u +%Y-%m-%d` via Bash and use the literal result. NEVER infer the current date from session memory, prior file contents, or context. When delegating to sub-agents, pass the verified date as a literal string.
13. **Maintain the summaries index**. Every weekly run prepends a row to `wiki/summaries.md` linking the new `outputs/weekly/YYYY-MM-DD_weekly_summary.md`, keeping the table in reverse-chronological order.
14. **Maintain the README ticker table**. The `## Tickers Covered` table in `README.md` is the top-level entry point. Specs:
    - **Order**: alphabetical by ticker (A → Z, case-sensitive).
    - **Columns** (exactly 4): `Ticker | Status | Last Updated | Punchline`.
    - **Ticker**: relative link `[TICKER](wiki/tickers/TICKER/TICKER.md)`.
    - **Status**: `Active` or `Paused` — mirror the ticker page header (per Rule #15).
    - **Last Updated**: ISO date of the most recent *material* update (NOT row-touched date, NOT quiet weeks).
    - **Punchline**: 1–2 sentences synthesizing latest thesis (typically Section 13 thesis sentence + action verbs). Update on material thesis change; preserve verbatim during quiet weeks.
    - **Add** a new ingest in alphabetical position; **Remove** a delisted/divested/retired ticker (history preserved in git).
    - **Counter line** (`*N tickers above.*`) directly below the table must reflect current count.
15. **Active / Paused ticker status**. Every ticker has a status declared in the header block of `[TICKER].md` on a `**Status**: Active` or `**Status**: Paused — since YYYY-MM-DD` line directly below `Last Updated`. README, `wiki/index.md`, `wiki/watchlist.md`, and the weekly cron all read from this. Pause/resume governed by Workflow C.
    - README and `index.md` include a `Status` column.
    - `watchlist.md` ranks Active only; Paused tickers move to a "Paused Tickers" footer with pause date.
    - Quiet week ≠ paused week. Active-quiet writes a `No Material Events` entry; Paused writes nothing.
16. **All sources must be linked** as real Markdown links — not bare text.
    - **Absolute URL** for public web (SEC EDGAR, IR pages, news, aggregators). Link to the *specific* document, not the publisher home page.
    - **Relative path** when the file is stored locally under `raw/[TICKER]/...` — e.g., `[Q4 2025 PR](../../../raw/[TICKER]/press-releases/2026-02-Q4-results.pdf)`. Prefer relative when the file exists locally.
    - **Format**: `[Human-readable label](URL-or-path)`. No bare `[Source: ...]` tags.
    - **Unresolvable**: append `[link pending]` so the next pass can fix it. Never silently drop a citation.
    - Applies to all `wiki/` and `outputs/` content.
17. **Visual emphasis & emoji conventions**. Each glyph carries a specific meaning — not decorative:

    | Emoji | Meaning |
    |---|---|
    | 🟢 | Bullish / Strengthened / Initiate / Add |
    | 🔴 | Bearish / Weakened / Exit / Avoid |
    | 🟡 | Neutral / Unchanged / Hold / Watch |
    | ⚠️ | Material risk / warning |
    | ✅ | De-risked / resolved / delivered (pair with `~~strikethrough~~`) |
    | 📅 | Date-anchored upcoming catalyst |
    | 💰 | Capital allocation / buyback / dividend |
    | 📈 / 📉 | Notable price or metric move (sparing) |
    | 🎯 | Price target / entry zone / trim zone |

    **Bold** punchlines and thesis-carrying numbers only. *Italics* for source attributions and meta-tags (*[Estimate]*). No HTML `<span style>` — GitHub render gaps. No hex colors.
18. **Summary section at the top of every ticker page**. `[TICKER].md` opens (after the header block, before Business Overview) with a `## Summary` section of **≤10 bullets** distilled from Sections 1–13 — not new analysis. Cover (pick most relevant): thesis sentence, moat verdict, pivotal question, recommendation verbs (non-holder / holder), entry/trim zones, BAIT verdict, next catalyst with date, top 1–2 risks, valuation anchor, price action. Use Rule #17 emoji. Refresh whenever Section 13 or Section 9 changes.
19. **Annual shareholder letters are required primary sources**. Every Workflow A ingest fetches and synthesizes 5 fiscal years of CEO/founder letters; letters take precedence over third-party summaries. Three patterns:

    | Pattern | When | Fetch |
    |---|---|---|
    | A — Annual letter publishers | Standalone annual letter (typ. Feb–Mar) | 5 letters (1/year × 5 yrs) |
    | B — Quarterly letter publishers | Letter to Shareholders with each quarterly print | All 4 letters × 5 yrs (up to 20). Q4 = primary annual-wrap weight. Min for first ingest: 5 Q4 + 3 most-recent quarterly = 8 letters. |
    | C — No standalone letter | Use Chairman's Letter in annual report or DEF 14A introductory letter | 5 letters; if neither exists, log gap in §4 RMC and rely on transcripts |

    Sub-5-year coverage: fetch all letters since IPO. Storage: `raw/[TICKER]/shareholder-letters/YYYY_letter.pdf` named by *fiscal year covered*. Synthesis surface: Section 4 (Management & Leadership) `### Recent Management Commentary — Primary Source Synthesis` subsection — verbatim quotes mapped to investment relevance, optional multi-year framework arc table when letters reveal evolution. New letter is a Meaningful Event; refresh §4 + extend arc on incremental.
20. **10-K MD&A and Risk Factors are required primary sources — last 5 fiscal years for first-run ingest**. The 10-K MD&A explains *why* numbers moved; multi-year Risk Factor evolution shows *how management's worldview has shifted*. Aggregator summaries flatten both. Required integration map:

    | 10-K Item | Wiki Section(s) | What to extract |
    |---|---|---|
    | Item 1 (Business) | §1, §2 | Founding insight, segment definitions |
    | Item 1A (Risk Factors) | **§6 (Key Risks)** | Verbatim language for the highest-impact 6–8; flag *new* risks vs. prior 10-K |
    | Item 7 (MD&A) | **§1, §3, §7** | Segment drivers, competitive dynamics, macro sensitivity |
    | Item 7A (Market Risk) | §6, §7 | Quantified rate/FX/commodity sensitivities |
    | Item 8 (Statements & Notes) | §1, §2, §8 | Segment data, contingencies, debt, share count |
    | Item 15 / DEF 14A | §4 | Exec comp, board, insider ownership |

    Synthesis pattern in §1: `### Primary Source: 10-K Segment Detail (FY[N])` subsection with multi-year MD&A commentary explaining drivers across the 5-year window. §6 risks each derive from Item 1A or MD&A; analyst-only risks tagged `*[Analyst speculation]*`. Workflow B diffs Item 1A year-over-year; newly added risks drive a §6 update with `[NEW in FY[N] 10-K]` tag. Source preference: SEC EDGAR HTML > IR-site PDF > analyst summaries quoting the 10-K. PDF binary fetches fall back to EDGAR HTML.
21. **Synthesis over transcription**. Primary sources inform; agent synthesis is the deliverable. Verbatim quotes only when paraphrase would weaken the insight. Replace 5+ row chronological tables of source extracts with a 2–4 sentence synthesis paragraph naming what genuinely changed. The 5-Year Strategic Framework Arc table for letters in §4 is preserved; the parallel Risk Factor table is retired in favor of prose.
22. **Ticker-page output discipline**. The page must stand alone without exposing schema mechanics:
    - **No CLAUDE.md self-references** in `[TICKER].md` or `outputs/[TICKER]/*.md`. Light references in `changelog.md` are OK (audit trail).
    - **No retrospective / "corrected from" / "prior framing" language** in page bodies. Git history is the audit trail. Acceptable in changelog.
    - **Table orientation**: time in columns, metrics in rows. Exception: ≤4-row summary tables (Bull/Bear/Base) where one-row-per-scenario reads better.
    - **Bullet preference**: sentences with 3+ data points → bullets.
23. **Section consolidation: Moat lives in §3 only**. The standalone "Moat Assessment" block between Business Overview and Pivotal Question is retired. Summary keeps a one-line moat verdict; all detail lives in §3.
24. **Competitive landscape integration in §3**. §3 must include a `### Competitive Landscape` subsection: named direct competitors (US + international where relevant) with market share + 1–2 sentence read on each peer's moat / threat vector; explicit framing of how *this company's* moat differs and what evidence supports the differentiator; honest tail-risk read. Apply judgment by ticker — some businesses have no peer comparison (a one-line note explaining structural uniqueness suffices); narrow peer sets get a 2-row table; broader categories warrant fuller tables. Cite each market share figure (Statista, Built With, peer 10-Ks, market-research reports).
25. **Risk Factor materiality filter**. §6 focuses on risks material to the *investment decision*, not every Item 1A line.
    - **Drop** universal corporate boilerplate ("revenue could fluctuate," generic payments regulation, generic cyber-attacks, generic third-party reliance, generic key-personnel risk).
    - **Keep** risks meeting at least one criterion:
      - (a) **Materially differentiated from peers** — meaningfully more severe for this company.
      - (b) **Not yet priced into the multiple** — explicitly state *"not priced in"* in Notes when so.
      - (c) **Tied to a specific thesis-break trigger** — a quantified condition the page commits to monitor.
      - (d) **Tied to a specific large discretionary investment** with uncertain outcomes (multi-billion capex bet, in-flight integration).
    - 5-Year Risk Factor Evolution Arc collapsed to a 2–4 sentence synthesis paragraph (per Rule #21).
26. **Risk/Reward calculation discipline**. R/R cited in Summary, §12 (PW EV Interpretation), and `watchlist.md` MUST anchor to the *same §11 scenario set*.
    - **Standard**: R/R = (Bull % upside) ÷ (Bear % downside) using midpoint or named scenario prices vs. current verified live price. Higher = more favorable.
    - **Multiple Bull tiers** (Bull + Bull+): state both, e.g., *"≈10:1 R/R (Bull / Bear), rises to ≈15:1 with Bull+ tail."* Don't average silently.
    - **Stop-loss / thesis-break-anchored R/R** is acceptable as a *secondary* framing in §12; the *headline* R/R is always §11 Bull-vs-Bear.
    - **Watchlist 3-column collapse**: blend Bull + Bull+ via probability-weighted average so PW EV reconciles to the canonical §11 number.

---

## Investment Framework — 13-Section Thesis Structure

The page header block (Schema / Last Updated / Status / Live Price), Summary, Business Overview, Pivotal Investment Question, and Key Stats Snapshot precede Section 1.

| # | Section | Purpose |
|---|---------|---------|
| 1 | Annual Financial Metrics | 4–6 year trend + recent quarters; primary 10-K segment detail |
| 2 | Revenue Mix & Geographic Split | Revenue streams + business model + region table + forward-looking shifts |
| 3 | Competitive Moat & Landscape | Wide / Narrow / None + sources + vulnerabilities + named competitors with market share + how-this-company-differs |
| 4 | Management & Leadership | CEO/CFO assessment + capital allocation track record + RMC subsection (per Rule #19) |
| 5 | Strategic Growth Initiatives | Growth vectors that justify forward multiples |
| 6 | Key Risks | Materiality-filtered Impact × Probability × Priced-In table (per Rule #25) |
| 7 | Industry-Specific Macro Analysis | TAM, structural dynamics, regulatory environment |
| 8 | Valuation & Comparable Analysis | Multiples, peer set, "fair price" range |
| 9 | **Catalyst & Sentiment Tracker** | Analyst ratings, short interest, options skew, insider activity, news, upcoming events |
| 10 | BAIT Framework | Behavioral / Analytical / Informational / Technical lenses |
| 11 | Bull / Bear / Base Cases | Scenario price targets with explicit probabilities summing to 100% |
| 12 | Probability-Weighted Expected Value | PW EV vs. current price; horizon stated; R/R per Rule #26 |
| 13 | **Recommendation & Bottom Line** | Action verb + price-level rationale + thesis-break triggers + next review trigger |

### Section 9 — Catalyst & Sentiment Tracker (detail)

Drives weekly incrementals. Standardized fields:

- **Live price + 52-wk range + % from high/low** (date-stamped)
- **Analyst consensus**: Buy/Hold/Sell counts, median target, high/low; rating changes since last update with firm name + direction
- **Short interest**: % of float, days-to-cover, WoW + MoM delta. Flag sustained >10% MoM increase
- **Options skew (optional)**: 30-day put/call, IV percentile if material
- **Insider activity (last 90 days)**: net buy/sell, transactions >$1M or by officers/directors (OpenInsider + SEC Form 4)
- **Recent corporate news (last 90 days)**: `[YYYY-MM-DD] [Event Type] — [one-line] [linked source]`
- **Upcoming catalysts**: earnings, shareholder meeting, FDA/regulatory date, product launch, contract decision

### Section 13 — Recommendation & Bottom Line (template)

```
**Thesis in one sentence**: [Single sentence stating the central thesis]

**For a non-holder**: [Initiate / Watch / Avoid] — [price-level rationale]
**For a current holder**: [Add / Hold / Reduce / Exit] — [price-level rationale]

**Attractive entry zone**: [$X – $Y] (rationale)
**Trim zone**: [$X – $Y] (rationale)
**Exit / avoid zone**: [$X – $Y] (rationale)

**Thesis-break triggers** (would force re-rating):
- [Specific quantified trigger]
- ...

**Next review trigger**: [Specific event or date]
```

---

## Frameworks (one-line index)

- **BAIT** (Mauboussin) — Section 10. Four lenses (Behavioral / Analytical / Informational / Technical), each rated Strong / Moderate / Weak. Triple+ overlap = highest conviction. Detail: `wiki/frameworks/bait.md`.
- **Moneyball** — Sections 11/12. Bull/Base/Bear price targets with explicit probabilities summing to 100%; PW EV vs. current price with horizon. Detail: `wiki/frameworks/moneyball.md`.
- **Asset Type Rules** — Per-asset-class key metrics + valuation primary (capital-light platform, three-sided marketplace, franchise royalty, financial/brokerage, pharma, managed care, mortgage, consumer staples, etc.). Detail: `wiki/frameworks/asset-types.md`.

---

## Workflow A — First-Run Ingest

Triggered by: "ingest [TICKER]" or "build wiki page for [TICKER]".

### Step 1 — Pre-flight
Read this `CLAUDE.md` and the `kg-investment-analysis` skill SKILL.md. If `wiki/tickers/[TICKER]/` already exists, switch to Workflow B.

### Step 2 — Fetch standard raw set
Create `raw/[TICKER]/` and populate:
- **Last 5 annual 10-Ks** (or all since IPO) → `filings/[TICKER]-10K-FY[YYYY].pdf`
- **Last 4 quarterly transcripts** → `transcripts/`
- **Last 4 quarterly press releases** → `press-releases/`
- **All 8-Ks in last 12 months** → `filings/`
- **Most recent DEF 14A** → `filings/`
- **Last 5 annual shareholder letters** (Pattern A/B/C per Rule #19) → `shareholder-letters/YYYY_letter.pdf`
- **Latest investor day deck** if available → `investor-day/`
- **User-supplied PDFs** → `analyst-reports/`

Source preference: SEC EDGAR > company IR > major aggregator. Log gaps; do not fabricate.

### Step 3 — Verify live data
Live price (Yahoo Finance; fallback CNBC/Google Finance/MarketWatch), 52-wk range, market cap, EV, float, short interest, analyst consensus, last 90 days insider activity.

### Step 4 — Synthesize the 13 sections
Compile from raw set, not media summaries. Cite primary source for every material claim. Tag estimates. Apply Rules #19 (shareholder letter integration → §4 RMC), #20 (10-K MD&A + Risk Factors integration map → §1, §3, §6, §7), #21 (synthesis over transcription), #22 (output discipline), #24 (competitive landscape in §3), #25 (risk materiality filter).

### Step 5 — Write wiki files
- `wiki/tickers/[TICKER]/[TICKER].md`:
  1. Header block (ticker, company name, schema version, Last Updated, `**Status**: Active`)
  2. Summary (≤10 bullets, Rule #18, emoji per Rule #17)
  3. Business Overview (1–2 paragraphs)
  4. Pivotal Investment Question
  5. Key Stats Snapshot
  6. Sections 1–13 (financial tables embedded inline in §1, §2, §8, §12; no duplication)
- `wiki/tickers/[TICKER]/changelog.md` — initial entry "v2 Initial Ingest"

Delete legacy `overview.md` / `thesis.md` / `financials.md` if present.

### Step 6 — Generate polished report
Write `outputs/[TICKER]/[TICKER]_initial_analysis_YYYY-MM-DD.md`.

### Step 7 — Update cross-cutting files
- `wiki/index.md` — add row, refresh ticker summary, refresh last-updated date
- `wiki/watchlist.md` — add row in attractiveness ranking
- `README.md` — insert row in alphabetical position (Rule #14)

### Step 8 — Commit and push
- `git add` all changed files
- `git commit -m "INGEST [TICKER]: v2 initial ingest — [headline]"`
- `git push origin <branch>` (Rule #10)

---

## Workflow B — Weekly Incremental

Triggered by: scheduled task every **Friday evening**, OR "weekly update" / "update [TICKER]".

### Step 1 — Determine baseline and active set
For each ticker in `wiki/tickers/`:
- Read `**Status**:` from header. **If `Paused`, skip entirely** (no fetch, no scan, no entry, no page change).
- If `Active`: baseline = date of latest `changelog.md` entry. Lookback window = everything since.

### Step 2 — Scan for meaningful events
Check the **Meaningful Events List** below across: company IR, SEC EDGAR, earnings calendar, analyst rating changes, short interest aggregator, insider Form 4 aggregator, news search.

### Step 3a — If material events exist
1. Fetch new raw material into `raw/[TICKER]/<subfolder>/`.
2. Walk the section-refresh checklist:

   | Section | Refresh on earnings/material event |
   |---------|------------------------------------|
   | 1 — Annual Financial Metrics | **Always** on earnings: add new quarter row + roll TTM |
   | 2 — Revenue Mix & Geographic Split | If segment / geo data disclosed |
   | 3 — Competitive Moat & Landscape | On competitor moves, market-share shifts, moat-altering events |
   | 4 — Management & Leadership | On management commentary, capital-allocation changes; refresh RMC if a new shareholder letter dropped |
   | 5 — Strategic Growth Initiatives | On new strategic disclosures |
   | **6 — Key Risks** | **Always scan**: resolved risks marked `~~struck~~ DE-RISKED [date]`; new risks added with Rule #25 filter |
   | 7 — Industry-Specific Macro | On regulatory / sector developments |
   | 8 — Valuation & Comparable | **Always** on earnings: re-compute multiples; refresh Assessment |
   | **9 — Catalyst & Sentiment Tracker** | **Always**: refresh price, consensus, actions, insiders, news, upcoming. Move delivered → "Delivered ✅" |
   | 10 — BAIT Framework | Refresh any B/A/I/T justification the new data alters |
   | 11 — Bull/Bear/Base Cases | Refresh assumptions/targets/probabilities if scenarios shifted |
   | 12 — PW EV | Recompute if §11 changed; verify R/R (Rule #26) |
   | **13 — Recommendation** | **Always review**: thesis sentence, verbs, zones, thesis-break triggers (DE-RISK resolved, add new) |

   §2/§3 rarely change on a single earnings event — refresh only on true strategic pivots, business-model changes, or moat-altering events.
3. Append `changelog.md` entry; `What Changed` block mirrors refreshed sections (one bullet per).
4. Update `wiki/index.md` last-updated + moved fields.
5. Update `wiki/watchlist.md` ranking + earnings calendar + price-targets if attractiveness changed.
6. Update `README.md` Last Updated + Punchline (Rule #14).
7. Refresh §0 Summary if §13 or §9 changed (Rule #18).

### Step 3b — If no material events (quiet week)
Write a `[YYYY-MM-DD] — No Material Events` changelog entry with snapshot (price, 52-wk %, short interest %, consensus median, news headlines reviewed and dismissed). Do NOT modify `[TICKER].md` or bump README dates.

### Step 4 — Write the weekly cross-ticker summary
`outputs/weekly/YYYY-MM-DD_weekly_summary.md`:
- Header: counts as `N active (X events / Y quiet) / M paused`
- Per-ticker section (Active only): action verb if changed, one-line "what happened", price delta vs. last week, recommendation delta, linked sources
- Cross-ticker macro callouts (rate moves, sector rotation)
- Upcoming catalysts in next 1–2 weeks
- **Paused tickers footer**: one-line list with pause dates (omit if empty)

Then prepend a row to `wiki/summaries.md` (Rule #13).

### Step 5 — Commit and push
- `git commit -m "WEEKLY YYYY-MM-DD: [N] events / [M] quiet — [headline]"`
- `git push origin <branch>`

---

## Workflow C — Pause / Resume

Triggered by `pause [TICKER][: <reason>]` or `resume [TICKER]`.

### C.1 — Pause
1. Verify ticker exists and is `Active` (no-op + surface if already Paused).
2. Run `date -u +%Y-%m-%d`.
3. In `[TICKER].md` header, set `**Status**: Paused — since YYYY-MM-DD`.
4. Append changelog entry stating reason + last active baseline.
5. Update `README.md` (Status → Paused; do NOT bump Last Updated/Punchline), `wiki/index.md` (Status → Paused), `wiki/watchlist.md` (remove from ranking; append to "Paused Tickers" footer).
6. Commit `PAUSE [TICKER]: <reason>` and push.

### C.2 — Resume (with catch-up incremental)
A multi-quarter pause may span multiple earnings, analyst clusters, and macro events — catch-up reconstructs all of them, not just price-stamping.

1. Verify status is `Paused`. Run `date -u +%Y-%m-%d`. Read pause-since date.
2. **Catch-up scan** over the full pause window (not last 7 days): all 10-Q/10-K filings, all earnings PRs + transcripts, all 8-Ks, full-window analyst rating changes (note clusters), current short interest + insider 90-day + analyst consensus, any management/M&A/regulatory/dividend/buyback events.
3. Apply the full Workflow B Step 3a section-refresh checklist. §9 must enumerate each earnings print in chronological order before settling on current state.
4. Set header `**Status**: Active`, bump `Last Updated`.
5. Append changelog entry:

   ```markdown
   ## [YYYY-MM-DD] — Resumed (Catch-Up)

   **Pause window**: [paused-since] → [today] ([N] days)
   **Events reconstructed in window**:
   - [YYYY-MM-DD] [Event Type] — one-line
   - ...

   **Sources reviewed**: [list of new files in raw/]

   ### What Changed (vs. pre-pause baseline)
   - [Section X]: [refresh summary]
   - ...

   ### Thesis Status
   - **Overall**: Strengthened / Weakened / Unchanged (vs. pre-pause)
   - **BAIT delta**: ...
   - **Price target delta**: ...

   ### Recommendation
   - **For a non-holder**: ...
   - **For a current holder**: ...

   **Next review trigger**: [event/date]
   ```

6. Update `README.md` (Status → Active, bump Last Updated, refresh Punchline), `wiki/index.md`, `wiki/watchlist.md` (re-insert into ranking, remove from Paused footer).
7. Commit `RESUME [TICKER]: catch-up over [N]-day window — <headline>` and push.

---

## Parallelization Patterns

- **Workflow A fetch phase**: optional fan-out — 3–4 parallel fetcher agents split by source type (filings / transcripts+PRs / shareholder letters / live data + insider+analyst). A single synthesizer agent then reads the aggregated raw output. Use when speed matters.
- **Weekly cron across N tickers**: parallelize trivially — one `Agent` call per Active ticker, dispatched as parallel tool uses in a single message.
- **Within a single ticker**: single agent. Section synthesis is dependency-dense (§12 PW EV depends on §11 scenarios depends on §6 risks + §10 BAIT) — section-level parallelism creates merge headaches exceeding the time saved.
- **Shared file writes** (`README.md`, `wiki/index.md`, `wiki/watchlist.md`, `wiki/summaries.md`): sequential. Never parallel writes to the same file across agents.
- **Agent definition**: prefer `~/.claude/agents/research-bot.md` (Sonnet; WebSearch / WebFetch / Edit / Write) for primary-source-fetch-heavy work; `general-purpose` for synthesis-heavy work.

---

## Meaningful Events List

- **Earnings**: 10-Q / 10-K, earnings PR, transcript
- **Annual shareholder letter published** (Pattern A/B/C per Rule #19)
- **Shareholder meeting**: annual, special, proxy vote outcomes
- **Strategic announcements**: product launch, market entry/exit, divestiture, restructuring
- **M&A**: acquisition announce/close, merger, JV, strategic partnership
- **Capital allocation**: buyback authorization/execution, dividend init/raise/cut/suspend, debt issuance, equity issuance
- **Analyst rating changes**: any upgrade/downgrade/initiation/target revision; cluster ≥3 firms in a week is special attention
- **Short interest delta**: >10% MoM, or sustained 3-week trend either direction
- **Insider activity**: any Form 4 >$1M, any cluster, any unusual pattern (CEO/CFO sell into decline)
- **Major regulatory action**: investigation, fine, ruling, new rule affecting business model, antitrust
- **Litigation**: material suit filed, settlement, judgment
- **Management changes**: CEO/CFO/COO appoint or depart, board changes
- **Credit / rating agency actions**: S&P / Moody's / Fitch rating change

Extensible — add new event types when encountered.

---

## Data Source Priority

| Data Type | Primary | Fallback |
|-----------|---------|----------|
| Live price | Yahoo Finance (`finance.yahoo.com/quote/[TICKER]`) | CNBC, Google Finance, MarketWatch (web search) |
| Filings | SEC EDGAR | Company IR site |
| Transcripts | Company IR, Motley Fool, Seeking Alpha | Yahoo Finance transcripts |
| Press releases | Company IR, BusinessWire, PRNewswire | Web search |
| Analyst ratings | Primary research firm releases | User-uploaded PDFs in `analyst-reports/`, TipRanks / Yahoo |
| Short interest | Aggregator (Fintel, ChartExchange, NASDAQ) | FINRA twice-monthly |
| Insider activity | OpenInsider | SEC EDGAR Form 4 direct |
| Options data | CBOE, Yahoo options chain | Barchart |

---

## changelog.md Format (Per Ticker)

Append-only. Most recent entry first.

### Standard event entry

```markdown
## [YYYY-MM-DD] — [Event Type: Earnings Q[X] / Strategic Announcement / Analyst Action / Insider Cluster / etc.]

**Trigger**: [What caused this update; cite primary source filename or URL]
**Sources reviewed**: [List of files in raw/ or URLs]

### What Changed
- [Specific metric or thesis element]
- [Direction and magnitude]

### Thesis Status
- **Overall**: Strengthened / Weakened / Unchanged
- **BAIT delta**: ...
- **Price target delta**: Bull $X → $Y | Base $X → $Y | Bear $X → $Y
- **Catalyst & Sentiment delta**: ...

### Recommendation
- **For a non-holder**: Initiate / Watch / Avoid — [rationale]
- **For a current holder**: Add / Hold / Reduce / Exit — [rationale]

**Next review trigger**: [event or date]
```

### Quiet-week entry

```markdown
## [YYYY-MM-DD] — No Material Events

**Lookback window**: [Prior baseline] → [today]
**Sources scanned**: IR, SEC EDGAR, analyst feed, short-interest, insider feed, news

### Snapshot
- Price: $X (Δ: ±Y%)
- 52-wk range: $L – $H (% from high: ±Z%)
- Short interest: A% of float (Δ MoM: ±B%)
- Analyst consensus: median $C (Δ: ±D%)
- News scanned and dismissed: [bullet list]

**Recommendation**: Unchanged.
**Next review trigger**: Next Friday (default), or [specific catalyst].
```

---

## index.md Maintenance

Required columns: `Ticker | Status | Company | Moat | Conviction | Last Updated | Summary`. Status is `Active`/`Paused` per Rule #15. Ticker links to `tickers/[TICKER]/[TICKER].md`.

Plus a Ticker Summary table: `Ticker | Price | vs. 52-wk High | FCF Yield | P/E Fwd | BAIT | Recommendation (non-holder / holder)`.

Plus a Pending Data Gaps table.

Update on every ingest or substantive change. Refresh the "last full index refresh" date at the bottom.

---

## watchlist.md Maintenance

Pure attractiveness ranking. **No portfolio allocation, no target %, no stock/options splits.** Active tickers only — paused move to a "Paused Tickers" footer (Rule #15).

Required columns: `Rank | Ticker | Conviction | BAIT Overlap | Asymmetry (PW EV vs. price) | Recommendation (non-holder / holder) | Next Catalyst`.

Plus the Price Targets Summary (Probability-Weighted) table, Earnings Calendar & Key Watch Events, and Cross-Portfolio Macro Watch Items.

The "Portfolio Allocation Summary" table was removed in v2 — do not re-introduce.

---

## Schema Co-Evolution

This file evolves. When a new framework is added, a new ticker type is encountered, or a new operation is needed:

1. Update this file first.
2. Apply the change to wiki content.
3. Commit `SCHEMA: vX.Y — [what changed and why]`.
4. Push to `origin`. The commit message is the audit trail (per Rule #5).

Browse evolution:
- `git log --oneline CLAUDE.md` — every schema commit
- `git log -p CLAUDE.md` — full diffs
- `git blame CLAUDE.md` — per-line attribution

Each `SCHEMA: vX.Y — ...` commit body captures the *rationale*, not just the *what* — that body is the durable record. v2.12 (April 2026) is current. Major changes bump the version; minor edits within a version do not.
