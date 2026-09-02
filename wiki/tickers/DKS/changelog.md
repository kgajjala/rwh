# DKS — Changelog

Append-only. Most recent entry first.

---

## [2026-09-02] — Schema migration v3.0 → v4.0

**Trigger**: Schema v4.0 promoted to [CLAUDE.md](../../../CLAUDE.md); DKS migrated as the in-flight ticker. No new research — same verified facts as the 2026-09-01 ingest, re-synthesized into the v4 page shape.
**Sources**: unchanged from the initial ingest below. Price re-verified per R4 — [Yahoo Finance](https://finance.yahoo.com/quote/DKS/), Sep 2, 11:40 AM EDT.

### Changed
- **Page rebuilt to v4**: 13 sections → 7, with Verdict / The Call / What I'd Have To Be Wrong About as front matter. Prose 3,445 → 1,460 words.
- **Re-marked to $136.79** (from $133.01, +2.8% on the day): 52-wk percentile ~10th → ~13th, from high –45.6% → –44.0%, FY26E P/E 11.6× → ≈12.0×, dividend yield 3.76% → 3.66%, EV $12.96B → $13.30B, EV/DICK'S segment EBIT ≈8.3× → **≈8.5×**.
- **R/R 6.0:1 → 5.2:1** and PW EV upside +53% → +49% — entirely spot-driven on a one-day rally. Scenarios, probabilities and PW EV ($204) are unchanged.

### Status
- **Thesis**: Unchanged — no new information, only a better container and a fresher price.
- **PW EV**: $204 (held) · **R/R**: 6.0:1 → 5.2:1 (spot) · **BAIT**: Triple (B+A+T), held
- **Verbs**: non-holder Initiate (scaled) · holder Hold-Add on weakness

**Next trigger**: Goldman Sachs fireside, 2026-09-14 — a replacement Foot Locker profitability timeline, and any comment on the unused $3.0B authorization. Otherwise Q3 FY2026, ~2026-11-24.

---

## 2026-09-01 — v3 Initial Ingest

**Trigger**: User requested a new ticker be added to the tracking list with full analysis. No prior DKS page existed → Workflow A (first-run ingest) per CLAUDE.md §6.

**Sources reviewed**:
- [Q2 FY2026 press release, Aug 25, 2026](../../../raw/DKS/press-releases/2026-08-25_Q2-FY26_earnings.txt) (stored locally) and its [8-K on EDGAR](https://www.sec.gov/Archives/edgar/data/1089063/000108906326000033/dks-20260824.htm)
- [Q1 FY2026 earnings release, May 27, 2026](https://www.sec.gov/Archives/edgar/data/1089063/000108906326000021/dks-2026502xex991earningsr.htm) — prior guidance baseline for the bridge
- [FY2025 Form 10-K (FYE Jan 31, 2026)](https://www.sec.gov/Archives/edgar/data/1089063/000108906326000007/dks-20260131.htm) — Item 1, Item 1A, segment detail
- [FY2025 Annual Report incl. CEO shareholder letter](../../../raw/DKS/shareholder-letters/2025_letter.txt) (Pattern C)
- [Q1 FY2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1089063/000108906326000027/dks-20260502.htm)
- [Q2 FY2026 earnings call transcript](https://www.fool.com/earnings/call-transcripts/2026/09/01/dicks-sporting-goods-dks-q2-2026-earnings-call-transcript/) + [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-dicks-sporting-goods-q2-2026-results-miss-as-shares-sink-93CH-4875453) (cross-checked, per Rule #18)
- [SEC XBRL company facts, CIK 0001089063](https://data.sec.gov/api/xbrl/companyfacts/CIK0001089063.json) — 5-year financial series pulled directly, not from summaries
- Four Form 4 filings parsed from raw EDGAR XML (Barrenechea, Eddy, Colombo, Mathrani)
- Live price [Yahoo Finance](https://finance.yahoo.com/quote/DKS/) (verified 12:20 PM EDT); [Fintel](https://fintel.io/ss/us/dks) short interest; [StockAnalysis](https://stockanalysis.com/stocks/dks/) consensus

### What Changed
- **New page** — v3.0 initial ingest; no prior state.
- **Live price**: $133.01 — ≈10th percentile of the 52-wk range ($120.40–$244.38), **–45.6% from high**, +10.5% off the low.
- **The event**: Q2 FY2026 (Aug 25) missed (non-GAAP EPS $3.53 vs. ~$3.76 consensus) and cut FY2026 guidance. Stock fell **30.7% to $124.31 — the worst single day in company history**.
- **Guidance bridge constructed from both primary releases** (the central analytical work of this ingest):
  - Consolidated non-GAAP EPS: $13.50–14.50 → **$11.00–12.00**
  - Consolidated GAAP EPS: $13.27–14.27 → **$10.94–11.94**
  - Foot Locker segment profit: **+$110–150M → $(80)M–$(40)M** (≈–$190M at midpoint)
  - Foot Locker proforma comp: +1.5% to +3.0% → **–2.0% to 0.0%**
  - DICK'S segment profit: $1.60–1.68B → $1.54–1.60B (≈–$70M)
  - DICK'S comp guidance: **+2.5% to +4.0% — unchanged**
  - ⇒ **~73% of the operating-income cut is located in Foot Locker**, a segment that is ~34% of sales and ~0% of profit.
- **Q2 segment results**: DICK'S comp **+4.9%** with gross margin **+79 bps** and ~200 bps of share gain; Foot Locker proforma comp **–3.6%** with a **$31.9M segment loss**. Q1 had been +6.0% / +0.6% with guidance *raised* — a 420 bps Foot Locker swing in one quarter.
- **Acquisition cost restated beyond the headline**: the $2.5B consideration (84% stock, 9.6M shares at ≈$219) understates it. Operating lease liabilities rose from ≈$3.12B (Aug 2025) to **≈$5.88B** (May 2026) — ~$2.8B assumed — plus restructuring charges of $515.8M to date against an expected total of up to **$750M**. ⇒ **≈$6B of committed capital** against a segment now guided to lose money.
- **FCF deterioration identified** (not in the headlines): FY2025 FCF of **$400M was below the $414M dividend**; gross capex quadrupled $308M (FY2021) → $1,137M (FY2025) → guided **$1.6B** for FY2026 while operating income falls. Cash fell to $914M from $1,231M YoY.
- **Vendor concentration**: 10-K discloses **Nike at ~31% of consolidated merchandise purchases** post-acquisition, with no long-term purchase contracts.
- 🟢 **Insider cluster (verified from raw Form 4 XML, all code "P", zero sales)**: four directors bought **≈$3.72M** on Aug 26–27, within 48 hours of the crash — Barrenechea $2.22M (17,000 sh @ $130.72), Colombo $0.79M, Eddy $0.51M, Mathrani $0.20M.
- **Shareholder-letter commitment falsified**: the FY2025 letter (May 2026) stated back-to-school *"is when we expect an inflection point in both sales and profitability for the Foot Locker Business."* It comped –3.6% and lost money instead. Management supplied **no replacement timeline** on the Q2 call. The other half of the letter's promise — Fast Break at ~250 stores by back-to-school — **was delivered and exceeded** (300–350 targeted globally by year-end, and Stack confirmed those stores outperform legacy doors).
- **Scenarios built** (5-yr terminal, FY2031E): Bull $330 (20%) / Base $215 (50%) / Bear $100 (30%); **PW EV $204**; R/R **≈6.0:1**.
- **Outsider grade: Steward (not Outsider)** — pro-cyclical buyback history (largest year FY2021 at COVID peak plus a $5.50 special dividend); H1 FY2026 repurchased just **$141M at a $196.38 average** weeks before the stock hit $124, leaving **$3.0B authorized and unused**; no buyback commentary on the Q2 call. Offsetting: funding 84% of Foot Locker in stock at ≈$219 was a genuinely Outsider-consistent use of expensive currency. Surfaced to §0 per Rule #25 (material capital-allocation event: buyback execution + 12th consecutive dividend raise to $5.00).
- **Data gaps logged**: short-interest readings (9.85% of float, 0.46 days-to-cover) both **pre-date the Aug 25 crash**; first post-event FINRA settlement publishes ~mid-September. Q2 FY2026 10-Q not yet filed at ingest.

### Thesis Status
- **Overall**: New — initiated **constructive**, on a located-not-diffuse guidance cut
- **BAIT**: **Triple (B + A + T)** — Behavioral Strong (record single-day drop), Analytical Strong (sum-of-the-parts available in management's own guidance table and not being done), Technical Moderate-Strong (10th percentile, 9.85% short float, but 0.46 days-to-cover means no squeeze), Informational Moderate (segment guidance is unusually granular; residual edge is that Foot Locker comps stay proforma until Q4 FY2026)
- **Price target**: New — Bull $330 / Base $215 / Bear $100; PW EV $204 (+53%, ≈+8.9%/yr price + ~3.8% dividend ≈ ~12.7%/yr total)
- **Catalyst & Sentiment**: Consensus **Buy**, median target **$166** (26 analysts). Post-print target cuts were uniform but **no rating changes** — JPMorgan $245→$188 (OW), Citi $280→$190 (Buy), UBS $275→$178 (Buy), BNP $169→$99 (Underperform). Multiple plaintiff-firm securities investigations opened (treated as noise absent a filed complaint surviving dismissal).

### Recommendation
- **For a non-holder**: 🟢 **Initiate (scaled)** — spot ~35% below PW EV and well inside the ≤$163 entry zone; scale rather than commit, since Q3 gross-margin pressure is pre-flagged as *"most pronounced"*
- **For a current holder**: 🟡 **Hold-Add on weakness** — nothing in Q2 impaired the DICK'S business; add on price, not on the Foot Locker narrative improving

**Next review trigger**: Goldman Sachs 33rd Annual Global Consumer & Retail Conference fireside, **2026-09-14, 11:30 AM ET** — watch for a replacement Foot Locker profitability timeline and any comment on the unused $3.0B authorization. Otherwise Q3 FY2026 earnings, ~2026-11-24.
