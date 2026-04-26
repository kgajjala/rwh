# AMZN — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.6+v2.7+v2.8 Retrofit (Primary-Source Synthesis Refresh)

**Trigger**: Schema retrofit batch under v2.8. Brings AMZN page to current schema (Rules #19, #20, #21, #22, #23, #24, #25, #26).

**Sources reviewed (new this pass)**:
- [Andy Jassy FY2025 Shareholder Letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2025-letter-to-shareholders) (Pattern A: published Apr 2026; covers FY2025)
- [Andy Jassy FY2024 letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2024-letter-to-shareholders)
- [Andy Jassy FY2023 letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2023-letter-to-shareholders)
- [Andy Jassy FY2022 letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2022-letter-to-shareholders)
- [Andy Jassy FY2021 letter (first as CEO)](https://www.aboutamazon.com/news/company-news/2021-letter-to-shareholders)
- [Jeff Bezos FY2020 letter (final)](https://www.aboutamazon.com/news/company-news/2020-letter-to-shareholders)
- [Q4 FY25 8-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm) — confirmed FY25 actuals: Rev $716.9B, Op Inc $80.0B, AWS Op Inc $45.6B
- [FY2024 10-K HTML](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm), [FY2023 10-K HTML](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) (5-year baseline indexed in `raw/AMZN/filings/AMZN-10K-INDEX.md`)
- [Yahoo Finance live price](https://finance.yahoo.com/quote/AMZN) (verified $255.08 at Apr 23 2026 close; 52-wk $178.85–$258.79; market cap $2.74T)
- [TipRanks AMZN](https://www.tipranks.com/stocks/amzn) — Strong Buy 42/3; avg PT $286
- TradingKey / Seeking Alpha / S&P Q1 FY26 previews (consensus rev $177.2B, EPS $1.63, AWS ~$36.8B; UBS bull case +38% AWS)

### What Changed (vs. prior v2.5 page)

- **Live price refreshed** $247 → **$255.08** (Apr 23 2026 close from Yahoo Finance); 52-wk high updated to $258.79
- **FY2025 actuals now booked** — Rev $716.9B (+12%), Op Inc $80.0B, AWS Op Inc $45.6B, NA Op Inc $29.6B, Intl Op Inc $4.7B (first profitable year for International segment at scale), FCF $7.7B (compressed by capex)
- **§2 (Annual Financial Metrics)**: Added FY21 baseline column; added segment op income rows (NA, Intl, AWS); added new `### Primary Source: 10-K Segment Detail` subsection with multi-year MD&A synthesis (NA op income +$32B swing FY22→FY25; AWS op margin 24%→37%)
- **§5 (Competitive Moat)**: Standalone "Moat Assessment" block above Pivotal Question retired (Rule #23). Added mandatory `### Competitive Landscape` subsection (Rule #24) with 4-pillar peer tables (Retail / Cloud / Advertising / Logistics) and explicit framing of how AMZN's cross-pillar reinforcement differs
- **§6 (Management & Leadership)**: Added `### Recent Management Commentary — Primary Source Synthesis` subsection with 7 verbatim quotes from FY20–FY25 letters mapped to investment relevance + 5-Year Capital Allocation Arc table tracing the restraint→reaccel→AI build-out cadence (Rule #19)
- **§8 (Key Risks)**: Boilerplate dropped per Rule #25; "not priced in" tags added to AI capex ROIC and Azure share loss rows; 5-Year Risk Factor Evolution table replaced with synthesis paragraph (Rule #21) — names AI risk factor first appearing FY23 10-K, capex/data-center concentration risk added FY24, COVID logistics overcapacity language removed by FY24
- **§11 (Catalysts)**: Refreshed all analyst PTs (BMO $315, KeyBanc $325, BofA $298); added April 9 Jassy AWS AI $15B run rate disclosure; updated Q1 FY26 print 3 days out
- **§13/§14 scenarios**: Bull/Bear/Base unchanged in price targets; current price reset to $255.08 compresses R/R from prior framing — now ~1.7:1 (Bull/Bear midpoints) vs. ~3:1 at the Feb 2026 lows; PW EV $310 yields +22% / 7%/yr at $255 (vs. +26% at $247)
- **§15 (Recommendation)**: Non-holder verb softened from **Initiate** → **Initiate (small) / Watch** reflecting compressed margin-of-safety at $255 (–1.4% from 52-wk high) vs. prior $247 framing; thesis-break trigger added: "FY26 capex revised up >$250B without commensurate AWS AI revenue acceleration"
- **Summary** bullet-list rewritten under v2.8 emoji conventions; output discipline pass (no CLAUDE.md self-references; no "corrected from" language; tables time-in-columns; bullets for data-dense lines)
- **All sources linkified** per Rule #16 (eliminated [link pending] for Anthropic / Northwise / S&P)

### Thesis Status

- **Overall**: 🟡 **Unchanged → marginally weakened on price** — fundamentals strengthened (FY25 actuals beat, AWS reaccel, International profitability inflection), but $255 print compresses asymmetry vs. the $247 framing. Bear/Bull R/R now 1.7:1 vs. ~3:1 at Feb lows.
- **BAIT delta**: Triple overlap retained (A Mod-Strong + I Mod + T Mod); Behavioral remains only Moderate (no fear at near-high pricing)
- **Price target delta**: Bull $400 / Base $290 / Bear $170 unchanged from v2.5 — schema refresh, not thesis revision

### Recommendation

- **For a non-holder**: 🟡 **Initiate (small) / Watch** — preferred entry $220–235; current $255 is fair-price not value-price
- **For a current holder**: 🟡 **Hold** — let Q1 print resolve before adding; trim only above $310 without earnings re-rate

**Next review trigger**: 📅 **Q1 FY26 earnings — April 29, 2026 (post-close, 3 days out)**. Key items: AWS YoY growth (Street +22% vs. UBS +38% bull), AI revenue commentary, Q2 op income guide, FY26 capex affirmation, advertising growth rate, NA op margin.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added AMZN to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- AMZN Q4 FY25 earnings press release (AMZN IR, 2026-02-05)
- Q4 FY25 earnings call transcript (Yahoo Finance)
- Q3 FY25 ex-99.1 SEC filing
- CNBC "Amazon Q4 2025 earnings report" (2026-02-05)
- Futurum Group quarterly analyses (Q1–Q4 FY25)
- Morningstar pre-Q1 FY26 preview
- Yahoo Finance live price (2026-04-24)
- 24/7 Wall St "BofA + KeyBanc double upgrade" (2026-04-20)
- S&P Global big-tech earnings preview
- Capital.com tariff forecast piece (2026-03-30)
- Motley Fool 1-yr prediction (2026-04-15)
- Northwise Project Amazon 2030 forecast

### What Changed
- Initial compilation; no prior wiki content
- Live price verified ~$247 (Yahoo Finance / 24/7 Wall St cross-check, April 24, 2026)
- Q4 FY25: rev $213.4B (+14%); AWS $35.6B (+24%, "fastest in 13 quarters"); op income $25.0B
- **$200B FY26 capex guide** (vs. $77.7B FY24) — central thesis tension
- KeyBanc PT $285 → $325, BofA PT $275 → $298 ahead of April 29 Q1 print

### Thesis Status
- **Overall**: Initiated — Wide-moat mega-cap mid-cycle in generational AI infrastructure bet
- **BAIT signal**: Triple overlap (A Mod-Strong + I Mod + T Mod); Behavioral only Moderate; Conviction Moderate
- **PW EV**: ~$310 (3-yr) vs. spot ~$247 → +26% / ~8%/yr

### Recommendation
- **For a non-holder**: **Initiate** at $247 — quality-at-fair-price; pullback into $210–235 would offer margin of safety
- **For a current holder**: **Hold / Add modestly** into Q1 FY26 print

**Next review trigger**: Q1 FY26 earnings — April 29, 2026 (post-close). 5 days from this writeup.
