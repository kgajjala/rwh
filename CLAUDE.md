# CLAUDE.md — kg-invest-wiki Schema (v2.10)

This is the instruction file for the LLM agent that maintains this wiki.
**Read this file at the start of every session before making any changes to `wiki/`, `raw/`, or `outputs/`.**

---

## What This Wiki Is

A personal, position-agnostic investment knowledge base maintained by an LLM agent.
It accumulates and compounds knowledge from primary sources over time so that every
session starts from the latest synthesis, not a blank page.

- **Owner**: Karthik G
- **Started**: April 2026
- **Schema version**: v2.10 (April 2026)
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
│   │   ├── shareholder-letters/  ← Annual CEO/founder letters (last 5 yrs + new on incremental)
│   │   ├── investor-day/         ← Slide decks, conference presentations
│   │   └── analyst-reports/      ← User-uploaded PDFs from research firms
│   ├── clippings/                ← General articles, not ticker-specific
│   └── analyses/                 ← Legacy folder — pre-v2 imports (read-only)
├── wiki/                         ← LLM-owned. Write and maintain everything here.
│   ├── index.md                  ← Master catalog. Updated on every ingest.
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
5. **Per-ticker `changelog.md` is the only event log**. The session-wide
   `wiki/log.md` was retired in v2.10 — every material action lives in
   the relevant ticker's `changelog.md` entry, which is the durable
   audit trail. Cross-ticker / schema-only events live in commit
   messages.
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
    fails, surface the failure to the user (and to the affected ticker's
    `changelog.md` if the failure is mid-Workflow-B).
11. **One wiki page per ticker**. The per-ticker folder contains exactly two
    files: `[TICKER].md` (the single consolidated wiki page covering business
    overview, all 15 thesis sections, and embedded financial tables) and
    `changelog.md` (append-only event log). Do not create separate
    `overview.md`, `thesis.md`, or `financials.md` files. If legacy v1 files
    exist, fold them into `[TICKER].md` and delete them on first re-ingest.
12. **Date discipline**. Before writing any date-stamped artifact (header
    "Last Updated", changelog entry title, output filename, log entry, or
    weekly summary filename), the agent MUST run `date -u +%Y-%m-%d` via
    Bash and use that result as the literal date string. NEVER infer the
    current date from session memory, prior file contents, conversation
    context, or any other source. Stale dates have caused material thesis
    framing errors (e.g., calling an earnings event "one week away" when
    it was the same day). When delegating to sub-agents, pass the verified
    date as a literal string in the prompt — agents must not be expected
    to derive it correctly themselves.
13. **Maintain the summaries index**. After every weekly run, prepend a row
    to `wiki/summaries.md` (the index of cross-ticker weekly summaries) so
    that the Markdown table at the top stays in reverse-chronological order
    and links to each new `outputs/weekly/YYYY-MM-DD_weekly_summary.md`.
14. **Maintain the README ticker table**. The `## Tickers Covered` table in
    `README.md` is the top-level entry point for the wiki. It must be kept
    in sync — every ticker `add`, every Workflow B `material update`, and
    every ticker `removal` must update this table in the same commit:
    - **Order**: alphabetical by ticker symbol (case-sensitive; A → Z).
    - **Columns** (exactly four): `Ticker` | `Status` | `Last Updated` | `Punchline`.
    - **Ticker** column: a relative Markdown link to the ticker page —
      `[TICKER](wiki/tickers/TICKER/TICKER.md)`.
    - **Status** column: `Active` or `Paused`. Mirror exactly what is in
      the ticker page header. Per Rule #15.
    - **Last Updated** column: ISO date `YYYY-MM-DD` — the date of the most
      recent material update to that ticker's `[TICKER].md` (NOT the date
      the row in this table was last touched, and NOT the date of a quiet
      week — only material updates bump this).
    - **Punchline** column: 1–2 sentences synthesizing the latest thesis
      state (typically pulled from Section 13's `Thesis in one sentence`
      plus the action verb pair). Should communicate "what is this ticker
      and what's the read right now" to a reader who's never seen it.
      Update on every material thesis change; preserve verbatim during
      quiet weeks.
    - **Quiet weeks**: do NOT update the `Last Updated` date or the
      `Punchline` for tickers with no material events. The table is a
      snapshot of the latest substantive state, not run-cadence.
    - **Add**: when ingesting a new ticker under Workflow A, insert the
      new row in correct alphabetical position in the same commit.
    - **Remove**: if a ticker is removed (delisted, divested, or
      explicitly retired), delete the row in the same commit; preserve
      the historical changelog and last `[TICKER].md` snapshot in git
      history but the README should reflect current coverage only.
    - **Counter line**: the line directly below the table that begins
      `*N tickers above.*` (or similar) must reflect the current count.
15. **Active / Paused ticker status**. Every ticker has a status: `Active`
    (default — included in the weekly cron) or `Paused` (excluded from the
    weekly cron until explicitly resumed). Status is a single source of
    truth declared in the **header block of `wiki/tickers/[TICKER]/[TICKER].md`**
    on a `**Status**: Active` or `**Status**: Paused — since YYYY-MM-DD` line
    placed directly below the `Last Updated` line. README, `wiki/index.md`,
    `wiki/watchlist.md`, and the weekly cron all read from this. Pausing
    and resuming are governed by Workflow C below.
    - The README ticker table must include a `Status` column (column 2:
      `Ticker | Status | Last Updated | Punchline`).
    - `wiki/index.md` must include a `Status` column.
    - `wiki/watchlist.md` ranks **Active tickers only**. Paused tickers are
      listed in a separate "Paused Tickers" footer section with their pause
      date — they are not actionable but must remain visible so they are
      not forgotten.
    - **Quiet weeks vs. paused weeks are different**. A quiet week for an
      Active ticker still produces a `No Material Events` changelog entry
      and snapshot. A Paused ticker writes nothing during a weekly run.
16. **All sources must be linked**. Every `[Source: ...]` citation and
    every date-stamped event bullet that names a source MUST be a real
    Markdown link, not bare text.
    - **Absolute URL** for anything on the public web — SEC EDGAR
      filings (`https://www.sec.gov/...`), company IR press releases
      and transcripts, news articles, aggregators (Yahoo Finance,
      stockanalysis.com, Fintel, MarketBeat, OpenInsider, etc.).
      Always link to the *specific* document (the 8-K page, the
      press-release URL, the transcript URL), not the publisher's
      home page.
    - **Relative path** when the underlying document is stored
      locally under `raw/[TICKER]/...` — e.g.
      `[Q4 2025 PR](../../../raw/CPNG/press-releases/2026-02-Q4-results.pdf)`.
      Prefer the relative link when the file exists locally; the web
      URL is the fallback when it does not.
    - **Format**: `[Human-readable label](URL-or-path)`. The label
      should name the source briefly (e.g. "Coupang Q4 2025 PR",
      "10-K FY2025", "Yahoo Finance"). Do NOT use bare `[Source: ...]`
      tags or unlinked publisher names anywhere in `wiki/` or `outputs/`.
    - **Unresolvable sources**: if no URL or local path can be
      identified for a citation, leave the bare text and append
      `[link pending]` so the next pass can fix it. Never silently
      drop the citation.
    - This rule applies to all wiki content (`wiki/tickers/*/*.md`,
      `wiki/index.md`, `wiki/watchlist.md`, `wiki/summaries.md`,
      `wiki/frameworks/*.md`) and all generated outputs
      (`outputs/[TICKER]/*.md`, `outputs/weekly/*.md`).
