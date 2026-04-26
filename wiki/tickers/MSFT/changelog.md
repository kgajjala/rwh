# MSFT — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: Schema upgrade from v2.5 to v2.9 (13-section structure). Applied as part of batch retrofit.
**Sources reviewed**:
- [Microsoft FY2025 Annual Report / Nadella Letter](https://www.microsoft.com/investor/reports/ar25/index.html) — FY2025 shareholder letter fetched and stored in raw/MSFT/shareholder-letters/2025_letter.html
- [Microsoft FY2024 Annual Report / Nadella Letter](https://www.microsoft.com/investor/reports/ar24/index.html) — stored as 2024_letter.html
- [Microsoft FY2023 Annual Report / Nadella Letter](https://www.microsoft.com/investor/reports/ar23/index.html) — stored as 2023_letter.html
- [Microsoft FY2022 Annual Report / Nadella Letter](https://www.microsoft.com/investor/reports/ar22/index.html) — stored as 2022_letter.html
- [Microsoft FY2021 Annual Report / Nadella Letter](https://www.microsoft.com/investor/reports/ar21/index.html) — stored as 2021_letter.html
- [MSFT IR Q2 FY2026 PR (2026-01-28)](https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q2/press-release-webcast)
- [MSFT IR Q3 FY2025 PR](https://www.microsoft.com/en-us/Investor/earnings/FY-2025-Q3/press-release-webcast)
- [MSFT IR Q4 FY2025 PR](https://www.microsoft.com/en-us/Investor/earnings/FY-2025-Q4/press-release-webcast)
- [stockanalysis.com — Income Statement, Cash Flow, Balance Sheet, Forecast](https://stockanalysis.com/stocks/msft/financials/)
- [Finviz — MSFT live price/quote](https://finviz.com/quote.ashx?t=MSFT)
- [Fintel — MSFT short interest](https://fintel.io/ss/us/msft)
- [Kinsta — Cloud market share / Synergy Research Q4 2025](https://kinsta.com/azure-market-share/)
- SEC EDGAR 10-K HTML access blocked (403 errors); 10-K synthesis sourced from annual report IR pages and stockanalysis.com

### What Changed
- **Schema**: Renumbered from 15-section (v2.5) to 13-section (v2.9) structure. Old §1 (Why Exist) retired — content moved to Business Overview header. Old §3+§4 merged into new §2 (Revenue Mix & Geographic Split). Moat Assessment standalone block retired — content moved to §3. Sections renumbered throughout.
- **Summary**: Refreshed with emoji vocabulary and ≤10 bullets; moat one-liner added; BAIT verdict + price action bullets added
- **§3 (Competitive Moat & Landscape)**: Added Competitive Landscape subsection with named competitors (AWS, GCP, Salesforce, Oracle, SAP), market share data (Synergy Research Q4 2025), and explicit framing of Microsoft's cross-stack differentiation vs. peers
- **§4 (Management)**: Added full "Recent Management Commentary — Primary Source Synthesis" subsection with verbatim Nadella letter quotes from FY2021–FY2025, each mapped to investment relevance. Added 5-Year Capital Allocation Arc synthesis paragraph
- **§5 (Strategic Growth Initiatives)**: Expanded with 8 distinct growth vectors including commercial RPO $625B signal and Copilot monetization math
- **§6 (Key Risks)**: Applied materiality filter; removed generic boilerplate; kept only differentiated/not-priced-in/thesis-break/large-uncertain-investment risks; replaced arc table with synthesis paragraph per v2.8 Rule #21
- **§8 (Valuation)**: Added peer comparison table with EV/Revenue and P/E columns; added valuation assessment paragraph
- **§11 (Bull/Bear/Base)**: Restated with explicit 30%/50%/20% probabilities and 12–18 month horizon
- **§12 (PW EV)**: Recomputed R/R anchored to §11 Bull/Bear midpoints per v2.8 Rule #26; R/R = 1.8:1
- **All sources linkified**: Every citation converted to real Markdown links
- **CLAUDE.md self-references removed** from page body
- **raw/MSFT/ directory created** with shareholder-letters/ subfolder; 5 letters stored (FY2021–FY2025)

### Thesis Status
- **Overall**: Unchanged — thesis initiated at v2.2 remains: deepest-moat mega-cap at a meaningful drawdown ahead of April 29 Q3 FY26 print
- **BAIT delta**: Unchanged — Quadruple overlap (B Strong + A Strong + I Moderate + T Strong); Conviction High
- **Price target delta**: Bull $720→$650 (restated as 12–18m not 3-yr) | Base $530 (unchanged) | Bear $320→$300 (restated); PW EV ~$520 (18m) vs. prior ~$565 (3-yr) — different horizons

### Recommendation
- **For a non-holder**: Initiate — entry zone $380–$440; PW EV ~$520 (18m) implies ~16%/yr expected return
- **For a current holder**: Add below $440 if cost basis above current; otherwise Hold

**Next review trigger**: Q3 FY26 earnings — April 29, 2026 (post-close, 2:30pm PT)

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added MSFT to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Microsoft FY2025 Annual Report (microsoft.com/investor/reports/ar25)
- Microsoft 10-K FY2025 (SEC EDGAR, msft-20250630)
- FY26 Q2 press release (MSFT IR, 2026-01-28)
- FY26 Q1 Intelligent Cloud Performance disclosure
- Q4 FY25 segment revenue and op income page
- Microsoft Q3 FY26 earnings date announcement (MSFT Source, 2026-04-08)
- Yahoo Finance live price (2026-04-24)
- Techi.com Microsoft 2026 forecast
- Futurum Group quarterly analyses (Q4 FY25, Q1 FY26, Q2 FY26)
- Beancount.io FY2025 earnings analysis (2026-03-23)
- Synyega FY25 review
- TIKR multi-year-low / $792 path coverage
- Motley Fool "April 29 — Most Important Tech Event of 2026" (2026-04-23)
- TheStreet Morgan Stanley pre-earnings reset
- Stocktitan Q3 FY26 announcement coverage
- S&P Global big-tech earnings preview

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $432.92 (Yahoo Finance / TheStreet, April 24, 2026)
- Stock at –22% from January 2026 high; YTD –8% after partial recovery
- FY2025 rev $281.7B (+15%); op income $128.5B (+17%); net income $101B
- Azure $75B+ FY25 (+34%); Q2 FY26 Azure +39% (decel from Q1 +40%)
- 15M paid M365 Copilot seats (new KPI introduced FY26 Q1)
- Q2 FY26 capex $37.5B (+66% YoY); FY26 capex consensus ~$80B
- Morgan Stanley reaffirmed $650 PT into the print

### Thesis Status
- **Overall**: Initiated — Deepest-moat mega-cap at a meaningful drawdown ahead of "the year's most important tech event"
- **BAIT signal**: **Quadruple overlap (B Strong + A Strong + I Moderate + T Strong)** — among the cleanest mega-cap setups in the wiki; Conviction High (event-driven)
- **PW EV**: ~$565 (3-yr) vs. spot $432.92 → +31% / ~10%/yr (incl. div)

### Recommendation
- **For a non-holder**: **Initiate** at $432.92 — Wide-moat quality at a meaningful drawdown; stage half pre-print, half post if risk-averse
- **For a current holder**: **Add** if cost basis above current; otherwise Hold

**Next review trigger**: Q3 FY26 earnings — April 29, 2026 (post-close, 2:30pm PT). 5 days from this writeup.
