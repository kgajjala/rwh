# ZG — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: v2.9 schema migration (15 → 13 sections + Rules #19–#26 application). Single-ticker serial run.

**Sources reviewed**:
- [Yahoo Finance — Z](https://finance.yahoo.com/quote/Z) live price ($45.41 close 2026-04-24)
- [Q4 2025 Shareholder Letter](https://s24.q4cdn.com/723050407/files/doc_earnings/2025/q4/presentation/Zillow-4Q25-Shareholders-Letter.pdf) (saved to `raw/ZG/shareholder-letters/2025_Q4_letter.pdf`)
- [Q4 2025 PR (PRNewswire)](https://www.prnewswire.com/news-releases/zillow-group-reports-fourth-quarter-and-full-year-2025-financial-results-302684089.html)
- [10-K FY2024 (SEC EDGAR HTML)](https://www.sec.gov/Archives/edgar/data/1617640/000161764025000016/z-20241231.htm) — full fetch returned 403; secondary parsed via search results + [last10k.com](https://last10k.com/sec-filings/zg/0001617640-25-000016.htm)
- [Redfin-Zillow rental syndication news](https://www.redfin.com/news/redfin-zillow-syndication/)
- [FTC litigation tracker — Inman](https://www.inman.com/2026/04/08/over-460k-documents-and-counting-catch-up-on-the-ftcs-legal-battle-with-zillow-and-redfin/)
- [Public.com / stockanalysis.com / MarketBeat](https://stockanalysis.com/stocks/z/forecast/) (analyst consensus)
- [Fintel](https://fintel.io/ss/us/zg) (short interest)

### What Changed
- **Schema**: Migrated 15-section → 13-section v2.9. Old §1 (Why Exist) folded into Business Overview + Pivotal Question header; old §3 (Geo) + §4 (Revenue Mix) merged into new §2; standalone Moat Assessment block retired (Rule #23) — all moat content now lives in §3.
- **§3 Moat & Landscape**: Added named-competitor table (Realtor.com / CSGP / RKT-Redfin / Apartments.com / RKT / Better.com / ANGI) with market positions and threat-vector reads (Rule #24).
- **§6 Risks**: Materiality-filtered per Rule #25 — dropped boilerplate; kept (a) CSGP/Homes.com $1B marketing assault (peer-differentiated, *not fully priced in*), (b) **FTC suit over $100M Redfin rental-syndication deal** [NEW — replaces prior single-line "Rocket-Redfin disintermediation" framing], (c) housing turnover trough, (d) Rocket-Redfin mortgage-attach overlap (re-scoped post-syndication-deal), (e) NAR ARPU compression, (f) MLS termination, (g) discretionary capex bet on LO+rentals salesforce, (h) state AG suits. Replaced 5-yr Risk Factor table with synthesis paragraph (Rule #21).
- **§4 Management**: Added Recent Management Commentary subsection (Rule #19, Pattern B — quarterly letters); 5-yr strategic-framework arc covering iBuying-shutdown → super-app pivot → Wacksman-era profitability.
- **§9 Catalyst & Sentiment**: Refreshed live price ($45.41 vs prior $45.63), Q4 25 / FY25 actuals, Q1 26 guide, FY26 outlook (mid-teens revenue / ~30% Rentals / margin expansion), FTC litigation timeline, $232M Q4 buyback.
- **§11/§12 Bull/Bear/Base + PW EV**: Refined to use FY28 horizon; PW EV $68.50 (+51%); R/R **3.2:1** (Rule #26 anchored to §11 midpoints) — replaces prior unanchored framing.
- **§13 Recommendation**: Refreshed thesis-break triggers — added FTC-forced-unwind trigger, 12% revenue-deceleration trigger, Rentals-share trigger.
- **Material thesis shift**: Discovery of the **$100M Zillow-Redfin rental-syndication deal** (Feb 2025) reframes the prior "Rocket-Redfin disintermediation" as *partial competition + partial partnership*. Rentals share went 54% → 63% on this deal; FTC suit over the deal is now the live regulatory wildcard, replacing pure competitive disintermediation as the dominant near-term overhang.
- **Verified live price**: $45.41 (Z) vs prior wiki $45.63 (ZG); within rounding for ZG/Z share-class proxy.

### Thesis Status
- **Overall**: **Strengthened** vs. v2.5 — operating data (first profitable year, Mortgages +37%, Rentals +39%, FCF +36%) confirms super-app monetization is converting; competitive narrative softened by Redfin syndication-deal mitigant.
- **BAIT delta**: B Strong (unchanged), A Strong (strengthened — $420M FCF + 24% margin record), I Moderate (strengthened — FTC base-rate-dismissal signal under-modeled), T Weak (unchanged).
- **Price target delta**: Bull $95 (unchanged) | Base $68 (unchanged) | Bear $30 (unchanged). PW EV $68 (+51%, unchanged).
- **Catalyst & Sentiment delta**: Short interest 7.9% (unchanged); analyst median $81–84 (vs prior $86–92 — modest cut as targets adjusted to current spot); FTC litigation now active wildcard.

### Recommendation
- **For a non-holder**: 🟢 **Initiate** at $45 — asymmetric setup; PW EV +51%; deepest behavioral mispricing in housing complex.
- **For a current holder**: 🟢 **Add** in $40–50 zone — buy the cycle trough + FTC overhang.

**Next review trigger**: Q1 2026 earnings — early May 2026.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added ZG to wiki on 2026-04-24 as part of a 25-ticker expansion batch (Group E).

**Sources reviewed**:
- Yahoo Finance live price (2026-04-24)
- Zillow Q4 2025 / FY2025 press release (2026-02-10, PRNewswire)
- Q4 2025 earnings call transcript (Motley Fool, Seeking Alpha, 2026-02-10)
- HousingWire coverage of Rocket-Redfin combination
- MarketBeat, public.com, stockanalysis.com (analyst consensus, April 2026)
- Nasdaq, Fintel (short interest 7.89%)
- GuruFocus (April 2026 valuation update)
- Zillow IR site

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $45.63 (Yahoo Finance, April 24, 2026)
- Captured –49% drawdown from $90 highs and Rocket-Redfin overhang as central setup
- Documented strong segment-level execution (Mortgages +39%, Rentals +45%)

### Thesis Status
- **Overall**: Initiated — Constructive (dominant marketplace at deep cycle trough)
- **BAIT signal**: Triple overlap (B + A Strong + I Moderate); T Weak
- **PW EV**: $69 (3-yr) vs. $45.63 spot = +51% upside

### Recommendation
- **For a non-holder**: **Initiate** — Asymmetric entry at $45.63; PW EV +51%, median analyst target +88–102%
- **For a current holder**: **Add** — Concentrate adds in $40–50 zone

**Next review trigger**: Q1 2026 earnings — early May 2026
