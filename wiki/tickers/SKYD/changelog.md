# SKYD — Changelog

## [2026-11-18] — Initial ingest (v7.0, Workflow A)

**Trigger**: User request to add SKYD. Skydance Corporation (f/k/a Paramount Skydance, PSKY) closed its Warner Bros. Discovery acquisition on Oct 6, 2026 and reported Paramount's last standalone quarter on Nov 9.
**Sources**: [`raw/SKYD/transcripts/2026-11-09_Q3-2026_call_motleyfool.txt`](../../../raw/SKYD/transcripts/2026-11-09_Q3-2026_call_motleyfool.txt) · [`raw/SKYD/filings/2026-11-09_10-Q_Q3-2026_secondary-summary_ppcland.txt`](../../../raw/SKYD/filings/2026-11-09_10-Q_Q3-2026_secondary-summary_ppcland.txt) · [`raw/SKYD/filings/2026-10-06_8-K_closing_summary_stocktitan.txt`](../../../raw/SKYD/filings/2026-10-06_8-K_closing_summary_stocktitan.txt) · [WBD Q2 2026 release](https://www.sec.gov/Archives/edgar/data/1437107/000143710726000072/wbd2q26earningsrelease08.htm) · gaps logged in [`raw/SKYD/SOURCES.md`](../../../raw/SKYD/SOURCES.md)

### Scorecard
- First ingest; no prior tests.

### Changed
- New v7 report: segment model on a FY2026 pro forma base (revenue ≈$65B, adjusted EBITDA ≈$12.4B [Estimate]) with ≈$6B of annual interest; owner FCF per share × multiple at a 5-year terminal.
- Cases: Bull $19.44 (20%, management's plan in full), Base $8.20 (50%, synergies half-offset by 6%/yr linear decline), Bear $0.51 (30%, covenant breach and equity raise).
- Price verified at $6.83 (Nov 18, 10:47 AM ET, StockAnalysis real-time); the Yahoo quote page was stale at the Oct 27 print and was not used.
- Outsider grade: Anti-Outsider (row added to `outsiders.md`); asset type mapped to Subscription / streaming with linear networks.

### Status
- **Thesis**: n/a (initial)
- **PW EV**: $8.14 · **PW return/yr**: 6.5% (hurdle 13%) · **R/R**: 2.0:1 (Bear ≈−92%) · **BAIT**: Single (B, Mod)
- **Verbs**: non-holder 🟡 Watch (entry ≤$5.04) · holder 🟡 Hold

**Next trigger**: 📅 Q4 2026 print with FY2027 guidance and pro forma financials (~early March 2027), test 1.
