# SHOP sources and gaps

## 2026-11-05 (Q3 2026 update, v5 to v7 migration)
Fetched and stored (www.sec.gov returns 403 to scripts; the built-in browser reads it in full):
- Q3 release (8-K Ex. 99.1), full text via the browser: press-releases/2026-11-03_Q3-2026_earnings.txt
- Q3 10-Q (144K chars), MD&A, liquidity, issuer purchases and cover read via the browser: filings/2026-11-03_10-Q_Q3-2026_extract.txt
- Q3 call: full Motley Fool transcript read in the browser; key passages cross-checked against Investing.com: transcripts/2026-11-03_Q3-2026_earnings-call.txt
- Earnings-day media (CNBC Squawk, TBPN) and the Sep 10 Goldman Sachs conference via write-ups: appearances/2026-11-03_CNBC-TBPN_finkelstein.txt
- Analyst reports (user-supplied PDFs, PDFKit text): analyst-reports/2026-11-04_MBI_shop3q26.txt, analyst-reports/2021-04-09_MBI_anti-amazon-protagonist.txt
- XBRL company facts via scripts/xbrl.py (FY2020–FY2025 plus Sep 30 2026 balance sheet)
- Price: Yahoo quote page, $153.03 at the Nov 4 close (4:00 PM EST), 52-wk $94.00–$180.88, market cap $196.9B; total-return series via scripts/prices.py
- Consensus and Nov 3–4 target changes: StockAnalysis; short interest: MarketBeat (Oct 15 settlement); 10-year Treasury: FRED DGS10 (4.95% on Nov 3)

Gaps (not fabricated):
- Goldman Sachs Communacopia (Sep 10) transcript not retrieved; a secondary summary only.
- CNBC Squawk and TBPN full interviews not retrieved; quotes are from write-ups.
- Insider sales: Form 144 notices Aug 5 – Sep 25; Shopify insiders' executed sales are not on Form 4 in the EDGAR list (the only Form 4, Aug 31, is Shopify's own Klaviyo warrant exercise). Executed amounts unverified.
- S-3ASR filed Nov 3 (universal shelf) read only through the 10-Q description; no offering announced.
- FY2025 10-K Item 1A diff not run in this update; the Q3 10-Q says no material change in risk factors.
- 10-K Item 7 for FY2021–FY2024 not re-read; the five-year record comes from XBRL.
- Earlier raw files (Q2 release, Q2 10-Q, 2026 circular, Q2 call notes) are from the 2026-09-23 update.
