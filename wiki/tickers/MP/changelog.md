# MP — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: Schema migration from v2.5 (15-section) to v2.9 (13-section); live data refresh; primary source fetch for shareholder letter pattern classification, 10-K context, and recent Q4 2025 + 10X news.

**Sources reviewed**:
- Yahoo Finance / CNBC / search aggregators (live price ~$60.73, April 24–26, 2026)
- [MP Materials Q4 2025 / FY2025 press release](https://investors.mpmaterials.com/investor-news/news-details/2026/MP-Materials-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx) (BusinessWire, Feb 26, 2026)
- [Q4 2025 earnings call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-mp-materials-q4-2025-sees-eps-beat-revenue-miss-93CH-4530227) (Investing.com)
- [10X Northlake campus announcement](https://investors.mpmaterials.com/investor-news/news-details/2026/MP-Materials-Selects-Northlake-Texas-as-the-Site-of-10X-a-New-U-S--Rare-Earth-Magnet-Manufacturing-Campus/default.aspx) (Feb 26, 2026)
- [SEC EDGAR — MP 10-K FY2024](https://www.sec.gov/Archives/edgar/data/1801368/000180136825000009/mp-20241231.htm)
- [SEC EDGAR — annual report to shareholders FY2023](https://www.sec.gov/Archives/edgar/data/1801368/000180136824000038/annualreporttoshareholders.pdf)
- [OpenInsider — MP Form 4 insider trades](http://openinsider.com/MP); [StockTitan — Litinsky April 2026 sales](https://www.stocktitan.net/sec-filings/MP/form-4-mp-materials-corp-de-insider-trading-activity-917b65ce44d0.html)
- [Fintel — MP short interest](https://fintel.io/ss/us/mp) (18.9% of float)
- [stockanalysis.com financials](https://stockanalysis.com/stocks/mp/financials/); [stockanalysis.com forecast](https://stockanalysis.com/stocks/mp/forecast/)
- [MarketBeat MP forecast](https://www.marketbeat.com/stocks/NYSE/MP/forecast/)
- [Wedbush initiation — Investing.com](https://www.investing.com/news/analyst-ratings/wedbush-initiates-mp-materials-stock-with-outperform-rating-93CH-4623144)
- [Bloomberg Intelligence rare earth market share press release](https://www.bloomberg.com/company/press/world-scrambles-for-rare-earths-to-erode-chinas-dominance-from-90-to-69-market-share-and-gain-pricing-power-according-to-bloomberg-intelligence/)
- [Rare Earth Market Outlook March 2026](https://rare-earth-mining.com/rare-earth-market-pricing-analysis-march-2026/)
- Multiple earnings releases FY2021–FY2024 (IR site) for management commentary arc
- [MP Q1 2026 earnings date announcement](https://www.businesswire.com/news/home/20260409589711/en/MP-Materials-Announces-Date-for-First-Quarter-2026-Financial-Results-and-Webcast)

### What Changed
- **Structure**: Migrated from 15-section v2.5 to 13-section v2.9 layout
- **Section 1 (Why Exist) retired**: Founding-insight content folded into Business Overview; pivotal question into its own header subsection
- **Old Sections 3+4 (Geographic + Revenue Mix) merged**: New Section 2 covers revenue mix + geographic split + segment economics + forward shifts in one place
- **Sections renumbered**: old 5–15 → new 3–13 throughout
- **Section 3 (Competitive Moat + Landscape)**: Added Competitive Landscape subsection with named peers (Lynas, Energy Fuels, China Northern Rare Earth, Shenghe) + market share context + explicit how-MP-differs framing; standalone Moat Assessment block retired
- **Section 4 (Management)**: Added Recent Management Commentary subsection; classified as Pattern C (no standalone annual letter); built 4-year executive commentary arc from earnings releases and proxy; new material added: CEO insider sales pattern (9 sales, $78M, 6 months) surfaced as a thesis risk
- **Section 6 (Key Risks)**: Applied Rule #25 materiality filter — dropped generic boilerplate; kept differentiated risks including CEO insider selling pattern (new — not in prior version); added 5-year risk factor evolution synthesis paragraph; updated Priced-In column
- **Section 7 (Macro)**: Updated with China market-share trajectory data (90% → 69% by 2030 per Bloomberg Intelligence), NdPr deficit projections 2025–2027, "physical AI economy" framing from Q4 2025 call
- **Section 8 (Valuation)**: Refreshed multiples; added peer comparison table with Lynas/Energy Fuels context
- **Section 9 (Catalyst & Sentiment Tracker)**: Fully refreshed — confirmed Q1 2026 earnings **May 7, 2026**; updated short interest to 18.9% (vs. 14.47% prior); updated insider activity (Litinsky $78M in 6 months — material new finding); added Wedbush $90 initiation Apr 20; added 10X campus as upcoming catalyst
- **Section 10 (BAIT)**: Updated T lens (elevated short interest 18.9% vs. 14.47%) and B lens (10X commitment added to bear concern); updated BAIT verdict note on CEO insider sales as counterweight
- **Section 11 (Bull/Bear/Base)**: Revised probabilities — Bull 25% (was 30%), Bear 25% (was 20%) reflecting elevated execution risk from 10X + CEO insider selling; Base 50% unchanged; Bear case price raised to $28 (was $32) reflecting dilution risk
- **Section 12 (PW EV)**: Recomputed — PW EV ~$80.50 (vs. ~$85 prior) reflecting revised scenario probabilities; R/R = ~2.1:1; R/R rule anchored to Section 11 Bull/Bear midpoints per Rule #26
- **Section 13 (Recommendation)**: Refreshed thesis sentence, non-holder/holder verbs; added next-review checklist items (CEO commentary on insider sales; 10X construction update; deferred Magnetics revenue); added CEO departure as thesis-break trigger
- **Summary**: Refreshed per Rule #18 — added CEO insider selling ⚠️ bullet; updated 10X framing; updated BAIT verdict
- **Sources**: All citations linkified per Rule #16; all sources are absolute URLs
- **Rule #21 (Synthesis)**: 5-Year Risk Factor Evolution replaced with synthesis paragraph; verbose source tables collapsed to prose where appropriate
- **Rule #22**: No CLAUDE.md self-references in page body; table orientation discipline applied; bullets for data-dense sentences

### Thesis Status
- **Overall**: **Unchanged** vs. prior version — constructive strategic-asset thesis intact; PW EV modestly lower (~$80.50 vs. ~$85) due to revised probabilities reflecting 10X execution risk and CEO insider selling pattern
- **BAIT delta**: Unchanged Triple overlap verdict; T upgraded (18.9% short, up from 14.47%); B modestly weakened (CEO selling creates overhang)
- **Price target delta**: Bull $130 (unchanged) | Base $82 (was $80) | Bear $28 (was $32)

### Recommendation
- **For a non-holder**: 🟢 **Initiate** in $48–62 entry zone — strategic-asset thesis with 3-yr PW EV ~$80.50 (+33%); best entry on dips
- **For a current holder**: 🟢 **Hold / Add** — incremental adds in $50–62 zone; monitor CEO insider sales quarterly

**Next review trigger**: Q1 2026 earnings — **May 7, 2026** (post-close, 5pm ET); key items: PPA income run-rate, Magnetics segment EBITDA, 10X construction update, balance sheet cash burn, CEO commentary on insider sales

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added MP to wiki on 2026-04-24 as part of a 25-ticker expansion batch (Group E).

**Sources reviewed**:
- Yahoo Finance live price (2026-04-24)
- MP Materials Q4 2025 / FY2025 press release (IR)
- MP Materials DoD partnership press release (2025-07-09, IR)
- CNBC coverage of Saudi Maaden JV (2025-11-19)
- Mining.com coverage of $150M Pentagon loan
- 24/7 Wall St. Wedbush $90 PT coverage (2026-04-20)
- MarketBeat, public.com, stockanalysis.com (analyst consensus, April 2026)
- Fintel, Benzinga (short interest 14.47%)
- Columbia CGEP analysis of strategic-minerals policy
- Seeking Alpha "Market Is Missing This Rare Earth Opportunity"

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $60.73 (Yahoo Finance, April 24, 2026)
- Captured DoD partnership ($400M pref + $110/kg floor + 10-yr offtake) as transformational catalyst
- Documented Magnetics segment commercial launch + Apple/GM offtakes
- Saudi Maaden JV noted as long-dated optionality

### Thesis Status
- **Overall**: Initiated — Constructive (strategic-asset compounder; unique moat)
- **BAIT signal**: Triple overlap (A + I Strong + B/T Moderate)
- **PW EV**: $85 (3-yr) vs. $60.73 spot = +40% upside

### Recommendation
- **For a non-holder**: **Initiate** — Strategic-asset thesis; PW EV +40%, Wedbush bull $90
- **For a current holder**: **Hold / Add** — Concentrate adds in $50–62 zone; tolerate fuller valuation given asset uniqueness

**Next review trigger**: Q1 2026 earnings — early May 2026
