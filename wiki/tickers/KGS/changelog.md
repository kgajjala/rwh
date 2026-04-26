# KGS — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: Schema upgrade from v2.5 (15-section) to v2.9 (13-section). No new earnings event — this is a structural and primary-source enrichment pass.

**Sources reviewed**:
- [KGS 10-K FY2025](../../../raw/KGS/filings/KGS-10K-FY2025.htm) (SEC EDGAR CIK 0001767042, filed Feb 2026)
- [KGS 10-K FY2024](../../../raw/KGS/filings/KGS-10K-FY2024.htm) (SEC EDGAR, filed Feb 2025)
- [KGS 10-K FY2023](../../../raw/KGS/filings/KGS-10K-FY2023.htm) (SEC EDGAR, filed Feb 2024)
- [FY2025 Proxy DEF 14A](../../../raw/KGS/shareholder-letters/2025_proxy_DEF14A.htm) (SEC EDGAR, filed Mar 27, 2026 — contains first-ever CEO letter from Mickey McKee)
- [FY2024 Proxy DEF 14A](../../../raw/KGS/shareholder-letters/2024_proxy_DEF14A.htm) (SEC EDGAR — governance-only, no CEO letter)
- [FY2023 Proxy DEF 14A](../../../raw/KGS/shareholder-letters/2023_proxy_DEF14A.htm) (SEC EDGAR — governance-only, no CEO letter)
- [stockanalysis.com KGS](https://stockanalysis.com/stocks/kgs/) — live price ($65.98 as of Apr 24, 2026), financials, analyst consensus
- [Fintel short interest](https://fintel.io/ss/us/kgs) — 6.49% of float, 6.41 days-to-cover
- [OpenInsider KGS](https://openinsider.com/kgs) — insider activity
- AROC and USAC peer data for Competitive Landscape (§3)

### What Changed
- **Schema**: Restructured from 15 sections (v2.5) to 13 sections (v2.9). Retired old §1 (Why Exist + Pivotal Q — now in Business Overview header); merged old §3 (Geographic Revenue Mix) + §4 (Revenue Mix) into new §2. Renumbered old §5–§15 as new §3–§13.
- **§1 Annual Financial Metrics**: Added Adj EBITDA reconciliation table from FY2025 10-K ($715.0M vs. $81.6M GAAP net income); added quarterly trajectory table (Q1–Q4 2025); added 10-K Segment Detail subsection with MD&A-derived drivers; added debt structure table. Corrected utilization from "~98%" to 97.7% (FY2025 10-K actual).
- **§2 Revenue Mix & Geographic Split**: Added unit economics table; added geographic split from 10-K (82.8% Permian + Eagle Ford); added revenue mix evolution table (FY2022→FY2025); documented Kodiak Power Solutions as distinct revenue stream.
- **§3 Competitive Moat & Landscape**: Added mandatory Competitive Landscape subsection (new v2.9 requirement). Named peers AROC and USAC with HP, utilization, revenue, EBITDA, EV/EBITDA, dividend. Key finding: both AROC and USAC entered distributed power in 2025–2026, reducing KGS's first-mover window for Kodiak Power Solutions.
- **§4 Management & Leadership**: Added Pattern C RMC subsection with 6 verbatim quotes from Mickey McKee's first-ever CEO letter (FY2025 proxy). Documented 3-year management commentary arc (FY2023: IPO cadence; FY2024: governance-only proxy; FY2025: first CEO letter signals maturing public-company posture).
- **§6 Key Risks**: Materiality-filtered per Rule #25 — dropped boilerplate (generic earnings fluctuation, generic cyber, generic key-person). Retained 5 material risks: natural gas / E&P cycle, Kodiak Power Solutions integration risk, leverage + rate sensitivity, tariff exposure, LNG oversupply tail. Marked EQT overhang as ✅ resolved (EQT fully exited Dec 2, 2025). Added 2-sentence Risk Factor Evolution synthesis paragraph replacing prior multi-row table.
- **§8 Valuation**: Added peer comparison table (KGS/AROC/USAC). Updated fair price estimate to $48–62/share ($65.98 above range). Refreshed assessment paragraph.
- **§9 Catalyst & Sentiment Tracker**: Updated analyst consensus to Strong Buy 7/0/0 (was "Moderate Buy 7B/1H/1S"); avg target raised to $57.17, high $69. Added Goldman Sachs PT raise ($60→$69, Apr 20), Bank of America PT raise ($45→$70, Apr 13). Updated live price to $65.98.
- **§10 BAIT Framework**: Updated verdict to Double overlap (A+I Moderate), conviction Low-Moderate.
- **§11 Bull/Bear/Base Cases**: Refreshed with DPS integration upside, refinancing tailwind, and competitor power-gen threat factored in. Bull $95 (30%), Base $75 (50%), Bear $38 (20%).
- **§12 PW EV**: PW EV = $73.60 (vs. $65.98 spot) = ~11.6% total upside over 3 years, ~7%/yr incl. dividend. R/R = 1.04:1 at $65.98 (unfavorable); improves to ~2.9:1 at $50–55 entry zone.
- **§13 Recommendation**: Confirmed Watch (non-holder) / Hold (current holder). Entry zone $50–55. Updated 8 thesis-break triggers including KPS revenue <$50M in first 12 months post-DPS-close and adj EBITDA margin compression below 62%.
- **Summary section**: Refreshed to 10 bullets reflecting v2.9 state.

### Thesis Status
- **Overall**: Unchanged — Quality compounder at fair value; not a bargain at $65.98. Thesis strengthened slightly by DPS acquisition closing, EQT overhang cleared, and analyst consensus upgrade to Strong Buy. Weakened slightly by competitor power-gen entry (AROC, USAC both launched distributed power initiatives) reducing KPS first-mover advantage window.
- **BAIT delta**: Behavioral upgraded from Weak to Moderate (EQT overhang gone, narrative improving). T remains Moderate. Net conviction: Low-Moderate, Double overlap.
- **Price target delta**: Bull $95 | Base $75 | Bear $38 — consistent with prior framing; DPS upside priced into Bull, not Base.
- **Catalyst & Sentiment delta**: Analyst consensus upgraded (7/0/0 Strong Buy). EQT overhang fully resolved. Short interest 6.49%.

### Recommendation
- **For a non-holder**: 🟡 **Watch** — wait for pullback into $50–55 entry zone; current $65.98 above fair-value range, R/R ~1:1 is not asymmetric
- **For a current holder**: 🟡 **Hold** — collect 3.0% dividend + mid-single-digit earnings growth; no urgency to add at the 52-wk high

**Next review trigger**: 📅 Q1 2026 earnings — May 11, 2026 (first print with partial DPS contribution; validate KPS pipeline bookings and updated adj EBITDA guidance)

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added KGS to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Kodiak Gas Services Q4 2025 / FY2025 earnings press release (IR, 2026-02-25)
- Q4 2025 earnings call transcript (Motley Fool, Globe and Mail)
- Yahoo Finance live price + 52-week range (2026-04-24)
- stockanalysis.com price history and forecast page
- MarketBeat analyst consensus (Moderate Buy, 7B/1H/1S, avg target ~$56)
- Goldman Sachs PT raise note ($60 → $69, 2026-04-20)
- Bank of America PT raise ($45 → $70, 2026-04-13)
- J.P. Morgan reiteration (2026-04-16)
- Daily Political coverage of 52-wk high (2026-04-20)
- StockStory pre-Q4 preview piece

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $62.16 (Yahoo Finance / stockanalysis.com cross-check, April 24, 2026)
- Stock at 52-wk high after +83% 6-month run; near-fair-value setup
- DPS acquisition (~$675M) closing early April 2026 — adjacency into AI-data-center power gen

### Thesis Status
- **Overall**: Initiated — Quality compounder at fair value, not a bargain
- **BAIT signal**: Single overlap (A only Moderate); Behavioral and Technical both **Weak**; conviction Low-Moderate
- **PW EV**: ~$72 vs. spot $62.16 (3-yr) → +16% ex-div, ~7–8%/yr incl. dividend

### Recommendation
- **For a non-holder**: **Watch** — wait for pullback into $50–55 entry zone; current setup not asymmetric
- **For a current holder**: **Hold** — collect 3.2% dividend + mid-single-digit growth; no need to add at the high

**Next review trigger**: Q1 2026 earnings (late April / early May 2026) — first print with partial DPS contribution.
