# WING — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-17] — v2.1 Schema Migration + Price Refresh (Workflow A consolidation)

**Trigger**: Migration of WING wiki from v1 (4-file: overview/thesis/financials/changelog) to v2.1 (single consolidated `WING.md` + `changelog.md`). Triggered by user request as part of batch v2.1 rollout. Legacy v1 files (overview.md, thesis.md, financials.md) deleted; content folded into `WING.md`. Live price refreshed.

**Sources reviewed**:
- Yahoo Finance JSON API (live price $189.37; 52-wk $142.24–$388.14; April 17, 2026)
- Prior wiki v1 files (overview.md, thesis.md, financials.md, changelog.md from 2026-04-05 ingest)
- ir.wingstop.com FY2025 release (Feb 2026, prnewswire.com); stockanalysis.com (income statement); franchisetimes.com / 1851franchise.com (international + unit economics)

### What Changed from Prior Entry (2026-04-05)

- **Live price**: $152.51 → **$189.37** (+24% since prior ingest); stock has recovered modestly off the $142.24 52-wk low
- **Drawdown framing**: Prior wiki noted –61% off all-time high; current measured drawdown **–51% from $388.14 52-wk high**. Drawdown is even larger than the prior wiki suggested when measured on the trailing 12-month basis.
- **Asymmetry compressed**: At $152.51 the prior wiki computed PW EV of ~$187 (+22%). At $189.37 the same scenario probabilities yield PW EV of ~$199 (~+5%). The asymmetric entry zone has substantially closed; the Tranche 1 zone of $140–160 has been exited to the upside.
- **Schema migration**: Consolidated 4 files → 2 files per v2.1 CLAUDE.md. Position-sizing language removed (no tranche %, no allocation %, no stock/options split). Section 11 now "Catalyst & Sentiment Tracker"; Section 15 now "Recommendation & Bottom Line" with action verbs (Watch / Hold) and explicit price zones.
- **Thesis-break trigger flagged as proximate**: The prior wiki's defined trigger of "two consecutive quarters of SSS < –5%" has not yet activated, but FY2025's –3.3% combined with weak market sentiment suggests Q1 2026 SSS could push the trigger active. Section 11 and Section 15 reflect this increased proximity.

### Thesis Status
- **Overall**: **Unchanged** — same core thesis, refreshed data; conviction modestly *lower* than at $152.51 entry due to compressed asymmetry
- **BAIT delta**:
  - B: Strong (unchanged; –51% drawdown is real over-reaction relative to 22-yr SSS history)
  - A: Moderate (unchanged; unit-growth math + intact franchisee economics)
  - I: Weak (unchanged; no informational asymmetry — SSS is heavily covered)
  - T: Moderate (unchanged; below 200-day MA, oversold-recovering)
  - Overall: Triple overlap (B-Strong + A-Moderate + T-Moderate). Conviction Lower-Moderate at $189 vs. Moderate at $152.
- **Price target delta (18-month scenarios)**: Bull $260–300 (25%) unchanged | Base $180–220 (50%) unchanged | Bear $100–130 (25%) unchanged. PW EV ~$199 → ~+5% from $189.37 (vs. ~+22% from $152.51).
- **Catalyst & Sentiment delta**: Stock recovered ~24% from prior entry; thesis-break trigger (–5% SSS for two quarters) not active but proximate.

### Recommendation
- **For a non-holder**: **Watch** — at $189 the asymmetric entry has substantially closed. Initiate only if (a) price drops back into $140–160 zone, OR (b) Q1 2026 SSS confirms stabilization at flat-to-positive (then initiate $190–210 with confirmation). Avoid full sizing pre-print.
- **For a current holder**: **Hold** — do not add at $189; do not exit pre-print. Q1 2026 earnings (late April / early May) is binary. A SSS print of –5% or worse would activate Reduce; flat-or-better would support Hold/Add on confirmation.

**Attractive entry zone**: $140 – $160
**Trim zone**: $260 – $310
**Exit / avoid zone**: >$340

**Thesis-break triggers**:
1. Two consecutive quarters of domestic SSS worse than –5% (primary, may be proximate)
2. Q1 2026 SSS < –5% with management commentary indicating structural drivers
3. Net new unit guidance cut below 15%
4. Franchisee distress: closures accelerating, AUV < $1.8M
5. International AUV compression continuing
6. CEO Skipworth departure or management discontinuity

**Next review trigger**: **Q1 2026 earnings — expected late April / early May 2026**. Domestic SSS print is the make-or-break number.

---

## 2026-04-05 — Initial Thesis Compilation

**Trigger**: First full wiki import — thesis compiled from live data (Yahoo Finance,
stockanalysis.com, ir.wingstop.com FY2025 release, web search).
**Data points reviewed**:
- FY2021–FY2025 annual financials (revenue, EBITDA, EPS — FCF data pending 10-K fetch)
- FY2025 full year results: $697M revenue (+11.4%), adj. EBITDA $244M (+15.2%),
  net income $174M (+60%), system-wide sales $5.3B (+12.1%), 3,056 units (+493 net new)
- Domestic same-store sales: **–3.3% in FY2025** (first SSS decline in 22 years)
- FY2026 guidance: flat to low-single digit domestic SSS; 15-16% global unit growth
- Franchise economics: 6% royalty rate, 5.5% advertising fund (raised 2025), $2.0M AUV
- Stock: $152.51 (near 52-week low $142.24; 61% off all-time high $388.14)

### What Changed
- First-time compilation — no prior thesis to compare against
- Critical new data point: First domestic SSS decline in 22 years (–3.3%)
  - This is the sole reason for the 61% drawdown from peak
  - The thesis hinges on whether SSS is cyclical (recoverable) or structural (permanent)
- Positive counterpoint: 493 net new units in FY2025 (record); system is financially healthy
- ⚠️ FCF data not populated — fetch from WING 10-K

### Thesis Status
- **Overall**: Established — **Medium Conviction** (elevated SSS uncertainty)
- **BAIT delta**: B-STRONG (61% drawdown from peak; behavioral oversell on first-ever SSS
  negative) + A-MODERATE (unit growth math compounds royalty even at 0% SSS; under-
  appreciated by SSS-focused sell-side) + T-MODERATE (near 52-week low; short squeeze
  potential on any positive Q1 2026 SSS) = Triple Overlap (lower conviction than BKNG/UNH)
- **Price targets**:
  - Bull: $260–$300 (25%) | Base: $170–$200 (50%) | Bear: $80–$100 (25%)
  - Probability-weighted EV: ~$187 (~+22% from $153)

### Action
- [x] Buy more — Tranche 1: 50% of position at $140–$160; current $153 is in range
- [ ] Trim — N/A (not yet in position)
- [ ] Hold — N/A
- [ ] Watch — **Q1 2026 domestic SSS is the single most important data point**

**Data gaps to resolve**:
- ⚠️ WING FCF and quarterly capex from 10-K
- ⚠️ Quarterly SSS breakdown by quarter in 2025 (was it worsening or improving into Q4?)
- ⚠️ Debt structure and interest coverage details

**Next review trigger**: Q1 2026 earnings (expected late April/early May 2026) —
domestic SSS is the make-or-break number. Any reading worse than –3% is thesis-weakening;
worse than –5% triggers position reassessment.

**Thesis-break trigger**: Two consecutive quarters of domestic SSS < –5%; close position.

---

## 2026-04-05 — INIT

**Trigger**: Wiki initialization — stub created.
**Thesis Status**: Pending first import
**Next review trigger**: Import from raw/analyses/
