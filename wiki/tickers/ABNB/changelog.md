# ABNB — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

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
