# DIS — Changelog

Append-only. Most recent entry first.

---

## 2026-07-01 — v3 Initial Ingest

**Trigger**: User requested a first-run wiki ingest ("run an update for DIS stock"); no prior DIS page, raw/ folder, or wiki reference existed. Workflow A per CLAUDE.md. Timing is material — this ingest lands ~3.5 months after Josh D'Amaro became Disney's CEO (March 18, 2026, succeeding Bob Iger) and captures the first full earnings cycle of the new leadership era.

**Sources reviewed**: Live price via WebSearch aggregation (direct Yahoo/CNBC/Google Finance click-through 403'd this session — [Rule #7] verified via two independent WebSearch passes instead); [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/0001744489/000174448925000155/dis-20250927.htm) and FY2021–FY2024 10-Ks (search-extracted, direct SEC EDGAR fetch blocked by session egress policy); [2026 DEF 14A proxy](https://investors.thewaltdisneycompany.com/files/doc_financials/2025/ar/2026-Proxy-Statement.pdf); Q3 FY2025 through Q2 FY2026 earnings releases/transcripts (4 quarters); FY2023–FY2025 shareholder/Chairman letters (Pattern C — embedded in the DEF 14A, not a standalone letter); Disney Experiences capex-plan and ESPN DTC strategic research; MarketBeat/Fintel/StockTitan for analyst consensus, short interest, and insider Form 4 filings. Built from a 4-agent parallel research fan-out (SEC filings / transcripts+press releases / shareholder letters+strategy / live market data), per CLAUDE.md's Workflow A fetch-phase parallelization pattern.

### What Changed
- **New page** — v3.0 initial ingest; no prior state.
- **Live price**: $98.84 (July 1, 2026); 52-wk range $92.18–$124.61 (~21st percentile, −21% from high).
- **CEO succession resolved**: **Josh D'Amaro** became Disney's ninth CEO effective March 18, 2026, succeeding Bob Iger (now Senior Advisor + board director through Dec 31, 2026). Dana Walden named President & Chief Creative Officer. James Gorman is Board Chairman (since Jan 2026).
- **FY2025 (record)**: revenue $94.4B (+3%), total segment operating income $17.6B (+12%), adjusted EPS $5.93 (+19%, ~19% 3-yr CAGR). Experiences segment operating income $10.0B (record).
- **Streaming turnaround compounding**: Disney+/Hulu operating income +72% YoY (Q1 FY26) then +88% YoY (Q2 FY26) on fall-2025 price increases, tracking the 10% FY26 SVOD-margin target — from a ~$4B FY2022 DTC loss.
- **Disclosure change**: Disney stopped reporting Disney+/Hulu/ESPN+ subscriber counts and ARPU after Q3 FY2025 (Q4 FY25 was the last full disclosure: 196M combined Disney+/Hulu subs). Investors now track streaming via revenue/margin only.
- **ESPN DTC app** launched August 21, 2025 ($29.99/mo Unlimited tier, ~80% of signups via Disney+/Hulu bundle); NFL Network/RedZone acquired from the NFL (closed Jan 31, 2026) for a 10% NFL equity stake in ESPN. Sports segment operating income declining (Q1 FY26 −23% incl. a $110M YouTube TV blackout hit; Q2 −5%; Q3 FY26 guided −14% YoY) on a sports-rights cost step-up (NBA ~$2.6B/yr from FY2026).
- **Capital allocation**: dividend raised to $1.50/yr (from $1.00, declared Nov 2025); FY26 buyback target raised $7B→$8B (at the May 2026 Q2 print); net debt/EBITDA fell to 1.9× — lowest since 2018 (pre-Fox). **Outsider grade: Steward (not Outsider)** — programmatic capital discipline, genuine deleveraging, but not Thorndike-style opportunistic-cheap-stock buying.
- **Strategic**: ~$60B, ~10-year Experiences capex plan (record $6.43B FY25 Experiences capex, +75.7% YoY); Disney Cruise Line fleet expansion (Destiny, Adventure, Believe; target 13 ships by 2031); Abu Dhabi 7th resort announced (Miral-funded licensing model, early 2030s); Hulu fully bought out (100% Disney-owned since July 24, 2025, ~$9B total); India Star business in the JioStar JV (Disney 36.84% minority stake); Venu Sports JV confirmed dead (Jan 2025).
- **Key risk newly surfaced**: **FCC/ABC broadcast-license dispute** — a March-2025 DEI investigation led the FCC to order early renewal of 8 ABC station licenses (April 2026); Disney filed "under protest" in May 2026, calling it unconstitutional First Amendment retaliation. Unresolved, escalating, no clean precedent — flagged as the top thesis-relevant regulatory risk.
- **Scenarios built**: Bull $210 (25%) / Base $150 (50%) / Bear $75 (25%); PW EV $146; R/R ~4.7:1. Entry (20% MoS) ≈ $117 → spot ($98.84) already sits below the entry threshold.
- **Raw data gaps**: SEC EDGAR / Disney IR / most third-party mirrors returned HTTP 403 on automated fetch this entire session (session-wide egress policy denial, not source-specific) — all figures cross-verified via WebSearch extraction with individual citations, none fabricated. Notable unresolved gaps: verbatim FY2024-vs-FY2025 Item 1A risk-factor diff; full FY2025 Sports segment operating income (secondary-sourced only); FY2021–FY2022 shareholder letters (Chapek-era, not retrieved); exact GAAP-vs-adjusted EPS reconciling items for Q2 FY2026 and full-year FY2025; ESPN DTC app subscriber count (never disclosed by management); complete FY2021–FY2023 segment-level breakdown on the current 3-segment basis.

### Thesis Status
- **Overall**: Initiated at Strengthened-leaning — clean CEO transition, compounding streaming profitability, and record Experiences earnings sit underneath a stock priced like legacy media, gated on the FCC/ABC dispute and sports-rights cost inflation resolving without lasting damage.
- **BAIT delta**: New — Double-to-triple overlap (A-Strong; B-Moderate/Strong; I-Moderate). Not a deep-value contrarian setup, but a plausible sector-sentiment mispricing.
- **Price target delta**: New — Bull $210 / Base $150 / Bear $75; PW EV $146.
- **Catalyst & Sentiment delta**: New — Strong Buy consensus (~26 Buy/4 Hold/1 Sell, avg PT ~$134); short interest low (~1–1.5% of float); no insider red flags (all recent Form 4 activity is routine compensation, not open-market selling); post-Q2-print analyst PT-raise cluster (JPMorgan/MoffettNathanson/Guggenheim).

### Recommendation
- **For a non-holder**: 🟢 Initiate — spot already sits below the ~$117 20%-MoS entry line on PW EV $146.
- **For a current holder**: 🟡 Hold-Add — thesis strengthened on the Q2 FY26 beat and clean D'Amaro handoff; add on further weakness toward $75–90.

**Next review trigger**: Q3 FY2026 earnings (~Aug 12, 2026 est.) — tests the guided ~14% YoY ESPN operating-income decline and whether domestic park attendance improves sequentially as management guided.
