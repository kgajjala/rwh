# LULU — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: Schema migration from v2.2 (15-section structure) to v2.9 (13-section structure) — structural renumbering, primary-source synthesis depth, and competitive landscape integration
**Sources reviewed**:
- [LULU FY2025 10-K (filed 2026-03-17)](https://www.sec.gov/Archives/edgar/data/1397187/000139718726000020/0001397187-26-000020-index.htm) — Items 1, 1A, 7, 7A, 8 extracted and synthesized
- [LULU FY2024 10-K (filed 2025-03-27)](https://www.sec.gov/Archives/edgar/data/1397187/000139718725000013/0001397187-25-000013-index.htm) — Item 1A risk factor comparison baseline
- [LULU DEF 14A Proxy (filed 2025-04-29)](https://www.sec.gov/Archives/edgar/data/1397187/000139718725000017/lulu-20250429.htm) — CEO commentary (FY2024); Pattern C letter determination
- [LULU DEF 14A Proxy (filed 2024-04-25)](https://www.sec.gov/Archives/edgar/data/1397187/000139718724000013/lulu-20240424.htm) — CEO commentary (FY2023); Power of Three ×2 framework
- [Finviz — LULU](https://finviz.com/quote.ashx?t=LULU) — market cap, EV, P/E, short interest, analyst target (April 24, 2026)
- [StockAnalysis — LULU](https://stockanalysis.com/stocks/lulu/financials/) — annual financials FY2021–FY2025
- [StockAnalysis — LULU Forecasts](https://stockanalysis.com/stocks/lulu/forecast/) — analyst consensus, rating breakdown, recent PT changes

### What Changed
- **Header**: Schema version bumped from v2.2 → v2.9; `**Status**` line retained (Active); `**Ticker Type**` updated to "Specialty Apparel / Athletic Lifestyle Retailer"
- **Summary**: Refreshed ≤10-bullet Summary with emoji vocabulary (v2.9 Rule #17/18); added moat verdict line; retained all key thesis bullets
- **Section structure**: Renumbered from 15 sections to 13 sections; old §1 (Why Does This Company Exist) retired — content merged into Business Overview; old §3 (Geographic Mix) + §4 (Revenue Mix) merged into new §2 (Revenue Mix & Geographic Split); old §5–15 renumbered to new §3–13
- **§1 (Annual Financial Metrics)**: Corrected FY2025 actual EPS to $13.26 (vs. placeholder estimate); added Primary Source 10-K Segment Detail subsection with MD&A verbatim commentary on segment-level margin drivers (Americas –390bps gross margin, China Mainland +250bps operating margin, tariff impact $275M actuals); added FY2021 data column
- **§2 (Revenue Mix & Geographic Split)**: Added segment table with FY2024 vs FY2025 operating margins per segment; added forward-looking China mix-shift analysis with margin-accretive framing
- **§3 (Competitive Moat & Landscape)**: Added mandatory Competitive Landscape subsection (Rule #24) with 6 named competitors (Nike, Adidas, Under Armour, Vuori, Alo Yoga, Athleta/On Running); market share estimates; how-LULU-differs evidence; honest tail-risk read on Vuori as most credible threat
- **§4 (Management & Leadership)**: Added Pattern C shareholder letter determination (LULU does not publish standalone annual letters; pattern is proxy statement CEO commentary); added Recent Management Commentary — Primary Source Synthesis subsection with verbatim Calvin McDonald quotes from FY2024 and FY2023 proxy DEF 14A; 3-year management arc; investment relevance mapping
- **§6 (Key Risks)**: Applied Rule #25 materiality filter; dropped generic boilerplate (generic earnings miss, generic IT, generic key personnel); added "Priced In?" column; added two newly-discovered FY2025 10-K Item 1A risks ("dupe" products proliferation, AI-enabled shopping tools); converted 5-Year Risk Factor Evolution to synthesis paragraph (Rule #21)
- **§12 (PW EV)**: Added explicit R/R calculation anchored to §11 Bull/Bear midpoints per Rule #26; stated Bull+ tail separately
- **§13 (Recommendation & Bottom Line)**: Added explicit exit/avoid zone; refined thesis-break triggers with quantified thresholds throughout; added O'Neill-specific triggers

### Thesis Status
- **Overall**: Unchanged — thesis initiated 2026-04-24 remains Cautious Watch / Moderate conviction
- **BAIT delta**: No change; Double overlap (B Strong + A Moderate) confirmed via primary source synthesis
- **Primary source delta**: FY2025 10-K confirmed $275M tariff impact (matches guide); China 40% segment op margin confirmed (upgrades China thesis leg); "dupe" products risk addition to 10-K Item 1A is a new bearish signal not in prior analysis
- **Price target delta**: Unchanged — Bull $290 / Base $200 / Bear $80 / PW EV ~$192

### Recommendation
- **For a non-holder**: Watch — bias to Initiate below $135; primary source synthesis confirms China growth quality (40% seg op margin) is genuine but "dupe" products + AI shopping tools newly entering 10-K risk factors are net-negative for moat thesis
- **For a current holder**: Hold — do not exit at –58%; asymmetry favors patience at current levels

**Next review trigger**: Q1 FY26 earnings — early June 2026 (est.)

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added LULU to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- lululemon Q4 FY2025 / FY2025 earnings release (2026-03-17)
- lululemon CEO succession announcement (2025-12-11)
- lululemon Heidi O'Neill CEO appointment (2026-04-23)
- Yahoo Finance live price endpoint (2026-04-24)
- MarketBeat, TipRanks, Public.com, Daily Political — analyst consensus April 2026
- CNBC, Motley Fool earnings call coverage (2026-03-18)
- TradingKey, Seeking Alpha, UBS research notes

### What Changed
- Initial compilation; no prior wiki content
- Live price verified at $143.80 (Yahoo Finance, April 24, 2026)
- Established LULU as Premium consumer apparel asset type
- Recorded –57.7% drawdown from 52-wk high of $340.25; trading at 52-wk low
- Documented FY26 guidance light: revenue $11.35–11.50B, EPS $12.10–12.30, op margin –250bps
- Heidi O'Neill (ex-Nike) CEO appointment effective Sep 8, 2026; market –13% reaction
- Andre Maestrini insider buy ~$494K at ~$151 noted as positive signal

### Thesis Status
- **Overall**: Initiated — Cautious / Watch
- **BAIT signal**: Moderate — Double overlap (B Strong + A Moderate); Conviction Moderate
- **PW EV**: ~$192 (3-yr) vs. $143.80 spot = +34% / +10.2% annualized

### Recommendation
- **For a non-holder**: Watch — Bias to Initiate below $135; insider buy + decade-low P/E constructive but bear-case probability 25% non-trivial.
- **For a current holder**: Hold — Do not exit at –58%; asymmetry has shifted favorably. Add only on weakness toward $130.

**Next review trigger**: Q1 FY26 earnings (early June 2026, est.).