17. **Visual emphasis & emoji conventions**. Use bold, italics, and a
    small standardized emoji vocabulary so key points are scannable.
    Do not sprinkle emoji decoratively — each glyph below carries a
    specific meaning:
    - 🟢 **Bullish / Strengthened thesis / Initiate / Add** — Section
      9 status, changelog "Strengthened", Section 13 action verbs
    - 🔴 **Bearish / Weakened thesis / Exit / Avoid** — same surfaces
    - 🟡 **Neutral / Unchanged / Hold / Watch** — same surfaces
    - ⚠️ **Material risk or warning** — Section 6 high-impact rows,
      thesis-break triggers in Section 13
    - ✅ **De-risked / resolved / delivered catalyst** — pair with
      the `~~struck-through~~` pattern from v2.3
    - 📅 **Date-anchored upcoming catalyst** — earnings dates, FDA
      decisions, shareholder meetings in Section 9 "Upcoming"
    - 💰 **Capital allocation / buyback / dividend event**
    - 📈 / 📉 **Notable price or metric move** (sparing — only when
      magnitude is the point)
    - 🎯 **Price target / entry zone / trim zone** in Section 13
    - **Bold** the punchline of each section's first paragraph and
      the action-verb line in Section 13. **Bold** key numbers in
      tables only when they carry the thesis (an MLR print, a Korea
      op-margin delta) — not every number.
    - *Italics* for source attributions inside paragraphs and for
      meta-tags (*[Estimate]*, *[Analyst consensus]*).
    - Markdown does not render hex colors — semantic color is conveyed
      via the emoji palette above. Do not embed HTML `<span style>`
      tags; they break GitHub rendering in some views.
18. **Summary section at the top of every ticker page**. Every
    `wiki/tickers/[TICKER]/[TICKER].md` MUST open (immediately after
    the header block, before "Business Overview") with a `## Summary`
    section (literal heading — not "Section 0 — Summary") containing
    **up to 10 bullets** distilled from the rest of the page. The
    Summary is a synthesis, not new analysis — every bullet must be
    supported by content already in Sections 1–13.
    - Bullets should cover (pick the 10 most thesis-relevant):
      thesis sentence, moat verdict, pivotal question, recommendation
      verbs (non-holder / holder), entry/trim zones, BAIT verdict,
      next catalyst with date, top 1–2 risks, key valuation anchor,
      price action context.
    - Use the emoji vocabulary from Rule #17 to make signals scannable.
    - Refresh on every material update (Workflow B Step 3a) — list
      `Summary` as a refreshed section in the changelog `What Changed`
      block whenever Section 13 or Section 9 changed.
19. **Annual shareholder letters are required primary sources**.
    Every Workflow A ingest MUST fetch and synthesize **the last 5
    fiscal years of CEO/founder shareholder letters**. **Letters
    take precedence over third-party media summaries** — they are
    the unfiltered, archived expression of management's framework
    and the highest-fidelity primary source for understanding
    capital allocation philosophy, strategic shifts, succession
    messaging, and operational priorities. There are three
    publication patterns; apply the matching path:
    - **Pattern A — Annual letter publishers** (e.g. Berkshire
      Hathaway, JPMorgan, Markel, Constellation Software): fetch
      one annual letter per fiscal year × 5 years = 5 letters.
      Letter typically published Feb–March covering the prior
      fiscal year.
    - **Pattern B — Quarterly letter publishers** (e.g. DoorDash,
      Shopify, Netflix, Spotify, Coupang): some companies
      substitute a "Letter to Shareholders" published with each
      quarterly earnings release for a standalone annual letter.
      Fetch **all 4 quarterly letters from each of the last 5
      fiscal years = up to 20 letters**. The Q4 letter usually
      serves as the de facto annual wrap and gets primary
      synthesis weight; Q1–Q3 letters add intra-year directional
      color and signal shifts. For first-year ingest of a Pattern
      B company, prefer fetching at minimum the Q4 letter from
      each of the last 5 years, plus the most recent 4 quarterly
      letters (= 5 + 3 = 8 letters minimum). If bandwidth allows,
      pull all 20.
    - **Pattern C — No standalone shareholder letter** (e.g. some
      legacy industrial companies): fetch the "Chairman's Letter"
      or "Letter to Shareholders" from the annual report front
      matter, or the proxy statement (DEF 14A) introductory
      letter, for each of the last 5 fiscal years. If neither
      exists, log the gap explicitly in the §6 RMC subsection
      and rely on earnings call transcripts.
    - **Sub-5-year coverage**: For companies <5 years public,
      fetch all letters published since IPO regardless of pattern.
    - **Storage**: `raw/[TICKER]/shareholder-letters/YYYY_letter.pdf`
      (or `.html`) — one file per fiscal year covered, named by the
      *fiscal year* the letter discusses (not the publication year).
      So Buffett's letter published Feb 2025 covering FY2024 →
      `raw/BRK.B/shareholder-letters/2024_letter.pdf`.
    - **Synthesis surface**: Section 6 (Management & Leadership) is
      the home for verbatim quotes from shareholder letters. Add a
      `### Recent Management Commentary — Primary Source Synthesis`
      subsection within Section 6, with two child subsections:
      `#### Verbatim quotes mapped to investment relevance` (one
      bullet per quote with citation + investment relevance) and,
      when the letter arc reveals a multi-year framework (e.g.,
      capital-allocation philosophy, succession messaging, segment
      commentary), `#### N-Year [Topic] Arc` containing a
      chronological table that traces the evolution. Quote letters
      directly with date and link; never paraphrase from third-party
      summaries unless the primary source is genuinely unavailable.
      *Note: This subsection lives within Section 6 because the wiki
      schema's Section 7 is "Strategic Growth Initiatives." Do not
      confuse with the kg-investment-analysis skill's Mode A schema
      (which numbers "Recent Management Commentary" as Section 7);
      the wiki schema takes precedence.*
    - **Workflow B (incremental)**: A new annual shareholder letter
      is a Meaningful Event (see list below). When a new letter
      drops (typically Feb–March each year for calendar-year filers),
      Step 3a must include a Section 6 RMC subsection refresh that
      incorporates verbatim quotes from the new letter and extends
      the multi-year arc table by one row. Old letters in
      `shareholder-letters/` are never deleted — they accumulate as
      the archive.
    - **Source preference**: Company IR site > SEC EDGAR DEF 14A or
      annual-report inclusions > third-party transcription. For
      Berkshire specifically, letters live at
      `https://www.berkshirehathaway.com/letters/YYYYltr.pdf`. For
      most companies the IR site lists letters as PDFs; some
      (e.g., AMZN) embed them in the proxy statement.
    - **Rationale**: This rule was added in v2.6 after the BRK.B
      ingest demonstrated that 5 years of Buffett letters + Abel's
      first letter materially sharpened the thesis (continuity of
      framework, succession-discount mispricing, operational
      quantification not present in any prior letter). Aggregator
      summaries flattened these distinctions; the letters did not.
