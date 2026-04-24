# Watchlist — Cross-Ticker Ranking

> **Schema v2 note (2026-04-24)**: Allocation columns and tranche-sizing language
> were removed when CLAUDE.md was migrated to v2 (position-agnostic). The
> ranking and price-target tables below are legacy v1 content and will be
> re-derived as each ticker is re-ingested under Workflow A. The v2 columns are:
> Rank · Ticker · Conviction · BAIT Overlap · Asymmetry (PW EV vs. price) ·
> Recommendation (non-holder / holder) · Next Catalyst.

*Updated by LLM agent after each full thesis cycle or earnings update.*
*Last updated: 2026-04-24 (schema migration; per-ticker content pending re-ingest)*
*Prices as of 2026-04-16/17 (Yahoo Finance / analysis files)*

---

## Conviction Ranking

| Rank | Ticker | Conviction | BAIT Overlap | Asymmetry | Recommendation | Next Catalyst |
|------|--------|-----------|--------------|-----------|----------------|---------------|
| 1 | UNH | Medium (high BAIT) | Quadruple | 3:1 (~+33% EV, 24-mo) | Initiate — attractive at $250–$285 | Q1 2026 MLR (April 2026) |
| 2 | BKNG | High | Triple | 1.5:1 (~+17% EV, 18-mo) | Initiate — attractive at ~$155–$170 post-split | Q1 2026 earnings (May 2026) |
| 3 | LLY | High | Triple | 2:1 (~+11% EV, 12-mo) | Initiate — attractive at $900–$950 | Orforglipron FDA approval (2026) |
| 4 | WING | Medium | Triple (lower conviction) | 2:1 (~+22% EV, 18-mo) | Initiate (speculative) — attractive at $140–$160 | Q1 2026 domestic SSS (April 2026) |
| 5 | SCHW | Medium | Double | 2:1 (~+17% EV, 18-mo) | Initiate / Hold — attractive at $88–$96 | Q1 2026 NIM + rate outlook (April 2026) |
| 6 | RKT | Medium | Double (B+A) | 2.5:1 (~+51% PW EV, 1-3yr) | Initiate (speculative) — attractive at $14–$16 | Q1 2026 earnings (April 30, 2026) |
| 7 | SHOP | High | Triple (B+A+I) | 1.8:1 (~+79% PW EV, 18-mo) | Initiate (speculative) — attractive at $115–$125 | Q1 2026 earnings (~May 2026) |
| 8 | DASH | Low-Medium | Double (B+A) | 1.2:1 (–26% PW EV 5-yr) | Watch — better entry at $140–$150 | Q1 2026 earnings (~May 2026) |
| 9 | PG | Medium | Weak (no overlap) | 1.1:1 (~+7% PW EV, 3-yr) | Watch / Conditional | Q3 FY2026 earnings (April 24) |

**Ranking rationale**:
- UNH ranked #1 on BAIT (quadruple overlap) and normalized earnings asymmetry (10x trough P/E), despite elevated operational uncertainty
- BKNG ranked #2 on highest moat quality + FCF yield (~6.8%) + imminent split-adjusted accessibility
- LLY ranked #3 on strongest secular growth + manufacturing moat, but near-term upside is smaller
- WING ranked #4 — compelling asymmetry but narrowest moat and SSS uncertainty
- SCHW ranked #5 — solid NII recovery story, lowest asymmetry, rate-sensitive
- RKT ranked #6 — strong PW upside (+51%) but highest execution risk (acquisition integration, rate sensitivity, RESPA lawsuit, $10.6B goodwill); BAIT is Double vs. Triple/Quad for others

---

## Earnings Calendar & Key Watch Events

