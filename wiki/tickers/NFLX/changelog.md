# NFLX — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Retrofit (13-Section Restructure + Primary-Source Synthesis)

**Trigger**: Schema migration v2.5 → v2.9 — 15 → 13 section consolidation, plus first-time primary-source ingest of shareholder letters and multi-year 10-Ks per Rules #19, #20, #21–#26.

**Sources reviewed (newly fetched into raw/)**:
- 7 quarterly shareholder letters: 2026 Q1, 2025 Q4, Q3, Q2, 2024 Q4, 2022 Q4, 2021 Q4 (Q1 2025 + Q4 2023 mirrors returned 403/404 — `[link pending]`)
- 3 annual 10-Ks: FY2025 (filed Jan 23, 2026), FY2024, FY2023 — all SEC EDGAR HTML
- Q1 2026 earnings call transcript PDF
- Yahoo Finance live price ($93.24 verified 2026-04-24)
- MarketBeat / Public.com / Benzinga analyst consensus + short interest
- SecForm4 / Stocktitan insider activity (CFO sale Apr 2, 2026; Hastings $32.7M sale early Feb 2026)

### What Changed
- **Structural**: Migrated from 15 sections to 13 (v2.9). Old §1 (Why Exist + Pivotal Question) retired into header subsections; old §3 + §4 merged into new §2 (Revenue Mix & Geographic Split); old §5 + standalone Moat block consolidated into new §3 (Competitive Moat & Landscape) per Rule #23.
- **New §3 Competitive Landscape subsection** added per Rule #24 — DIS+/Max/Prime/AppleTV+/PARA/Peacock/YouTube/TikTok/national champions table with Nielsen Gauge market share and explicit "how NFLX moat differs" framing.
- **New §1 Primary Source: 10-K MD&A multi-year synthesis** — three readings across FY21–FY25 10-Ks (2022 inflection, FY26 31.5% margin commitment, content-cash-vs-amort cash flow tailwind).
- **New §4 Recent Management Commentary subsection** per Rule #19 — verbatim quotes from Q1 26, Q4 25, Q3 25 letters mapped to investment relevance + 5-Year Strategic Framework Arc table.
- **§6 Key Risks rewritten under Rule #25 materiality filter** — dropped boilerplate (cyber, generic third-party); kept ad-ARPU-ramp (not priced in), content-cost-re-acceleration (discretionary investment), attention-share leakage (peer-differentiated), engagement plateau, EU regulatory, FX. Added `5-Year Risk Factor Evolution Synthesis` paragraph per Rule #21 (replaces the bulk Risk Factor table).
- **§9 Catalyst & Sentiment Tracker refreshed** with current short interest (1.81% of float, 1.6 days to cover), insider activity (Hastings, Peters, Neumann sales; routine director option grants), latest analyst consensus (37 Buy / 12 Hold / 1 Sell, $115 median target), and post-Q1 26 news (WBD $2.8B termination receipt; FY26 op margin guide raised to 31.5%).
- **§12 R/R discipline** per Rule #26 — 2.9:1 explicitly anchored to §11 Bull $160 vs. Bear $70 midpoints from current $93.24; PW EV $119.50 unchanged from v2.5 but methodology now reconciled.
- **Summary section** rewritten to ≤10 emoji-tagged bullets per Rule #18 with R/R headline.
- **All sources linkified** per Rule #16; local-file relative paths preferred where raw/ exists.

### Thesis Status
- **Overall**: **Strengthened** vs. v2.5 baseline. FY26 op margin guide *raised* to 31.5% (was 30%+ vague); FCF guide *raised* to $12.5B (incl. $2.8B WBD); ad revenue trajectory $1.5B (FY25 actual) → $3B (FY26 guide) on track with +70% YoY advertiser count growth; 4,000+ advertiser milestone is the cleanest forward indicator. Material thesis shifts from v2.5: (a) WBD termination demonstrates licensing-bargaining leverage; (b) Netflix Ads Suite first-party serving in production at scale; (c) live-events flywheel proven (Joshua–Paul 33M AMA); (d) all four regions printing +15–18% growth simultaneously.
- **BAIT delta**: Unchanged at Triple-lens (B + A + I Moderate); T weak. Conviction **Moderate**.
- **Price target delta**: Bull $160 / Base $115 / Bear $70 unchanged. PW EV ~$119.50.
- **Catalyst & Sentiment delta**: Insider activity skewed selling (Hastings, Peters, Neumann); short interest still low (~1.8%); analyst panel still skewed Buy.

### Recommendation
- **For a non-holder**: 🟢 Initiate (small, scaled) at $93.24; better entry $80–88
- **For a current holder**: 🟡 Hold / Add on weakness below $90

**R/R**: 2.9:1 (Bull $160 vs. Bear $70 from §11)
**Next review trigger**: Q2 2026 earnings — mid-July 2026 (estimated)

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added NFLX to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Netflix Q1 2026 earnings press release & shareholder letter (April 16, 2026)
- Yahoo Finance live price (2026-04-24)
- Netflix IR (10-for-1 stock split announcement October 30, 2025; effective November 17, 2025)
- CNBC, IndexBox, TIKR.com Q1 2026 coverage
- MarketBeat / Public.com / TipRanks / stockanalysis.com analyst consensus

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $93.24 (Yahoo Finance, April 24, 2026 intraday)
- Note: Netflix executed a 10-for-1 stock split effective Nov 17, 2025; current price is post-split

### Thesis Status
- **Overall**: Initiated — small Initiate verdict for non-holders post Q1 selloff; Hold/Add on weakness for holders
- **BAIT signal**: Triple-lens (B + A + I moderate); T weak; Conviction Moderate
- **PW EV**: ~$119.50 (3-yr) vs. $93.24 spot → +28% (~9%/yr) — mildly favorable

### Recommendation
- **For a non-holder**: Initiate (small, scaled); $80–88 better entry zone
- **For a current holder**: Hold / Add on weakness below $90

**Next review trigger**: Q2 2026 earnings (mid-July 2026, estimated)
