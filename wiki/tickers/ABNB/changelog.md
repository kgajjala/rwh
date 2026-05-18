# ABNB — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-05-18] — Paused (Workflow C.1)

**Trigger**: User-directed pause — no longer tracking this ticker.
**Last Active Baseline**: [2026-05-10 Q1 2026 Earnings + v2.4→v2.14 Schema Migration](#) (entry below).

### What Changed
- Status: Active → **Paused — since 2026-05-18**
- ABNB removed from `wiki/watchlist.md` Conviction Ranking; added to Paused Tickers footer.
- `wiki/index.md` Status column → Paused (Last Updated preserved at 2026-05-10 per Workflow C.1 step 5).
- `README.md` Status column → Paused (Last Updated + Punchline preserved per Workflow C.1 step 5).

### Thesis Status
- **Overall**: Unchanged at pause-point. Q1 2026 step-change print + raised FY26 guidance already captured in the same-day Workflow B entry. May 20 Summer Release optionality remains on-record at pre-pause baseline; coverage frozen until resume.

**Next review trigger**: Resume on user request (Workflow C.2 catch-up).

---

## [2026-05-10] — Q1 2026 Earnings + v2.4→v2.14 Schema Migration

**Trigger**: Q1 2026 earnings reported May 7, 2026 (post-close); Q1 2026 Shareholder Letter (Pattern B per CLAUDE.md Rule #19); plus full v2.14 lazy migration overlay applying Rules #18, #23, #24, #25, #26.

**Sources reviewed**:
- [Q1 2026 Shareholder Letter PDF](https://s26.q4cdn.com/656283129/files/doc_financials/2026/q1/Q1-26-Shareholder-Letter.pdf) — saved to `raw/ABNB/shareholder-letters/` (URL reference; binary PDF)
- [Q1 2026 8-K via StockTitan](https://www.stocktitan.net/sec-filings/ABNB/8-k-airbnb-inc-reports-material-event-fa489e87ecd6.html) — full financial metrics extracted
- [Q1 2026 Earnings Call Transcript via Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/05/07/airbnb-abnb-q1-2026-earnings-call-transcript/) — CEO/CFO quotes extracted
- [Yahoo Finance — ABNB live price](https://finance.yahoo.com/quote/ABNB) — $141.49 (2026-05-08)
- [StockAnalysis — ABNB statistics](https://stockanalysis.com/stocks/abnb/statistics/) — short interest, float, shares
- [Benzinga — analyst upgrades May 2026](https://www.benzinga.com/analyst-stock-ratings/upgrades/26/05/52243432/this-airbnb-analyst-turns-bullish-here-are-top-5-upgrades-for-monday-2)
- [TIKR — Oppenheimer upgrade pre-print](https://www.tikr.com/blog/airbnb-reports-q1-2026-earnings-today-two-analyst-upgrades-suggest-the-market-is-still-underpricing-the-stock)
- [StockTitan Form 4 (Mertz May 6)](https://www.stocktitan.net/sec-filings/ABNB/form-4-airbnb-inc-insider-trading-activity-0856ba01b4ee.html); [Gebbia Form 4 (May 4)](https://www.stocktitan.net/sec-filings/ABNB/form-4-airbnb-inc-insider-trading-activity-4ce5c0f658d7.html)
- [Skift — loyalty program](https://skift.com/2026/02/18/airbnb-tests-loyalty-benefits-chesky-says-program-could-be-a-massive-accelerant/)
- [Rental Scale-Up — May 20 Summer Release preview](https://www.rentalscaleup.com/airbnb-may-20-2026-summer-release-what-to-expect-and-why-this-update-matters-more-than-ever/)

### What Changed

**Q1 2026 Earnings — Key Metrics**:
- Revenue: **$2.678B (+18% YoY)** — beat high-end of $2.59–2.63B guide by ≈2pts; acceleration from +12% FY2025
- GBV: **$29.2B (+19% YoY; +13% ex-FX)** — above the "low-teens" guide; sequential acceleration from Q4's +16%
- Nights & Seats Booked: **156.2M (+9% YoY)**
- ADR: **$187 (+9% YoY; +4% ex-FX)**
- Adj. EBITDA: **$519M (+24% YoY); 19% margin** — up 100bps YoY
- Net Income: **$160M; EPS $0.26** — missed consensus ≈$0.30 by ≈13%
- FCF: **$1.704B** ($4.54B TTM, 36% TTM margin)
- Buyback: **$1.1B in Q1**; authorization remaining reduced from $5.6B → **$4.5B**
- Balance sheet: **$12.1B cash + ST investments**; received investment-grade (A-/Baa1); issued $2.5B senior notes; repaid $2.0B converts
- App nights: **63% of total** (up from 58%), +22% YoY — owned-channel deepening

**Q2 2026 Guide**:
- Revenue: $3.54–$3.60B (+14–16% YoY; ≈3pt FX tailwind)
- GBV: Low double digits
- Adj. EBITDA margin: up YoY; ≈100bps ME conflict headwind

**FY2026 Guide (raised)**:
- Revenue growth: low-to-mid-teens (raised from low-double-digits)
- Adj. EBITDA margin: at least 35%

**New Primary Source — Q1 2026 Letter (Chesky)**:
- AI writes 60% of new code (≈2× industry); AI resolves 40% of support contacts (up from 33% in Q4)
- Cross-sell quantified for first time: 25% of new Experience bookers add stay/service; 55% of hotel bookers return to book a home
- May 20 Summer Release confirmed: hotels product/strategy updates, AI search, experiences expansion
- World Cup 2026: 100,000+ homes newly listed
- Loyalty: Chesky confirms testing; framed as "could be a massive accelerant"

**Analyst actions**:
- Oppenheimer: Perform → Outperform, $180 PT (May 4, pre-print)
- Evercore ISI: PT $145 → $155 (May 8)
- Benchmark: PT $145 → $160 (May 8)
- Deutsche Bank: PT $165 → $170 (May 8)
- B. Riley: PT $170 → $180 (May 8)
- Wells Fargo: already Overweight $178 (April 22)
- Consensus median PT now ≈$154 (up from ≈$149)

**v2.14 Schema Migration applied**:
- **Header**: Schema v2.8 → v2.14; Last Updated → 2026-05-10; Live Price updated to $141.49
- **Rule #18 (Summary)**: Full 4-part Summary block — thesis+verbs, 8-col scenario table, 6-cell KPI strip, 3🟢 + 3⚠️ + Next read — written fresh; replaces v2.8 bullet-list summary
- **Rule #23 (Moat in §3 only)**: Standalone "Competitive Moat" section (was §5) merged into §3; all moat detail lives in §3; standalone block removed
- **Rule #24 (Competitive Landscape)**: Existing §5 Competitive Landscape (already partially migrated in v2.8) retained and refreshed in §3
- **Rule #25 (Risk materiality filter)**: §6 fully filtered; Q2 GBV deceleration risk added; ME conflict headwind added; May 20 Summer Release failure added as new thesis-break trigger
- **Rule #26 (5-yr terminal §11; PW EV anchors §13)**: Horizon extended 3-yr → 5-yr (FY2028 → FY2030); Bull+ scenario added at $300/10%; scenarios recalibrated; PW EV $162 → **$175** (old 3-yr) → **$189** (new 5-yr); R/R ~3.4:1 → **≈5.5:1**; §13 zones updated
- **Section numbering**: Aligned with v2.14 13-section structure (§1–§13); prior ABNB used non-standard numbering (§2 was Geographic, §4 was Revenue Mix, §10 was Valuation, §11 was Catalyst, §12 was BAIT, §13 was Bull/Bear, §14 was PW EV, §15 was Recommendation) — all renumbered
- **§4 (Management)**: Q1 2026 letter commentary added; multi-year arc table extended with Q1 2026 column; CFO balance-sheet upgrade and investment-grade ratings added
- **§5 (Strategic Growth)**: Hotels cross-sell metric added; May 20 Summer Release added as formal catalyst; World Cup supply added; loyalty program added
- **§6 (Risks)**: Q2 GBV deceleration + ME conflict added; May 20 failure added; prior 5-yr risk arc table replaced with synthesis paragraph per Rule #21
- **§9 (Catalyst & Sentiment)**: Full refresh — price, analyst actions (6 new entries), insider activity (Mertz May 6 + Gebbia May 4 + equity grants), next earnings Aug 5 confirmed
- **§10 (BAIT)**: BAIT conviction upgraded Low-Moderate → Moderate; double-overlap (A/T); cross-sell quantification and AI compounding are the analytical edge drivers
- **§11 (Bull/Bear/Base)**: 5-yr terminal horizon; Bull+ at $300/10%; Bull $250/25%; Base $175/45%; Bear $90/20%
- **§12 (PW EV)**: Recomputed; PW EV $189 vs. $141.49 = +34% / ≈+6%/yr; R/R ≈5.5:1

### Thesis Status

- **Overall**: **Strengthened** — Q1 beat + FY2026 guidance raised + cross-sell metrics quantified for first time; BAIT upgraded
- **BAIT delta**: Low-Moderate → **Moderate** (double overlap A/T); cross-sell data is the new analytical edge
- **Price target delta**: PW EV $162 (3-yr) → **$189 (5-yr)** | Bull $210 (3-yr) → **$250 (5-yr)** | Base $160 → **$175** | Bear $95 → **$90** | R/R ≈3.4:1 → **≈5.5:1**
- **Catalyst & Sentiment delta**: 6 analyst actions (2 upgrades, 4 PT raises); consensus PT $149 → $154; 2 new insider transactions (Mertz May 6; Gebbia May 4); next earnings Aug 5 confirmed; May 20 Summer Release added as near-term catalyst

### Recommendation

- **For a non-holder**: **Initiate** — cross-sell thesis now quantified; FCF yield ≈5.4% at $141.49; stronger entry below $130
- **For a current holder**: **Add on dips** / **Hold** — quality compounder; May 20 catalyst + $4.5B buyback support; trim into $195+

**Next review trigger**: May 20, 2026 Summer Release (hotels strategy, AI search, experiences rollout, loyalty signal). Then Q2 2026 earnings ≈Aug 5, 2026.

---

## [2026-05-01] — No Material Events

**Lookback window**: 2026-04-26 → 2026-05-01
**Sources scanned**: IR, SEC EDGAR, analyst feed, short-interest, insider feed, news

### Snapshot
- Price: **$140.36** (Δ vs. last entry: **−1.7%** from $142.82) — [WallStreetZen ABNB forecast](https://www.wallstreetzen.com/stocks/us/nasdaq/abnb/stock-forecast)
- 52-wk range: $110.81 – $147.25 (% from high: **−4.7%**)
- Short interest: not freshly polled — prior baseline holds
- Analyst consensus: median target $150.10 across 33 analysts; recent: Tigress Financial / Wells Fargo / Truist all clustered ~$150 in late-March/early-April (already in baseline) — [TIKR Q1 preview](https://www.tikr.com/blog/airbnb-stock-pulls-back-before-earnings-is-210-fair-value-still-possible)
- News scanned and dismissed:
  - Q1 print expected May 7, 2026 post-close — pre-print drift; no thesis-changing news in window

**Recommendation**: Unchanged.
**Next review trigger**: **Q1 2026 earnings — May 7, 2026 post-close** (tests $2.59–2.63B revenue guide / GBV growth low-teens / Experiences scaling; first post-print weekly will absorb).

---

## [2026-04-26] — v2.6+v2.7+v2.8 Retrofit (Schema Refactor)

**Trigger**: Batch retrofit applying v2.6 (shareholder-letter + 10-K MD&A primary-source synthesis), v2.7 (5-year baselines + Pattern B quarterly-letter substitution), and v2.8 (synthesis discipline, output discipline, moat-section consolidation, competitive-landscape integration, risk-factor materiality filter, R/R discipline). No new earnings event since prior baseline.

**Sources reviewed**:
- [Q4 2025 Shareholder Letter PDF](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q4/Airbnb_Q4-2025-Shareholder-Letter.pdf) — fetched
- [Q4 2025 Earnings Call Transcript via Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/02/12/airbnb-abnb-q4-2025-earnings-call-transcript/) — primary CEO/CFO quote source
- [Airbnb 10-K FY2024 SEC EDGAR HTML](https://www.sec.gov/Archives/edgar/data/1559720/000155972025000010/abnb-20241231.htm) — Item 1A risk factors and MD&A via aggregator summary
- [StockTitan 10-K summary](https://www.stocktitan.net/sec-filings/ABNB/10-k-airbnb-inc-files-annual-report-eacbf4dc6b2e.html) — 10-K Item 1A extraction (PDF binary fallback)
- [Skift Research — STR market share 2024](https://skift.com/2025/03/14/short-term-rentals-airbnbs-dominance-and-bookings-gains-in-1-chart/) — competitive landscape data
- StockTitan Form 4 filings (CFO Mertz March + April 2026 sales)
- Yahoo Finance live price re-verification (price unchanged at $142.82 from prior 2026-04-24 verification)

### What Changed (by Section)

- **Header** — bumped Schema v2.5 → v2.8; Last Updated 2026-04-25 → 2026-04-26
- **Summary** — refreshed; added explicit moat verdict line per Rule #23 (moat consolidated to §5); R/R figure (~3.4:1) added per Rule #26 anchored to §13 Bull/Bear midpoints
- **Business Overview** — retired the standalone "Moat Assessment" block per Rule #23; integrated Q4 2025 operational scale stats (121.9M nights, ADR $168, 5M+ hosts from 10-K)
- **§2 (Annual Financial Metrics)** — added `### Primary Source: 10-K Segment Detail (FY2024)` subsection with 61% international revenue + take-rate stability + direct-traffic dominance synthesis; refreshed quarterly trajectory with Q4 actuals (nights & seats, ADR, EBITDA margin)
- **§3 (Geographic)** — added Brazil top-5 + first-time-booker contributor #2 detail from Q4 2025 letter
- **§5 (Competitive Moat)** — added mandatory `### Competitive Landscape` subsection per Rule #24 with named peers (BKNG, Vrbo/EXPE, TCOM, MMYT, hotels) + market share figures (Skift) + explicit framing of how ABNB's moat differs (verb brand, ~90% direct traffic, +16pt share gain 2019→2024, BKNG marketing intensity comparison)
- **§6 (Management)** — added `### Recent Management Commentary — Primary Source Synthesis` subsection with Chesky/Mertz Q4 2025 verbatim quotes + 5-year strategic-framework arc table (lodging-vs-multi-vertical, capital allocation, AI, international); Form 4 detail integrated
- **§7 (Strategic Growth)** — refreshed with AI-native support specifics (1/3 of NA support resolved by AI) + Project Hawaii framing + Reserve Now Pay Later
- **§8 (Key Risks)** — applied Rule #25 materiality filter; dropped boilerplate; added differentiation/priced-in/thesis-break tags; added IRS $1.3B IP-valuation dispute (not priced in) + AI-search disruption risk + Italian tax-withholding settlements; replaced multi-row "5-Year Risk Factor Evolution Arc" table with synthesis paragraph per Rule #21
- **§9 (Macro)** — added EU-wide STR rules effective May 2026 + Italian settlements detail + Q1 ~3pt FX tailwind disclosure
- **§10 (Valuation)** — refreshed peer comparison with FCF-margin and YoY growth columns; sharpened the "why discount to BKNG" framing; added 19–20× EV/FCF re-rating implied $165–175 fair value
- **§11 (Catalyst & Sentiment)** — refreshed price/short interest/insider activity; short cover from 4.2% → 2.4% noted; CFO Mertz March + April 10b5-1 sales added; EU STR rules May 2026 added to upcoming catalysts
- **§13 / §14** — scenario probabilities and PW EV preserved (no new fundamentals shift); added explicit R/R framing per Rule #26 (~3.4:1 Bull/Bear)
- **§15 (Recommendation)** — refreshed thesis-break triggers (added IRS adverse ruling + BKNG share-gain acceleration as new triggers); preserved entry/trim/exit zones
- **Sources** — appended primary-source PDFs and Q1/Q2/Q3 2025 + Q4 2024 shareholder letter URLs

### Thesis Status
- **Overall**: **Unchanged** vs. prior v2.5 framing — quality compounder at fair-to-modestly-rich price
- **BAIT delta**: Unchanged (single overlap A Moderate; T event-dependent); Conviction Low-Moderate
- **Price target delta**: Bull/Base/Bear unchanged ($210 / $160 / $95); PW EV $162; R/R now stated explicitly ~3.4:1
- **Catalyst & Sentiment delta**: Short interest decreased 4.2% → 2.4% (post-Q4 cover); CFO 10b5-1 sales noted; Q1 2026 print May 7 unchanged

### Recommendation
- **For a non-holder**: **Watch** — initiate on pullback into $120–130 zone (~6.5% FCF yield)
- **For a current holder**: **Hold** — trim into $170+ if reached

**Next review trigger**: Q1 2026 earnings on May 7, 2026 (post-close). GBV YoY ≥14% to confirm Q4 inflection.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added ABNB to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Airbnb Q4 2025 / FY2025 press release and earnings call transcript (2026-02-12, IR / Motley Fool / Stocktitan)
- Airbnb Q1 2026 earnings preview (financialcontent.com / barchart 2026-04-21)
- Wells Fargo upgrade note via 247wallst.com (2026-04-22)
- Yahoo Finance JSON API live price (2026-04-24)
- Analyst consensus aggregators (TipRanks, MarketBeat, stockanalysis.com)

### What Changed
- Initial compilation; no prior wiki content for this ticker.
- Live price verified at $142.82 (Yahoo Finance, April 24, 2026); trading 3% off 52-wk high of $147.25.
- FY2025 confirmed: revenue $12.2B (+12%), FCF $4.6B (38% margin), $3.8B buyback, $5.6B authorization remaining.
- Q4 2025 GBV +16% YoY = highest growth in 2 years — the inflection.
- FY26 guide: Q1 revenue $2.59–2.63B (+14–16%), full-year low-double-digit acceleration.
- Wells Fargo upgrade to Overweight April 22, 2026 with $178 PT (citing AI-driven product gains).
- 3-year PW EV ~$162 vs. spot $142.82 = +13% return (modest positive).

### Thesis Status
- **Overall**: Initiated — Watch (non-holder) / Hold (holder)
- **BAIT signal**: Single-overlap (A only Moderate); Conviction Low-Moderate
- **PW EV**: $162 vs. spot $142.82 (+13% over 3 years, ~4.5%/yr)

### Recommendation
- **For a non-holder**: Watch — initiate on pullback into $120–130 zone.
- **For a current holder**: Hold — quality compounder; trim into $170+ if reached.

**Next review trigger**: Q1 2026 earnings on May 7, 2026 (post-close). Key item: GBV YoY growth ≥14% to confirm Q4 inflection.