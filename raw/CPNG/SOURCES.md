# CPNG sources and gaps

## 2026-11-04 (Q3 2026 update, v5 to v7 migration)
Fetched and stored as labelled extracts (www.sec.gov returns 403 to scripts; data.sec.gov works):
- Q3 release (8-K Ex. 99.1) and 10-Q, through WebFetch (summaries, not verbatim): press-releases/2026-11-03_Q3-2026_earnings.txt, filings/2026-11-03_10-Q_Q3-2026_extract.txt
- Q3 call: full transcript read in the built-in browser (Investing.com); verbatim excerpts in transcripts/2026-11-03_Q3-2026_earnings-call.txt
- XBRL company facts via scripts/xbrl.py (annual series FY2020-FY2025 plus Sep 30 2026 balance sheet)
- Price: Yahoo chart API, regular close $15.23 on 2026-11-03 (pre-print); overnight session ~$14.54 per the Yahoo quote page, which showed an error banner
- Korea Times (2026-11-04) and FNnews (2026-11-04) write-ups for the KFTC fine range and Kim's comments

Gaps (not fabricated):
- Form 4 XML: www.sec.gov blocked; the filing list shows Form 4s on Aug 11 (two) and Oct 5 and Form 144s on Aug 10 and Oct 2, contents not read.
- Short interest: no October settlement found; last figure is Aug 14 (69.0M shares, Curved Trading).
- Post-print analyst target changes: none published at retrieval time.
- Second full transcript, DEF 14A re-read, FY2025 Item 1A diff, 10-Q Item 1A and MD&A liquidity narrative: not read.
- IR events page: not opened; no appearance outside the Q3 call was found for Oct 3 - Nov 4 (search only).
- Raw files for the 10-Ks, Q2 call and Q2 release cited in earlier changelog entries were never stored (see changelog 2026-10-02).
