# AKAM Raw Source Index

Ingest of 2026-11-06 (Workflow A, v7.0). CIK 1086222.

> `www.sec.gov` Archives return HTTP 403 to scripted curl even with a browser User-Agent (confirmed on 2026-11-06). Filings were read in the built-in browser (`document.body.innerText`) and stored here as labelled extracts, not verbatim files. `data.sec.gov` XBRL company-facts and submissions JSON work and were used for the multi-year series.

## Stored in raw/AKAM/

| File | What | Source |
|---|---|---|
| press-releases/2026-11-05_Q3-2026_earnings_extract.txt | Q3 2026 release: P&L, balance sheet, cash flow, solution revenue, guidance | [8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001086222/000108622226000097/exhibit991-q32026.htm) |
| press-releases/2026-09-24_Anthropic-agreement_extract.txt | $11.6B Anthropic agreement and warrant terms | [8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/1086222/000119312526401048/d288154dex991.htm) |
| transcripts/2026-11-05_Q3-2026_earnings-call_extract.txt | Q3 call: prepared remarks and Q&A, quoted passages | [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/11/06/akamai-akam-q3-2026-earnings-call-transcript/) (read in full) |
| filings/2026-03-31_DEF14A_extract.txt | Incentive plan metrics and weights; ownership | [DEF 14A](https://www.sec.gov/Archives/edgar/data/1086222/000108622226000042/akam-20260330.htm) |

## Read but not stored (cited in the report)

- Q2 2026 release (guidance table, Aug 6, 2026): [8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001086222/000108622226000083/exhibit991-q22026.htm)
- Q2 2026 10-Q, Note 7 Debt (convertible notes table and conversion terms): [10-Q](https://www.sec.gov/Archives/edgar/data/1086222/000108622226000086/akam-20260630.htm)
- FY2025 10-K: MD&A overview, cash-flow statement, customer concentration, RPO, Item 1A headings: [10-K](https://www.sec.gov/Archives/edgar/data/1086222/000108622226000022/akam-20251231.htm)
- FY2022 10-K cash-flow statement (FY2020–22 capex): [10-K](https://www.sec.gov/Archives/edgar/data/1086222/000108622223000078/akam-20221231.htm)
- XBRL company facts (FY2021–25 series): https://data.sec.gov/api/xbrl/companyfacts/CIK0001086222.json
- Prices and 52-week range: Yahoo Finance; cross-check StockAnalysis (statistics, forecast). Total-return series via `skills/kg-investment-analysis/scripts/prices.py` (AKAM, NET, SPY).
- Insiders: OpenInsider (180 days). Consensus and Nov 6 target changes: StockAnalysis forecast page.

## Gaps (logged, not fabricated)

- **Q3 2026 10-Q**: not yet filed on 2026-11-06 (8-K only).
- **Q1 2026 release and call**: not read; Q1 guidance (CIS growth of at least 50%, ~$4.5B revenue, ~$6.78 EPS) comes from secondary reports (MarketBeat, Barchart) and is tagged as such in the promises ledger. Link: [Q1 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001086222/000108622226000054/exhibit991-q12026.htm).
- **Second Q3 transcript** (R9 cross-check): one full transcript read (Fool); Benzinga, MarketBeat and Seeking Alpha versions exist but were not read.
- **IR slide with the 13% IRR / 15% ROIC calculation**: stated on the call; the slide itself was not retrieved.
- **Item 1A**: headings scanned; full text not read. New-versus-prior-year comparison not done.
- **Shareholder letters (R9)**: Akamai publishes none; the proxy and 10-K stand in.
- **Appearances (R9)**: web search found no conference or media appearances by Leighton or McGowan in the window beyond the quarterly calls and the Sept 24 Anthropic call. The IR events page was not retrieved.
- **Investor day**: none found in the window; the promises ledger leans on secondary reports for the 2022 cloud target.
- **Form 4 XML**: blocked to scripts; OpenInsider table used.
- **Short interest month-over-month change**: not retrieved.
- **S&P / Moody's rating action**: search results conflicted (March 2026 versus September 2026); not verified and not cited.
- **Scuttlebutt**: no competitor filings read for this ingest.
