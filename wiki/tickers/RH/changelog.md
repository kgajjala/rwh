# RH — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: Schema upgrade from v2.5 to v2.9 (13-section structure; competitive landscape; shareholder letters; 10-K primary sources; materiality-filtered risks; synthesis-first rules).

**Sources reviewed**:
- [RH FY2025 10-K (EDGAR HTML, filed 2026-04-01)](https://www.sec.gov/Archives/edgar/data/1528849/000110465926037992/rh-20260131x10k.htm) — full text extracted: MD&A, risk factors, debt structure, segment detail, liquidity section
- [RH Q4 FY2025 8-K Exhibit 99.2 (filed 2026-03-31)](https://www.sec.gov/Archives/edgar/data/1528849/000110465926037775/rh-20260331xex99d2.htm) — Q4/FY2025 financial tables, FY2026 guidance, Q1 FY2026 guidance, Gary Friedman strategic framing
- [stockanalysis.com — RH financials](https://stockanalysis.com/stocks/rh/financials/) — FY2021–FY2025 annual P&L and balance sheet
- [stockanalysis.com — RH analyst forecasts](https://stockanalysis.com/stocks/rh/forecast/) — 14-analyst consensus, recent rating changes
- [Fintel — RH short interest](https://fintel.io/ss/us/rh) — short interest 35.62% of float confirmed
- [Yahoo Finance — RH quote](https://finance.yahoo.com/quote/RH) — live price $137.51 verified April 24, 2026
- [ir.rh.com/financials-filings/annual-reports](https://ir.rh.com/financials-filings/annual-reports) — confirmed shareholder letter pattern (FY2020–FY2021 only; FY2022–FY2025 no standalone letter)
- SEC EDGAR CIK 1528849 submissions JSON — confirmed 10-K filing dates FY2021–FY2025

### What Changed
- **Structure**: Renumbered from 15-section v2.5 to 13-section v2.9; retired old Section 1 (Why Exist + PIQ → header subsections); merged old Sections 3+4 → new Section 2 (Revenue Mix & Geographic Split); renumbered old Sections 5–15 → new Sections 3–13
- **Section 1 (Financial Metrics)**: Added precise EBITDA vs. Adj EBITDA reconciliation from 10-K (FY2025 Adj EBITDA $596.5M, 17.3% margin — materially higher than old wiki's ~14% estimate which was confusing FY2026 guidance for FY2025 actuals); added segment table (RH Segment $3.24B / Waterworks $198M); highlighted inventory reduction $1.02B → $819M
- **Section 2 (Revenue Mix)**: New merged section from old §3+§4; added hospitality economics (65% of gallery rent subsidy per 10-K); added international JV income improvement ($-11.4M → +$5.0M)
- **Section 3 (Competitive Moat & Landscape)**: Renamed from §5; added mandatory Competitive Landscape subsection with 5-peer table + market share estimates + peer-by-peer RH differentiation; upgraded moat sources table; added tail-risk on competitive position (WSM Gallery program)
- **Section 4 (Management)**: Renamed from §6; added Recent Management Commentary subsection; documented Pattern C letter pattern (FY2022–FY2025 no standalone letters); synthesized Gary Friedman's strategic framing from 10-K MD&A and Q4 press release including $20–25B global brand target (material upgrade from prior $5.4–5.8B North America target)
- **Section 5 (Strategic)**: Renamed from §7; added RH Estates detail (spring 2026 launch); added RH Guesthouse Aspen; added RH Residences / RH Media optionality; noted IEEPA tariff ruling and replacement tariff structure
- **Section 6 (Key Risks)**: Renamed from §8; applied Rule #25 materiality filter (dropped generic boilerplate); added NEW risks: shareholder litigation (multiple lawsuits filed Apr 2026), international execution confirmed by Germany $19M impairments, RH Estates product miss; upgraded tariff probability to 35% (IEEPA complexity); updated risk factor evolution synthesis paragraph; changed from 5-yr arc table to 2–4 sentence synthesis paragraph per v2.8/v2.9 rules
- **Section 7 (Macro)**: Renamed from §9; added IEEPA tariff ruling detail (Feb 20, 2026); added peer 2-year revenue comparison data (RH +15% vs. PB –6%, Ethan Allen –15%)
- **Section 8 (Valuation)**: Renamed from §10; updated with precise debt structure ($2,347M net financial debt, ~8.3× EV/Adj EBITDA); updated analyst consensus (median $170, not $183–212 as in old wiki — significant downgrade cluster post Q4 miss); added GS Strong Sell at $88
- **Section 9 (Catalyst & Sentinel)**: Renamed from §11; refreshed analyst actions table with 5 April 2026 rating changes; upgraded short interest signal from "moderately elevated" to 35.62% of float (highly elevated — significant BAIT T upgrade); added shareholder litigation and RH Estates launch as upcoming catalysts; added IEEPA tariff ruling as recent news
- **Section 10 (BAIT)**: Renamed from §12; upgraded T lens from Weak → Moderate on 35.62% short interest discovery; revised BAIT verdict to "B Strong + T Moderate" (from prior "B Strong + A Moderate")
- **Section 11 (Scenarios)**: Renamed from §13; adjusted Bear probability 25% → 30% (litigation + weak Q1 guide); adjusted Bull probability 30% → 25%; scenarios otherwise unchanged ($400 Bull / $200 Base / $60 Bear)
- **Section 12 (PW EV)**: Renamed from §14; updated PW EV ~$208 (from ~$225) reflecting probability shifts; updated return +51% / +11%/yr (from +64% / +13%/yr); R/R maintained at ~3.4:1
- **Section 13 (Recommendation)**: Renamed from §15; added shareholder litigation to thesis-break triggers; added RH Estates product miss signal; strengthened entry zone rationale with inventory clean signal; added note on short squeeze non-linearity in S12 interpretation
- **Summary**: Fully refreshed with updated bullets and emoji vocabulary; updated moat verdict line; updated BAIT verdict; updated price action to include –19% session collapse
- **Header**: Bumped schema v2.5 → v2.9; refreshed Last Updated; live price re-verified
- **Sources**: All 15+ sources linkified per Rule #16

### Thesis Status
- **Overall**: Strengthened slightly on primary-source review — FY2025 actual adj EBITDA of 17.3% was better than old wiki's ~14% estimate (which confused guidance with actuals); inventory destocking completion ($1.02B → $819M) is a genuine positive signal; 2-year revenue outperformance vs. all peers confirms market share gains.
- **Offsetting**: Q1 FY2026 guidance is materially weak (–2 to –4% revenue, 5.5–6.5% adj EBITDA); shareholder lawsuits add a new tail risk; short interest 35.62% suggests professional skepticism remains elevated.
- **BAIT delta**: T upgraded Weak → Moderate on 35.6% short interest discovery; overall BAIT verdict shifts from "B + A" to "B + T" double overlap
- **Price target delta**: Bull $400 (unchanged) | Base $200 (unchanged) | Bear $60 (unchanged) | PW EV $225 → $208 (probability shift)

### Recommendation
- **For a non-holder**: Watch / selective Initiate — unchanged thesis, better primary-source grounding
- **For a current holder**: Hold — unchanged

**Next review trigger**: Q1 FY2026 earnings (~June 2026)

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added RH to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- RH Q4 2025 earnings release and call (2026-04-01, Motley Fool transcript, Chain Store Age, Alphastreet)
- Yahoo Finance live price endpoint (2026-04-24)
- stockanalysis, public.com, Investing.com, TipRanks — analyst consensus April 2026
- TD Cowen PT update (April 2026)
- RH IR financials & filings page
- CNBC tariff coverage (2025-09-12)

### What Changed
- Initial compilation; no prior wiki content
- Live price verified at $137.51 (Yahoo Finance, April 24, 2026)
- Established RH as Premium luxury home furnishings (cyclical specialty retail) asset type
- Recorded –46.5% from 52-wk high, +29.4% above 52-wk low
- Documented Q4 2025 miss: revenue $842.62M (vs. $873M cons.), adj EPS $1.53 (vs. $2.22 cons.), $190M tariff impact
- Documented FY26 guide: revenue +4 to +8%, adj EBITDA margin 14–16%, cash flow $300–400M
- 2030 long-term target: $5.4–5.8B revenue, 25–28% adj EBITDA margin, debt-free 2029

### Thesis Status
- **Overall**: Initiated — Cautious / Watch with selective Initiate bias
- **BAIT signal**: Moderate — Double overlap (B Strong + A Moderate); cyclical-trough setup
- **PW EV**: ~$225 (4-yr) vs. $137.51 spot = +64% / +13.1% annualized

### Recommendation
- **For a non-holder**: Watch / selective Initiate — Asymmetry favorable but leverage + timing risk argues small initial position. Aggressive add below $115.
- **For a current holder**: Hold — Asymmetry has shifted. Add only on weakness toward $115.

**Next review trigger**: Q1 FY26 earnings (early June 2026, est.).