20. **10-K MD&A and Risk Factors are required primary sources —
    last 5 fiscal years for first-run ingest**.
    Workflow A fetches the **last 5 annual 10-K filings** (or all
    available since IPO if <5 years public). The 10-K is the most
    authoritative single document for understanding the business,
    its segments, its risks, and management's own framing of
    operating performance. Fetching alone is insufficient — the
    10-Ks must be *synthesized*, with verbatim segment commentary
    and Risk Factors quotes integrated into the relevant sections
    of the wiki page, and **multi-year Risk Factor evolution
    analyzed across the 5-year baseline** (which risks were added,
    removed, or upgraded in emphasis over time — a leading
    indicator of management's evolving worldview). Aggregators
    (stockanalysis.com, Macrotrends, Yahoo Finance) parse the
    10-K but flatten the management commentary; the 10-K MD&A
    explains *why* numbers moved, and the multi-year Risk Factor
    diff explains *how management's risk framing has evolved* —
    both are genuinely incremental analytical edges over
    aggregator data.
    - **Required integration map** (which 10-K Item feeds which
      wiki section):

      | 10-K Item | Wiki Section(s) | What to extract |
      |---|---|---|
      | Item 1 (Business) | §1 (Why Exist), §4 (Revenue Mix) | Founding insight, segment definitions, business-model description |
      | Item 1A (Risk Factors) | **§8 (Key Risks)** | Verbatim risk-factor language for the highest-impact 6–8 risks; flag any *new* risks added vs. prior 10-K |
      | Item 7 (MD&A) | **§2 (Financial Metrics), §5 (Moat), §9 (Macro)** | Segment-level revenue/earnings driver commentary; competitive dynamics; macro sensitivity language |
      | Item 7A (Market Risk) | §8 (Key Risks), §9 (Macro) | Quantified rate, FX, commodity sensitivities |
      | Item 8 (Statements & Notes) | §2, §4, §10 (Valuation) | Segment data tables, contingencies, debt structure, share count detail |
      | Item 15 / DEF 14A | §6 (Management) | Exec comp, board, insider ownership |

    - **Synthesis pattern in §2**: Add a `### Primary Source: 10-K
      Segment Detail (FY[N])` subsection (analogous to the
      shareholder-letter pattern in §6) containing a segment table
      and 3–5 bullets of MD&A-derived insight that the headline
      numbers do not convey on their own. Direct quotes from the
      MD&A are encouraged. Example pattern from BRK.B v2.6: BNSF
      operating margin +250bps to 34.5% with the *"lower operating
      expenses from improved operating efficiencies, lower
      litigation accruals, and a lower effective income tax rate"*
      MD&A explanation — that commentary changes the read from
      "BNSF was up" to "BNSF margin expansion is structurally
      cost-discipline-driven and repeatable."
    - **Synthesis pattern in §8**: Risk Factors should not be a
      generic list invented by the agent. Each row in the
      Impact × Probability × Priced-In table must be supported
      either by an Item 1A risk-factor quote, by management
      commentary in MD&A, or by an external primary source
      (regulator, court filing). Risks that exist *only* in
      analyst speculation but are not surfaced anywhere in the
      10-K should be tagged `*[Analyst speculation]*` so the
      reader can weigh them differently.
    - **5-Year Risk Factor Evolution Arc** (analogous to the
      letter-arc pattern in §6): On first-run ingest, after
      fetching all 5 10-Ks, build a `### 5-Year Risk Factor
      Evolution Arc` subsection within §8 containing a
      chronological table of which Item 1A risk factors were
      added, removed, or *materially re-worded* across the
      5-year window. New risk factors are management's earliest
      signal of changing worldview — often appearing in 10-K
      Item 1A 1–2 years before they show up in earnings.
      Examples to capture: regulatory regime shifts (e.g.
      gig-worker classification appearing in 10-K 1A around
      2018–2020), AI-disruption risk language appearing in
      2022–2024 10-Ks for software companies, supply-chain
      risk language appearing in 2020–2021 10-Ks. The arc
      surfaces the management worldview shift, not just the
      current snapshot.
    - **Year-over-year comparison (incremental runs)**: When the
      new fiscal year's 10-K is fetched in Workflow B, *diff
      against the prior year's 10-K Item 1A* — newly-added Risk
      Factors are management's clearest signal that something
      material has changed (often before it shows up in
      earnings). Any *added* risk factors should drive a §8
      update with a `[NEW in FY[N] 10-K]` tag in the Notes
      column, and the 5-year arc table should be extended by
      one row.
    - **Workflow B (incremental)**: A new 10-K filing (typically
      Feb–March each year) is already a Meaningful Event (the
      "Earnings: 10-K filing" entry in the list below). Step 3a
      must include §2 segment-detail refresh + §8 Risk Factors
      diff against prior year + §5 / §9 MD&A update where
      relevant.
    - **Source preference**: Direct fetch from
      `[company]/[year]ar/[year]ar.pdf` or SEC EDGAR HTML version
      of the 10-K > intermediate analyst summaries (e.g.
      Stansberry, Insurance Business, Morningstar) > aggregator
      summaries. PDF binary parsing is unreliable; if the PDF
      fetch returns binary, fall back to the SEC EDGAR HTML
      version or to high-quality analyst summaries that explicitly
      quote the 10-K. Always cite the 10-K as the underlying
      source, even when working from an intermediate.
    - **Rationale**: Added in v2.6 alongside Rule #19 after the
      BRK.B ingest revealed that 10-K MD&A segment commentary
      (BNSF margin drivers, BHE PacifiCorp wildfire reserve
      normalization, GEICO ad-spend framing) was materially more
      informative than aggregator data. Aggregators report the
      *what*; 10-K MD&A explains the *why*.

21. **Synthesis over transcription** (added v2.8). Primary sources
    (letters, 10-Ks, transcripts) inform analysis; the agent's
    synthesis is the deliverable, not the primary-source extracts.
    - Verbatim quotes are valuable only when they are the most
      efficient way to convey a specific insight that paraphrase
      would weaken (e.g., a CEO's exact framing language, a 10-K
      Item 1A risk that surfaces a leading indicator, a specific
      quantified target). When agent paraphrase conveys the same
      insight more concisely, prefer paraphrase.
    - Multi-row chronological tables of source extracts (e.g., the
      "5-Year Risk Factor Evolution Arc table" originally added in
      v2.7) often add bulk without analytical edge. **Replace such
      tables with a 2–4 sentence synthesis paragraph** that names
      what genuinely changed and what it implies for the thesis.
      The 5-Year Strategic Framework Arc table for letters in §6
      is preserved (the multi-year strategic context is the
      analytical edge), but the parallel Risk Factor table is
      retired in favor of a short paragraph.
    - Heuristic: if a table has 5+ rows where each row is mostly
      a primary-source quote with minimal cross-row analytical
      structure, collapse it into prose.

22. **Ticker-page output discipline** (added v2.8). The wiki page
    is what the user reads; it must stand alone without exposing
    the agent's internal schema mechanics.
    - **No CLAUDE.md self-references in ticker page bodies**. Lines
      like *"Per CLAUDE.md v2.X Core Rule #N"*, *"per the v2.6
      Pattern B"*, etc. must NOT appear in `wiki/tickers/[TICKER]/[TICKER].md`
      or `outputs/[TICKER]/*.md`. Schema enforcement is internal
      and lives in this CLAUDE.md file. Light references in
      `wiki/tickers/[TICKER]/changelog.md` are acceptable since
      changelog is the audit trail.
    - **No retrospective / "corrected from" / "prior framing"
      language in ticker page bodies**. Git history is the audit
      trail. The page should reflect the *current* state cleanly.
      Acceptable in changelog entries; unacceptable in the page.
    - **Table orientation discipline**: time in columns, metrics in
      rows. Apply consistently across annual financial metrics,
      quarterly trend, segment, valuation, peer-comparison, and
      catalyst tables. The exception is small (≤4-row) summary
      tables like the Bull/Bear/Base scenarios where a one-row-per-
      scenario layout is more readable.
    - **Bullet-point preference for data-dense sentences**. When a
      sentence contains 3+ distinct data points (numbers, dates,
      named entities, ratios), break into bullets. Prose is fine
      for narrative exposition; bullets win when the reader needs
      to scan or compare.

23. **Section consolidation: Moat + Competitive Landscape live in
    Section 5 only** (added v2.8). The earlier "Moat Assessment"
    standalone block between Business Overview and Pivotal Question
    is **retired** as redundant.
    - **Summary section** keeps a one-line moat verdict (e.g.,
      *"Wide and Widening — switching costs + network effects +
      AI-standard-setter"*).
    - **Section 5 (Competitive Moat)** holds all moat detail —
      sources, vulnerabilities, AND the new mandatory `### Competitive
      Landscape` subsection (per Core Rule #24 below).
    - The Header / Key Stats Snapshot stays as is. No content
      duplication between the Summary verdict line and Section 5.

24. **Competitive landscape integration in Section 5** (added v2.8).
    Moat without competitor context is incomplete. Section 5 must
    include a `### Competitive Landscape` subsection, formatted to
    enable direct comparison and answer the question *"how is this
    company's moat different from competitors and what evidence
    supports it?"*
    - **Required content (when competitors exist)**:
      1. Named direct competitors (US + international where
         relevant) with **market share** and a 1–2 sentence read
         on each peer's moat / threat vector.
      2. Explicit framing of how *this company's* moat differs —
         what it has that competitors don't, and what evidence
         supports the differentiator (e.g., cross-border revenue
         growth as evidence of international moat; switching-cost
         retention metric as evidence of platform stickiness).
      3. Honest tail-risk read on competitive position (e.g., is
         there a peer that is well-capitalized, currently losing,
         and could escalate?).
    - **Apply judgment by ticker**: not every ticker has direct
      competitors. **Berkshire Hathaway** has no peer comparison —
      a one-line note explaining structural uniqueness is enough.
      **Sin-stock or franchise-royalty businesses** with narrow
      peer sets get a tight 2-row table. **Software / consumer /
      retail** typically warrant a fuller table.
    - **Source preference**: Statista, Built With, market-research
      reports, peer 10-Ks (for revenue / share figures), trade
      press. Cite each market share figure.

25. **Risk Factor materiality filter** (added v2.8). Modifies and
    supplements Core Rule #20 (which mandated 10-K Item 1A risk
    integration). The Section 8 risk table must focus on **risks
    that are material to the investment decision**, not catalog every
    Item 1A line item.
    - **Drop**: universal corporate boilerplate that applies to
      every public company in the same line of work. Examples:
      - "Revenue could fluctuate and miss expectations" (every
        company)
      - "We are subject to payments-related regulation" (every
        company processing payments)
      - "Cyber-attacks could harm our business" (every digital
        company)
      - "We rely on third-party providers" (every SaaS company)
      - "We may not retain key personnel" (every company)
    - **Keep** risks that are at least one of:
      - **(a) Materially differentiated from peers** — the risk
        is meaningfully more severe for this company than for its
        competitors (e.g., gig-worker reclassification is more
        severe for DASH/UBER than for SHOP).
      - **(b) Not yet priced into the multiple** — the market has
        not yet discounted this. **Explicitly state "not priced
        in"** in the Notes column when this is the case; it is
        actionable analytical information.
      - **(c) Tied to a specific thesis-break trigger** — the
        risk maps to a quantified condition the page commits to
        monitor (e.g., "Q1 SSS < –7%" or "MLR > 88% sustained").
      - **(d) Tied to a specific large discretionary investment**
        where outcomes are uncertain (e.g., a $5B AI capex
        commitment with no proven ROI; a multi-year tech-stack
        unification project; a multi-billion-dollar acquisition
        currently being integrated).
    - **5-Year Risk Factor Evolution Arc**: Per Rule #21, drop
      the chronological table and replace with a tight synthesis
      paragraph (2–4 sentences) that names what genuinely changed
      across the 5-year window and what it implies for the thesis.
      Multi-year evolution evidence remains valuable; the bulk
      table format does not.

26. **Risk/Reward calculation discipline** (added v2.8; section
    numbers updated v2.9). The R/R figure cited in the Summary,
    Section 12 (PW EV Interpretation), and `wiki/watchlist.md`
    (Conviction Ranking + Price Targets Summary) MUST anchor to
    the **same Section 11 scenario set** on the ticker page.
    - **Standard convention**: R/R = (Bull case % upside) ÷
      (Bear case % downside) using midpoint or named scenario
      prices vs. current verified live price. Higher = more
      favorable.
    - **Multiple Bull tiers (e.g., Bull + Bull+)**: state both
      explicitly — e.g., *"~10:1 R/R (Bull / Bear), rises to
      ~15:1 with the Bull+ tail."* Don't average them silently.
    - **Stop-loss / thesis-break-anchored R/R** (using the §9
      thesis-break alert price as the downside) is acceptable
      as a *secondary* framing in the Section 12 Interpretation
      paragraph for transparency, but the *headline* R/R figure
      must always be the Section 11 Bull-vs-Bear ratio.
    - **Watchlist Price Targets table**: when the 3-column
      template requires collapsing a 4-scenario set, blend the
      top tiers (Bull + Bull+) into a single "Bull blend" row by
      probability-weighted average so the PW EV reconciles to
      the canonical Section 11 number. Don't substitute a
      different scenario set.

---

## Investment Framework — 13-Section Thesis Structure

Every ticker's `thesis.md` follows this structure. The page header
block (Schema / Last Updated / Status / Live Price), Summary
section, Business Overview, Pivotal Investment Question, and
Key Stats Snapshot precede Section 1.

| # | Section | Purpose |
|---|---------|---------|
| 1 | Annual Financial Metrics | 4–6 year trend + recent quarters; primary 10-K segment detail |
| 2 | Revenue Mix & Geographic Split | Revenue streams + business model + region table + forward-looking shifts |
| 3 | Competitive Moat & Landscape | Wide / Narrow / None + sources + vulnerabilities + named competitors with market share + how-this-company-differs evidence |
| 4 | Management & Leadership | CEO/CFO assessment + capital allocation track record + Recent Management Commentary subsection (per Rule #19) |
| 5 | Strategic Growth Initiatives | The growth vectors that justify forward multiples |
| 6 | Key Risks | Materiality-filtered Impact × Probability × Priced-In table (per Rule #25) |
| 7 | Industry-Specific Macro Analysis | TAM, structural dynamics, regulatory environment |
| 8 | Valuation & Comparable Analysis | Multiples, peer set, "fair price" range |
| 9 | **Catalyst & Sentiment Tracker** | Analyst ratings, short interest, options skew, insider activity, recent news, upcoming events |
| 10 | BAIT Framework | Behavioral / Analytical / Informational / Technical lenses |
| 11 | Bull / Bear / Base Cases | Scenario price targets with explicit probabilities summing to 100% |
| 12 | Probability-Weighted Expected Value | PW EV vs. current price; horizon stated; R/R per Rule #26 |
| 13 | **Recommendation & Bottom Line** | Action verb (Initiate / Add / Reduce / Exit / Hold / Avoid), price-level rationale, thesis-break triggers, next review trigger |

**Retired in v2.9**: Section 1 ("Why Does This Company Exist? +
Pivotal Investment Question") was duplicative of the Business
Overview + Pivotal Investment Question header subsections that
already precede the numbered sections. Section 3 ("Geographic
Revenue Mix") and Section 4 ("Revenue Mix & Business Model") were
merged into the new Section 2 since both cover revenue
composition.

### Section 9 — Catalyst & Sentiment Tracker (detail)

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

### Section 13 — Recommendation & Bottom Line (detail)

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

Section 10 of every thesis. Four lenses:

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

Section 11 / 12 of every thesis. All scenario price targets carry explicit
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
- **Last 5 annual 10-K filings** (or all available since IPO if <5
  years public) → `filings/[TICKER]-10K-FY[YYYY].pdf` named by
  fiscal year covered. Per Core Rule #20, the multi-year baseline
  enables Risk Factor evolution analysis and multi-year MD&A
  strategic-shift detection — both genuinely incremental analytical
  edges over single-year synthesis.
- **Last 4 quarterly earnings transcripts** → `transcripts/`
- **Last 4 quarterly earnings press releases** → `press-releases/`
- **All 8-K filings in last 12 months** → `filings/`
- **Most recent DEF 14A (proxy statement)** → `filings/`
- **Last 5 annual shareholder letters** (or all available since IPO if
  <5 years public) → `shareholder-letters/YYYY_letter.pdf` named by
  fiscal year covered (per Core Rule #19). For Berkshire-style
  companies the letter is standalone; for most others it is in the
  annual report or proxy statement front-matter.
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

**Shareholder letter integration** (per Core Rule #19): Section 6
(Management & Leadership) MUST contain a `### Recent Management
Commentary — Primary Source Synthesis` subsection that quotes each
of the last 5 letters verbatim, mapped to investment relevance. When
the letters reveal a multi-year framework arc — capital allocation
philosophy, succession messaging, segment-level emphasis evolution —
add a "5-Year [Topic] Arc" subsection or table that traces the
chronology. Sections 5 (Moat) and 6 (Management) should also pull
verbatim quotes when the letters specifically address moat sources,
executive endorsements, or capital-allocation discipline.

**10-K MD&A and Risk Factors integration** (per Core Rule #20):
Read Item 1A (Risk Factors) and Item 7 (MD&A) directly across **the
last 5 10-Ks** — do not rely on aggregator summaries for narrative
content. (a) Section 2 gets a `### Primary Source: 10-K Segment
Detail (FY[N])` subsection with verbatim MD&A commentary explaining
segment drivers across the 5-year window — *why* numbers moved over
time, not just the most recent year. (b) Section 8 (Key Risks) must
derive each risk from a 10-K Item 1A risk factor or MD&A commentary;
rows that come from analyst speculation get an `*[Analyst
speculation]*` tag. (c) Add a `### 5-Year Risk Factor Evolution Arc`
subsection within Section 8 — chronological table of which Item 1A
risks were added/removed/re-worded across the 5-year window
(management's earliest worldview-shift signal). (d) When a new 10-K
is filed in Workflow B, *diff Item 1A* against the prior year's
10-K — newly added risk factors must drive a Section 8 update with a
`[NEW in FY[N] 10-K]` tag and extend the 5-year arc table. (e) If
the 10-K PDF returns binary (common for large PDFs via WebFetch),
fall back to SEC EDGAR HTML version or high-quality analyst
summaries that explicitly quote the 10-K — always cite the 10-K as
the underlying source.

### Step 5 — Write wiki files
- `wiki/tickers/[TICKER]/[TICKER].md` — single consolidated wiki page. Required structure:
  1. **Header block** — ticker, company name, schema version, last-updated date,
     and a `**Status**: Active` line (per Core Rule #15). New ingests start `Active`.
  2. **Summary** (≤10 bullets per Rule #18 — thesis sentence, moat, recommendation, entry zone, BAIT verdict, next catalyst, top risks; emoji-tagged per Rule #17)
  3. **Business Overview** (1–2 paragraphs: what the company does, brands, revenue streams)
  4. **Moat Assessment** (Wide / Narrow / None + sources + vulnerabilities)
  5. **Pivotal Investment Question** (the one question the thesis turns on)
  6. **Key Stats Snapshot** (price, market cap, EV, FY revenue, FCF, key operating metrics)
  7. **Sections 1–13** of the 13-section thesis structure (financial tables embedded inline in Sections 1, 2, 8, 12 — do not duplicate elsewhere)
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

### Step 8 — Commit and push
- `git add` all changed files (raw additions, wiki page, changelog, index, watchlist, log, outputs)
- `git commit` with message `INGEST [TICKER]: v2 initial ingest — [one-line headline]`
- `git push origin <branch>` — never leave the commit local-only

---

## Workflow B — Weekly Incremental (Mode B)

Triggered by: scheduled task every **Friday evening**, OR manual command
"weekly update" / "update [TICKER]".

### Step 1 — Determine baseline and active set
For each ticker in `wiki/tickers/`:
- Read the `**Status**:` line from the header block of `[TICKER].md`.
- **If `Paused`, skip the ticker entirely**. Do not fetch raw, do not
  scan for events, do not write a changelog entry, do not modify the
  page. Paused tickers are reported only as a count + list in the
  weekly summary footer.
- If `Active`: read the latest entry in `wiki/tickers/[TICKER]/changelog.md`.
  The baseline is the date of that entry. The lookback window is
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
2. Update **all affected sections** of `[TICKER].md` (the single wiki page).
   For an **earnings event**, the *mandatory* update surface is broader than
   just Sections 9 + 13. Walk through every section in this checklist and
   refresh anything the new data invalidates (per v2.9 13-section structure):

   | Section | When to refresh on earnings/material event |
   |---------|--------------------------------------------|
   | 1 — Annual Financial Metrics | **Always** on earnings: add the new quarter row + roll TTM figures |
   | 2 — Revenue Mix & Geographic Split | Refresh if segment / geographic data was disclosed |
   | 3 — Competitive Moat & Landscape | Refresh on competitor moves, market share shifts, moat-altering events |
   | 4 — Management & Leadership | Refresh on management commentary, capital-allocation changes; update RMC subsection if a new shareholder letter was published |
   | 5 — Strategic Growth Initiatives | Refresh on new strategic disclosures |
   | **6 — Key Risks** | **Always** scan: any risk that the new data resolves should be marked `~~struck through~~` with **DE-RISKED [date]**; new risks should be added with the materiality filter (Rule #25) applied; risk Notes refreshed if "Watch [event X]" was the resolved event |
   | 7 — Industry-Specific Macro Analysis | Refresh on regulatory or sector developments |
   | 8 — Valuation & Comparable Analysis | **Always** on earnings: re-compute multiples on new EPS/FCF; refresh Assessment paragraph if trough-vs-normalized framing shifted |
   | **9 — Catalyst & Sentiment Tracker** | **Always**: refresh price, analyst consensus, recent actions, insider activity, recent news, upcoming catalysts. Move delivered events from "Upcoming" to "Delivered ✅" |
   | 10 — BAIT Framework | Refresh any B/A/I/T justification paragraph that the new data alters |
   | 11 — Bull/Bear/Base Cases | Refresh assumptions and price targets if scenarios shifted; adjust probabilities if the event materially de-risks one branch |
   | 12 — PW EV | Recompute if Section 11 changed; verify R/R figure (Rule #26) |
   | **13 — Recommendation & Bottom Line** | **Always** review: refresh thesis sentence, non-holder/holder verbs, entry/trim/exit zones, **thesis-break triggers** (mark resolved triggers as DE-RISKED, add new ones the event surfaced) |

   Sections 2, 3 rarely change on a single earnings event — refresh only on
   true strategic pivots, business-model changes, or moat-altering events.
3. Append a `changelog.md` entry using the standard format below. The
   `What Changed` block must mirror the section refreshes performed (one
   bullet per refreshed section is good practice).
4. Update `wiki/index.md` last-updated date and any summary-row fields
   that moved (price, BAIT, recommendation).
5. Update `wiki/watchlist.md` ranking, earnings calendar, and
   price-targets table if attractiveness changed.

### Step 3b — If no material events (quiet week)
1. Write a `[YYYY-MM-DD] — No Material Events` changelog entry containing a
   snapshot: live price, 52-wk range %, short interest %, analyst consensus
   median target, any minor news headlines reviewed and dismissed.
2. This entry sets the new baseline. Do not modify `[TICKER].md`.

### Step 4 — Write the weekly cross-ticker summary
After all tickers are processed, write:
`outputs/weekly/YYYY-MM-DD_weekly_summary.md`

Required content:
- Header: date, ticker counts split as `N active (X events / Y quiet) / M paused`
- Per-ticker section (Active only) with: action verb (if changed), one-line "what happened",
  price delta vs. last week, recommendation delta if any, source links
- Cross-ticker macro callouts (rate moves, sector rotations) where relevant
- Upcoming catalysts in the next 1–2 weeks
- **Paused tickers footer**: one-line list of paused tickers with pause date
  (`PAUSED: ABNB (since 2026-05-15), DELL (since 2026-06-02)`). If empty, omit.

### Step 5 — Commit and push
- `git add` all changed files
- `git commit` with message `WEEKLY YYYY-MM-DD: [N] events / [M] quiet — [one-line headline]`
- `git push origin <branch>`

---

## Workflow C — Pause / Resume (Mode C)

Triggered by user commands:
- `pause [TICKER]` or `pause [TICKER]: <reason>` — move ticker to Paused.
- `resume [TICKER]` — move ticker to Active and run a catch-up incremental.

### C.1 — Pause

1. Verify the ticker exists at `wiki/tickers/[TICKER]/`. Confirm current
   status is `Active` (no-op if already Paused; surface this to the user).
2. Run `date -u +%Y-%m-%d` (Core Rule #12).
3. In `[TICKER].md` header block, change the `**Status**:` line to
   `**Status**: Paused — since YYYY-MM-DD`.
4. Append a changelog entry:

   ```markdown
   ## [YYYY-MM-DD] — Paused

   **Reason**: [user-provided reason, or "Owner request" if none given]
   **Last active baseline**: [date of prior changelog entry]

   No further weekly updates will be written until the ticker is
   resumed via `resume [TICKER]`. The wiki page is frozen as of this date.
   ```

5. Update `README.md` ticker table: set `Status` column to `Paused` for
   this row. Do NOT bump `Last Updated`. Do NOT modify `Punchline`.
6. Update `wiki/index.md`: set `Status` column to `Paused`.
7. Update `wiki/watchlist.md`: remove the row from the Conviction Ranking
   and append/update the "Paused Tickers" footer section with
   `[TICKER] — paused since YYYY-MM-DD`.
8. Commit (`PAUSE [TICKER]: <one-line reason>`) and push.

### C.2 — Resume (with catch-up incremental)

The resume operation MUST reconstruct what happened during the paused
window. A multi-quarter pause may span multiple earnings prints, analyst
revisions, and macro events — the catch-up must surface all of them so
the thesis is faithfully brought current, not just price-stamped.

1. Verify current status is `Paused`. If `Active`, no-op and surface.
2. Run `date -u +%Y-%m-%d`.
3. **Determine pause window**: `[paused-since date] → [today]`. Read
   the `Paused — since YYYY-MM-DD` value from the header.
4. **Catch-up scan** (mandatory — do all of the following for the full
   pause window, not just last 7 days):
   - Pull all 10-Q / 10-K filings from SEC EDGAR in window into
     `raw/[TICKER]/filings/`.
   - Pull all earnings press releases + transcripts in window into
     `raw/[TICKER]/press-releases/` and `raw/[TICKER]/transcripts/`.
   - Pull all 8-K filings in window into `raw/[TICKER]/filings/`.
   - Scan analyst rating changes across the entire window, not the last
     7 days. Note clusters and net direction.
   - Pull current short-interest, insider Form 4 (90-day), and current
     analyst consensus.
   - Note any management changes, M&A, regulatory actions, dividend or
     buyback authorizations during the window.
5. **Apply the full Workflow B Step 3a section-refresh checklist** —
   walk all 13 sections per the v2.9 structure and refresh anything
   the accumulated window data invalidates. Section 9 (Catalyst &
   Sentiment Tracker) must explicitly enumerate each earnings print
   in the window, in chronological order, before settling on the
   current state.
6. In `[TICKER].md` header, change `**Status**:` back to `**Status**: Active`
   and bump `**Last Updated**` to today.
7. Append a changelog entry:

   ```markdown
   ## [YYYY-MM-DD] — Resumed (Catch-Up)

   **Pause window**: [paused-since date] → [today] ([N] days)
   **Events reconstructed in window**:
   - [YYYY-MM-DD] [Event Type] — one-line summary
   - [YYYY-MM-DD] [Event Type] — one-line summary
   - ...

   **Sources reviewed**: [list of new files in raw/]

   ### What Changed (vs. pre-pause baseline)
   - [Section X]: [summary of refresh]
   - [Section Y]: [summary of refresh]
   - ...

   ### Thesis Status
   - **Overall**: Strengthened / Weakened / Unchanged (vs. pre-pause)
   - **BAIT delta**: ...
   - **Price target delta**: ...

   ### Recommendation
   - **For a non-holder**: ...
   - **For a current holder**: ...

   **Next review trigger**: [Specific event or date]
   ```

8. Update `README.md` (Status → `Active`, bump `Last Updated`, refresh
   `Punchline`), `wiki/index.md` (Status → `Active`, refresh row),
   `wiki/watchlist.md` (re-insert into Conviction Ranking, remove from
   Paused footer).
9. Commit (`RESUME [TICKER]: catch-up over [N]-day window — <headline>`)
   and push.

---

## Meaningful Events List (extensible)

Trigger a wiki update when any of the following occur during the lookback window:

- **Earnings**: 10-Q / 10-K filing, earnings press release, earnings call transcript
- **Annual shareholder letter published** (per Core Rule #19): typically
  Feb–March each year for calendar-year filers. New letter must be
  fetched into `raw/[TICKER]/shareholder-letters/YYYY_letter.pdf`,
  Section 7 refreshed with verbatim quotes, and any maintained
  multi-year arc table extended with the new row.
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

## index.md Maintenance

Required columns (no allocation column):

| Ticker | Status | Company | Moat | Conviction | Last Updated | Summary |

The `Status` column is `Active` or `Paused` per Core Rule #15. The `Summary`
column carries the short recommendation/BAIT note that previously lived in
the `Status` column under v2.4.

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
**Active tickers only** — paused tickers are excluded from the Conviction
Ranking and listed in a separate "Paused Tickers" footer section per Rule #15.

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
4. **Push to `origin`**. The commit message is the audit trail for
   schema-level changes (per Core Rule #5; `wiki/log.md` was retired
   in v2.10).

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

### v2.2 changelog (April 2026 — date discipline + summaries index)
- **Added Core Rule #12: Date discipline.** Before writing any date-stamped
  artifact, the agent must run `date -u +%Y-%m-%d` and use that as a literal
  string. Never infer dates from context. Sub-agent prompts must pass the
  verified date as a literal. This rule was added in response to a
  date-anchor-drift incident where 2026-04-17 was propagated as the
  "current date" across 31 files when the actual session date was
  2026-04-24, causing PG's "one week away" framing to be wrong on the day
  of its earnings print.
- **Added `wiki/summaries.md`** as a reverse-chronological index of all
  weekly summaries. Auto-maintained by the weekly cron routine
  (`trig_01R1X9aCDwHQDfUmkSii1bWb`).
- **Added Core Rule #13: Maintain the summaries index.** Each weekly run
  must prepend a row to `wiki/summaries.md`.
- The weekly cron routine `kg-invest-wiki-weekly` was created on
  2026-04-24 to fire every Friday at 22:00 UTC (6pm EDT / 5pm EST).
  Routine ID: `trig_01R1X9aCDwHQDfUmkSii1bWb`.

### v2.3 changelog (April 2026 — full update surface for material events)
- **Expanded Workflow B Step 3a "update surface" from 3 sections to a
  full 11-section checklist.** The prior schema only mandated refreshing
  Sections 2, 11, 13/14, 15 on material events. This caused stale
  Section 8 (Key Risks) entries on UNH after the Q1 2026 earnings beat
  (the row "MLR stays > 88% in 2026 — Watch Q1 2026 MLR closely" was
  not updated when Q1 MCR printed at 83.9%, well below the 88%
  threshold).
- **New mandate**: For an earnings event, walk through Sections 2, 3, 6,
  7, 8, 9, 10, 11, 12, 13, 14, 15 and refresh anything the new data
  invalidates. Sections 8 and 10 are now flagged as "always scan" surfaces.
  Strike-through (`~~text~~ DE-RISKED [date]`) is the prescribed pattern
  for retired risks and triggers — preserves history while clarifying
  current state.
- **Changelog entries should mirror section refreshes** — one bullet per
  refreshed section in the `What Changed` block, so reviewers can audit
  whether the full surface was walked.

### v2.4 changelog (April 2026 — README ticker table maintenance)
- **Added Core Rule #14: Maintain the README ticker table.** The
  `## Tickers Covered` table in `README.md` is the top-level entry
  point for the wiki — alphabetical, with three columns
  (`Ticker` | `Last Updated` | `Punchline`). Every Workflow A ingest,
  Workflow B material update, and ticker removal must update this table
  in the same commit. Quiet weeks do NOT update the row (the table
  reflects the latest substantive thesis state, not run cadence).
- The weekly cron routine prompt was updated to include README ticker
  table maintenance as a mandatory cross-cutting refresh step (alongside
  index.md, watchlist.md, summaries.md).

### v2.5 changelog (April 2026 — Active / Paused ticker status + linked sources + Summary section)
- **Added Core Rule #15: Active / Paused ticker status.** Every ticker
  carries a status declared in the `**Status**:` line of its page header.
  `Active` (default) means the weekly cron updates it; `Paused` means
  the weekly cron skips it entirely until it is resumed. The owner uses
  pause/resume to mute coverage on tickers that are temporarily
  uninteresting (e.g., divested, in workout, or just out of attention)
  without losing the wiki page or its history.
- **Added Workflow C — Pause / Resume.** `pause [TICKER][: <reason>]`
  freezes a ticker; `resume [TICKER]` reactivates it AND runs a
  catch-up incremental that reconstructs every material event during
  the pause window (multiple earnings prints, analyst clusters,
  management changes, etc.) and walks the full Workflow B Step 3a
  section-refresh checklist. The catch-up changelog entry must
  enumerate every event that occurred during the window — a multi-quarter
  pause cannot be discharged with a price-stamp.
- **Workflow B Step 1** now reads each ticker's status and skips paused
  tickers entirely (no quiet-week entry, no fetch). The weekly summary
  reports counts as `N active (X events / Y quiet) / M paused` and lists
  paused tickers in a footer.
- **README ticker table** gains a `Status` column (column 2). Total of
  four columns: `Ticker | Status | Last Updated | Punchline`.
- **`wiki/index.md`** gains a `Status` column. The pre-existing column
  previously labeled `Status` (which carried recommendation summaries)
  is renamed to `Summary` to avoid collision.
- **`wiki/watchlist.md`** ranks Active tickers only. Paused tickers
  move to a "Paused Tickers" footer section.
- **`log.md`** gains `PAUSE` and `RESUME` ACTION verbs.
- **Added Core Rule #16: All sources must be linked.** Every
  `[Source: ...]` citation and date-stamped event bullet must be a
  real Markdown link — absolute URL for web sources (SEC EDGAR,
  company IR, news, aggregators), relative path when the file is
  stored locally under `raw/[TICKER]/...`. Bare `[Source: name]`
  text is no longer acceptable. Unresolvable citations get a
  `[link pending]` tag for the next pass.
- **Added Core Rule #17: Visual emphasis & emoji conventions.**
  Standardized a small emoji vocabulary (🟢🔴🟡⚠️✅📅💰📈📉🎯) so
  thesis status, risks, and catalysts are scannable at a glance.
  Bold reserved for section punchlines and thesis-carrying numbers;
  italics for source attributions and `*[Estimate]*`-style meta tags.
  Hex colors / HTML spans explicitly disallowed (GitHub render gaps).
- **Added Core Rule #18: Summary section at the top of every ticker
  page.** Up to 10 bullets distilled from Sections 1–15, emoji-tagged,
  refreshed whenever Section 11 or 15 changes. Gives a reader the
  entire thesis at a glance before scrolling.
- **Updated Workflow A Step 5** per-ticker file structure to add the
  `Summary` section between the header block and Business Overview.
- **Existing-content sweep**: a one-time retrofit pass linkified
  citations and added Summary sections to all 34 ticker pages
  without re-fetching primary sources or recomputing analysis.

### v2.6 changelog (April 2026 — primary-source synthesis depth: shareholder letters + 10-K MD&A)
- **Added Core Rule #19: Annual shareholder letters are required
  primary sources.** Every Workflow A ingest must fetch and
  synthesize the **last 5 annual shareholder letters** (CEO/founder
  letters) for each ticker, and every Workflow B incremental run
  must detect a newly-published letter and refresh accordingly.
  Letters take precedence over third-party media summaries — they
  are the unfiltered, archived expression of management's framework
  and the highest-fidelity primary source for capital allocation
  philosophy, strategic shifts, succession messaging, and operational
  priorities. This rule was added after the BRK.B initial ingest
  demonstrated that 5 years of Buffett letters + Abel's first
  letter materially sharpened the thesis (continuity of framework,
  succession-discount mispricing, operational quantification not
  present in any prior letter — *"each percentage point of margin
  improvement = ~$230M of incremental cash flow"* from Abel's
  FY2025 letter). Aggregator summaries flattened these distinctions.
- **Added Core Rule #20: 10-K MD&A and Risk Factors are required
  primary sources — last 5 fiscal years for first-run ingest.**
  Workflow A fetches the **last 5 annual 10-Ks** (parallel to the
  shareholder-letter rule). Fetching alone is insufficient — the
  10-Ks must be *synthesized*, with verbatim Item 1A (Risk Factors)
  and Item 7 (MD&A) commentary integrated into the relevant
  sections. Specifically: §2 gets a `### Primary Source: 10-K
  Segment Detail (FY[N])` subsection (with multi-year context);
  §8 (Key Risks) derives each row from Item 1A or MD&A (analyst
  speculation tagged `*[Analyst speculation]*`); §5 / §9 pull MD&A
  competitive-dynamics and macro-sensitivity language. **§8 also
  gets a `### 5-Year Risk Factor Evolution Arc` subsection** —
  chronological table of which Item 1A risks were
  added/removed/re-worded across the 5-year window. **Workflow B
  diffs Item 1A year-over-year** — newly-added risk factors are
  management's earliest signal of material change and drive §8
  updates with `[NEW in FY[N] 10-K]` tags + extend the arc table.
  PDF fetch failures fall back to SEC EDGAR HTML or analyst
  summaries that quote the 10-K directly.

  **Rationale**: The BRK.B ingest revealed that 10-K MD&A commentary
  (BNSF margin drivers, BHE PacifiCorp wildfire reserve normalization,
  GEICO intentional ad-spend framing) was materially more informative
  than aggregator data — aggregators report *what* moved, the 10-K
  MD&A explains *why*. The 5-year baseline was added (during the SHOP
  v2.6 application) because Risk Factor *evolution* is a leading
  indicator of management's worldview shift — risks often appear in
  Item 1A 1–2 years before they show up in earnings (e.g.
  gig-worker classification language in 2018–2020 ride-share 10-Ks,
  AI-disruption risk language in 2022–2024 software 10-Ks). The
  multi-year arc surfaces this; a single-year snapshot does not.
- **New raw subfolder**: `raw/[TICKER]/shareholder-letters/`. Files
  named by *fiscal year covered* (not publication year), e.g.
  `2024_letter.pdf` for Buffett's letter published Feb 2025
  covering FY2024.
- **Workflow A Step 2** updated to add the last-5-letters fetch
  alongside 10-K/10-Q/8-K/DEF 14A/transcripts/press-releases.
- **Workflow A Step 4** synthesis now requires a
  `### Recent Management Commentary — Primary Source Synthesis`
  subsection within Section 6 (Management & Leadership), with
  verbatim quotes mapped to investment relevance and an optional
  multi-year framework arc table. Section 6 is used (not Section 7)
  because the wiki schema's Section 7 is "Strategic Growth
  Initiatives" — see Rule #19 note about disambiguation from the
  kg-investment-analysis skill schema.
- **Meaningful Events List** gains "Annual shareholder letter
  published" as a Workflow B trigger event.
- **BRK.B**: First ticker built under v2.6. Fetched 6 letters
  (FY2020–FY2025); built verbatim-quote synthesis + 5-Year Capital
  Allocation Arc table within Section 6. Also pulled 10-K segment
  precision (BNSF op margin +250bps to 34.5%, BHE +6.7% earnings
  on PacifiCorp wildfire reserve normalization, GEICO –$1B driven
  by intentional +$1.4B ad acceleration) and added a proper
  Section 8 (Key Risks) table that was previously missing in the
  v2.5 ingest. Other 34 tickers will be backfilled with their own
  shareholder-letter passes in subsequent runs (flagged as a
  pending v2.6 retrofit).
- **Pending follow-up**: Retrofit pass to add `shareholder-letters/`
  + Section 6 RMC subsections to the other 34 existing tickers.
  Should be done in batches matching the v2.4 25-ticker batch
  approach. Not blocking — incremental Workflow B runs will pick
  up new letters going forward; the retrofit just establishes the
  5-year baseline.

### v2.7 changelog (April 2026 — 5-year baselines + quarterly-letter substitution)
- **Extended Core Rule #19 with quarterly-letter substitution**.
  Three publication patterns explicitly defined:
  - **Pattern A (annual letter publishers)**: BRK, JPM, Markel,
    Constellation Software → fetch 5 annual letters
  - **Pattern B (quarterly letter publishers)**: DASH, SHOP, NFLX,
    Spotify, CPNG → fetch all 4 quarterly letters × 5 years (up
    to 20 letters); Q4 letter gets primary annual-wrap weight,
    Q1–Q3 add intra-year directional color
  - **Pattern C (no standalone letter)**: fall back to chairman's
    letter in annual report or DEF 14A introductory letter
  This was added because the BRK.B v2.6 ingest assumed the BRK
  pattern would generalize, but the DASH v2.6 application
  immediately surfaced that DoorDash publishes quarterly letters
  not annual ones — and the SHOP v2.7 application confirmed
  Shopify follows the same Pattern B convention. The substitution
  rule prevents the agent from incorrectly logging a "no letters
  available" gap when the company publishes quarterly instead.
- **Extended Core Rule #20 with 5-year 10-K baseline + 5-Year
  Risk Factor Evolution Arc**. Workflow A now fetches the **last 5
  annual 10-K filings** (parallel to the 5-year letter rule), not
  just the most recent. Synthesis adds a `### 5-Year Risk Factor
  Evolution Arc` subsection within Section 8 — chronological table
  of which Item 1A risks were added/removed/re-worded across the
  5-year window. Rationale: Risk Factor *evolution* is a leading
  indicator of management's worldview shift — risks often appear
  in Item 1A 1–2 years before they show up in earnings (e.g.
  gig-worker classification language in 2018–2020 ride-share
  10-Ks; AI-disruption risk language in 2022–2024 software 10-Ks;
  supply-chain risk in 2020–2021 manufacturing 10-Ks). The
  multi-year arc surfaces this; a single-year snapshot does not.
- **Workflow A Step 2** updated: 10-K fetch is now "Last 5 annual
  10-K filings" instead of "Latest 10-K." Files named by fiscal
  year covered: `filings/[TICKER]-10K-FY[YYYY].pdf` (or `.htm`).
- **Workflow A Step 4** synthesis instructions updated to require
  multi-year MD&A context in §2 and the 5-Year Risk Factor
  Evolution Arc in §8.
- **SHOP**: First ticker built under v2.7. Pattern B applied
  (Tobi Lütke does not publish standalone annual letters; quarterly
  letters from FY2020–FY2025 + 2015 IPO Letter + April 2025
  "AI is non-optional" memo). Multi-year 10-K segment evolution
  table added to §2 (Subscription Solutions reaccelerated 2023→2025
  from price + Plus mix; Merchant Solutions increasingly the
  growth engine). Section 6 RMC subsection surfaces the cleanest
  Tobi-Lütke intrinsic-value signal in 11 years of public-company
  history: the **first-ever $2B share buyback authorized at the
  $125–135 zone (Feb 2026)**.
- **Pending follow-up**: 32 remaining tickers still need v2.6+v2.7
  primary-source synthesis retrofit. BRK.B (v2.6 source ingest),
  DASH (v2.6), SHOP (v2.7) are the three completed examples.
  Batch retrofit approach (5–7 parallel agents) recommended.

### v2.8 changelog (April 2026 — synthesis discipline + page output quality)

User review of the v2.7 SHOP output surfaced several quality issues
common across v2.6/v2.7 enrichments. v2.8 codifies the corrections.

- **Added Core Rule #21: Synthesis over transcription.** Primary
  sources are inputs, not outputs. Verbatim quotes are valuable
  only when paraphrase would weaken the insight. Multi-row
  chronological tables of source extracts (like the v2.7 "5-Year
  Risk Factor Evolution Arc" table) typically add bulk without
  edge — replace with 2–4 sentence synthesis paragraphs.
- **Added Core Rule #22: Ticker-page output discipline.** Three
  conventions:
  - No CLAUDE.md self-references (*"Per CLAUDE.md v2.X Core Rule #N"*)
    in ticker page bodies. Schema enforcement is internal; light
    references in changelog entries are fine.
  - No retrospective / *"corrected from"* / *"prior framing"*
    language in pages. Git history is the audit trail.
  - Table orientation discipline: time in columns, metrics in
    rows. Bullet-point preference for sentences with 3+ data points.
- **Added Core Rule #23: Section consolidation — moat lives in
  Section 5 only.** The standalone "Moat Assessment" block between
  Business Overview and Pivotal Question is retired. Summary keeps
  a one-line moat verdict; all detail lives in Section 5.
- **Added Core Rule #24: Competitive landscape integration in
  Section 5.** Moat without competitor context is incomplete.
  Section 5 must include a `### Competitive Landscape` subsection
  with named peers + market share + 1–2 sentence read on each
  peer's moat / threat vector + explicit framing of how this
  company's moat differs and what evidence supports it. Apply
  judgment by ticker — Berkshire has no peer comparison; Shopify
  / DoorDash / Coupang warrant fuller tables.
- **Added Core Rule #25: Risk Factor materiality filter.**
  Modifies/supplements Rule #20. Drop universal corporate
  boilerplate (every-company risks like generic earnings
  fluctuation, generic payments regulation, generic cyber).
  Keep risks that are: (a) materially differentiated from peers,
  (b) not yet priced into the multiple — *and explicitly state
  "not priced in"* in the Notes column when so, (c) tied to a
  specific thesis-break trigger, OR (d) tied to a specific
  large discretionary investment with uncertain outcomes (e.g.
  multi-billion-dollar capex bet, in-flight integration).
  5-Year Risk Factor Evolution Arc collapsed from table to
  synthesis paragraph (per Rule #21).
- **Added Core Rule #26: Risk/Reward calculation discipline.**
  R/R figures cited in Summary, Section 14, and watchlist must
  anchor to the same Section 13 scenario set on the ticker page.
  Standard convention: Bull / Bear from §13 midpoints. Multiple
  Bull tiers stated explicitly. Watchlist 3-column Price Targets
  template collapses 4-scenario sets via probability-weighted
  Bull blend so PW EV reconciles to the canonical Section 13
  number.
- **Pending application**: SHOP refactor under v2.8 happens in
  the same session. The other 31 tickers (32 minus SHOP) need
  the v2.6+v2.7+v2.8 retrofit batch.

### v2.9 changelog (April 2026 — section consolidation: 15 → 13 sections)

User review of the v2.8 SHOP output identified two structural
duplications: Section 1 ("Why Does This Company Exist? + Pivotal
Investment Question") was redundant with the Business Overview +
Pivotal Investment Question header subsections, and Section 3
("Geographic Revenue Mix") + Section 4 ("Revenue Mix & Business
Model") covered the same conceptual ground (revenue composition).

- **Section 1 retired.** Founding insight content lives in
  Business Overview (header subsection); the Pivotal Investment
  Question is its own header subsection between Moat verdict and
  Key Stats Snapshot.
- **Sections 3 + 4 merged into new Section 2 ("Revenue Mix &
  Geographic Split")** covering revenue streams + business model
  + geographic split + forward-looking shifts in one place.
- **Sections renumbered**: old 5–15 → new 3–13. The 13-section
  structure is the new canonical layout. Cross-references in all
  Core Rules (#14, #17, #18, #20, #25, #26, #19) updated to the
  new numbering. Workflow A Step 5 file structure and Workflow B
  Step 3a section-refresh checklist updated.
- **Cross-section references that changed** (most thesis-relevant):
  - Bull/Bear/Base scenarios: was Section 13 → now Section 11
  - PW EV: was Section 14 → now Section 12
  - Recommendation & Bottom Line: was Section 15 → now Section 13
  - Catalyst & Sentiment Tracker: was Section 11 → now Section 9
  - BAIT Framework: was Section 12 → now Section 10
  - Key Risks: was Section 8 → now Section 6
  - Competitive Moat & Landscape: was Section 5 → now Section 3
  - Management & Leadership: was Section 6 → now Section 4
- **Application**: SHOP and DASH both refactored under v2.9 in
  the same session as the schema bump. The 30 remaining tickers
  need v2.6+v2.7+v2.8+v2.9 retrofit (the structural renumbering
  is the most disruptive piece — recommend one-pass per ticker
  applying all four schema versions together).

### v2.10 changelog (April 2026 — retire `wiki/log.md`)

User review identified that `wiki/log.md` was duplicative of the
per-ticker `changelog.md` audit trail and added writing burden to
every workflow without providing analytical value. Per-ticker
`changelog.md` already captures the substantive event log for each
ticker, and commit messages capture cross-cutting / schema-only
events. The session-wide `LOG [YYYY-MM-DD HH:MM] [ACTION]` format
was a grep-friendly artifact from v1 that has not earned its keep
in v2 practice.

- **Retired**: `wiki/log.md` and the entire "log.md Format" section
  (ACTION verbs INIT / INGEST / UPDATE / WEEKLY / LINT / FETCH /
  PRICE / REPORT / SCHEMA / PUSH / DELETE / PAUSE / RESUME).
- **Core Rule #5 rewritten**: now states that per-ticker
  `changelog.md` is the only event log; cross-ticker / schema-only
  events live in commit messages.
- **Core Rule #10** (push discipline) updated: push failures surface
  to the user (and to the affected ticker's `changelog.md` if
  mid-Workflow-B) rather than to `log.md`.
- **Workflow A Step 7**: removed the `wiki/log.md` line.
- **Workflow B Step 5 (was "Log") and Step 6 (Commit)**: collapsed
  into a single "Step 5 — Commit and push."
- **Workflow C.1 / C.2**: removed `LOG ... PAUSE` and `LOG ...
  RESUME` append steps; renumbered remaining steps.
- **Schema Co-Evolution**: removed the `LOG ... SCHEMA ALL` and
  `LOG ... PUSH ALL` append steps; commit message is now the
  schema-level audit trail.
- **Directory layout diagram**: removed `log.md` from the
  `wiki/` tree.
- **File deletion**: `wiki/log.md` deleted in the same commit as
  the schema bump. Historical content preserved in git history.

Historical references to `log.md` in earlier v2 changelog entries
(v2.1, v2.5) are left intact as they describe the schema state at
that version. They do not imply current-state behavior.