| Ticker | Next Expected Event | Key Watch Item | Signal If Positive | Signal If Negative |
|--------|-------------------|---------------|-------------------|-------------------|
| BKNG | Q1 2026 earnings (~May 2026) | Connected Trip % of transactions | Re-rate toward 20x EV/EBITDA | SSS concern; AI disintermediation narrative |
| LLY | Orforglipron FDA approval (2026) | Priority review: 1-2 month timeline | Re-rate; oral GLP-1 TAM expansion | Delay → BKNG-style narrative re-ignition |
| LLY | Q1 2026 earnings (~April/May 2026) | Zepbound + Mounjaro trajectory | Confirm guidance path | Miss → thesis delay |
| WING | Q1 2026 earnings (~late April 2026) | **Domestic SSS** | Thesis confirming; short squeeze | Thesis-weakening |
| UNH | Q1 2026 earnings (~April 2026) | **Medical Loss Ratio** | Multiple expansion catalyst | Thesis-delaying |
| SCHW | Q1 2026 earnings (~April 2026) | NIM trend + sweep balance rebuild | Re-rate to 22-25x; buyback signal | Rate-cut risk realization |
| RKT | Q1 2026 earnings (April 30, 2026) | **Adj revenue ≥ $2.6B + EBITDA run-rate** | Thesis confirming; 5th consecutive beat | Below $2.4B on no external shock = thesis break |
| SHOP | Q1 2026 earnings (~May 2026) | **Revenue growth ≥ +25% + gross margin stable** | Thesis continuing | Growth <20% + margins compressed = cautionary |
| DASH | Q1 2026 earnings (~May 2026) | **Adj EBITDA ≥ $675M + H2 margin improvement commentary** | Base case tracking | Below $650M or no H2 guidance = thesis weakening |
| PG | Q3 FY2026 earnings (April 24, 2026) | **Organic sales growth ≥ 2% + tariff on track** | Shows stabilization | Further guidance cut or dividend concern = thesis break |

---

## Price Targets Summary (Probability-Weighted)

| Ticker | Current Price | Bear (prob) | Base (prob) | Bull (prob) | PW Expected Value | Upside |
|--------|--------------|-------------|-------------|-------------|-------------------|--------|
| BKNG | $168 post-split | $112 (20%) | $197 (50%) | $250 (30%) | $196 | +17% |
| LLY | $935.58 | $700 (20%) | $1,015 (50%) | $1,300 (30%) | $1,037 | +11% |
| WING | $152.51 | $95 (25%) | $187 (50%) | $280 (25%) | $187 | +22% |
| UNH | $277.26 | $200 (25%) | $360 (45%) | $525 (30%) | $369 | +33% |
| SCHW | $93.77 | $70 (20%) | $110 (50%) | $137 (30%) | $110 | +17% |
| RKT | $14.96 | $9 (20%) | $22 (55%) | $35 (25%) | $22.65 | +51% |
| SHOP | $117–121 | $113 (15%) | $193 (45%) | $252 (30%) + $325 (10%) | ~$216 | +79% |
| DASH | $176 | $50 (20%) | $110 (50%) | $215 (30%) | ~$130 | –26% (5-yr scenario) |
| PG | $143.35 | $125 (30%) | $160 (45%) | $177.50 (25%) | ~$154 | +7% |

*All price targets are 12-24 month horizons except noted. UNH targets 24-month. RKT targets 1-3 year. DASH targets 5-year. SHOP targets 18-month.*

---

## Key Macro Watch Items (Cross-Portfolio)

| Macro Variable | Portfolio Impact | Direction to Watch |
|----------------|-----------------|-------------------|
| Federal Reserve rate path | SCHW NIM (direct); BKNG ADR/travel (indirect) | Any cut cycle = SCHW negative; no cuts = SCHW positive |
| U.S. consumer health | WING SSS; BKNG room nights; DASH order frequency | Consumer stress = WING / DASH pressure; BKNG more resilient (international) |
| CMS Medicare Advantage rates | UNH MLR recovery | Favorable CMS 2027 rates = UNH significant upside |
| GLP-1 oral competition | LLY competitive positioning | Viking/Roche NDA = LLY multiple pressure |
| AI in travel | BKNG existential risk | Watch Google, OpenAI travel agent product launches |
| 30-year mortgage rates | RKT origination volume (critical); SCHW NIM (indirect) | Any sustained move below 6.25% = RKT bull trigger; above 7.5% = RKT bear |
| Housing lock-in effect unlock | RKT purchase volume + Redfin traffic | Rate relief → unlock → RKT volume surge; watch 30-yr weekly averages |
| Gig worker reclassification (federal AB5) | DASH unit economics (existential) | Any federal legislative movement = DASH thesis-break risk |
