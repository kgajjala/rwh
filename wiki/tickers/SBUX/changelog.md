# SBUX — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit + Boyu JV Close + FY25/Q1 FY26 Refresh

**Trigger**: v2.9 schema retrofit (13-section structure, retired old §1 + merged §3/§4 into new §2). Material thesis events captured in window since v2.5 (2026-04-24): the **Starbucks-Boyu Capital China JV closed early April 2026** ($13B EV total; Boyu 60% / SBUX 40%; ~8K stores transition to licensed model), and the **FY2025 10-K (filed Nov 14, 2025) + Q4 FY2025 print (first global comp growth in 7 quarters, +1%)** had not been fully integrated into the prior page.

**Sources reviewed**:
- [SBUX FY2025 10-K — SEC EDGAR HTML, filed Nov 14 2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm) + [PDF mirror](https://s203.q4cdn.com/326826266/files/doc_financials/2025/q4/SBUX-9-28-2025-10-K-FINAL.pdf)
- [Q1 FY2026 release, Jan 28 2026](https://investor.starbucks.com/news/financial-releases/news-details/2026/Starbucks-Reports-Q1-Fiscal-Year-2026-Results/default.aspx)
- [Q4 FY2025 release, Oct 29 2025](https://investor.starbucks.com/news/financial-releases/news-details/2025/Starbucks-Reports-Q4-and-Full-Fiscal-Year-2025-Results/default.aspx) + [Q4 FY25 transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2025/10/29/starbucks-sbux-q4-2025-earnings-call-transcript/)
- [Boyu JV close press release, Apr 2026](https://about.starbucks.com/press/2026/starbucks-and-boyu-capital-finalize-joint-venture-to-accelerate-long-term-growth-in-china/)
- [Jefferies upgrade note, Apr 13 2026](https://247wallst.com/investing/2026/04/13/jefferies-upgrades-starbucks-to-hold-as-china-franchise-exit-and-u-s-stabilization-improve-visibility/) and [JPMorgan note, Apr 24 2026](https://www.dailypolitical.com/2026/04/24/jpmorgan-chase-co-forecasts-strong-price-appreciation-for-starbucks-nasdaqsbux-stock.html)
- Live price verified at $98.67 via [stockanalysis.com](https://stockanalysis.com/stocks/sbux/) (Yahoo Finance fetch failed — page error; cross-confirmed via stockanalysis + MarketBeat)

### What Changed
- **Schema migration to v2.9**: 13-section structure. Retired old §1 (Why Exist + Pivotal Question) — both moved to header subsections. Merged old §3 (Geographic Mix) + §4 (Revenue Mix) into new §2. Retired standalone Moat Assessment block (now in §3 only per Rule #23). Re-numbered Sections 5–15 → 5–13.
- **§3 Competitive Moat & Landscape**: Added required Competitive Landscape subsection (Rule #24) — named MCD, DNUT, Tim Hortons, Luckin, Cotti, Costa, Blue Bottle, Keurig with market share + how-SBUX-differs framing.
- **§6 Key Risks**: Materiality-filtered per Rule #25 — dropped boilerplate, added "Priced In?" column, flagged GLP-1 demand risk and Niccol-key-person risk as "not priced in." Replaced multi-row 5-Year Risk Factor Evolution table with synthesis paragraph (Rule #21).
- **Niccol RMC subsection**: Confirmed Pattern C letter status (no standalone shareholder letter; commentary lives in proxy intro + 10-K front-matter + earnings calls). Multi-year strategic-framework arc table added with Niccol-era milestones from Sept 2024 → April 2026.
- **§1 Primary Source 10-K Segment Detail**: FY25 segment-level MD&A synthesis added (NA margin compression as Niccol "tax", International incl. China dynamics, Channel Development as ~45–50% margin annuity, restructuring charge framing).
- **§9 Catalyst & Sentiment Tracker**: Refreshed with Boyu close, Jefferies/JPM analyst actions, FY25 10-K filing, Q4 FY25 + Q1 FY26 results, restructuring announcement.
- **§11/§12 scenarios + R/R**: Bull/Base/Bear refreshed (Bull $150, Base $118, Bear $72 / 30/50/20%) reflecting Boyu JV royalty optionality. PW EV $118 vs spot $98.67 = +20% / ~6%/yr; R/R ~1.9:1 (Bull/Bear midpoints) per Rule #26.
- **§13 Bottom Line + thesis-break triggers**: Added Boyu transition-friction trigger; preserved core Q2/Q3 transaction triggers.
- **Summary section**: Refreshed with Boyu close as 🟢 thesis-strengthening event; updated R/R to 2.4:1 framing; thesis verb softened from prior "Watch" toward "Watch / Initiate-on-dip" given improved floor.
- **Key Stats Snapshot**: Updated price/52-wk/market cap/dividend/store count (40,990 with Sept 2025 restructuring); added Boyu JV close line.

### Thesis Status
- **Overall**: 🟢 **Strengthened** vs. prior v2.5. Two consecutive quarters of inflection delivered (Q4 FY25 first global comp +1% in 7Q; Q1 FY26 first U.S. transactions +3% in 8Q) plus Boyu JV close ($13B EV at premium to retained-business multiples) materially de-risked the China overhang. Margin recovery half of thesis still un-validated.
- **BAIT delta**: A lens slightly more positive (Boyu royalty optionality not in consensus models); B/I/T unchanged. Net: still single-overlap, conviction now Low-to-Moderate (was Low).
- **Price target delta**: Bull $145 → $150; Base $115 → $118; Bear $70 → $72. PW EV $115 → $118.
- **Catalyst & Sentiment delta**: Boyu close (Apr 2026) was the single largest sentiment-positive event; Jefferies upgrade and JPM constructive note followed.

### Recommendation
- **For a non-holder**: 🟡 Watch / Initiate-on-dip — still do not initiate ahead of Apr 28 print; better risk/reward at $85–92 entry zone. Boyu close has improved the floor.
- **For a current holder**: 🟡 Hold — China overhang is now resolved; do not exit. Add only on Q2 transaction confirmation + dip into entry zone.

**Next review trigger**: Q2 FY2026 earnings — April 28, 2026 (post-close). Key items: (1) U.S. comparable transactions ≥0%, (2) global comp vs. 3%+ guide, (3) op margin direction, (4) Boyu JV royalty / 40% stake first commentary, (5) FY26 EPS guide reaffirmation.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added SBUX to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Starbucks Q1 FY2026 press release and earnings call transcript (2026-01-28, IR / Motley Fool)
- Starbucks Q2 FY2026 earnings previews (Motley Fool 2026-04-22, IBTimes 2026-04, Seeking Alpha 2026-04, TIKR)
- Yahoo Finance JSON API live price (2026-04-24)
- Analyst consensus aggregators (TipRanks, MarketBeat, stockanalysis.com)

### What Changed
- Initial compilation; no prior wiki content for this ticker.
- Live price verified at $98.67 (Yahoo Finance, April 24, 2026).
- Q1 FY2026 (Dec 28, 2025) printed first U.S. transaction growth (+3%) in eight quarters — Niccol turnaround inflection.
- FY26 guide: 3%+ comp growth, $2.15–2.40 Non-GAAP EPS, slight op margin improvement.
- Stock trading near 52-wk highs ($104.82) at –5.9% off; +30.7% above 52-wk low ($75.50).
- Q2 FY2026 earnings April 28, 2026 (post-close) is the immediate binary catalyst.
- 3-year PW EV ~$115 vs. spot $98.67 = +17% return (modest positive, event-binary).

### Thesis Status
- **Overall**: Initiated — Watch (non-holder) / Hold (holder)
- **BAIT signal**: Single-overlap (A only Moderate); Conviction Low
- **PW EV**: $115 vs. spot $98.67 (+17% over 3 years, ~5%/yr + ~2.4% dividend)

### Recommendation
- **For a non-holder**: Watch — do not initiate ahead of April 28 print; better to underwrite at post-print price. Attractive entry $85–92.
- **For a current holder**: Hold — print is binary; do not add or exit ahead of April 28.

**Next review trigger**: Q2 FY2026 earnings on April 28, 2026 (post-close). Key item: U.S. comparable transactions (must be ≥0% to validate Q1 inflection).
