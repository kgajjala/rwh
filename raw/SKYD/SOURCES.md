# SKYD raw set — first ingest 2026-11-18

Skydance Corporation (f/k/a Paramount Skydance, PSKY; f/k/a Paramount Global, PARA). CIK 0002041610. Class B (non-voting) trades as SKYD on NYSE from 2026-10-06. Warner Bros. Discovery (CIK 0001437107) acquired 2026-10-06.

## Stored here
- `transcripts/2026-11-09_Q3-2026_call_motleyfool.txt` — full Q3 2026 call (Motley Fool). https://www.fool.com/earnings/call-transcripts/2026/11/10/skydance-skyd-q3-2026-earnings-call-transcript/
- `filings/2026-11-09_10-Q_Q3-2026_secondary-summary_ppcland.txt` — line-by-line write-up of the Q3 10-Q, shareholder letter and call (secondary). https://ppc.land/skydance-faces-6bn-yearly-interest-bill-after-97bn-warner-takeover/
- `filings/2026-10-06_8-K_closing_summary_stocktitan.txt` — closing 8-K (financing, PIPE, warrants). https://www.stocktitan.net/sec-filings/PSKY/8-k-paramount-skydance-corp-reports-material-event-e1470761c887.html
- `press-releases/2026-10-06_wbd-close_8k-ex99-1_via-stocktitan.txt` — closing press release (8-K Ex-99.1).
- `press-releases/2026-11-09_Q3-2026_trending-schedules_investing-summary.txt` — trending schedules summary (Investing.com). Note: its share-price line ($16.91) is wrong; ignore.
- WBD Q2 2026 release (primary, EDGAR): https://www.sec.gov/Archives/edgar/data/1437107/000143710726000072/wbd2q26earningsrelease08.htm — LTM adj EBITDA $8.8B; Q2 revenue $8,717M (−11%); Streaming adj EBITDA $512M; Studios $96M; Global Linear Networks $1,446M; net leverage 3.4×.

## Gaps (logged, not fabricated)
- ir.skydance.com (shareholder letter, trending schedules, official transcript): fetch not approved in this session. Figures taken from the call transcript and two secondary write-ups that agree with each other.
- SEC EDGAR browse/XBRL API: not reachable from the sandbox; 10-K Item 1A/7 for FY2021–25 not read; XBRL series replaced by StockAnalysis (S&P Global) annual tables for Paramount and WBD.
- DEF 14A CD&A (incentive metrics and weights): not retrieved. Aggregator shows CEO pay ≈$63.2M, ~98% equity/bonus.
- Form 4 (90 days): not read. Insider signal used: Ellison family bought 1.24B shares for $14.85B in the October PIPE at $12.00.
- Pro forma combined financials: company will publish before the Q4 call; the page's FY2026 pro forma base is an author's estimate.
- Price-history series (`prices.py`): Yahoo chart API blocked from the sandbox; chart built from StockAnalysis daily closes.
- Letters (R9): Paramount Skydance has no standalone annual letter; quarterly shareholder letters exist on IR (not fetchable).
- Appearances (R9) swept Oct 6–Nov 18: earnings call Nov 9; no CEO conference or podcast transcripts found in the window. Investor Day scheduled 1H 2027.
