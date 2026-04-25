# BKNG — Changelog

*Append-only. Most recent entry first.*

---

## [2026-04-17] — v2.1 Format Migration (Workflow A re-ingest)

**Trigger**: User-directed migration of BKNG wiki from v1 (4-file: overview/thesis/financials/changelog) to v2.1 (single consolidated `BKNG.md` + changelog.md) per updated CLAUDE.md schema. Prior v1 files deleted; superseded by `BKNG.md`.

**Sources reviewed**:
- Yahoo Finance JSON API (live price $180.25, 52-wk $150.62–$233.58, post-25-for-1-split effective Apr 2, 2026)
- Prior wiki v1 files (overview.md, thesis.md, financials.md from 2026-04-05 ingest)
- Q4 2025 / FY2025 earnings release (Feb 2026)
- Booking Holdings IR (stock split announcement, $700M 2026 reinvestment framework)
- stockanalysis.com (income statement, cash flow, balance sheet history)
- Analyst consensus aggregators (MarketBeat, TipRanks)

### What Changed from Prior Entry (2026-04-05)

- **Live price**: $4,194.31 pre-split → $180.25 post-split (25-for-1 split effective Apr 2, 2026). Net move: roughly flat to modestly positive on a split-adjusted basis (pre-split equivalent ~$4,506).
- **52-week range**: Re-based to post-split: $150.62–$233.58 (previously $3,765–$5,839 pre-split).
- **Schema migration**: Consolidated 4 v1 files into single `BKNG.md` per v2.1. Section 11 (Catalyst & Sentiment Tracker) added per v2.1 schema. Section 15 restructured (Recommendation & Bottom Line — non-holder vs. holder; entry/trim/exit zones; thesis-break triggers).
- **Removed**: All portfolio-sizing language (no tranche %, no position % allocations, no stock/options split). Per v2.1 Core Rule #3.
- **Substantive thesis content**: Unchanged — Wide moat, Triple-overlap BAIT (B-Strong + A-Strong + I-Moderate + T-Moderate), favorable PW EV, positive Connected Trip + AI-amplifier thesis.

### Thesis Status
- **Overall**: **Unchanged** — same core thesis, refreshed price and format. Triple-overlap BAIT still applies post-split.
- **BAIT delta**:
  - B: Strong (unchanged) — AI-disintermediation fear narrative not supported by data; 8% room night growth, high-20s% Connected Trip growth
  - A: Strong (unchanged) — buyback compounding + Connected Trip attach + sub-0.5× PEG
  - I: Moderate (unchanged) — $700M ROI framework + 10% customer service cost saves underpriced
  - T: Moderate (unchanged) — 25-for-1 split now effective; mechanical retail-accessibility tailwind active
  - Overall: **Triple overlap. Conviction: High.**
- **Price target delta (18-mo, post-split)**: Bull $245 (30%) | Base $200 (50%) | Bear $110 (20%). PW EV ~$195.50 → +8.5% over 18 months from $180.25; meaningful 3-year compounding upside ($280–$320 range).

### Recommendation
- **For a non-holder**: **Initiate** at $180.25 — Triple-overlap BAIT, Wide moat, sub-0.5× PEG, ~6.4% FCF yield, stock-split tailwind. Asymmetry favorable on both 18-mo and 3-yr horizons.
- **For a current holder**: **Add** on pullback to $155–$170 (attractive entry zone); **Hold** at current $180. Q1 2026 print (early May) is the next confirmation point.

**Attractive entry zone**: $155 – $175
**Trim zone**: $235 – $260
**Exit / avoid zone**: >$280

**Thesis-break triggers**:
1. Room night growth <5% for two consecutive quarters
2. Connected Trip transaction % stalls or contracts
3. Google antitrust resolution that empowers Google Hotels aggression
4. Merchant mix growth stalls below 75%
5. Management cuts $700M reinvestment framework or 9/9/15 long-term target
6. Glenn Fogel CEO departure
7. Demonstrable AI-agent intercept of EU bookings (measurable share loss)
8. FY2026 EPS guidance withdrawn or guided meaningfully below post-split equivalent

**Next review trigger**: **Q1 2026 earnings — early May 2026**. Watch Connected Trip %, merchant mix, room-night growth vs. ~9% target, AI product KPIs, $700M reinvestment progress.

---

## 2026-04-05 — Initial Thesis Compilation

**Trigger**: First full wiki import — no prior raw/analyses/ material; thesis compiled
from live data (Yahoo Finance, stockanalysis.com, IR releases, web search).
**Data points reviewed**:
- FY2021–FY2025 annual financials (revenue, EBITDA, EPS, FCF, balance sheet)
- Q4 2025 and FY2025 earnings release highlights
- Q4 2024 earnings release (room nights, gross bookings, merchant mix)
- Management commentary: Q4 2025 earnings call (Fogel + Steenbergen)
- Analyst consensus: 29-34 analysts, avg price target ~$5,880–$6,072 (pre-split)
- Stock split announcement: 25-for-1, effective 4/2/2026; split-adjusted trading 4/6/2026

### What Changed
- First-time compilation — no prior thesis to compare against
- Key data points established:
  - FY2025: $26.9B revenue (+13%), $9.1B FCF, 1.235B room nights (+8%), 70% merchant mix
  - $700M strategic reinvestment in 2026 → ~$400M incremental revenue / ~$300M EBITDA benefit
  - Connected Trip: low-double digit % of transactions, growing high-20s%
  - Airline tickets: 68M booked (+37%); attractions +80%
  - Post-split price: ~$168 (25-for-1 split; pre-split price $4,194)
  - 52-week range: $3,765–$5,839 (pre-split); stock is 28% off peak

### Thesis Status
- **Overall**: Established — **High Conviction**
- **BAIT delta**: B-STRONG (AI fear narrative not supported by data) + A-STRONG (FCF
  compounding + Connected Trip underappreciated) + I-MODERATE ($700M ROI framework
  underappreciated) + T-MODERATE (stock split retail accessibility) = Triple Overlap
- **Price targets (post-split)**:
  - Bull: $240–$260 (30%) | Base: $185–$210 (50%) | Bear: $100–$120 (20%)
  - Probability-weighted EV: ~$196 (~+17% from $168)

### Action
- [x] Buy more — Tranche 1: 40% of position at $155–$170 (post-split); current price $168 is in range
- [ ] Trim — N/A
- [ ] Hold — not yet; establishing position
- [ ] Watch — Connected Trip % as leading thesis-confirmation KPI

**Next review trigger**: Q1 2026 earnings (expected May 2026) — watch Connected Trip %,
merchant mix trend, room night growth, and any AI product metrics disclosed.

---

## 2026-04-05 — INIT

**Trigger**: Wiki initialization — stub created.
**Thesis Status**: Pending first import
**Next review trigger**: Import from raw/analyses/
