# CPNG — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-05-10] — Q1 2026 Earnings + v2.8→v2.14 Schema Migration

**Trigger**: Q1 2026 earnings printed May 5, 2026 (post-close); 8-K filed May 5, 2026. Stock declined ≈15% to $16.98 by May 10 on deeper EBITDA miss and Q2 margin headwind guidance. Two sell-side downgrades (Citi, Deutsche Bank) on May 6–7.

**Sources reviewed**:
- [Coupang Q1 2026 8-K (May 5, 2026)](https://www.stocktitan.net/sec-filings/CPNG/8-k-coupang-inc-reports-material-event-e31cba6cbdbf.html) — primary financial figures
- [Q1 2026 Earnings Release PDF](https://s206.q4cdn.com/919117365/files/doc_financials/2026/q1/2026-Q1_Earnings-Release.pdf)
- [Q1 2026 Earnings Call Transcript — Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/05/05/coupang-cpng-q1-2026-earnings-transcript/)
- [Q1 2026 Earnings Call Transcript — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/coupang-cpng-q1-2026-earnings-035143906.html)
- [Yahoo Finance — CPNG live quote](https://finance.yahoo.com/quote/CPNG) (price $16.98, 2026-05-10)
- [MarketBeat — CPNG analyst ratings](https://www.marketbeat.com/stocks/NYSE/CPNG/forecast/) (4B/5H/2S; median $26.92)
- [Finviz — CPNG](https://finviz.com/quote.ashx?t=CPNG) (short interest 2.94%; forward P/E 34.85; EV $29.49B)
- [StockTitan — Greenoaks/Neil Mehta Form 4](https://www.stocktitan.net/sec-filings/CPNG/form-4-coupang-inc-insider-trading-activity-c035d8ad4bac.html) (7.35M shares purchased March 2026)
- [Investing.com — Morgan Stanley target cut](https://www.investing.com/news/analyst-ratings/morgan-stanley-cuts-coupang-stock-price-target-on-margin-outlook-93CH-4663575)
- Raw files: `raw/CPNG/press-releases/2026-Q1-earnings-release.txt`; `raw/CPNG/transcripts/2026-Q1-earnings-call-transcript.txt`

### What Changed

- **Header**: Schema v2.8 → v2.14; Last Updated 2026-04-26 → 2026-05-10; Live Price $20.51 → $16.98
- **Summary (Rule #18)**: Rebuilt as full 4-part v2.14 block — Thesis sentence + verb line; Scenario Table (5-yr terminal FY2030E); KPI Strip; Why/Why not/Next read bullets
- **Key Stats Snapshot**: Added Q1 2026 actuals — $8.5B revenue (+8% CC); Product Commerce $7.2B (+5% CC); DO $1.3B (+28%); gross margin 27.0% (–228 bps); adj EBITDA $29M (0.3%); EPS –$0.15; active customers 23.9M; WOW 80% recovery; Q2 guide +9–10% CC / –300–400 bps EBITDA margin; next earnings Aug 4, 2026
- **§1 (Annual Financial Metrics)**: Added Q1 2026 to quarterly trend table; updated FY2026E estimates to reflect post-Q1 consensus revision to $37.8B revenue; added FCF row (TTM $301M compressed from $1.025B)
- **§2 (Revenue Mix)**: Added Q1 2026 segment actuals; updated Taiwan narrative with "cohort retention reminiscent of early Korea" quote
- **§3 (Competitive Moat & Landscape — Rule #23/24)**: Added Taiwan peers (Shopee, Momo, PChome) and Farfetch peers (Net-a-Porter, Mytheresa); updated AliExpress as explicitly raised in Q1 Q&A; flagged Farfetch silence in Q1 transcript
- **§4 (Management & Leadership — Rule #19)**: Added Q1 2026 verbatim quotes (Bom Kim, Gaurav Anand); updated RMC synthesis with 2026 "absorb underutilization" framing; added Greenoaks Form 4 as external intrinsic-value reference
- **§5 (Strategic Growth Initiatives)**: Updated Korea recovery / Taiwan / Farfetch / WOW status from Q1 2026 data
- **§6 (Key Risks — Rule #25)**: Rebuilt materiality filter — added EBITDA trough extension risk (Developing Offerings, Rule #25(d)); added Farfetch silent deterioration risk ("not priced in"); added CEO governance regulatory review risk; updated AliExpress threat as Q1-Q&A confirmed; dropped resolved/generic items; risk factor evolution condensed to prose per Rule #21
- **§7 (Industry Macro)**: Minor updates — AliExpress cross-border growing Korean share now confirmed in Q1 Q&A; Taiwan TAM narrative unchanged
- **§8 (Valuation)**: Updated multiples to $16.98 / $29.5B EV; updated peer table; assessment updated for EBITDA denominator trough compression
- **§9 (Catalyst & Sentiment Tracker)**: Full refresh — live price $16.98 (–50% from 52-wk high); analyst consensus downgraded to Hold (4B/5H/2S) from prior Strong Buy; added Citi + DB downgrades; Barclays + BofA + MS maintain Buy/Overweight; short interest ≈2.9%; Greenoaks insider buy added; Q1 2026 earnings news added; next earnings catalyst Aug 4, 2026; prior "May 5, 2026" catalyst moved to delivered (no ✅ markup — it's a past event, captured in news)
- **§10 (BAIT)**: Updated — B (Strong; –50% capitulation, two downgrades); A (Strong; WOW recovery, monthly trajectory, Greenoaks buy reference); I (Moderate; Taiwan cohort quote buried; Farfetch silence is info gap); T (Weak; near 52-wk low, fresh downgrades, 3-month wait for next catalyst). Verdict: Double overlap (B+A)
- **§11 (Bull/Bear/Base)**: Extended to 5-year terminal (FY2030E) per Rule #26; Bear raised to 25% / $9 (deeper EBITDA trough + Farfetch risk); Base $22 at 45% (FY2030E recovery required); Bull $36 at 22%; Bull+ $48 at 8%
- **§12 (PW EV)**: Recomputed — PW EV ≈$24 at $16.98; +41% / ≈+7%/yr; R/R ≈2.4:1 Bull/Bear; rises to ≈3.8:1 with Bull+. Entry zone at current price is viable but trough is extended
- **§13 (Recommendation)**: Updated verb line — non-holder Watch (unchanged), holder Hold (unchanged but entry zone expanded lower to $14–18 from $16–19; Greenoaks $18.40–$18.68 is new reference floor); thesis-break triggers updated — added Farfetch negative YoY growth, stock below $16.74 technical break, WOW recovery plateau below 90%

### Thesis Status
- **Overall**: 🔴 **Weakened** vs. v2.8 — Q1 EBITDA collapse ($29M vs. $382M prior year) and Q2 guide (–300–400 bps EBITDA YoY) are materially more negative than prior thesis assumed; management deferred margin expansion to 2027; Farfetch absent from transcript. Moat signals (WOW 80% recovery, Taiwan cohort read) are intact but are not near-term earnings catalysts.
- **BAIT delta**: Double overlap maintained (B+A); T downgraded from Weak-to-Moderate → Weak (two fresh downgrades; near 52-wk low; 3-month wait)
- **Price target delta**: Bull $36 (unchanged) | Base $22 (unchanged) | Bear $9 (from $11 — deeper trough, Farfetch risk). PW EV $26 (3-yr at $20.51) → $24 (5-yr at $16.98)
- **Catalyst & Sentiment delta**: Consensus downgraded to Hold (4B/5H/2S) from Strong Buy; Citi + DB downgrades; next catalyst Aug 4, 2026 (was May 5, 2026); Greenoaks 7.35M share purchase at $18.40–$18.68 is new insider signal

### Recommendation
- **For a non-holder**: 🟡 **Watch** — PW EV +41% / ≈+7%/yr at $16.98 is modestly attractive; entry zone $14–18; small starter position viable for patient holders; wait for Q2 (Aug 4) to confirm Korea trajectory
- **For a current holder**: 🟡 **Hold** — moat intact; WOW recovery demonstrates structural stickiness; net cash funds all 2026 burn; Greenoaks insider buy at $18.40–$18.68 provides downside reference; do not exit; do not add aggressively until Q2 confirms trajectory

**Next review trigger**: 📅 Q2 2026 earnings — August 4, 2026.

---

## [2026-04-26] — v2.6+v2.7+v2.8 Retrofit + Q4 2025 Material Update

**Trigger**: Scheduled v2.8 retrofit batch + integration of material Q4 2025 earnings (printed 2026-02-26) + 33M-account data incident + $1.2B voucher charge + Q1 2026 guide-down to +5–10% CC + 2026 Developing Offerings EBITDA loss guide $950M–$1B. The prior v2.5 page predated the Q4 2025 print and substantially mis-stated Q3 2025 figures (recorded $8.5B / $145M op income vs. actual $9.3B / $162M).

**Sources reviewed** (per Rules #19, #20, #21):
- [Coupang FY2024 10-K (cpng-20241231)](https://www.sec.gov/Archives/edgar/data/1834584/000183458425000030/cpng-20241231.htm) — Item 1A Risk Factors + Item 7 MD&A
- [FY2023 10-K](https://www.sec.gov/Archives/edgar/data/1834584/000183458424000023/cpng-20231231.htm), [FY2022 10-K](https://www.sec.gov/Archives/edgar/data/1834584/000183458423000023/cpng-20221231.htm) — multi-year baseline
- [Q4 2025 earnings call script (Coupang IR)](https://s206.q4cdn.com/919117365/files/doc_financials/2025/q4/Q4-25-Earnings-Call-Script_Final.pdf) — Bom Kim + Gaurav Anand verbatim
- [Q3 2025 earnings call script](https://s206.q4cdn.com/919117365/files/doc_financials/2025/q3/3Q25-Earnings-Script-_-F.pdf)
- [Insider Monkey Q4 2025 transcription](https://www.insidermonkey.com/blog/coupang-inc-nysecpng-q4-2025-earnings-call-transcript-1708133/) — verbatim quote source
- [Yahoo Finance live quote](https://finance.yahoo.com/quote/CPNG) (price $20.51 verified 2026-04-24)
- [StockTitan Q1 2026 calendar](https://www.stocktitan.net/news/CPNG/coupang-to-announce-first-quarter-2026-results-on-may-5-kue8t1ctd4wc.html)
- [Yahoo Finance breach + earnings recaps](https://finance.yahoo.com/news/coupang-cpng-q4-2025-earnings-160202733.html)

### What Changed

- **Schema**: v2.5 → v2.8. Removed standalone Moat Assessment block (Rule #23); consolidated into Section 5. Risk Factor materiality filter applied (Rule #25). R/R re-anchored to Section 13 (Rule #26).
- **Summary**: Re-tagged Bullish → Neutral; recommendation softened to Watch / Hold pending Q1 print.
- **Section 2**: Added FY2024 10-K MD&A subsection; corrected Q3 2025 figures ($9.3B / +18% / $162M); added Q4 2025 quarterly trend including breach-related EBITDA collapse to $267M.
- **Section 5**: Added new Competitive Landscape subsection per Rule #24 — named Korean peers (Naver, Kakao, 11Street, SSG, Lotte ON, AliExpress) with market shares and moat-differentiation framing.
- **Section 6**: Built Recent Management Commentary subsection per Rule #19 — 7 verbatim Bom Kim + Gaurav Anand quotes from Q4 2025 call mapped to investment relevance + 5-year strategic framework synthesis paragraph.
- **Section 8**: Re-built per Rule #25 materiality filter — added breach-overhang risk (#1, "partially priced in"), added DO 2026 burn risk (#2, "not priced in", per Rule #25(d)). Risk Factor evolution rendered as synthesis paragraph per Rule #21.
- **Section 11**: Updated all live-price + analyst + insider + news fields. Earnings date corrected from May 12 to May 5. Added 5.9M-share Q4 2025 buyback execution disclosure ($243M of $1B utilized).
- **Section 13/14**: Re-built scenarios from breach-impacted base. PW EV revised from ~$28 (v2.5) to ~$26. R/R compressed from 5:1 (v2.5) to ~3:1.
- **Section 15**: Recommendation softened — non-holder Initiate → Watch; holder Add → Hold. Entry zone shifted from $17–22 to $16–19 to reflect lower asymmetry.

### Thesis Status
- **Overall**: 🟡 **Weakened** vs. v2.5 — the breach + DO burn step-up materially reduce 3-yr PW EV and asymmetry; moat is intact but near-term setup is more uncertain.
- **BAIT delta**: Triple overlap → Double overlap (T downgraded; behavioral case still strong but informational edge somewhat exhausted post-call disclosure).
- **Price target delta**: Bull $42 → $36 | Base $26 → $22 | Bear $13 → $11. PW EV $28 → $26.
- **Catalyst & Sentiment delta**: Earnings date corrected to May 5; analyst median target revised down to $27.74; new active $1B buyback disclosure ($243M utilized).

### Recommendation
- **For a non-holder**: 🟡 **Watch** — wait for May 5 Q1 print to validate "January was the trough" thesis; initiate post-print on Korea Product Commerce CC growth recovery above +6%.
- **For a current holder**: 🟡 **Hold** — moat intact, gross-margin expansion continued through Q4, $1B buyback signal at sub-$22; add only on $17 retest, reduce only on Q1 trough-call failure.

**Next review trigger**: 📅 Q1 2026 earnings — May 5, 2026 (post-close).

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added CPNG to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Coupang Q4 2025 / FY2025 earnings press release (Coupang IR, Feb 2026)
- Q3 2025 earnings press release (2025-11)
- Q3 2025 earnings call transcript (Yahoo Finance)
- Yahoo Finance live price (2026-04-24)
- stockanalysis.com / MarketBeat consensus forecast page
- TipRanks earnings page
- Quiver Quantitative pre-earnings opinion piece
- Fintel / MarketBeat short interest data (Mar 2026)
- Korea Herald Coupang Play / Paramount+ launch coverage
- Wikipedia entries (Coupang, Coupang Play)
- aboutcoupang.com WOW membership materials
- ainvest.com membership ecosystem and operational efficiency pieces
- Investor's Podcast Network intrinsic value piece

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $20.58 (Yahoo Finance, April 24, 2026)
- Stock at –40% from 52-wk high; near 52-wk low
- FY2025 rev $34.5B (+14%); Q4 2025 op income only $8M (deliberate reinvestment)
- Korea op margin expanding 30–50 bps annually; Dev Off (Farfetch + Taiwan) drag intentional
- ~14M Rocket WOW members in Korea; 3× spend uplift

### Thesis Status
- **Overall**: Initiated — Wide-moat Korean e-commerce platform at deep valuation discount
- **BAIT signal**: Triple overlap (B Strong + A Strong + I/T Moderate); Conviction Moderate-High
- **PW EV**: ~$28 (3-yr) vs. spot $20.58 → +36% / ~11%/yr

### Recommendation
- **For a non-holder**: **Initiate** — among the most asymmetric setups in the wiki; clean Buffett/Munger framing
- **For a current holder**: **Add modestly** into May 12 print if cost basis is above market; otherwise Hold

**Next review trigger**: Q1 2026 earnings — May 12, 2026 (post-close). Korea margin expansion is the central read.
