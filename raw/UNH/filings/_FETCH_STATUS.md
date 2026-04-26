# UNH raw/filings — fetch status (2026-04-26 v2.9 retrofit)

SEC EDGAR direct fetch returned HTTP 403 during retrofit (rate-limit / blocked UA).
Known canonical filing URLs documented for next-pass refresh:

- **FY2024 10-K** (period 2024-12-31, filed Feb 2025): https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm
- **FY2023 10-K** (period 2023-12-31, filed Feb 2024): https://www.sec.gov/Archives/edgar/data/731766/000073176624000045/unh-20240221.htm (proxy period 2024-02-21 wrapper)
- **FY2025 10-K** (period 2025-12-31, expected filed Feb 2026): [link pending] — accession not yet enumerated
- **FY2022 10-K**, **FY2021 10-K**, **FY2020 10-K**: [link pending] — to be backfilled in next pass

Current synthesis in UNH.md draws Item 7 (MD&A) and Item 1A (Risk Factors) commentary
from the press releases, earnings transcripts, and FY2024 10-K accession above. Multi-year
Risk Factor evolution paragraph in §6 is built from observable narrative arc rather than
verbatim 10-K diff (next-pass enrichment task).
