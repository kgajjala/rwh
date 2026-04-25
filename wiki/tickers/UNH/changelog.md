# UNH — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-24] — v2.1 Schema Migration + Recovery-in-Progress Refresh

**Trigger**: Migration of UNH wiki from v1 (4-file: overview/thesis/financials/changelog) to v2.1 (single consolidated `UNH.md` + `changelog.md`). Triggered by user request as part of batch v2.1 rollout. Legacy v1 files deleted; content folded into `UNH.md`. Live price refreshed — recovery has materially advanced since prior ingest.

**Sources reviewed**:
- Yahoo Finance JSON API (live price $354.92; 52-wk $234.60–$424.12; April 24, 2026)
- Prior wiki v1 files (overview.md, thesis.md, financials.md, changelog.md from 2026-04-05 ingest at $277.26)
- businesswire.com FY2025 release; stockanalysis.com; medicaremarketinsights.com; fiercehealthcare.com; unitedhealthgroup.com IR

### What Changed from Prior Entry (2026-04-05)

- **Live price**: $277.26 → **$354.92** (+28% since prior ingest); the recovery thesis is materially playing out
- **52-week range re-set**: Prior wiki's $606.36 52-wk high is now outside the trailing 12-month window. New 52-wk range is **$234.60 – $424.12**, with the high recently re-tested then sold off to $355 (significant volatility — suggests market remains uncertain about whether the recovery extends to the bull case or stalls)
- **Drawdown framing**: From "54% off 52-wk high $606" → **–16.3% off new 52-wk high $424.12**, but **+51.3% above the $234.60 low**
- **Asymmetry compressed**: At $277.26 the prior wiki computed PW EV of ~$369 (+33% over 24 months). At $354.92 with the same scenario probabilities (Bull 30% / Base 50% / Bear 20%) the PW EV is ~$420 (~+18% over 24 months). Asymmetry remains favorable but is no longer exceptional; ~28% of the recovery has been captured.
- **Bull/Bear/Base preserved structurally** but recalibrated: Bull $500–550 (30%), Base $400–430 (50%, narrowed up from prior $340–380 to reflect recovery progress), Bear $250–300 (20%, narrowed up from prior $180–220 — the deep capitulation low of $234 was the test and was passed).
- **BAIT verdict preserved as Quadruple Overlap (B+A+I-Strong, T-Moderate)** — UNH retains the highest BAIT-overlap signal in the wiki universe per user instruction
- **Schema migration**: Consolidated 4 files → 2 files per v2.1. Position-sizing language removed (no tranche %, no allocation %, no stock/options split). Section 11 now "Catalyst & Sentiment Tracker"; Section 15 now "Recommendation & Bottom Line" with action verbs.
- **Recent volatility note**: The recent re-test of $424.12 followed by drop to $354.92 is meaningful — the market is testing whether the recovery extends; this is not a smooth grind higher

### Thesis Status
- **Overall**: **Strengthened** in terms of operational execution (price action validates Hemsley discipline + MA repricing thesis); **Slightly Weaker on asymmetry** simply because price has moved up
- **BAIT delta**:
  - B: Strong (preserved; behavioral edge is now the gap from $355 to fair value, smaller than the gap from $277)
  - A: Strong (preserved; trough-to-normalized EPS gap remains underappreciated)
  - I: Strong (preserved; Hemsley + MA exit + Optum restructuring detail underweighted)
  - T: Moderate (preserved; recovery in progress, no new mechanical catalyst)
  - Overall: **Quadruple overlap maintained** per user instruction. Conviction High on long-term thesis; asymmetry now Moderate (vs. High at $277).
- **Price target delta (24-month scenarios)**: Bull $500–550 (30%) preserved | Base $400–430 (50%) tightened upward | Bear $250–300 (20%) tightened upward. PW EV ~$420 → ~+18% from $354.92 (vs. ~+33% from $277.26 to ~$369 PW EV).
- **Catalyst & Sentiment delta**: Stock has materially recovered (+28% since prior entry); $234 capitulation low has been left behind; recent $424 retest then drop to $355 indicates ongoing volatility within the recovery channel.

### Recommendation
- **For a non-holder**: **Watch / Initiate selectively** — initiate in $300–340 zone on any Q1 MLR pullback. At $355 the prior wiki's $250–285 attractive entry is missed; full sizing here gives away too much margin of safety. Bull case still offers +40%+ but pre-Q1 binary risk warrants partial sizing only.
- **For a current holder**: **Hold / Add selectively on pullbacks** — do not exit. Add in $300–340 zone if offered. Trim above $470 unless bull case is clearly confirmed by sequential MLR < 87%.

