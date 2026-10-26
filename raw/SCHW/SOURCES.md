# SCHW Raw Source Index

Schwab (CIK 0000316709). Inventory kept so a later session knows what is stored and what is missing.

## Stored

| Item | File | Original |
|---|---|---|
| 10-K FY2021 to FY2025 | filings/SCHW-10K-FY20xx.htm | EDGAR |
| 10-Q Q2 2026 | filings/SCHW-10Q-2026Q2.txt | https://www.sec.gov/Archives/edgar/data/316709/000031670926000031/schw-20260630.htm |
| DEF 14A 2026 | filings/SCHW-DEF14A-2026.txt | EDGAR |
| Q4 2025 release (8-K Jan 21, 2026) | press-releases/2026-01-21_Q4-2025_earnings.txt | https://content.schwab.com/web/retail/public/about-schwab/schw_8k_01212026.pdf |
| Q2 2026 release (Jul 21) | press-releases/2026-07-21_Q2-2026_earnings.txt | EDGAR exhibit 99.1 |
| Q3 2026 release (8-K Oct 15) | press-releases/2026-10-15_Q3-2026_earnings.txt | https://content.schwab.com/web/retail/public/about-schwab/schw_8k_101526.pdf |
| Investor Day 2024, 2026 | investor-day/ | IR |
| Summer Business Update notes (Jul 21) | appearances/2026-07-21_summer-business-update_wurster-verdeschi.txt | see file |
| Fall Business Update notes (Oct 15) | appearances/2026-10-15_fall-business-update_wurster-verdeschi.txt | see file |
| Annual-report letters 2020 to 2025 | shareholder-letters/ | IR (PDF) |

## Gaps (logged 2026-10-26)

- **Q3 2026 10-Q** is not filed yet (expected early November). The Q3 balance sheet, liquidity and rate-sensitivity figures in the update come from the earnings release only. Re-check Item 1A and the dynamic NII table when it lands.
- **Q1 2026 release** (https://content.schwab.com/web/retail/public/about-schwab/schw_8k_04162026.pdf) downloaded but PDFKit extracted no text. The Q1 numbers used (five-quarter table, $2.4B buyback) come from the Q2 and Q3 releases and the prior page.
- **Q3 2026 call transcript, second source.** Only the Motley Fool transcript (via Mitrade) was retrievable; Investing.com and Seeking Alpha had no Q3 2026 version. The Fall Business Update slide deck URL pattern (schw_fall_business_update_10152026.pdf and variants) returned 404.
- **Q4 2025 and Q1 2026 call transcripts** not stored (R9 asks for four); the releases are.
- **Form 4s** read from OpenInsider's table of SEC Form 4 filings (https://openinsider.com), not from the XML. www.sec.gov Archives pages return 403 to scripts; data.sec.gov works.
- **Short interest** from MarketBeat (FINRA data, settlement Oct 15, 2026).
- **IR events page** (aboutschwab.com/schwabevents) not fetched; forward dates (IMPACT Oct 29, Winter Business Update January 2027) from Yahoo and the call.
- WebFetch returns summaries, not verbatim text, for sec.gov pages; a browser read of the page text was used for the call transcript.
