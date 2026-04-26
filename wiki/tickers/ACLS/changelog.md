# ACLS — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.6+v2.7+v2.8 Retrofit (Schema Refactor)

**Trigger**: Batch retrofit applying v2.6 (shareholder-letter + 10-K MD&A primary-source synthesis), v2.7 (5-year baselines + Pattern C fallback for non-letter publishers), and v2.8 (synthesis discipline, output discipline, moat-section consolidation, competitive-landscape integration, risk-factor materiality filter, R/R discipline). No new earnings event since prior baseline; integrates Veeco-merger-arbitrage framing established in October 2025 announcement and February 2026 stockholder approval.

**Sources reviewed**:
- ACLS FY2025 10-K (SEC EDGAR HTML, accession 0001104659-26-020461, filed 2026-02-26) — Item 1A risk factors and Item 7 MD&A
- ACLS FY2024 10-K (SEC EDGAR HTML, [acls-20241231x10k.htm](https://www.sec.gov/Archives/edgar/data/1113232/000155837025001855/acls-20241231x10k.htm))
- Five-year 10-K baseline indexed in `raw/ACLS/filings/ACLS-10K-FY2025-source.md`
- ACLS DEF 14A introductory letter / chairman's letter (Pattern C — no standalone shareholder letter; gap logged)
- Q4 2025 / FY2025 press release + transcript (2026-02-17)
- Veeco merger announcement (2025-10-01) and shareholder approval (2026-02)
- B. Riley upgrade analysis (April 2026)
- Yahoo Finance live price re-verification at $143.13 (after-hours $145.16) on 2026-04-24

### What Changed (by Section)
- **Header**: Schema bumped v2.5 → v2.8; Last Updated 2026-04-26.
- **Summary**: Refreshed to ≤10 emoji-tagged bullets per Rule #18; Veeco-merger-arbitrage framing surfaced explicitly.
- **Business Overview**: Standalone "Moat Assessment" block retired per Rule #23; one-line moat verdict moved to Summary, full detail consolidated into §5.
- **§2 (Annual Financial Metrics)**: Added `Primary Source: 10-K Segment Detail` subsection with multi-year MD&A across the 5 fetched 10-Ks — Systems vs CS&I split, SiC end-market trajectory FY2021→FY2025, 150→200mm wafer transition narrative.
- **§5 (Competitive Moat)**: Added `Competitive Landscape` subsection per Rule #24 — named peers (AMAT for ion-implant overlap, ASMI, Tokyo Electron, KLAC for broader semicap; Sumitomo Heavy / Nissin for legacy implant); market-share figures (70–80% SiC implant); explicit framing of how ACLS's moat (Purion platform leadership in mature-node implant + multi-year customer-qualification switching costs) differs from peers.
- **§6 (Management & Leadership)**: Added `Recent Management Commentary — Primary Source Synthesis` subsection with Russell Low / prior-CEO Mary Puma earnings-call and DEF 14A quotes; capital-allocation discipline + cycle-management framework arc surfaced (despite Pattern-C gap on standalone letters).
- **§8 (Key Risks)**: Materiality filter applied per Rule #25 — universal corporate boilerplate dropped; kept SiC end-market overcapacity, China exposure, Veeco-integration execution (large discretionary investment per Rule #25(d)), Purion competitive displacement. 5-year Risk Factor evolution collapsed from table to 2–4 sentence synthesis paragraph per Rule #21.
- **§11 (Catalyst & Sentiment)**: Refreshed price/short/insider/upcoming as of 2026-04-26.
- **§13–§14**: R/R recomputed per Rule #26 anchored to §13 Bull/Bear midpoints — ~1.1:1 (Bull $215 / Bear $80).
- **§15 (Recommendation)**: Refreshed entry/trim/exit zones; thesis-break triggers retained.

### Thesis Status
- **Overall**: Unchanged (vs. prior v2.5 baseline) — schema-driven refactor; underlying read unchanged at ~3% pa from spot.
- **BAIT delta**: Unchanged (single-overlap, T Strong, A Moderate; Conviction Low at $143).
- **Price target delta**: Bull / Base / Bear unchanged.

### Recommendation
- **For a non-holder**: Watch — do not chase +186% rally; wait for $95–$115 entry zone or post-Q1 pullback / merger-close clarity.
- **For a current holder**: Hold — preserve Veeco-merger optionality through 2H 2026 close.

**Next review trigger**: Q1 2026 earnings — May 7, 2026 (post-close). Key items: revenue vs $195M guide, Veeco transaction/integration cost magnitude, FY26 reaffirmation, book-to-bill, SiC/memory order-book color, China commentary.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added ACLS to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Axcelis Q4 2025 / FY2025 press release and earnings call (~2026-02-17, IR / Stocktitan / Motley Fool / Globe and Mail)
- B. Riley upgrade analysis (Trefis, themarketsdaily.com 2026-04-20/21)
- FinancialContent ACLS deep dive (2026-03-25)
- SimplyWallSt narrative analysis on SiC market share
- Yahoo Finance JSON API live price (2026-04-24)
- Investing.com 52-wk high coverage; analyst consensus aggregators (MarketBeat, Daily Political)

### What Changed
- Initial compilation; no prior wiki content for this ticker.
- Live price verified at $143.13 (Yahoo Finance, April 24, 2026); near 52-wk high $147.94; +186% trailing year; +208% above 52-wk low $46.52.
- FY2025 confirmed: revenue $839M (vs. record $1.13B FY23), NI $120M.
- Q4 2025 strong beat: $238M revenue, $1.49 EPS (vs. $1.12 cons.).
- Q1 2026 guide: ~$195M revenue / $0.71 non-GAAP EPS.
- FY2026 outlook: flat overall — DRAM/HBM growth offsetting power decline.
- B. Riley upgrade Apr 20–21 to Buy with $150 PT sparked +10% rally.
- 70–80% SiC implant share; 8-inch SiC wafer transition is multi-year tailwind.
- 3-year PW EV ~$154.50 vs. spot $143.13 = +8% return — low forward asymmetry after the 186% rally.

### Thesis Status
- **Overall**: Initiated — Watch (non-holder) / Hold (holder).
- **BAIT signal**: Single-overlap (T Strong, A Moderate); Conviction Low for new entries.
- **PW EV**: $154.50 vs. spot $143.13 (+8% over 3 years, ~2.6%/yr).

### Recommendation
- **For a non-holder**: Watch — do not chase +186% rally. Wait for $95–115 entry zone (post-print pullback if Q1 disappoints).
- **For a current holder**: Hold — trim into $160–180 if reached on clean Q1 beat.

### Data Gaps Flagged
- Precise geographic revenue split (pending 10-K full read)
- Specific short interest %
- Recent insider Form 4 cadence not retrieved

**Next review trigger**: Q1 2026 earnings on May 7, 2026 (post-close). Key items: revenue vs. $195M guide, FY26 reaffirmation, book-to-bill, SiC/memory order book color.