**Attractive entry zone**: $300 – $340
**Trim zone**: $470 – $520
**Exit / avoid zone**: >$580

**Thesis-break triggers**:
1. Q1 2026 reported MLR > 89.5% with no improvement trajectory (primary, immediate reduction)
2. DOJ files formal antitrust complaint seeking Optum divestiture
3. Hemsley resignation or Board instability
4. Optum Health FY2026 adj. earnings < $2B (worse than 2025)
5. MA membership exits beyond 2M (signals competitive loss vs. discipline)
6. New CEO appointment without continuity from Hemsley plan
7. Sequential MLR worsening two consecutive quarters in 2026

**Next review trigger**: **Q1 2026 earnings — expected late April 2026**. Q1 MLR vs. 89.1% trailing is the make-or-break print. A clean sub-88% Q1 MLR could trigger meaningful re-rating toward bull case; a >89.5% print would activate trigger #1.

---

## 2026-04-05 — Initial Thesis Compilation

**Trigger**: First full wiki import — thesis compiled from live data (Yahoo Finance,
stockanalysis.com, businesswire.com FY2025 results, fiercehealthcare.com, web search).
**Data points reviewed**:
- FY2021–FY2025 annual financials (revenue, EBITDA, EPS, FCF)
- FY2025 full year results: $447.6B revenue (+11.8%), MLR 89.1% (vs. 85.5% in FY2024),
  EBITDA $23.3B (vs. $36.4B in FY2024), EPS $13.23 (vs. $15.51), FCF $16.1B (–22%)
- UNH expected to exit 1.3–1.4M Medicare Advantage members in 2026 (margin > scale)
- CEO Andrew Witty resigned May 13, 2025; Stephen Hemsley (former CEO 2006-2017) returned
- 2025 annual guidance was suspended mid-year due to accelerating medical costs
- Optum Health adj. earnings: collapsed from $7.9B (FY2024) to $2.3B (FY2025)
- DOJ antitrust investigation into UNH vertical integration: ongoing
- Stock: $277.26 (54% off 52-week high $606.36; 3-year lows)

### What Changed
- First-time compilation — no prior thesis to compare against
- Critical negative events in 2025 (all material to thesis):
  1. MLR 89.1% — worst in UNH history, ~400bps above normalized range
  2. CEO resignation + guidance suspension — most severe credibility event in decades
  3. Optum Health $5.6B earnings decline — vertical integration thesis challenged
  4. DOJ antitrust investigation — existential tail risk, low probability
  5. Brian Thompson assassination (Dec 2024) — unprecedented reputational damage
- Positive counters established in thesis:
  - Hemsley return = credibility signal
  - $16.1B FCF even at trough = quality floor
  - Proactive 1.3M MA member exits = margin discipline > scale (bullish for MLR recovery)
  - BAIT quadruple overlap — highest in portfolio

### Thesis Status
- **Overall**: Established — **Medium Conviction** (elevated uncertainty, high risk/reward)
- **BAIT delta**: B-STRONG + A-STRONG + I-STRONG + T-MODERATE = **Quadruple Overlap**
  Highest BAIT signal across portfolio. Thesis: market is pricing permanent impairment;
  data supports cyclical impairment with strong recovery trajectory.
- **Price targets**:
  - Bull: $500–$550 (30%) | Base: $340–$380 (45%) | Bear: $180–$220 (25%)
  - Probability-weighted EV: ~$369 (~+33% from $277 on 24-month horizon)

### Action
- [x] Buy more — Tranche 1: 40% of position at $250–$285; current $277 is in range
- [ ] Trim — N/A (establishing position)
- [ ] Hold — N/A
- [ ] Watch — **Q1 2026 MLR** is the single most important data point (expected April 2026)

**Data gaps to resolve**:
- ⚠️ Quarterly MLR breakdown by segment (MA vs. Medicaid vs. Commercial)
- ⚠️ Full balance sheet detail from UNH 10-K (debt, dividend coverage)
- ⚠️ DOJ investigation status and scope (public filings only)
- ⚠️ 2026 guidance (company did not provide formal 2026 guidance as of Jan 2026)

**Next review trigger**: Q1 2026 earnings (expected April 2026) — MLR is the make-or-break
number. Q1 MLR above 89.5% = thesis delay; Q1 MLR at 87-88% = thesis confirming; below
87% = significant re-rating catalyst.

**Thesis-break triggers**:
- DOJ files formal antitrust complaint seeking Optum divestiture
- Q1 2026 MLR > 89.5% with no evidence of improvement trajectory
- Hemsley resignation or Board instability

---

## 2026-04-05 — INIT

**Trigger**: Wiki initialization — stub created.
**Thesis Status**: Pending first import
**Next review trigger**: Import from raw/analyses/
