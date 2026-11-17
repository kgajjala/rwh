# NVDA raw sources and gaps

First ingest: 2026-11-17 (Workflow A, v7). Fetch method per the repo's SEC notes: XBRL JSON via `scripts/xbrl.py`; filings read through WebFetch summaries (not verbatim) where noted.

## Stored here

| File | What | Verbatim? |
|---|---|---|
| `press-releases/2026-08-26_Q2FY27_CFO_commentary.txt` | CFO commentary, Q2 FY2027 (IR PDF, PDFKit extract) | Yes |
| `transcripts/2026-08-26_Q2FY27_earnings_call.txt` | Q2 FY2027 call, FactSet corrected transcript (IR-hosted PDF) | Yes |
| `filings/2026_10-K_FY2026_extract.md` | FY2026 10-K: competition, customers, risk-factor lines, buybacks, segment income | Summary extract |
| `filings/2026_DEF14A_extract.md` | 2026 proxy: incentive metrics, goals, payouts, ownership | Summary extract |
| `filings/2026-11-12_8-K_CEO_transition_extract.md` | 8-K on Huang's resignation | Summary extract |
| `appearances/2026-09-10_goldman-communacopia_huang.md` | Goldman Sachs Communacopia fireside | Summary extract |
| `appearances/2026-10-21_gtc-berlin_huang.md` | GTC Berlin keynote | Summary extract |
| `../clippings/2026-11-03_AMD_Q3_2026_prepared_remarks.txt` | AMD Q3 2026 prepared remarks (competitor) | Yes |

## Gaps (logged, not fabricated)

- **10-Ks FY2022–FY2025**: not read; multi-year numbers come from SEC XBRL company facts. Item 1A was not diffed year over year; FY2026 risk lines are summary quotes.
- **Shareholder letters**: Pattern C. Nvidia publishes no standalone letter; the annual report (ARS PDF, `a2026-annualxreportxwebxfi.pdf`) was not parsed. Gap.
- **Q1 FY2027 and Q3/Q4 FY2026 releases and transcripts**: not stored; quarter figures used are from the Q2 FY2027 CFO commentary (which restates Q1 FY2027 and Q2 FY2026).
- **Form 4s (90 days)**: OpenInsider fetch failed; www.sec.gov Form 4 XML blocked to scripts. Gap.
- **Investor day**: none held recently; GTC 2026 roadmap read through SemiAnalysis and HPCwire.
- **Huang separation terms**: not disclosed in the Nov 12 8-K.
- **Mellanox and Arm deal prices**: from memory of the announcements, marked `[link pending]` in the report.
