# DASH — Changelog

*Append-only. Most recent entry first.*

---

## [2026-04-29] — Schema v2.13 Summary migration + price refresh

**Trigger**: Manual format migration to v2.13 Rule #18 Summary block (4-part structure: thesis+verbs · 8-col scenario table · 6-cell KPI strip · 3+3 Why/Why-not bullets one-per-line). Live price re-verified.

**Sources reviewed**: [stockanalysis.com — DASH live quote](https://stockanalysis.com/stocks/dash/) (intraday 2026-04-29).

### What Changed
- Header: Schema v2.9 → v2.13; Last Updated 2026-04-25 → 2026-04-29; live price $176.78 (4/24) → **$169.33 (4/29, –1.54% session)**.
- §0 Summary: rebuilt in v2.13 4-block structure. Scenario table surfaces R/R explicitly (~0.4:1 at spot, anchored to §11 Bull $215 / Bear $50 5-yr terminals per Rule #26). KPI strip slots 4–5 carry US share (60–67%) + subscriber base (35M, +59%) — most thesis-relevant for a three-sided marketplace.
- No section content (§1–§13) altered — pure format migration plus price-line refresh. Thesis, scenarios, recommendation, and zones all unchanged from 2026-04-25 baseline.

### Thesis Status
- **Overall**: Unchanged. Watch (non-holder, $140–155 entry) / Hold (current holder).
- **BAIT delta**: Unchanged — Double overlap (B+A+I Mod, T Weak), Conviction Low-Moderate.
- **Price target delta**: Unchanged — Bull $215 / Base $110 / Bear $50 (5-yr terminals); PW EV ~$130.
- **Catalyst & Sentiment delta**: Price drifted from $176.78 (4/24) → $169.33 (4/29) = –4.2% over 5 sessions; not material on its own.

### Recommendation
- **For a non-holder**: 🟡 Watch — entry $140–155 unchanged.
- **For a current holder**: 🟡 Hold — pre-Q1 (May 6) discipline unchanged.

**Next review trigger**: Q1 2026 earnings — May 6, 2026 (post-close). Hard catalyst.

---

## [2026-04-25] — v2.7+v2.8+v2.9 Combined Refactor (5-yr 10-Ks + Pattern B letters + synthesis discipline + structural consolidation)

**Trigger**: DASH selected as the second ticker (after SHOP) to validate the v2.9 13-section structure on a different business model. Combined application of v2.7 (5-year 10-K + Pattern B quarterly letter baselines), v2.8 (synthesis-over-transcription, ticker-page output discipline, materiality filter, competitive landscape integration), and v2.9 (15 → 13 section consolidation) in one pass.

### What Changed
- **Schema header bumped** from v2.6 → v2.9 (skipped v2.7+v2.8 individual stamps; one pass).
- **Summary**: Added Moat verdict bullet (Narrow); existing primary-source signal bullet preserved with cleaner phrasing.
- **Business Overview**: Bullet-ified extensively. Replaced 2 text-heavy paragraphs with structured bullets covering scale, geographic footprint, revenue model, and 2025 transformation summary. Added explicit founding-insight context that was previously buried in Section 1.
- **Standalone "Moat Assessment" block** between Business Overview and Pivotal Question: REMOVED (Rule #23). All moat content now lives in new Section 3 only.
- **Section 1 (Why Does This Company Exist? + Pivotal Investment Question)**: REMOVED per Rule #23 (v2.9). Founding insight folded into Business Overview; Pivotal Question retained as a header subsection.
- **Sections 3 + 4 merged into new Section 2 ("Revenue Mix & Geographic Split")** per v2.9 — single section with revenue streams table + key operating leverage commentary + multi-year geographic split table (FY2022–FY2026E) showing the international % step-change from 12% → 28-30% post-Deliveroo full year.
- **Section 3 (Competitive Moat & Landscape)**: New combined section per Rule #24. Moat sources table + new comprehensive Competitive Landscape subsection with US food-delivery share table (DoorDash 60-67%, Uber Eats 22-25%, Grubhub 7-10%, Instacart, Amazon Fresh) + International landscape table by region (Wolt + Deliveroo positioning vs. Just Eat, Uber Eats, Talabat, foodpanda, Meituan, Coupang Eats, etc.) + 4 evidence-backed differentiators of DASH's moat vs. peers + tail-risk read flagging Instacart cross-category escalation as the under-priced competitor risk.
- **Section 6 (Key Risks, was Section 8)**: Restructured per v2.8 Rule #25 materiality filter. Removed 7 universal corporate boilerplate rows (quarterly fluctuation, profitability sustainability, growth deceleration, systems failures, merchant dependency, third-party reliance, generic founder dependency). Renamed `Source` column → `Priced In?` column with explicit Partially / Yes / Not flagging per row. Added 2 new rows per Rule #25(d): "Multi-billion-dollar Deliveroo + SevenRooms integration with uncertain outcome" (Partially priced — Wolt precedent provides mitigation) and "Instacart cross-category escalation" (Not priced in — could acquire/partner with restaurant-delivery player). 5-Year Risk Factor Evolution Arc collapsed from table to 1-paragraph synthesis per Rule #21.
- **Sections renumbered**: old 5-15 → new 3-13.
- **Removed all "Per CLAUDE.md v2.X Core Rule #N" lines** from page body per Rule #22 (Section 2 segment detail subsection, Section 4 RMC subsection, Section 6 risks intro, Sources). Light references retained in changelog only.
- **Cross-references updated**: "Section 8 risk" → "Section 6 risk"; "see Section 11" → "see Section 9".
- **Recent Quarterly Trend table**: was already in time-in-columns / metrics-in-rows format from prior v2.6 ingest — no change needed for orientation.

### Thesis Status
- **Overall**: Unchanged. PW EV $130, Double BAIT, Low-Moderate conviction, Watch / Hold (entry $140-155) all preserved. The v2.9 refactor is a structural / quality refinement, not a thesis revision.
- **New analytical edge surfaced** by Competitive Landscape subsection: explicit framing of DASH as the only delivery platform building horizontally across food + grocery + retail + restaurant CRM simultaneously — Uber Eats is rides-led, Grubhub is restaurant-only, Instacart is grocery-only. The vertical-depth differentiator is the cleanest moat argument and is implicit in consensus models but not articulated.
- **Materiality-filtered Section 6** elevated 2 risks consensus does not assign material probability to: Deliveroo integration (Wolt precedent provides mitigation) and Instacart cross-category escalation. Both should be tracked actively.

**Next review trigger**: 📅 **May 6, 2026 — Q1 2026 earnings (post-close)**. First print under Deliveroo full consolidation; H2 2026 grocery/retail commentary will set the FY2026 thesis test.

---

## [2026-04-25] — v2.6 Primary-Source Enrichment (5 Letters + 10-K MD&A)

**Trigger**: First Workflow B refresh after CLAUDE.md v2.6 schema bump (Core Rules #19 + #20). DASH used as the test case to validate that v2.6's primary-source synthesis depth requirements work on a non-Berkshire ticker with a different management voice (Tony Xu) and a different document mix (single-segment marketplace vs. holding company).

**Sources reviewed (additions to v2.5 baseline, all primary)**:
- [Tony Xu IPO Letter / S-1 (Dec 2020)](https://www.sec.gov/Archives/edgar/data/1792789/000119312520292381/d752207ds1.htm) — founding mission verbatim
- [Tony Xu FY2022 Letter (Feb 16, 2023)](https://www.sec.gov/Archives/edgar/data/1792789/000162828023003889/dashq42022ex991.htm) — Wolt rationale verbatim
- [Tony Xu FY2024 Letter (Feb 11, 2025)](https://www.sec.gov/Archives/edgar/data/1792789/000162828025004877/dashq42024ex992-shareholde.htm) — explicit 4-principle framework
- [Tony Xu FY2025 Letter / Q4 2025 release (Feb 18, 2026)](https://ir.doordash.com/news/news-details/2026/DoorDash-Releases-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx) — Deliveroo *"massive and expensive undertaking"*
- [Q4 2025 Earnings Call Transcript (Feb 18, 2026)](https://www.fool.com/earnings/call-transcripts/2026/02/18/doordash-dash-q4-2025-earnings-call-transcript/) — Deliveroo early-proof + DashPass + autonomous + AI commerce
- [DoorDash 10-K FY2024 (HTML)](https://www.sec.gov/Archives/edgar/data/1792789/000162828025005715/dash-20241231.htm) — Item 1A Risk Factors verbatim
- [DoorDash 10-K FY2025 — StockTitan summary](https://www.stocktitan.net/sec-filings/DASH/10-k-door-dash-inc-files-annual-report-16ce41338de6.html) — Item 1A Risk Factors verbatim (10 verbatim quotes)

### What Changed
- **Schema header**: Bumped DASH page to v2.6.
- **Section 2** (Annual Financial Metrics): Added `### Primary Source: 10-K Segment Detail (FY2025)` subsection per Rule #20 — verbatim 10-K MD&A commentary on segment performance, Deliveroo accounting (intangible categories), DashPass economics, New Verticals trajectory, tech-stack consolidation. Added "What this changes vs. aggregator-only data" 3-bullet synthesis flagging the Q4 FCF compression as integration cost (not deteriorating economics), Tony Xu's *"slightly higher than 2025, excluding Deliveroo"* expectation-setter, and the under-reported 35M subscriber count (+59% YoY).
- **Section 6** (Management & Leadership): Added `### Recent Management Commentary — Primary Source Synthesis` subsection per Rule #19 — verbatim quotes from 5+ letters (IPO + FY2022 + FY2024 + FY2025 + Q4 2025 call) mapped to investment relevance + 5-Year Strategic Framework Arc table + three-observation synthesis. Key insight: the Tony Xu 4-principle framework + Wolt-precedent execution + explicit 2026 expectation-setting *materially reduces* the integration-risk discount currently priced.
- **Section 8** (Key Risks): Restructured per Rule #20 — every row now has a `Source` column flagging whether it's derived from verbatim 10-K Item 1A language, MD&A commentary, or analyst speculation. Added 5 new rows from verbatim Item 1A (quarterly fluctuation, profitability sustainability, growth deceleration, systems failures, merchant dependency) that the v2.5 ingest had missed. Existing rows enriched with verbatim quotes. **Integration risk re-rated**: Wolt is now positive precedent (lowered conjunctive failure probability from 20% → 12–15%). Risks tagged `*[Analyst speculation]*` for transparency.
- **Summary**: Added new 📈 bullet calling out the primary-source signal arc (Tony Xu *"massive and expensive undertaking"* expectation-setting + Wolt precedent + Deliveroo *"growing much faster than expected"* + H2 2026 grocery/retail unit-economics inflection as dominant 2026 catalyst).
- **Sources & Citations**: Restructured into "Primary sources (per CLAUDE.md v2.6 Rules #19 + #20)" + "Tony Xu shareholder letters" + "Coverage and context" + "Live market data" buckets.

### Thesis Status
- **Overall**: 🟢 **Strengthened** vs. v2.5 — the 5-year letter arc demonstrates that the Deliveroo acquisition is internally consistent with the FY2020 founding mission and the FY2022 Wolt playbook (positive precedent), not strategy drift. The –38% drawdown is more time-discount than fundamental-deterioration.
- **BAIT lens**: B+I-Strong now slightly stronger; A unchanged; T unchanged. Conviction ticks from Low-Moderate to **Moderate**.
- **Price target**: Unchanged numerically, but the integration-risk probability re-rate suggests modest tilt to base case from bear case in Section 13/14.
- **New finding**: Tony Xu's explicit framing that FY2026 EBITDA margin will be *"slightly higher than 2025, excluding Deliveroo"* is the most precise expectation-setter in the disclosure cycle and is meaningfully more bullish than the aggregator narrative of "soft 2026 guide."

### Recommendation
- **For a non-holder**: 🟡 Watch — entry zone $140–155 unchanged; primary-source confirmation modestly tightens the entry-zone discipline.
- **For a current holder**: 🟡 **Hold (with bias-to-Add at $155 or below post-Q1)** — strengthened by primary-source confirmation but Q1 2026 print on May 6 is the binary catalyst.

**Next review trigger**: 📅 **May 6, 2026 — Q1 2026 earnings (post-close)**. First print under Deliveroo full consolidation; H2 2026 grocery/retail commentary will set the FY2026 thesis test.

### Test of v2.6 Schema
- **Rule #19 application worked cleanly on a non-Berkshire ticker**: Tony Xu's 4-principle framework + 5-year letter arc surfaced a nuance (Wolt-precedent execution as integration-risk mitigant) that the v2.5 page missed.
- **Rule #20 application worked cleanly with a non-Buffett-style 10-K**: DASH's Risk Factors are clearly enumerated; the verbatim Item 1A integration into Section 8 surfaced 5 risks the v2.5 ingest had missed and provided clean source attribution.
- **The "PDF binary fallback" path was used**: SEC HTML 10-K fetch returned 403; fall-back to StockTitan's structured 10-K summary worked, and the underlying 10-K is cited as the source per Rule #20.

---

## [2026-04-24] — v2.1 Full Re-Ingest (Workflow A) — Fresh Analysis

**Trigger**: User requested fresh report on DASH under the updated v2.1 schema (position-agnostic, single-page consolidated wiki). Prior v1 multi-file structure (overview.md, thesis.md, financials.md) consolidated and deleted; superseded by single `DASH.md`.

**Sources reviewed**:
- Yahoo Finance live chart API (live price $176.78, 52-wk $143.30–$285.50; Apr 24, 2026 intraday; previous close $187.22 = –5.6% session)
- MarketBeat, TipRanks, Public.com (analyst consensus: 34 Buy / 10 Hold / 0 Sell; median target ~$252–278)
- Recent analyst actions: Stifel PT cut $215 → $185 (Apr 10); Bernstein new Buy (Apr 13); MoffettNathanson PT cut $279 → $276 (Apr 14); JPMorgan Buy maintained (Apr 15)
- secform4.com, stocktitan.net (Form 4 filings): Stanley Tang sold 23,125 @ $150 on Apr 2 (unusual — at 52-wk low); Andy Fang, Keith Yandell, Stanley Tang RSU grants Apr 20 (routine)
- Fintel (short interest): 3.45% of float, ~13.17M shares; peer avg 11.07% (DASH is under-shorted)
- DoorDash IR (Q1 2026 earnings date: May 6, 2026 post-close; BusinessWire 2026-04-09)
- DoorDash 10-K FY2025 filed Feb 18, 2026 (SEC EDGAR CIK 1792789; 31,400+ employees, 40+ countries, 9M+ Dashers earned >$20B in 2025)
- Q4 2025 / FY2025 results: Revenue $3.96B Q4 / $13.72B FY; Adj EBITDA $780M Q4 / $2.78B FY; GAAP NI $213M Q4 / $935M FY; orders 903M Q4 (+32%); MAU 56M; subs 35M
- Prior wiki ingest (raw/analyses/DoorDash_Fundamental_Analysis.md.pdf, Mar 2026)

### What Changed from Prior Entry (2026-04-06)

- **Live price**: Unchanged net ($176 → $176.78) but with violent session (–5.6% on Apr 24 from $187.22)
- **52-week high/low**: High unchanged at ~$285 (Oct 2025). Low now $143.30 (set in March 2026) — stock has re-tested lows and recovered modestly
- **Analyst consensus**: Has meaningfully widened: Stifel now at $185 (effectively "fair value here"), median still $252–278. The dispersion signals genuine analytical disagreement, not consensus conviction
- **Insider signal**: Stanley Tang's Apr 2 sale at $150 (52-wk low) is a new data point — the cleanest negative insider signal to date. Alfred Lin's prior $100M buy still dominates in dollar terms
- **Q1 2026 earnings confirmed**: May 6, 2026 post-close
- **Short interest added**: 3.45% of float — notably under-shorted vs. 11% peer average. Reframes the behavioral setup from "bears piled in" to "longs capitulating"
- **Schema change**: Consolidated from 4 files (overview/thesis/financials/changelog) to 2 files (DASH.md + changelog.md) per v2.1 CLAUDE.md. No substantive thesis change — format migration only.

### Thesis Status
- **Overall**: **Unchanged** — same core thesis, refreshed data. Stock is *interesting* but not a high-conviction buy at $176.78
- **BAIT delta**:
  - B: Moderate (unchanged; now reinforced by Tang insider sale and –5.6% session)
  - A: Moderate (unchanged)
  - I: Moderate (unchanged; reinforced by new insider data)
  - T: Weak (unchanged; no new mechanical catalyst)
  - Overall: Double overlap (B+A+I, all Moderate). Conviction Low-Moderate.
- **Price target delta (5-yr scenarios)**: Bull $215 (30%) unchanged | Base $110 (50%) unchanged | Bear $50 (20%) unchanged. PW EV ~$130 (5-yr) — still below current $176.78
- **Catalyst & Sentiment delta**: Analyst target dispersion widened ($185 – $360). Short interest confirmed low. Stanley Tang insider sale at lows added to the watchlist.

### Recommendation
- **For a non-holder**: **Watch** — initiate only in $140–155 attractive entry zone. At $176.78 the 5-year PW EV ($130) is below spot; inadequate compensation for execution + integration + regulatory risk. Tactical trade on May 6 earnings beat is possible but sizing should reflect binary-outcome risk.
- **For a current holder**: **Hold** — do not add, do not exit pre-print. Exiting at –38% off highs forfeits the re-rating optionality on a clear H2 re-acceleration print. Add only if price drops into $140–155 AND thesis remains intact.

**Attractive entry zone**: $140 – $155
**Trim zone**: $245 – $275
**Exit / avoid zone**: >$300

**Thesis-break triggers**:
1. Q1 2026 adj EBITDA < $650M absent external shock
2. Full-year 2026 adj EBITDA guide implies H2 < 55% when refreshed at Q2
3. U.S. market share falls below 58% for two consecutive quarters
4. Gig-worker reclassification legislation advances at state or federal level
5. Advertising revenue growth <25% YoY for two consecutive quarters
6. Deliveroo FY2026 adj EBITDA < $140M (30% below $200M target)
7. New commission cap legislation in a top-10 U.S. metro
8. Tony Xu founder departure

**Next review trigger**: **Q1 2026 earnings — May 6, 2026 (post-close)**. Items to check: (1) adj EBITDA vs. $675–775M guide, (2) H2 pacing commentary + any FY guide update, (3) Deliveroo contribution toward $200M FY target, (4) advertising revenue growth rate, (5) grocery unit economics timeline.

---

## [2026-04-06] — Initial Ingest (from raw/analyses/DoorDash_Fundamental_Analysis.md.pdf)

**Trigger**: User requested DASH ingest from raw analysis PDF (analysis date: 2026-03-02).

**Data points reviewed**:
- DoorDash_Fundamental_Analysis.md.pdf (8-page Buffett/Munger framework analysis)
- Sources within PDF: DASH SEC filings, Q4 2025 earnings press release (Feb 18, 2026), Q4 2025 earnings call, analyst reports (DA Davidson, Truist, BofA, JPMorgan, Morgan Stanley, Evercore ISI)

### What Changed
- Initial compilation — no prior wiki pages existed for DASH
- Overview, thesis, financials, changelog all created from scratch
- Key developments covered in analysis: (1) Q4 2025 revenue $3.96B (+38% YoY), Adj EBITDA $780M (+38%); (2) FY2025 revenue $13.72B, first sustained GAAP profitability ($935M net income); (3) Deliveroo acquisition closed Oct 2, 2025 (~$3.9B); SevenRooms acquired 2025 (~$1.2B); (4) Q3 2025 EPS miss ($0.55 vs. $0.69 est.) + "several hundred million" incremental spend announcement triggered –17% stock drop; (5) stock –38% from $286 52-week high to ~$176; (6) 35M subscribers at year-end, 56M MAU; (7) $5B buyback authorized Feb 2025, $0 executed

### Thesis Status
- **Overall**: Initiated — Watch / Cautious Starter (not a strong buy at current $176; better entry at $140-150 or $120)
- **BAIT signal**: Double overlap (B+A), Low-Moderate conviction
  - B=Moderate (behavioral selloff real but valuation was elevated before; partial mean reversion)
  - A=Moderate (SBC halving, Deliveroo contribution, H2 2026 seasonality underweighted)
  - I=Moderate (Q4 beat, Alfred Lin purchases, Deliveroo slightly ahead of plan)
  - T=Weak (no buyback, no split, no index catalyst)
- **PW EV**: ~$130 vs. $176 price = –26% (5-year horizon) — implies stock is still slightly overvalued at current levels even after the selloff
- **Key insight**: The Buffett/Munger framing in the source analysis explicitly concludes the stock is not a strong buy at $176; better entry exists at $120-140

### Price Targets (5-year scenarios to 2030)
- Bull: ~$215 (30%) — requires revenue $25B + EBITDA margins 15%
- Base: ~$110 (50%) — revenue $22B + EBITDA margins 12%
- Bear: ~$50 (20%) — growth slows, margin pressure, regulation

### Action
- [ ] Buy — only if/when price reaches $140-150 (T2 entry); full position at $120
- [x] Watch — monitor Q1 2026 EBITDA trajectory and H2 2026 margin improvement confirmation
- [ ] Trim — not applicable (no position yet)

**Thesis-break triggers (would close even a starter position)**:
1. Q1 2026 adj EBITDA < $650M absent external shock
2. U.S. market share falls below 58% for 2 consecutive quarters
3. Gig worker reclassification legislation passed (state or federal)
4. EBITDA margin (% of GOV) does not improve in H2 2026 as guided

**Next review trigger**: Q1 2026 earnings (~May 2026); specifically: adj EBITDA vs. $675-775M guidance and H2 margin improvement commentary
