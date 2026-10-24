# SNOW — Changelog

Append-only event log. Newest first.

---

## [2026-10-24] — Initial ingest (Workflow A, schema v7.0)

**Trigger**: User request to add SNOW to the tracker with a full analysis, specifically asking what caused the stock's collapse at the onset of powerful LLMs and what drove the recovery.
**Sources**: [FY2026 10-K](../../../raw/SNOW/filings/2026-03-20_10-K_FY2026.txt) · [Q2 FY2027 10-Q](../../../raw/SNOW/filings/2026-09-04_10-Q_Q2-FY2027.txt) · [2026 DEF 14A](../../../raw/SNOW/filings/2026-05-18_DEF-14A.txt) · quarterly releases [Q3 FY2026](../../../raw/SNOW/press-releases/2025-12-03_Q3-FY2026-results.txt), [Q4 FY2026](../../../raw/SNOW/press-releases/2026-02-25_Q4-FY2026-results.txt), [Q1 FY2027](../../../raw/SNOW/press-releases/2026-05-27_Q1-FY2027-results.txt), [Q2 FY2027](../../../raw/SNOW/press-releases/2026-09-02_Q2-FY2027-results.txt) · 8-Ks for the [CEO performance award](../../../raw/SNOW/filings/2026-07-15_8-K.txt), [annual meeting](../../../raw/SNOW/filings/2026-06-29_8-K.txt), [Observe/board resignation](../../../raw/SNOW/filings/2026-01-28_8-K.txt), [CRO change](../../../raw/SNOW/press-releases/2026-03-31_press-release.txt) and the [$3.75B converts](../../../raw/SNOW/press-releases/2026-09-29_convertible-notes-pricing.txt) · [appearance sweep](../../../raw/SNOW/appearances/2026_appearance-sweep.txt) · SEC XBRL company facts · 90 days of Form 4 XML · Q1 and Q2 FY2027 call transcripts.

### Scorecard
No prior tests — first ingest. Three kill criteria written, resolving Dec 2, 2026, late February 2027 and ~March 2027.

### Changed
- **New page at schema v7.0.** Deep dive: *Snowflake: The Year the Market Changed Its Mind Twice.*
- **The round trip, diagnosed.** Peak $277.14 (Nov 3, 2025) → trough $121.11 (Apr 10, 2026), −56.3% in 110 sessions → $325.43 (Oct 23, 2026), +168.7%. The business never stumbled: product revenue grew 29%, 30%, 34%, 37% across the window with RPO up 37–42%.
- **Cause of the fall.** Not an earnings event. Guidance. Q4 FY2026 was guided to 27% growth on Dec 3 (−11.4% next session) and FY2027 to $5,660M / 27% on Feb 25, which the market read as AI-driven deceleration. The agentic-disruption thesis (ClickHouse's Aaron Katz; Databricks at $134B growing >55% with 10× the AI revenue) supplied the narrative, and the Apr 9 sector repricing on managed-agent fears (NET −12%, SNOW −9%, NOW −7%) supplied the capitulation.
- **Cause of the recovery.** The guide was a methodological artifact. Robins: forecasts are "based on observed consumption patterns," and CoCo had no observed behaviour to forecast from — he later said "CoCo had the largest driver to the increase in our forecast." FY2027 guidance went $5,660M → $5,840M (May 27, +36.5% in a session) → $6,070M / 36% (Sep 2, +16.6%). Ramaswamy: first-party AI "contributed approximately half of the acceleration."
- **The open question is not AI, it is compensation.** Owner earnings (CFO − SBC − capex) have been negative every year: −$511M, −$341M, −$355M, −$565M, −$480M FY2022–FY2026. SBC was 34.2% of FY2026 revenue. $3,398M of buybacks since FY2024 and the diluted share count still rose 12% in five years. Invested capital is ≈zero (−$120M at FY2026 year-end), so ROIC/ROIIC are not meaningful and the high-ROIIC compounder flag does not apply.
- ⚠️ **Governance.** Say-on-pay rejected in 2025 and again on Jun 29, 2026 (44% support); shareholders also carried a majority-voting proposal against the board. Sixteen days later the committee granted a 1,000,000-share CEO award with tranches at $324–$531, every one of which implies an 8.4–11.3%/yr shareholder return — below the hurdle. Insiders sold **$521.6M** in 90 days with zero open-market purchases.
- **Model**: FY2027 base → FY2032 terminal, valued on **owner earnings** (`eps_excludes_sbc`), exit multiples capped at 25× in the Base because 25× is where implied perpetual growth equals the 4.96% ten-year yield.

### Status
- **Thesis**: New — good business, wrong price.
- **PW EV**: $241 · **PW return/yr**: −5.8% (hurdle 13%) · **R/R**: 0.3:1 · **Entry**: ≤$131 · **BAIT**: Single (A), bearish
- **Verbs**: non-holder 🟡 Watch · holder 🔴 Trim
- Break-even and price-implied Bear odds are both negative: no probability weighting of the case set earns even 9%/yr from $325.43. The Bull alone, with certainty, returns 4.0%/yr.

**Next trigger**: 📅 Q3 FY2027, December 2, 2026 — tests 1 and 2 (product gross margin ≥74.0%, growth ≥37%).
