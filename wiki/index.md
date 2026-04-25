# kg-invest-wiki — Index

Master catalog of all wiki pages. Updated by the LLM agent on every ingest or
substantial wiki change. Each entry: link, one-line summary, last updated, status.

**Schema**: v2.1 — single consolidated `[TICKER].md` per ticker (legacy v1
overview/thesis/financials files have been folded in and deleted).

---

## Tickers

| Ticker | Company | Moat | Conviction | Last Updated | Status |
|--------|---------|------|-----------|--------------|--------|
| [BKNG](tickers/BKNG/BKNG.md) | Booking Holdings | Wide | High | 2026-04-17 | v2.1 — Triple BAIT (B+A-Strong); Initiate / Hold-Add |
| [LLY](tickers/LLY/LLY.md) | Eli Lilly | Wide | High | 2026-04-17 | v2.1 — Triple BAIT (A+I-Strong); Initiate measured / Hold-Add on pullback |
| [WING](tickers/WING/WING.md) | Wingstop | Narrow | Medium | 2026-04-17 | v2.1 — Asymmetry compressed at recovery; Watch / Hold pre-Q1 SSS |
| [UNH](tickers/UNH/UNH.md) | UnitedHealth Group | Wide | Medium-High | 2026-04-17 | v2.1 — Quadruple BAIT preserved; recovery underway; Watch / Hold-Add |
| [SCHW](tickers/SCHW/SCHW.md) | Charles Schwab | Narrow-Wide | High | 2026-04-17 | **v2.1 + Q1 2026 beat** — STRENGTHENED; Triple BAIT (B+A+I-Strong); Initiate / Add (post-beat 52-wk low) |
| [RKT](tickers/RKT/RKT.md) | Rocket Companies | Narrow-Emerging Wide | Medium | 2026-04-17 | v2.1 — Double BAIT (B+A); Initiate Spec. / Hold-Add; Q1 print Apr 30 |
| [SHOP](tickers/SHOP/SHOP.md) | Shopify | Wide | High | 2026-04-17 | v2.1 — STRENGTHENED; Triple+ BAIT; Initiate / Add-Hold |
| [DASH](tickers/DASH/DASH.md) | DoorDash | Narrow | Medium | 2026-04-17 | v2.1 — Double BAIT (all Moderate); Watch / Hold; entry $140-155 |
| [PG](tickers/PG/PG.md) | Procter & Gamble | Wide (under pressure) | Medium | 2026-04-17 | v2.1 — Q3 FY26 earnings Apr 24 = binary; Watch / Hold pre-print |

---

## Ticker Summary

| Ticker | Price (4/17/26) | vs. 52-wk High | vs. 52-wk Low | BAIT | Recommendation (non-holder / holder) |
|--------|----------------|---------------|--------------|------|--------------------------------------|
| BKNG | $180.25 | –22.8% (post-split) | +19.7% | Triple (B+A-Strong) | Initiate / Hold-Add |
| LLY | $883.96 | –22.0% | +41.7% | Triple (A+I-Strong) | Initiate measured / Hold-Add on pullback |
| WING | $189.37 | –51.2% | +33.1% | Triple (lower conviction) | Watch / Hold pre-Q1 SSS |
| UNH | $354.92 | –16.4% | +51.3% | Quadruple (B+A+I-Strong, T-Mod) | Watch / Hold-Add (selective $300-340) |
| SCHW | $88.50 | –17.7% | +11.6% | Triple (B+A+I-Strong) | **Initiate** / **Add** (post-beat new 52-wk low) |
| RKT | $15.60 | –35.9% | +40.8% | Double (B+A) | Initiate Spec. / Hold-Add on weakness |
| SHOP | $125.83 | –30.9% | +42.8% | Triple+ (B+A-Strong+I+T-Mod) | Initiate / Add-Hold |
| DASH | $176.78 | –38.1% | +23.4% | Double (B+A+I-Mod) | Watch / Hold (entry $140-155) |
| PG | $148.18 | –13.3% | +7.7% | Weak | Watch / Hold pre-Q3 FY26 (Apr 24) |

---

## Frameworks

| Framework | Description | File |
|-----------|-------------|------|
| BAIT | Mauboussin Behavioral/Analytical/Informational/Technical | [frameworks/bait.md](frameworks/bait.md) |
| Moneyball | Probability-weighted scenario scoring | [frameworks/moneyball.md](frameworks/moneyball.md) |
| Asset Types | Valuation approaches by business model | [frameworks/asset-types.md](frameworks/asset-types.md) |

*(Position Sizing framework retired in v2 — wiki is position-agnostic per Core Rule #3.)*

---

## Other Pages

| Page | Description |
|------|-------------|
| [watchlist.md](watchlist.md) | Cross-ticker attractiveness ranking (no allocation; v2.1) |
| [log.md](log.md) | Append-only event log |

---

## Pending Data Gaps (flag for next session)

| Ticker | Gap | Source Needed |
|--------|-----|--------------|
| LLY | FCF, operating cash flow, capex from 10-K | SEC EDGAR / investor.lilly.com |
| LLY | Precise drug revenue breakdown FY2025 full year | LLY 10-K or Q4 press release |
| LLY | Geographic revenue by region (exact %) | LLY 10-K segment note |
| WING | FCF, operating cash flow from 10-K | SEC EDGAR / ir.wingstop.com |
| WING | Quarterly SSS trend by quarter within FY2025 | WING 10-K or quarterly releases |
| UNH | Full balance sheet: debt structure, dividend coverage | UNH 10-K |
| UNH | 2026 formal guidance (not yet provided as of Jan 2026) | UNH next earnings release |
| SCHW | Insider activity (last 90 days) | OpenInsider / SEC Form 4 |
| SCHW | Tangible book value per share (for P/TBV calculation) | SCHW balance sheet |
| RKT | Short interest % of float | Fintel / aggregator |
| RKT | Insider activity (last 90 days) | OpenInsider / SEC Form 4 |
| RKT | Full FY2025 adj revenue (post-acquisition, full year) | RKT 10-K |
| RKT | Segment revenue breakdown (origination vs. servicing vs. Redfin) | Q4 2025 earnings supplement |
| RKT | FCF / operating cash flow (GAAP) | RKT 10-K |

---

*Last full index refresh: 2026-04-17 (v2.1 schema migration — all 9 tickers consolidated to single-page format)*
