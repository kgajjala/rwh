# BRK.B — Changelog

## [2026-04-26] — v2.8 Refactor (synthesis discipline + page output quality)

**Trigger**: Apply CLAUDE.md v2.8 schema (Core Rules 21–26) to BRK.B page. No new earnings event; this is a quality refactor of the v2.6 primary-source synthesis baseline established 2026-04-25.

**Sources reviewed**:
- [Yahoo Finance — BRK-B](https://finance.yahoo.com/quote/BRK-B) — live price re-verified at $469.32 (Apr 24 close; after-hours $471.00)
- No new primary-source filings or letters since 2026-04-25 baseline (next earnings/letter event is May 3, 2026)

### What Changed
- **Header**: Schema v2.5 → **v2.8**; Last Updated 2026-04-25 → **2026-04-26**.
- **Summary**: Tightened to 10 emoji-tagged bullets including a one-line moat verdict ("Wide and structurally peerless") per Rule #23. R/R now stated as ~2.8:1 anchored to Section 13 Bull/Bear midpoints (Rule #26).
- **Standalone "Moat Assessment" block REMOVED** between Business Overview and Pivotal Question (Rule #23). All moat detail consolidated into Section 5 only.
- **Section 2** (Annual Financial Metrics): Broadened "Primary Source: 10-K Segment Detail" subsection from FY2025-only single-year to **multi-year MD&A** (FY2023 → FY2025) with time-in-columns table per Rule #22. Multi-year synthesis preserved as 4-bullet prose, not row-by-row source extracts.
- **Section 5** (Competitive Moat): Added new `### Competitive Landscape` subsection per Rule #24. For BRK.B specifically, calls out structural uniqueness ("no direct comparable in U.S. public markets") with a tight 4-row analogue table (Markel, Fairfax, Loews, large-cap bank insurance peers) framing what's similar / what's different. Tail-risk read confirms BRK's competitive risks are *internal* (succession, cash drag, GEICO) not external.
- **Section 8** (Key Risks): Applied Rule #25 materiality filter — dropped boilerplate (rate-cut compression, equity-portfolio mark-to-market, generic Apple-stake risk) and kept the 7 risks that are differentiated for BRK, not fully priced, or tied to a thesis-break trigger. Each row now has explicit "Differentiated" / "Not fully priced" / "Tied to thesis-break trigger" notes. **Replaced any prior 5-Year Risk Factor Evolution table with a 3-sentence synthesis paragraph** (Rule #21) covering PacifiCorp wildfire language escalation FY2020 → FY2024, succession-execution risk formalization FY2023–FY2024, and GEICO competitive lag handled via MD&A not Item 1A.
- **Section 6** (RMC + 5-Year Capital Allocation Arc): **Letter arc table preserved** (the multi-year strategic context is the analytical edge; preserved per Rule #21 explicit carve-out). Verbatim Buffett/Abel quotes consolidated; investment-relevance bullets retained.
- **Sections 11, 13, 14, 15**: Light refresh — May 3 meeting now "7 days away" (vs. "1 week away"); Section 14 Interpretation now explicitly states R/R ~2.8:1 anchored to Section 13 (Rule #26). No price/scenario changes — primary-source baseline unchanged since 2026-04-25.
- **Output discipline (Rule #22)**: Removed "Per CLAUDE.md v2.6 Core Rule #19" self-reference from Section 6 RMC subsection. No retrospective / "corrected from" language. Tables verified time-in-columns / metrics-in-rows where applicable.
- **Sources & Citations** section retained.

### Thesis Status
- **Overall**: 🟡 **Unchanged** — this is a presentation refactor, not a thesis update. Underlying primary-source synthesis from 2026-04-25 v2.6 enrichment remains the baseline.
- **BAIT lens**: Unchanged — Triple BAIT (B+I-Strong, A-Moderate).
- **Price target**: Unchanged — PW EV ~$543 over 3yr; R/R ~2.8:1 (Bull $650 / Bear $405 vs. spot $469.32).

### Recommendation
- **For a non-holder**: 🟢 **Initiate (small/scaled)** — unchanged.
- **For a current holder**: 🟢 **Hold-Add** — unchanged.

**Next review trigger**: 📅 **May 3, 2026** — Annual Shareholder Meeting + Q1 2026 earnings (Abel's first as CEO). Material-event update per Workflow B Step 3a expected that weekend.

**Note on raw/ folder**: Primary source PDFs cited throughout (5 letters, 10-K, 10-Q, press releases) are referenced via canonical URLs at berkshirehathaway.com and SEC EDGAR; local `raw/BRK.B/{shareholder-letters,filings,...}` mirroring is a pending follow-up gap from the v2.6 ingest and does not block synthesis since URL citations are stable.

---

## [2026-04-25] — v2.6 Primary-Source Enrichment (10-K + 6 Shareholder Letters)

**Trigger**: User request to incorporate primary-source data from the actual SEC 10-K and the last 5+ years of annual shareholder letters into the analysis.

**Sources reviewed (additions to v2.5 baseline)**:
- [Buffett FY2020 Letter](https://www.berkshirehathaway.com/letters/2020ltr.pdf) — "American Tailwind"; record $24.7B buybacks
- [Buffett FY2021 Letter](https://www.berkshirehathaway.com/letters/2021ltr.pdf) — $27B record buybacks
- [Buffett FY2022 Letter](https://www.berkshirehathaway.com/letters/2022ltr.pdf) — buyback discipline ("stupid if done at a premium")
- [Buffett FY2023 Letter](https://www.berkshirehathaway.com/letters/2023ltr.pdf) — Munger tribute; "secret sauce" = time; BNSF century quote
- [Buffett FY2024 Letter](https://www.berkshirehathaway.com/letters/2024ltr.pdf) — final letter; Abel succession announcement; "tailwinds are gone"
- [Abel FY2025 Letter](https://www.berkshirehathaway.com/letters/2025ltr.pdf) — first Abel letter; "intentional and deliberate"; operational margin quantification
- [Berkshire 2025 10-K](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) MD&A segment detail (via [SEC EDGAR-indexed sources](https://stansberryresearch.com/whitney-tilsons-daily/my-analysis-of-berkshire-hathaways-fourth-quarter-and-full-year-2025-earnings))

### What Changed
- **Section 2** (Annual Financial Metrics): Added "Primary Source: 10-K Segment Detail (FY2025)" subsection with precision figures from MD&A — BNSF operating margin +250bps to 34.5% (vs. 32.0% in 2024); BHE after-tax earnings +$249M / +6.7% (driven by PacifiCorp wildfire reserve normalization); GEICO –$1B explicitly framed as +$1.4B intentional ad acceleration; insurance underwriting profit –20% FY (vs. just –54% Q4 in v2.5 narrative). Updated FY2024/FY2025 revenue precision to $371.43B / $371.44B.
- **Section 5** (Competitive Moat): Added verbatim Buffett FY2023 quotes — float "continues to come at no cost," BNSF "century from now" quote, "secret sauce" = time framing.
- **Section 6** (Management & Leadership): Added Buffett's verbatim FY2024 endorsement of Abel ("a great manager, a tireless worker and an honest communicator"; "vividly shown his ability to act"). Added new `### Recent Management Commentary — Primary Source Synthesis` subsection containing: (a) verbatim quotes from all 6 letters mapped to investment relevance; (b) 5-Year Capital Allocation Philosophy Arc table; (c) three-observation synthesis on what the arc reveals about the succession discount. Per CLAUDE.md v2.6 Core Rule #19.
- **Section 7** (Strategic Growth Initiatives): Renumbered from prior Section 8 to align with wiki schema (was incorrectly using kg-investment-analysis skill numbering).
- **Section 8** (Key Risks): NEW section added — was missing in v2.5 ingest. Standard Impact × Probability × Priced-In table with 9 risks; flags PacifiCorp wildfire re-escalation and Abel hesitation as the two highest-impact / least-priced risks worth tracking.
- **Summary section**: Added new bullet calling out the 5-year letter arc and Abel's operational quantification as the primary-source signal.
- **Sources & Citations**: Added new "Shareholder letters (5-year baseline + Abel's first)" subsection with all 6 letter URLs + letters index.

### Thesis Status
- **Overall**: 🟢 **Strengthened** vs. v2.5 — primary-source synthesis confirms continuity of Buffett's framework under Abel; March 2026 buyback is internally consistent with FY2022 + FY2025 letter discipline. The "succession discount" is *measurably* unwarranted on framework grounds.
- **BAIT lens**: Unchanged — Triple BAIT (B+I-Strong, A-Moderate); informational edge sharpened by primary-source confirmation.
- **Price target**: Unchanged — PW EV ~$543 over 3yr.
- **New finding**: Abel's *"each percentage point of margin = ~$230M of incremental cash flow"* quantification is a **genuinely new compounding lever** Buffett never explicitly articulated. BNSF's 2025 +250bps margin gain alone implies ~$575M of Year-1 lift on Abel's framework. Modest upside vs. v2.5 base case.

### Recommendation
- **For a non-holder**: 🟢 **Initiate (small/scaled)** — strengthened by primary-source confirmation
- **For a current holder**: 🟢 **Hold-Add** — unchanged

**Next review trigger**: 📅 May 3, 2026 — Annual Shareholder Meeting + Q1 2026 earnings (Abel's first as CEO).

---

## [2026-04-25] — v2.5 Initial Ingest

**Trigger**: User-requested first-run ingest under Workflow A (full Mode A 15-section deep dive). New ticker added to wiki coverage.

**Sources reviewed**:
- [Berkshire Hathaway 2025 Annual Report / 10-K (filed Mar 2, 2026)](https://www.berkshirehathaway.com/2025ar/2025ar.pdf)
- [Q4 2025 Press Release (Feb 28, 2026)](https://www.berkshirehathaway.com/news/feb2826.pdf)
- [Greg Abel's First Shareholder Letter (Feb 28, 2026)](https://www.berkshirehathaway.com/letters/2025ltr.pdf)
- [Q3 2025 10-Q (Nov 2025)](https://www.berkshirehathaway.com/qtrly/3rdqtr25.pdf)
- [Yahoo Finance — BRK-B (live price verified at $469.32 on 2026-04-24 close)](https://finance.yahoo.com/quote/BRK-B)
- [Stock Analysis — BRK.B financials](https://stockanalysis.com/stocks/brk.b/financials/)
- 13F filings (Q3 2025, Q4 2025) via [13F.info](https://13f.info/13f/000119312525282901-berkshire-hathaway-inc-q3-2025) and [Alert Invest](https://alert-invest.com/top-investors/warren-buffett-portfolio-13f/)

### What Changed
- **New wiki page created**: `wiki/tickers/BRK.B/BRK.B.md` (single consolidated page covering Summary + Business Overview + Moat + Pivotal Question + Key Stats + 15-section thesis with embedded financial tables, per Schema v2.5).
- **Summary section** (Rule #18): 10 bullets distilled from Sections 1–15 with emoji vocabulary per Rule #17.
- **Status**: Active (default for new ingest).
- **Initial state captured**:
  - Live price $469.32 (–13.4% from 52-wk high $542.07; +0.9% above 52-wk low $455.19)
  - Market cap ~$1.01T
  - FY2025 revenue $371.4B (flat YoY)
  - FY2025 operating earnings $44.5B (–6% YoY vs. $47.4B in 2024)
  - FY2025 net earnings $67.0B
  - Cash + Treasuries $373.3B at YE2025 ($321B in T-bills)
  - Insurance float $176B (+$5B YoY; record)
  - Equity portfolio $274B at Q4 2025 (top 5: AAPL 22.6%, AXP 20.5%, BAC 10.4%, KO 10.2%, CVX 7.2%)
  - P/E TTM 15.1× (below 5-yr range of 17–22×)

### Thesis Status
- **Overall**: 🟡 Initial — Triple BAIT overlap (B+I-Strong, A-Moderate); succession-anxiety drawdown is a rare cost-basis opportunity in a >$1T fortress.
- **BAIT lens**:
  - **B (Behavioral)**: 🟢 Strong — succession discount despite 2× operating earnings 2021–2025
  - **A (Analytical)**: 🟡 Moderate — 15.1× TTM is below historical band, but 2025 op-earnings declined 6% so the analytical edge requires confidence in 2026 stabilization
  - **I (Informational)**: 🟢 Strong — March 4, 2026 buyback resumption (first since May 2024) at ~$465–490 zone is the cleanest insider-judgment signal at $1T-cap
  - **T (Technical)**: 🟡 Moderate — at 52-wk low band; buyback resumption provides soft floor; no mechanical catalyst
- **Price target**:
  - Bull (3yr, 30%): $620–680
  - Base (3yr, 45%): $530–570
  - Bear (3yr, 25%): $380–430
  - **PW EV: ~$543** (3-yr); +15.7% absolute / ~5%/yr price + ~2%/yr buyback uplift = ~6–7%/yr total
- **Catalyst & Sentiment delta**: First-time capture. Annual meeting May 3, 2026 + Q1 2026 earnings same weekend = next inflection.

### Recommendation
- **For a non-holder**: 🟢 **Initiate (small/scaled)** — at $469.32, cost basis at bottom of 52-wk range with Abel buyback functionally setting soft floor. Scale into position over 3–6 months.
- **For a current holder**: 🟢 **Hold-Add** — adding on weakness toward $455 is high-conviction; structural quality unchanged.
- **Attractive entry**: $455–480 (matches Abel's resumed buyback zone)
- **Trim zone**: $560–620 (~18–19× TTM EPS; above historical band)
- **Exit / avoid**: $700+ (>22× TTM EPS without confirmed deployment inflection)

### Thesis-Break Triggers
- ⚠️ No material buybacks for 4 consecutive quarters (2026 Q1–Q4) AND cash position grows above $400B → "trapped capital" narrative
- ⚠️ GEICO operating earnings decline accelerating (–$2B+ YoY) OR insurance underwriting profit goes negative
- ⚠️ Major Abel-led acquisition at price >2× book / >18× normalized earnings (capital allocation discipline question)

**Next review trigger**: 📅 **May 3, 2026 — Annual Shareholder Meeting + Q1 2026 earnings (same weekend)**. First full disclosure cycle under Abel.
