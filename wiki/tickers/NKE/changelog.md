# NKE — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: Schema upgrade from v2.5 → v2.9. No new earnings event; structural retrofit only with primary source enrichment.

**Sources reviewed**:
- [Nike FY2025 10-K (SEC EDGAR, filed 2025-07-17)](https://www.sec.gov/Archives/edgar/data/320187/000032018725000047/nke-20250531.htm) — Item 1A Risk Factors, Item 7 MD&A segment detail, revenue by channel/product/geography
- [Nike FY2025 DEF 14A Proxy (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/320187/000032018725000048/nke-20250717.htm) — Shareholder letter pattern determination (Pattern C)
- [stockanalysis.com](https://stockanalysis.com/stocks/nke/financials/?p=quarterly) — Q1–Q3 FY2026 actual quarterly data (Q1: $0.49 EPS, Q2: $0.53 EPS, Q3: $0.35 EPS); updated analyst consensus
- [Fintel](https://fintel.io/ss/us/nke) — Short interest: 4.78% float, 3.56 days-to-cover
- [Yahoo Finance](https://finance.yahoo.com/quote/NKE) — Live price $44.69 (April 24, 2026) confirmed current
- SEC EDGAR 10-K filing index — confirmed 5 annual 10-Ks: FY2021–FY2025

**Schema changes applied**:
- Section 1 (Why Does This Company Exist) retired; founding insight moved to Business Overview; Pivotal Question is header subsection
- Old Sections 3 (Geographic Revenue Mix) + 4 (Revenue Mix & Business Model) merged into new Section 2 (Revenue Mix & Geographic Split)
- Sections renumbered: old §5–15 → new §3–13
- Standalone Moat Assessment block retired; moat verdict in Summary; detail in §3
- §3 (Competitive Moat & Landscape) added full Competitive Landscape subsection with 8 named peers + market share

**What Changed**:
- **§1 Annual Financial Metrics**: Added Q1–Q3 FY2026 actual data (previously estimated); added FY2025 10-K channel/product revenue table; added MD&A gross margin driver commentary
- **§2 Revenue Mix & Geographic Split**: Merged geographic + channel/business-model sections; added 10-K-sourced segment EBIT data (China –31%, APLA –19%, EMEA –49%, NA GM –90 bps)
- **§3 Competitive Moat & Landscape**: Added full Competitive Landscape table (Adidas, On, Hoka, New Balance, Puma, Under Armour, Anta, Li Ning) with market shares and moat reads
- **§4 Management & Leadership**: Added Pattern C shareholder letter note + FY2025 DEF 14A proxy letter quote from Mark Parker; added multi-year management philosophy arc from 10-K MD&A language evolution (FY2021–FY2025)
- **§6 Key Risks**: Applied Rule #25 materiality filter; removed generic boilerplate; retained 7 material, differentiated risks; added 5-year Risk Factor Evolution synthesis paragraph
- **§8 Valuation**: Updated analyst consensus: median $58 (was $66.85), 26-analyst breakdown
- **§9 Catalyst & Sentiment**: Added short interest 4.78% float (was "pending"); updated analyst targets (high $88 vs old $92)
- **§12 PW EV**: Added explicit R/R = ~3.6:1 per Rule #26 (Bull +101% / Bear –28.4%)
- **Summary**: Refreshed bullets for v2.9 structure

### Thesis Status
- **Overall**: Unchanged — Initiate (non-holder) / Add (holder)
- **BAIT delta**: No change (Triple overlap, Conviction Moderate-High)
- **Price target delta**: Bull $90 | Base $60 | Bear $32 — unchanged; R/R now explicitly stated at ~3.6:1

### Recommendation
- **For a non-holder**: Initiate — entry zone $40–48; dividend yield + Hill insider buy
- **For a current holder**: Add — incremental below $48; trim $70–85

**Next review trigger**: Q4 FY2026 earnings late June 2026. Key items: FY2027 guide (most critical), Q4 revenue vs. down 2–4% guide, China trajectory, GM direction, tariff commentary.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added NKE to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Nike Q3 FY2026 earnings press release and earnings call transcript (2026-03-31, IR / CNBC / Motley Fool / GuruFocus)
- Sporting Goods Intelligence coverage (2026-04-04)
- Daily Political (2026-04-17) on Hill insider buy
- stockanalysis.com analyst aggregator
- Yahoo Finance JSON API live price (2026-04-24)
- MarketBeat / Public.com / WallStreetZen forecasts

### What Changed
- Initial compilation; no prior wiki content for this ticker.
- Live price verified at $44.69 (Yahoo Finance, April 24, 2026); 12-year low territory; –44.3% from 52-wk high $80.17.
- Q3 FY2026 (Mar 31, 2026): revenue $11.3B flat, EPS $0.35 (–35%), GM 40.2% (–130 bps); Q4 guide revenue down 2–4%, China –20%.
- North America +3% revenue / +6% footwear in Q3 = early Hill turnaround signal.
- **CEO Elliott Hill bought $1,000,108 in stock on April 14, 2026** — material insider conviction signal at multi-year low.
- Dividend yield ~3.6% (highest in 20+ years).
- Analyst PT dispersion unusually wide: BNP $23 (Apr 1) to BMO $92 (Mar 2025); median $66.85.
- 3-year PW EV ~$60.50 + dividend ~11% over 3 years = ~14%/yr total return.

### Thesis Status
- **Overall**: Initiated — Initiate (non-holder) / Add (holder)
- **BAIT signal**: Triple-overlap (B Strong + A Moderate-Strong + I Moderate); Conviction Moderate-High
- **PW EV**: $60.50 + dividend = +46% total over 3 years (~14%/yr)

### Recommendation
- **For a non-holder**: Initiate — entry zone $40–48; dividend yield + Hill insider buy provide asymmetric setup.
- **For a current holder**: Add — incremental below $48 rational; trim only into $70–85.

### Data Gaps Flagged
- Precise FY26 / FY27 EPS consensus (estimates used)
- Specific short interest %
- Full insider Form 4 cadence beyond Hill's April 14 buy

**Next review trigger**: Q4 FY2026 earnings on late June 2026 (specific date TBD). Key items: Q4 revenue vs. guide, **FY27 guide** (first Hill-era full-year guide), China trajectory, gross margin, tariff commentary, dividend reaffirmation.
