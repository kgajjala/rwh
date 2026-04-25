# LLY — Changelog

*Append-only. Most recent entry first.*

---

## [2026-04-24] — v2.1 Format Migration (Workflow A re-ingest)

**Trigger**: User-directed migration of LLY wiki from v1 (4-file: overview/thesis/financials/changelog) to v2.1 (single consolidated `LLY.md` + changelog.md) per updated CLAUDE.md schema. Prior v1 files deleted; superseded by `LLY.md`.

**Sources reviewed**:
- Yahoo Finance JSON API (live price $883.96, 52-wk $623.78–$1,133.95)
- Prior wiki v1 files (overview.md, thesis.md, financials.md from 2026-04-05 ingest)
- Q4 2025 / FY2025 earnings release (Feb 2026, prnewswire) + 2026 guide ($80–83B revenue, $33.50–$35.00 EPS)
- LLY IR (orforglipron NDA/MAA submission with priority review voucher; retatrutide Phase 3 26.6% weight loss)
- biopharmadive.com, biospace.com, drugdiscoverytrends.com (pipeline coverage)
- stockanalysis.com (income statement, financial history)
- Analyst consensus aggregators (median target ~$1,000–$1,050)

### What Changed from Prior Entry (2026-04-05)

- **Live price**: $935.58 → $883.96 (–5.5% over the period). Stock has drifted toward the lower end of recent range as oral GLP-1 competitor narratives intensified.
- **52-week range refreshed**: $623.78–$1,133.95. Stock now –22% off peak (vs. –18% prior); +41.7% above the 52-wk low.
- **Schema migration**: Consolidated 4 v1 files into single `LLY.md` per v2.1. Section 11 (Catalyst & Sentiment Tracker) added per v2.1 schema. Section 15 restructured (Recommendation & Bottom Line — non-holder vs. holder; entry/trim/exit zones; thesis-break triggers).
- **Removed**: All portfolio-sizing language (no tranche %, no position % allocations, no stock/options split). Per v2.1 Core Rule #3.
- **Substantive thesis content**: Unchanged — Wide-but-concentrated moat, Triple-overlap BAIT (A-Strong + I-Strong + B-Moderate, T-Weak), favorable PW EV improved modestly given lower entry price.

### Thesis Status
- **Overall**: **Unchanged** — same core thesis, refreshed price and format. Lower entry price modestly improves PW EV math (now +17.4% over 18 months vs. +11% prior).
- **BAIT delta**:
  - B: Moderate (unchanged) — –22% pullback creates entry below momentum-crowd cost basis but stock isn't deeply mispriced on absolute terms
  - A: Strong (unchanged) — orforglipron $10–15B not in consensus; manufacturing moat undervalued; 0.5× PEG
  - I: Strong (unchanged) — orforglipron priority review accelerated FDA timeline; retatrutide superior efficacy data not priced in
  - T: Weak (unchanged) — no near-term mechanical catalysts
  - Overall: **Triple overlap (A+I+B). Conviction: High on analytical/informational; entry quality price-dependent.**
- **Price target delta (18-mo)**: Bull $1,300 (30%) | Base $1,015 (50%) | Bear $700 (20%). PW EV ~$1,037.50 → +17.4% over 18 months from $883.96.

### Recommendation
- **For a non-holder**: **Initiate** at $883.96 with a measured starter; **Add** aggressively in $750–$850 zone if reached. Triple-overlap BAIT + ~+17% 18-mo PW EV + orforglipron near-binary upside catalyst justify entry.
- **For a current holder**: **Hold** at $884; do not trim into the –22% drawdown that doesn't break thesis. **Add** on pullback to $750–$850. Q1 2026 print (late Apr / early May) is the next confirmation point on $80–83B FY guide and orforglipron timing.

**Attractive entry zone**: $750 – $850
**Trim zone**: $1,150 – $1,250
**Exit / avoid zone**: >$1,350

