# HD — Changelog

Append-only. Most recent entry first.

---

## [2026-05-10] — v2 Initial Ingest

**Trigger**: Workflow A first-run ingest per CLAUDE.md v2.14
**Sources reviewed**:
- [Q4 FY2025 earnings release (Feb 24, 2026)](https://ir.homedepot.com/news-releases/2026/02-24-2026-110040985) — primary financial data
- [StockAnalysis HD financials](https://stockanalysis.com/stocks/hd/financials/) — FY2021–FY2025 income statement + cash flow triangulation
- [StockAnalysis HD forecast](https://stockanalysis.com/stocks/hd/forecast/) — analyst consensus, FY2026E estimates
- [MarketBeat HD forecast](https://www.marketbeat.com/stocks/NYSE/HD/forecast/) — analyst ratings distribution, recent rating changes
- [Yahoo Finance HD quote](https://finance.yahoo.com/quote/HD) — live price, 52-wk range, P/E, dividend yield, beta
- [Supply Chain Dive — tariff impact](https://www.supplychaindive.com/news/home-depot-assesses-tariff-impact-sku-by-sku/567709/)
- [Home Depot IR SRS acquisition close](https://ir.homedepot.com/news-releases/2024/06-18-2024-153031934)
- [Home Depot IR SRS acquisition announcement](https://ir.homedepot.com/news-releases/2024/03-28-2024-100102814)
- [Home Depot quarterly earnings archive FY2025](https://ir.homedepot.com/financial-reports/quarterly-earnings/2025)
- [CNBC SRS Distribution rationale (Nov 2024)](https://www.cnbc.com/2024/11/15/why-home-depot-acquired-srs-distribution.html)
- [DigitalCommerce360 GMS acquisition (Jun 2025)](https://www.digitalcommerce360.com/2025/06/30/home-depot-b2b-5-billion-srs-distribution-acquisition-gms/)
- [IBISWorld US home improvement market share](https://www.ibisworld.com/united-states/company/home-depot-inc/8738/)
- [247WallSt HD vs LOW April 2026](https://247wallst.com/investing/2026/04/15/home-depot-vs-lowes-one-has-crushed-the-market-for-5-years-running/)
- [Rate.com housing report March 2026](https://www.rate.com/mortgage/resource/housing-report-04-13-2026)
- [Freddie Mac PMMS mortgage rates](https://www.freddiemac.com/pmms)
- [HD IR Q1 FY2026 earnings call scheduled May 19](https://ir.homedepot.com/news-releases/2026/05-05-2026-130040601)
- [HD DEF 14A FY2025](https://www.sec.gov/Archives/edgar/data/354950/000035495025000165/hd-20250504.htm) [link pending — EDGAR HTML]
- [AJC Decker compensation 2026](https://www.ajc.com/business/2026/03/home-depot-ceo-ted-decker-saw-his-total-compensation-rise-in-2025/)
- `raw/HD/filings/SOURCES.md` — full source index including gap log

**Data gaps**:
- EDGAR HTML 10-K direct fetch (hd-20250202.htm) returned 403; financials cross-verified via IR press release + StockAnalysis
- Annual report PDFs (FY2021–FY2025 shareholder letters) are binary — not parseable via WebFetch; letter themes synthesized from earnings call press releases and transcripts
- OpenInsider HD page returned ECONNREFUSED; insider data estimated from MarketBeat
- Short interest exact % not confirmed (Fintel 403); estimated <2% from Yahoo Finance key statistics
- Q1 FY2026 results not yet reported (earnings May 19, 2026)

### What Changed
- Initial build: all 13 sections written from scratch
- §1: FY2021–FY2025 financial tables built from IR press releases + StockAnalysis
- §2: Revenue mix by product category, Pro/DIY split, geographic breakdown
- §3: Competitive landscape including HD vs. LOW, FND, Menards, Ace, Amazon; moat assessment
- §4: Management table; capital allocation track record FY2021–FY2025; 5-yr letter arc (Pattern C — embedded in annual reports)
- §5: Strategic initiatives including SRS integration, Pro ecosystem, supply chain, Magic Apron AI
- §6: Key risks including housing lock-in, SRS integration risk, tariff exposure, Lowe's competition
- §7: TAM, housing market macro, tariff environment, mortgage rate sensitivity
- §8: Valuation snapshot, peer table, verdict
- §9: Live price, analyst consensus, 90-day rating changes, corporate news, upcoming catalysts
- §10: BAIT assessment — Double (B+A), Moderate-High conviction cyclical recovery call
- §11: Bull $530 / Base $395 / Bear $215 with 5-yr terminal scenarios
- §12: PW EV ≈$377 (+17% vs. $322 spot); R/R ~2:1 Bull/Bear; total return ~6.3%/yr including dividend
- §13: Initiate below $325 (non-holder); Hold (current holder); entry zone $295–$325; trim $400–$470

### Thesis Status
- **Overall**: Initiated — Moderate Conviction Housing Recovery Call
- **BAIT**: Double (B+A) — Moderate-High
- **Price target**: Bull $530 | Base $395 | Bear $215
- **PW EV**: ~$377 (+17% to spot at $322)

### Recommendation
- **For a non-holder**: 🟢 Initiate — below $325; 2.9% dividend; housing recovery optionality
- **For a current holder**: 🟡 Hold — add on dips below $310

**Next review trigger**: Q1 FY2026 earnings May 19, 2026 — watch U.S. comps, gross margin vs. 33.1% guidance, SRS commentary, and any FY2026 EPS guidance revision.
