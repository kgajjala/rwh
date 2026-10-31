# RIVN Raw Source Index

Rivian Automotive (CIK 0001874178). Updated 2026-10-31 for the Q3 2026 print (Oct 29) and the migration of the page to v7.0.

## Stored

| Item | File | Original |
|---|---|---|
| Q3 2026 earnings release (labelled extract with the full statements) | press-releases/2026-10-29_Q3-2026_earnings.txt | https://www.sec.gov/Archives/edgar/data/1874178/000187417826000065/ex-9913q26rivianearningspr.htm |
| Q3 2026 call notes (Q&A read in full; prepared remarks via a summary) | transcripts/2026-10-29_Q3-2026_call-notes.txt | https://www.fool.com/earnings/call-transcripts/2026/10/30/rivian-rivn-q3-2026-earnings-call-transcript/ |
| Q3 2026 deliveries release (Oct 2) | press-releases/2026-10-02_Q3-2026_production-deliveries.txt | EDGAR 8-K |
| Q2 2026 deliveries release, Q2 results, Q2 10-Q excerpts | press-releases/, filings/ | EDGAR |
| CFO transition 8-K (Aug 27); VW term-loan 8-K (Oct 7) | filings/ | EDGAR |
| Insiders and short interest (Oct 18) | filings/2026-10-18_insiders-and-short-interest.txt | OpenInsider, ORTEX, FINRA |
| Q2 call and Morgan Stanley Laguna notes | appearances/ | see files |

## Gaps (logged 2026-10-31)

- **Q3 2026 call prepared remarks** were not retrieved: the Motley Fool page begins at the first analyst question. The prepared-remark points (liquidity, VW and Uber milestones, DOE, CFO) come from a MarketBeat summary (https://www.marketbeat.com/instant-alerts/transcript-what-rivian-automotive-rivn-said-on-its-q3-earnings-call-2026-10-29/). A second full transcript was not stored.
- **Q3 2026 10-Q** (filed after the release) was not read; Item 1A, the DOE loan detail, the convertible terms and the exact share-issuance counts for the new page rest on the Q2 10-Q and the release. The shares from VW, Uber and the offering come from the 8-Ks stored in the earlier ingest; the employee line is a remainder.
- **DEF 14A**: the founder award's metric weights were not parsed `[link pending]`.
- **Regulatory credits** are disclosed for Q2 ($108M) and Q3 ($81M) only; the IEEPA tariff refund receivable in Q3 gross profit is undisclosed.
- **Post-print analyst target changes** and the FY2026 consensus were not retrieved.
- **Short interest** from StockAnalysis (Oct 30); FINRA settlement-date data not re-pulled.
- Form 4s read from OpenInsider's table, not the XML; its price column is unreliable.
- WebFetch returns summaries, not verbatim text, for some pages.
