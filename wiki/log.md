# kg-invest-wiki — Event Log

Append-only chronological record of all wiki operations.
Format: `LOG [YYYY-MM-DD HH:MM] [ACTION] [SCOPE] — [description]`
Never delete or modify existing entries.

---

LOG 2026-04-05 00:00 INIT ALL — Wiki created. Directory structure scaffolded. CLAUDE.md schema written. Stub pages created for BKNG, LLY, WING, UNH, SCHW. Frameworks scaffolded: BAIT, Moneyball, Position Sizing, Asset Types.
LOG 2026-04-05 12:00 PRICE ALL — Fetched live prices via Yahoo Finance JSON API: BKNG $4,194.31 | LLY $935.58 | WING $152.51 | UNH $277.26 | SCHW $93.77. All prices verified before valuation work.
LOG 2026-04-05 12:05 INGEST BKNG — Full thesis compiled from live data. Sources: stockanalysis.com (FY2021-2025 financials, cash flow, balance sheet), Yahoo Finance (price/valuation), web search (Q4 2025 earnings, management commentary, analyst consensus). Key data: $26.9B revenue, $9.1B FCF, 1.235B room nights, 70% merchant mix, $700M 2026 reinvestment. 25-for-1 stock split effective 4/2/2026 noted.
LOG 2026-04-05 12:10 UPDATE BKNG — Wrote overview.md, thesis.md (15 sections), financials.md, changelog.md. Verdict: Buy. BAIT: Triple overlap. PW EV: ~$196 post-split (+17%).
LOG 2026-04-05 12:15 INGEST LLY — Full thesis compiled from live data. Sources: stockanalysis.com (FY2021-2025 financials), Lilly IR press releases (Q4 2025, FY2025 results, 2026 guidance), prnewswire.com. Key data: $65.2B revenue (+45%), FY2026 guidance $80-83B, Mounjaro ~$23.5B, Zepbound ~$16.5B annualized, orforglipron filed with priority review. NOTE: FCF/capex data gap — pending LLY 10-K fetch.
LOG 2026-04-05 12:20 UPDATE LLY — Wrote overview.md, thesis.md (15 sections), financials.md, changelog.md. Verdict: Buy. BAIT: Triple overlap. PW EV: ~$1,037 (+11%).
LOG 2026-04-05 12:25 INGEST WING — Full thesis compiled from live data. Sources: stockanalysis.com (FY2021-2025 financials), ir.wingstop.com FY2025 results, prnewswire.com, franchise research. Key data: $697M revenue, $244M adj. EBITDA, 3,056 units, 493 net new units, –3.3% domestic SSS (first decline in 22 years), 2026 guidance flat to LSD SSS + 15-16% unit growth. NOTE: FCF data gap — pending WING 10-K fetch.
LOG 2026-04-05 12:30 UPDATE WING — Wrote overview.md, thesis.md (15 sections), financials.md, changelog.md. Verdict: Buy (Speculative). BAIT: Triple overlap (lower conviction). PW EV: ~$187 (+22%).
LOG 2026-04-05 12:35 INGEST UNH — Full thesis compiled from live data. Sources: stockanalysis.com (FY2021-2025 financials), businesswire.com FY2025 results (UNH IR), fiercehealthcare.com, medicaremarketinsights.com. Key data: $447.6B revenue, MLR 89.1% (vs. 85.5%), FCF $16.1B (–22%), CEO Witty resigned May 2025 → Hemsley returned, 1.3M MA members to exit 2026, Optum Health earnings $7.9B → $2.3B adj. DOJ investigation ongoing.
LOG 2026-04-05 12:40 UPDATE UNH — Wrote overview.md, thesis.md (15 sections), financials.md, changelog.md. Verdict: Buy (eyes open). BAIT: Quadruple overlap (highest in portfolio). PW EV: ~$369 (+33%, 24-month).
LOG 2026-04-05 12:45 INGEST SCHW — Full thesis compiled from live data. Sources: stockanalysis.com (FY2021-2025 financials), pressroom.aboutschwab.com FY2025 results, content.schwab.com Q4 2025, web search. Key data: $23.9B revenue (+22%), NII $11.75B, NIM 2.90%, client assets $11.9T (record), NNA $519B, FHLB debt $97B peak → $5.1B, TD Ameritrade integration complete. NOTE: FCF/capex data gap — pending SCHW 10-K fetch.
LOG 2026-04-05 12:50 UPDATE SCHW — Wrote overview.md, thesis.md (15 sections), financials.md, changelog.md. Verdict: Buy/Hold. BAIT: Double overlap. PW EV: ~$110 (+17%).
LOG 2026-04-05 12:55 UPDATE index.md — Full index refresh. All 5 tickers moved from "Stub — pending import" to "Active — full thesis compiled". Added pending data gaps table. Added ticker summary with prices, BAIT, verdicts.
LOG 2026-04-05 13:00 UPDATE watchlist.md — Full watchlist compiled. Conviction ranking: UNH #1 (quadruple BAIT), BKNG #2, LLY #3, WING #4, SCHW #5. Portfolio allocation targets set. Earnings calendar populated. Price targets summary table added. Cross-portfolio macro watch items documented.
