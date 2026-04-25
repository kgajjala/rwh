# RKT — Changelog

*Append-only. Most recent entry first.*

---

## [2026-04-17] — v2.1 Schema Migration (Consolidated Wiki Page)

**Trigger**: Wiki schema migration from v1 (4-file format: overview / thesis / financials / changelog) to v2.1 (single consolidated `[TICKER].md` page + changelog).

**Sources reviewed**:
- Existing v1 files (overview.md, thesis.md, financials.md)
- Yahoo Finance live price (verified Apr 17, 2026)
- Prior 2026-04-06 initial ingest

### What Changed
- Folded overview/thesis/financials into single `RKT.md` matching v2.1 DASH.md template structure
- Added explicit Section 11 Catalyst & Sentiment Tracker (new in v2)
- Rewrote Section 15 with non-holder/holder split, entry/trim/exit zones, expanded thesis-break triggers
- Removed all portfolio-sizing language (no tranche %, no allocation %, no stock/options split) per v2 Core Rule #3
- Updated price/52-wk to live data: **$15.60** (up from $14.96 prior); 52-wk low *$11.08* (down from prior $10.94 — further weakness in the window); 52-wk high $24.36 unchanged
- PW EV recalculated: $22.65 vs. $15.60 spot = **+45% expected return** over 2–3 years (was +51% at $14.96)
- BAIT verdict unchanged at Double overlap (B + A) — Moderate conviction
- Bull/Base/Bear scenarios unchanged ($35 / $22 / $9 with 25/55/20 weights)
- Deleted legacy v1 files: overview.md, thesis.md, financials.md

### Thesis Status
- **Overall**: **Unchanged** — operating thesis intact since 2026-04-06; no new earnings event in window; price moved from $14.96 → $15.60 (modest +4% drift)
- **BAIT delta**: B Strong / A Moderate-Strong / I Moderate / T Weak-Moderate — all unchanged from 2026-04-06
- **Price target delta**: Bull $35 / Base $22 / Bear $9 — unchanged
- **Catalyst & Sentiment delta**: 52-wk low extended slightly lower ($10.94 → $11.08); next catalyst Q1 2026 earnings April 30, 2026 (~13 days)

### Recommendation
- **For a non-holder**: **Initiate (Speculative)** — at $15.60 the asymmetry is favorable; better entry $11–14 if weakness offers it
- **For a current holder**: **Hold / Add on weakness** — Q1 2026 print is the catalyst that likely re-rates toward $20+

**Next review trigger**: Q1 2026 earnings — April 30, 2026.

---

## [2026-04-06] — Initial Ingest (from raw/analyses/RKT_analysis_2026-04-05.html)

**Trigger**: User added RKT analysis HTML to raw/analyses/; full wiki ingest requested.

**Data points reviewed**:
- RKT_analysis_2026-04-05.html (full 15-section analysis + price history)
- Sources within HTML: Q4 2025 earnings press release (Feb 26, 2026), Q4 2025 earnings call transcript, Q3/Q1 2025 press releases, CNBC Squawk Box interview (Feb 3, 2026), JPMorgan/Wells Fargo/BTIG analyst reports, SEC filings

### What Changed
- Initial compilation — no prior wiki pages existed for RKT
- Overview, thesis, financials, changelog all created from scratch
- Key developments since last known state: (1) Redfin acquisition closed July 2025 ($1.75B all-stock); (2) Mr. Cooper acquisition closed October 2025 ($14.2B all-stock); (3) Up-C structure collapsed June 30, 2025 → full C-corp; (4) Q4 2025 adj revenue $1.7B (beat $1.56B guide); Q4 EBITDA $592M; (5) Q1 2026 guidance $2.6-2.8B adj revenue; (6) Glenn Kelman (Redfin CEO) departed January 2026; (7) Compass partnership announced February 2026; (8) RESPA class-action lawsuit filed January 2026; (9) Stock –38.5% from Jan 16 52-week high of $24.36 despite Q4 beat

### Thesis Status
- **Overall**: Initiated — Buy (Speculative)
- **BAIT signal**: Double overlap (B+A); Behavioral = STRONG (post-beat selloff), Analytical = MODERATE-STRONG (MSR accounting complexity, Up-C collapse distortion, synergy pull-forward not priced), Informational = MODERATE, Technical = WEAK-MODERATE
- **BAIT verdict**: Less clean than BKNG; bear case has real teeth (rate sensitivity, integration risk, $10.6B goodwill)
- **PW EV**: ~$22.65 vs. $14.96 price = +51% upside

### Price Targets
- Bull: $35 (25%) — by 2028; platform + rate relief + synergies
- Base: $22 (55%) — 1-3 years; integration progresses, market normalizes
- Bear: $9 (20%) — rate re-inflation; integration fails; goodwill impaired

### Action
- [x] Buy (Speculative) — Start Tranche 1 at current $14-16 levels; 40-50% of target position
- [ ] Add — T2 at $10-12 if macro deterioration creates entry on intact thesis
- [ ] Add — T3 at $20-24 after Q1 2026 earnings confirmation
- [ ] Trim — Hold above $25+ pending reassessment

**Thesis-break triggers (would prompt reassessment)**:
1. Q1 2026 adj revenue < $2.4B (below guide bottom) absent external macro shock
2. Redfin attach rate falls back below 30%
3. Mr. Cooper synergy timeline extends beyond original 2027 target (after CFO said "ahead of schedule")
4. RESPA class-action certified with damages > $500M
5. GOS margin < 2.0% for 2 consecutive quarters

**Next review trigger**: Q1 2026 earnings — April 30, 2026
