# CELH — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

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
