# CELH — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-05-10] — Q1 2026 Earnings + v2.4→v2.14 Schema Migration

**Trigger**: Q1 2026 earnings print confirmed 2026-05-07 (actual; prior wiki listed 2026-05-12 estimate — corrected). Workflow B incremental + full v2.14 lazy migration overlay.
**Sources reviewed**:
- [Celsius Holdings IR — Q1 2026 Press Release (2026-05-07)](https://ir.celsiusholdingsinc.com/news/news-details/2026/Celsius-Holdings-Reports-First-Quarter-2026-Financial-Results/default.aspx)
- [BusinessWire — Q1 2026 PR mirror](https://www.businesswire.com/news/home/20260507453822/en/Celsius-Holdings-Reports-First-Quarter-2026-Financial-Results)
- [StockTitan — Q1 2026 8-K filing summary](https://www.stocktitan.net/sec-filings/CELH/8-k-celsius-holdings-inc-reports-material-event-f9ad80ab2804.html)
- [Q1 2026 transcript — Motley Fool (2026-05-07)](https://www.fool.com/earnings/call-transcripts/2026/05/07/celsius-celh-q1-2026-earnings-transcript/)
- [StockAnalysis — CELH analyst consensus](https://stockanalysis.com/stocks/celh/forecast/)
- [Fintel — CELH short interest (2026-05-08)](https://fintel.io/s/us/celh)
- [MarketBeat — CELH stock page](https://www.marketbeat.com/stocks/NASDAQ/CELH/)
- [Benzinga — CELH analyst ratings (JPMorgan $70, Rothschild $47)](https://www.benzinga.com/quote/CELH/analyst-ratings)
- [OpenInsider — CELH Form 4 insider activity](http://openinsider.com/CELH)
- [TradingView — post-earnings stock reaction](https://www.tradingview.com/news/stockstory:780c07e04094b:0-why-celsius-celh-shares-are-sliding-today/)

**Raw files added**:
- `raw/CELH/press-releases/2026-05-07_Q1-2026_PR.pointer.md`
- `raw/CELH/transcripts/2026-05-07_Q1-2026_transcript.pointer.md`

### What Changed
- **Earnings date confirmed**: 2026-05-07 (was estimated 2026-05-12 in prior wiki; earnings released pre-market May 7)
- **§ Header**: Schema v2.8 → v2.14; Last Updated 2026-04-26 → 2026-05-10; Live Price $33.26 → $32.29 (post-Q1 reaction)
- **§ Summary (Rule #18 v2.14)**: Rebuilt as 4-part per schema — thesis+verbs line / 8-col scenario table / 6-cell KPI strip / 3🟢+3⚠️+Next-read bullets. Prior 10-bullet freeform block retired.
- **§ Business Overview**: Q1 2026 brand revenue percentages updated (CELSIUS 44%, Alani 47%, Rockstar 9%)
- **§ Pivotal Investment Question**: Refreshed to frame CELSIUS +6% deceleration as the new open question; "fizz-free" thesis added
- **§ Key Stats Snapshot**: Full Q1 2026 data — $782.6M revenue, $0.41 Adj EPS, 48.3% GM, 25.0% Adj EBITDA margin, brand split, 20.9% category share
- **§2 Annual Financial Metrics**: Added Q1 2026 row; brand revenue detail table added; Primary Source MD&A synthesis updated with Q1 2026 gross-margin cadence data
- **§3 Competitive Moat & Landscape (Rule #23 + #24)**: Moat now fully consolidated in §3 only (was also partially in §5 Competitive Moat — renamed per CLAUDE.md section renumbering). CELSIUS deceleration added as vulnerability bullet. Rothschild initiation (international skepticism) added to tail-risk read.
- **§4 Management & Leadership**: Q1 2026 call quotes added (Langhans "Q2 side-step", Fieldly on fizz-free, Alani Nu flavor LTO, Rockstar "stabilization year", cannibalization deflect). 5-Year Arc table updated — 2026 row refreshed to "CELSIUS re-ignition" framing.
- **§5 Strategic Growth Initiatives**: Resequenced; CELSIUS fizz-free moved to #1 (most pressing near-term); Alani Nu integration now complete.
- **§6 Key Risks (Rule #25)**: CELSIUS structural risk probability raised 30% → 40%; Cannibalization risk added as new Row #7 (35%); GM failure risk probability raised 35% → 45%; new Row #10 (consensus too aggressive) added. Insider-cluster risk removed — Form 4 review confirms RSU tax-withholding, not discretionary sales; "$43.2M trailing" aggregate figure flagged as likely inaccurate.
- **§8 Valuation**: Multiples refreshed — EV/EBITDA ~9× (was ~10×) on lower price + higher consensus EBITDA; peer table updated.
- **§9 Catalyst & Sentiment Tracker**: Full refresh — Q1 2026 earnings event added; analyst actions (JPMorgan $70, Morgan Stanley $55, Rothschild $47 Neutral); short interest 10.5% (down from 11.71%); insider activity corrected (RSU withholding, not open-market sales); 52-wk low updated $32.30 → $31.80; upcoming catalysts updated (June shelf resets → Q2).
- **§10 BAIT**: Updated with Q1 print analysis — B Strong reinforced (beat but sold off); A Moderate maintained (fizz-free unproven); I Moderate updated (brand split detail, cannibalization info gap); T Moderate maintained.
- **§11 Bull/Bear/Base**: Extended from 3-year (2029) to **5-year (2031)** terminal per Rule #26. Probabilities adjusted: Bull 30% → 28%, Base 50% → 47%, Bear 20% → 25% (CELSIUS decel raises bear probability). Bear target $20 → $18 (more severe cannibalization scenario).
- **§12 PW EV**: Recomputed on 5-yr basis; PW EV maintained at ~$52. R/R updated: 3.5:1 → 3.7:1 (lower spot price). Annualized return revised from 16% to ~10% (longer 5-yr horizon vs. prior 3-yr).
- **§13 Recommendation**: Entry/trim/exit zones unchanged ($30–36 / $60–70 / >$85). Thesis-break triggers updated — Q1 print miss trigger marked ✅ DE-RISKED. Cannibalization confirmed trigger added. Next review = June shelf-reset data + Q2 earnings (est. Aug 2026).

### Thesis Status
- **Overall**: **Unchanged** vs. v2.8 — Q1 confirmed Alani Nu execution (bullish); CELSIUS +6% deceleration adds residual uncertainty (bearish offset); net thesis intact but conviction edge narrowed slightly
- **BAIT delta**: Triple overlap (B Strong + A Mod + T Mod) preserved; conviction Moderate-High (event-driven toward Q2)
- **Price target delta**: PW EV unchanged ~$52; R/R improved slightly to 3.7:1 on lower spot; sell-side mean targets drifted lower ($66.45 → $62–64) on Morgan Stanley / Rothschild drag
- **Catalyst & Sentiment delta**: Short interest down (11.71% → 10.5%); insider activity corrected (no discretionary selling); JPMorgan raised $70 post-Q1; Morgan Stanley moved to $55; new coverage Rothschild $47 Neutral

### Recommendation
- **For a non-holder**: 🟢 **Watch / Initiate small** — entry zone active at $32; PW EV $52 = 3.7:1 R/R; Q2 is the next inflection point
- **For a current holder**: 🟡 **Hold** — thesis intact; no thesis-break triggers hit; CELSIUS fizz-free needs Q2 to validate

**Next review trigger**: June 2026 shelf-reset scanner data; Q2 2026 earnings (est. August 2026).

---

## [2026-04-26] — v2.6 + v2.7 + v2.8 Retrofit (Schema Refresh)

**Trigger**: Scheduled retrofit pass to apply CLAUDE.md v2.6 (primary-source synthesis depth — letters + 10-K MD&A), v2.7 (5-year baselines + Pattern B/C letter substitution), and v2.8 (synthesis-over-transcription, output discipline, moat consolidation, competitive landscape integration, risk-factor materiality filter, R/R discipline) to CELH.

**Sources reviewed**:
- [Yahoo Finance — CELH](https://finance.yahoo.com/quote/CELH) (live price 2026-04-22 = $33.26; 52-wk $32.30–$66.74; market cap $8.55B; P/E 133)
- [Q4 2025 Earnings Call Transcript (Motley Fool, 2026-02-26)](https://www.fool.com/earnings/call-transcripts/2026/02/26/celsius-celh-q4-2025-earnings-call-transcript/) — verbatim Fieldly + Langhans quotes on PEP captaincy, Alani Nu integration, gross margin guide, Rockstar transition, capital allocation, shelf-space gains
- [TIKR Wall Street consensus piece](https://www.tikr.com/blog/wall-street-is-93-above-where-celsius-holdings-stock-trades-heres-why) — 19/22 Buy/Outperform, mean target $66.45, FY26E rev $3.38B / EBITDA $771M
- [MarketBeat — Earnings calendar](https://www.marketbeat.com/stocks/NASDAQ/CELH/earnings/) — Q1 2026 = 2026-05-12
- [MarketBeat — Short interest](https://www.marketbeat.com/stocks/NASDAQ/CELH/short-interest/) — 11.71% of float; CFO Langhans Form 4 2026-04-18
- [Statista energy drink US share](https://www.statista.com/statistics/306864/market-share-of-leading-energy-drink-brands-in-the-us-based-on-case-volume-sales/) — Red Bull ~35–40%, MNST ~30%, CELH ~20% (Q4'25)
- 5-year SEC EDGAR 10-K browse + DEF 14A 2025/2026 summaries — CIK 0001341766. Direct 10-K HTML fetches returned 403 from agent IP; pointer stubs created in raw/CELH/filings/, verbatim Item 1A re-fetch [link pending] for next pass

**Letter pattern**: **Pattern C** (no standalone shareholder letter). Management framework synthesized via Q4 earnings call transcripts + DEF 14A proxy summaries; pointer stubs for 5 years (2021–2025) created in raw/CELH/shareholder-letters/.

### What Changed (sections refreshed under v2.6/2.7/2.8)
- **Header**: Schema v2.5 → v2.8; Last Updated 2026-04-25 → 2026-04-26; live price refreshed $35.25 → $33.26
- **Summary** (Rule #18): regenerated, 10 emoji-tagged bullets; added R/R + capital-allocation signal + short-interest cover
- **Moat block (standalone)**: **retired** per Rule #23; one-line moat verdict in Summary; full detail consolidated into §5
- **§2 Annual Financials**: extended to 6-year table (FY21–FY26E); added Primary Source 10-K Segment Detail synthesis paragraph (Rule #20) covering 5-year MD&A arc; gross-margin trajectory ~46% FY25 → "low 50s" FY26 guide
- **§5 Competitive Moat + Competitive Landscape**: added required `### Competitive Landscape` subsection (Rule #24) with 7-row peer table (Red Bull, MNST, Bang, Ghost, C4, 5-Hour) + "how CELH's moat differs" framing + tail-risk read (MNST + KDP coordination)
- **§6 RMC Primary Source Synthesis** (Rule #19, Pattern C): added 6 verbatim Fieldly + Langhans quotes from Q4'25 call mapped to investment relevance; 5-Year Strategic Framework Arc table preserved (per Rule #21 — multi-year context retained as table; bulk Risk Factor table converted to synthesis paragraph)
- **§8 Key Risks** (Rule #25 materiality filter): retained 10 differentiated risks; explicitly tagged "**Not priced in**" on PepsiCo renegotiation + MNST/KDP coordination risks; 5-Year Risk Factor Evolution converted from table to synthesis paragraph (Rule #21); insider-cluster selling added as new risk row
- **§10 Valuation**: refreshed multiples on $33.26 price + $3.38B FY26E rev consensus; ~10× FY26E EV/EBITDA
- **§11 Catalyst Tracker**: full refresh — Q1 earnings date corrected to **2026-05-12** (was estimated May 11); short interest 11.71% / 17.39M shares; CFO Form 4 sale 2026-04-18; insiders trailing-3-mo $43.2M sold
- **§13/§14**: scenarios reframed off $33.26 spot; PW EV ~$52 (3-yr) → +56% / ~16% annualized; **Headline R/R per Rule #26 = 3.5:1 Bull/Bear** anchored to §13 scenarios
- **§15**: thesis sentence sharpened around PepsiCo captaincy moat; entry/trim/exit zones unchanged ($30–36 / $60–70 / >$80); thesis-break triggers refined; next review trigger 2026-05-12

### Thesis Status
- **Overall**: **Strengthened** vs. v2.5 — PepsiCo captaincy framework + Q4 buyback execution + shelf-space gains are net incremental positives; offset by CFO Form 4 selling overhang
- **BAIT delta**: Triple overlap (B Strong + A Moderate + T Moderate) preserved; conviction Moderate-High (event-driven)
- **Price target delta**: PW EV unchanged ~$52; mean sell-side target stepped up $61 → $66.45
- **Catalyst & Sentiment delta**: Short interest covered MoM (18.76M → 17.39M); insider selling adds noise; analyst consensus stronger (19/22 Buy)

### Recommendation
- **For a non-holder**: 🟢 **Initiate (small, scaled into the print)** at $33.26, or **Watch** if avoiding catalyst risk
- **For a current holder**: 🟡 **Hold / Add modestly** — drawdown has reset valuation; thesis-break triggers not yet hit

**Next review trigger**: Q1 2026 earnings — **2026-05-12**.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added CELH to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- CELH Q4 2025 / FY2025 earnings press release (CELH IR, Feb/Mar 2026)
- CELH Q3 2025 earnings release (2025-11-06)
- Alani Nu acquisition deal release (April 1, 2025)
- Yahoo Finance live price + 52-wk range (2026-04-24)
- WallStreetZen 1Y price target page ($61)
- MarketBeat earnings calendar (Q1 2026 est. May 11, 2026)
- SimplyWallSt valuation analysis
- Motley Fool "Massive Steal With Alani Nu" (2026-03-04)
- 24/7 Wall St Q3 173% revenue surge coverage
- Seeking Alpha phased Alani Nu rollout coverage
- SEC EDGAR (CELH ex-99.1 Q3 2025 filing)

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $35.25 (Yahoo Finance, April 24, 2026)
- Stock at –47% from late-2025 high; near 52-wk low — material drawdown
- Q4 2025 revenue +117% YoY ($721.6M); FY2025 record $2.5B
- Alani Nu integration tracking ahead of plan (>$1B FY25 revenue; +136% Q4 pro forma)

### Thesis Status
- **Overall**: Initiated — Asymmetric event-driven setup ahead of Q1 May 11 print
- **BAIT signal**: Triple overlap (B Strong + A Moderate + T Moderate); Moderate-High conviction conditional on Q1 confirmation
- **PW EV**: ~$52 (3-yr) vs. spot $35.25 → +47% / ~14%/yr

### Recommendation
- **For a non-holder**: **Initiate (small, scaled into the print)** OR **Watch** until Q1 confirms; both reasonable
- **For a current holder**: **Hold / Add modestly** — thesis intact, drawdown has reset valuation

**Next review trigger**: Q1 2026 earnings — May 11, 2026 (estimated). Hard binary catalyst.