**Thesis-break triggers**:
1. Orforglipron CRL or FDA delay >12 months past expected approval
2. Viking VK2735 Phase 3 oral data demonstrably superior to orforglipron
3. Novo oral semaglutide capturing >25% of new oral GLP-1 prescriptions in launch year
4. IRA Medicare negotiation announced for Mounjaro materially earlier than 2028
5. Manufacturing delay or write-down on the $50B U.S. capex program
6. FY2026 guidance withdrawn or revenue tracking <$78B by Q3 2026
7. Retatrutide Phase 3 efficacy disappointment (<20% weight loss)
8. David Ricks CEO departure

**Data gaps still open**:
- LLY FCF and capex from 10-K (manufacturing capex critical for FCF yield calc)
- Geographic revenue breakdown (verify vs. 10-K segment note)
- Quarterly revenue breakdown by drug for full-year FY2025

**Next review trigger**: **Q1 2026 earnings — late April / early May 2026**. Items: revenue tracking vs. $80–83B FY guide; tirzepatide volume vs. price split; Zepbound formulary expansion; orforglipron FDA status; manufacturing capex pace; Kisunla ramp data.

---

## 2026-04-05 — Initial Thesis Compilation

**Trigger**: First full wiki import — thesis compiled from live data (Yahoo Finance,
stockanalysis.com, Lilly IR press releases, web search).
**Data points reviewed**:
- FY2021–FY2025 annual financials (revenue, EBITDA, EPS — FCF data pending 10-K fetch)
- Q4 2025 earnings: Mounjaro $7.4B (+110%), Zepbound U.S. $4.2B (+122%)
- FY2025 annual: ~$65.2B revenue (+44.7%), EBITDA margin 43.4%
- FY2026 guidance: $80–83B revenue, $33.50–$35.00 non-GAAP EPS
- Pipeline updates: orforglipron NDA/MAA submitted, priority review voucher; retatrutide
  Phase 3 positive (26.6% weight loss); tirzepatide OSA/OA approvals/data
- Manufacturing commitment: $50B+ U.S. spend; $6.5B Texas API plant for orforglipron

### What Changed
- First-time compilation — no prior thesis to compare against
- Key data points established:
  - FY2025 revenue of $65.2B represents one of the fastest large-cap pharma growth
    trajectories ever (+45% YoY; +130% in 3 years from $28.3B in 2021)
  - Tirzepatide franchise (Mounjaro + Zepbound) estimated ~$40B combined in FY2025
  - Stock is 18% off 52-week high ($1,133.95); current price $935.58
  - FY2026E PEG ratio ~0.5x (27x P/E / ~50% EPS growth) — analytically compelling
  - ⚠️ FCF data not populated — manufacturing capex absorbs substantial cash; requires
    LLY 10-K fetch before full valuation finalization

### Thesis Status
- **Overall**: Established — **High Conviction**
- **BAIT delta**: A-STRONG (orforglipron revenue not priced in; manufacturing moat
  undervalued) + I-STRONG (orforglipron priority review accelerated timeline; retatrutide
  data superior) + B-MODERATE (18% off peak creates entry below momentum crowd)
  = Triple Overlap
- **Price targets**:
  - Bull: $1,200–$1,400 (30%) | Base: $980–$1,050 (50%) | Bear: $650–$750 (20%)
  - Probability-weighted EV: ~$1,037 (~+11% from $936)

### Action
- [x] Buy more — Tranche 1: 40% of position at $900–$950; current price $936 is in range
- [ ] Trim — N/A
- [ ] Hold — N/A (establishing position)
- [ ] Watch — Orforglipron FDA approval timeline (priority review: ~1-2 months from filing)

**Data gaps to resolve**:
- ⚠️ LLY FCF and capex from 10-K (manufacturing capex critical for FCF yield calc)
- ⚠️ Geographic revenue breakdown (verify vs. LLY 10-K segment note)
- ⚠️ Quarterly revenue breakdown by drug for FY2025 full year

**Next review trigger**: Orforglipron FDA approval announcement (highest priority);
Q1 2026 earnings (expected April/May 2026) for Zepbound/Mounjaro trajectory.

---

## 2026-04-05 — INIT

**Trigger**: Wiki initialization — stub created.
**Thesis Status**: Pending first import
**Next review trigger**: Import from raw/analyses/
