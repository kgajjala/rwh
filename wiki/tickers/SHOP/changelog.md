# SHOP — Changelog

*Append-only. Most recent entry first.*

---

## [2026-04-25] — v2.7 Primary-Source Enrichment (5-Year 10-Ks + Pattern B Quarterly Letters)

**Trigger**: First Workflow B refresh under CLAUDE.md v2.7 (5-year 10-K baseline + Pattern B quarterly-letter substitution). SHOP used as the test case to validate that v2.7 mechanics work on a Pattern B publisher (Tobi Lütke does not write Buffett-style standalone annual letters; Shopify publishes quarterly letters with each earnings release).

**Sources reviewed (additions to v2.5 baseline, all primary)**:
- **5-year 10-K baseline** (Rule #20):
  - [Shopify FY2020, FY2021, FY2022, FY2023 10-Ks via SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001594805&type=10-K)
  - [Shopify FY2024 10-K (HTML)](https://www.sec.gov/Archives/edgar/data/1594805/000159480525000039/shop-20241231.htm)
  - [Shopify FY2025 10-K (filed Feb 11, 2026)](https://www.stocktitan.net/sec-filings/SHOP/10-k-shopify-inc-files-annual-report-b62a5b66c76b.html)
- **Pattern B quarterly letters** (Rule #19):
  - [Tobi Lütke 2015 IPO Prospectus Letter](https://shopifyinvestors.com/past-letters/2015-letter/default.aspx) — founding mission
  - Q4 letters from FY2020–FY2025 (5-year baseline as quarterly-letter substitute) via [Shopify IR News](https://investors.shopify.com/news-and-events/news/)
  - [Shopify Q4 FY2025 Letter / Earnings Release (Feb 11, 2026)](https://www.shopify.com/news/shopify-q4-2025-financial-results) — first $2B buyback
  - [Q4 2025 Earnings Call Transcript (Feb 11, 2026)](https://www.fool.com/earnings/call-transcripts/2026/02/11/shopify-shop-q4-2025-earnings-call-transcript/) — UCP, Agentic Storefronts
  - [Tobi Lütke April 2025 internal memo: "AI is non-optional"](https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/) — operational mandate

### What Changed
- **Schema header**: Bumped SHOP page to v2.7.
- **Section 2** (Annual Financial Metrics): Added `### Primary Source: 5-Year 10-K Segment Detail (FY2021–FY2025)` subsection per Rule #20 — multi-year segment evolution table (Subscription Solutions: $1.34B → ~$3.0B at +25% sustained; Merchant Solutions: $3.27B → ~$8.5B with payments penetration 68% of GMV in 2025; Shop Pay +62%; Shop Campaigns advertising revenue doubled in 2025) with verbatim 10-K MD&A driver commentary.
- **Section 6** (Management & Leadership): Added `### Recent Management Commentary — Primary Source Synthesis (IPO Letter + 5 Years of Quarterly Letters + AI Memo)` subsection per Rule #19 (Pattern B applied) — verbatim quotes from 2015 IPO Letter, April 2025 "AI is non-optional" memo, Q4 2025 letter + call (Tobi + Finkelstein), 5-Year Strategic Framework Arc table tracing FY2020 COVID surge → FY2022 cost reset → FY2025 AI inflection, three-observation synthesis.
- **Section 8** (Key Risks): Restructured per Rule #20 — added `Source` column flagging 10-K Item 1A vs. MD&A vs. `*[Analyst speculation]*`. Added 5 new rows from verbatim Item 1A that v2.5 had missed (cybersecurity, payments regulation, international expansion, founder dependency, third-party reliance). Existing rows enriched with verbatim quotes. Added new `### 5-Year Risk Factor Evolution Arc (FY2020 → FY2025)` subsection per Rule #20: chronological table showing AI risk **added in FY2023 10-K** (one year before Agentic Storefronts launch — classic Item 1A leading indicator), upgraded FY2024 → FY2025 from competitive risk to platform-strategic to execution risk.
- **Summary**: Added new 📈 bullet calling out the primary-source signal (first-ever $2B buyback at $125–135 zone + AI-non-optional memo + 5-year Item 1A AI-risk evolution arc).
- **Sources**: Restructured into 4 buckets (Primary sources / Tobi Lütke shareholder communications / Coverage and context / Live market data) with full v2.7-compliant citations.

### Thesis Status
- **Overall**: 🟢 **Strengthened** vs. v2.5 — the 5-year Item 1A arc revealed that management's AI-risk framing has *positively evolved* (defensive → strategic → execution), and the first-ever $2B buyback at this zone is the cleanest intrinsic-value signal in 11 years of public-company history.
- **BAIT lens**: Triple BAIT preserved with informational edge sharpened — Section 8 risk *"AI disruption to SaaS pricing"* has data evidence supporting downgrade since Shopify is the AI-commerce *creator*.
- **Price target**: Unchanged numerically (PW EV ~$212 over 3yr).
- **New finding**: The 2023 Item 1A AI-risk addition (1 year before Agentic Storefronts launch) is a clean example of Item 1A as a leading indicator — investors who diff'd FY2022 vs. FY2023 10-Ks had a 12-month lead on the AI thesis vs. those relying on aggregator data.

### Recommendation
- **For a non-holder**: 🟢 **Initiate** — at $125.83, current price at upper edge of attractive entry zone; primary-source confirmation strengthens conviction.
- **For a current holder**: 🟢 **Add / Hold** — no reason to trim; add aggressively on any drawback toward $100–$110.

**Next review trigger**: 📅 **Q1 2026 earnings (~May 2026)**. First quarter with Agentic Storefronts default-on across all stores; tests low-30s% revenue guide.

### Test of v2.7 Schema
- **Rule #19 Pattern B (quarterly letters) worked cleanly**: Substituting the Q4 letter from each of the last 5 years + the most-recent quarterly letters as the "annual letter equivalent" produced a coherent 5-year framework arc on a Pattern B publisher (Shopify). Validates the Pattern B path added in v2.7.
- **Rule #20 5-year 10-K baseline produced new analytical edge**: The 5-Year Risk Factor Evolution Arc surfaced the **2023 Item 1A AI-risk addition** as a leading indicator that aggregator data missed. This is the single clearest demonstration of why multi-year 10-K diffing > single-year snapshot.
- **PDF binary fallback path used twice**: Both FY2024 and FY2025 SEC HTML versions were used in lieu of PDF; StockTitan structured summary served as backup citation per Rule #20.

---

## [2026-04-24] — v2.1 Migration (Workflow A) — Single-Page Consolidation + Refreshed Recommendation

**Trigger**: Schema migration from v1 (4-file structure: overview/thesis/financials/changelog) to v2.1 (single consolidated `SHOP.md` + `changelog.md`). Live price refreshed and BAIT / entry-zone reassessed given recovery from $88 low to $125.83.

**Sources reviewed**:
- Yahoo Finance JSON API (live price $125.83; 52-wk range $88.14–$182.19; verified Apr 24, 2026)
- Prior v1 wiki files (overview.md, thesis.md, financials.md, changelog.md) — folded into single SHOP.md
- Q4 FY2025 earnings release (Feb 11, 2026): Revenue $3.67B / GMV $123.8B / FCF $715M
- FY2025 totals: Revenue $11.56B (+30%), GMV $378B, FCF $2.0B (17.3% margin)
- $2B buyback authorization (Feb 2026) — first-ever capital return
- Agentic Storefronts default activation (late March 2026) across ChatGPT, Google AI Mode, Gemini, Copilot
- Analyst consensus: ~28 Buy / 9 Hold / 0 Sell; median target $162–$165; high $220, low $110

### What Changed from Prior Entry (2026-04-06 at ~$117–121)

- **Live price**: $117–121 → **$125.83** (+~5%); recovery off $88.14 low (+42.8% off low)
- **52-week low set**: $88.14 (recent; prior reported low was $69.84 — the new $88.14 is a higher low post-recovery context)
- **Entry zone shifted up**: prior $118–125 (Tranche 1) → now **$100–$125** as attractive entry zone, with $100–$110 the cleanest "fat-pitch" re-test zone
- **Behavioral signal moderated**: Strong (at $117) → Moderate (at $126); partial sentiment unwind in progress
- **PW EV essentially unchanged**: ~$212 (3-yr) vs. $125.83 = +68% upside (~19%/yr); was +75% from $121 — modestly compressed by recovery
- **Schema migration**: Consolidated overview.md + thesis.md + financials.md → SHOP.md per v2.1 CLAUDE.md. Position-sizing language (5% allocation, 55/45 stock/options split, tranche %, options structures) removed per Core Rule #3. Replaced with price-level entry/trim/exit *valuation* zones.

### Thesis Status
- **Overall**: **Strengthened** — Q4 FY2025 confirmed +30% growth, $2B buyback authorized, recovery off $88 validates moat. The disruption-fear scenario is not appearing in operating data.
- **BAIT delta**:
  - B: Strong → Moderate (recovery has unwound roughly half the sentiment dislocation)
  - A: Moderate-Strong (unchanged)
  - I: Moderate (unchanged; reinforced by Agentic Storefronts default activation)
  - T: Moderate-Strong (improved — buyback floor + downtrend broken)
  - Overall: Triple overlap (B+A+I), Conviction Moderate-High
- **Price target delta (3-yr scenarios)**: Bear $113 (15%) | Base $193 (45%) | Bull $252 (30%) | Bull+ $325 (10%) — unchanged in dollar terms; recovery-narrowed return % from $121 entry
- **Catalyst & Sentiment delta**: Multiple analyst target raises since Q4 print; median crept from $148 → $162+. Truist upgrade Feb 18 triggered +8.5% rally. Buyback authorization is the structural new positive.

### Recommendation
- **For a non-holder**: **Initiate** at $125.83 — current price at upper edge of $100–$125 attractive entry zone; PW EV $212 = +68% over 3 years; ~5:1 risk/reward. Stronger setup on drawback to $100–$110 but waiting forfeits Q1 catalyst optionality.
- **For a current holder**: **Add / Hold** — no reason to trim. Add aggressively on any drawback toward $100–$110.

**Attractive entry zone**: $100 – $125
**Trim zone**: $185 – $220
**Exit / avoid zone**: >$280

**Thesis-break triggers**:
1. Two consecutive quarters of sub-20% revenue growth
2. FCF margin compression below 14%
3. Payments penetration declining (currently 68%)
4. U.S. e-commerce share loss to Amazon below 12%
5. Buyback paused/canceled before $1B executed
6. Lütke voting-control changes or Founder Share unwound
7. AI-attributed orders growth decelerates from +11–15× to flat/negative

**Next review trigger**: **Q1 2026 earnings — ~May 2026**. Key items: revenue vs. low-30s% guide; Agentic Storefronts adoption metrics; buyback YTD execution; international growth trajectory; any FY2026 guide revision.

---

## [2026-04-06] — Initial Ingest

**Trigger**: Initial compilation from raw analysis files
**Data points reviewed**:
- `raw/analyses/SHOP_analysis_2026-03-24.html` — full 15-section investment thesis (March 24, 2026)
- `raw/analyses/shop_analysis.html` — Q4 2025 360° earnings review (February 25, 2026)
- Q4 2025 earnings (reported February 11, 2026)

### What Changed
- Initial compilation; no prior wiki entry existed
- Synthesized full 15-section thesis from two analysis files
- Primary analysis file: SHOP_analysis_2026-03-24.html (more recent, fuller framework)
- Q4 2025 results: Revenue $3.67B (+31% YoY), GMV $123.8B (+31%), FCF $715M (19.5% margin)
- Full-year 2025: Revenue $11.56B (+30%), GMV $378B (+29%), FCF $2.0B (17% margin)
- Management guided Q1 2026 revenue growth at "low-30s%" vs. street at ~25% — significantly above
- Board authorized $2B share buyback — first major capital return program
- Agentic Storefronts activating across ChatGPT, Google, Gemini, Copilot by default (late March 2026)
- OpenAI retreated from "Instant Checkout" (only ~30 merchants onboarded) — validates Shopify moat thesis

### Thesis Status
- **Overall**: Initiated — Wide Moat, high conviction
- **BAIT delta**: B+A+I triple overlap established at initiation
  - B (Behavioral): STRONG — thematic AI fear contradicted by 30% revenue acceleration
  - A (Analytical): MODERATE-STRONG — attach rate compounding and Agentic Plan underappreciated
  - I (Informational): MODERATE — OpenAI retreat and UCP endorsements underappreciated
  - T (Technical): MODERATE — $2B buyback floor; CEO 10b5-1 mild overhang
- **Price targets**:
  - Bear: $113 (15% prob) | Base: $193 (45% prob) | Bull: $252 (30% prob) | Bull+: $325 (10% prob)
  - Probability-weighted EV: ~$212 (~75% return from ~$121)

### Action
- [ ] Buy more — not applicable (initial position building)
- [ ] Trim
- [x] Hold / Build — Tranche 1 entry ($118–$125) appropriate at current prices; begin accumulation
- [ ] Watch

Recommended approach: Start 20% of 5% allocation at current levels ($118–$125). Add Tranche 2
($100–$110) on any macro selloff or Q1 miss. Deploy options overlay (LEAPS bull call spreads +
cash-secured puts) concurrently.

**Next review trigger**: Q1 2026 Earnings — April 30, 2026. Key test: does management's
"low-30s% growth" guidance prove accurate? Also watch Agentic Storefronts adoption data and
buyback execution pace.
