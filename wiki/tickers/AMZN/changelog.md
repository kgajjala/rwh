# AMZN — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-08-19] — Q2 FY2026: Record Operating Quarter Wrapped in a $50.5B Anthropic Mark; FCF Turns Negative; $50B OpenAI Investment Completed — plus v3.0 Schema Migration

**Trigger**: 110-day lookback (2026-05-01 → 2026-08-19). The page had drifted badly out of date — a prior session bumped the header to 2026-08-07 without refreshing any body content, so the analysis, price, market cap, percentile, and catalysts were all still at the 2026-05-01 state with no changelog entry. This pass rebuilds the page on current data and migrates it from the legacy 15-section layout to the **v3.0 13-section schema** (Rule #11, §15 migration discipline).

**Sources reviewed**:
- [Q2 FY2026 results / 8-K (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000024/amzn-20260630xex991.htm)
- [Investing.com — Q2 2026 slides: AWS +37%, FCF turns negative](https://www.investing.com/news/company-news/amazon-q2-2026-slides-aws-surges-37-free-cash-flow-turns-negative-93CH-4826472)
- [Seeking Alpha — Q3 guide $197–202B, 2026 capex lifted to ≈$220B](https://seekingalpha.com/news/4622393-amazon-outlines-q3-net-sales-of-197b-202b-while-lifting-2026-cash-capex-to-about-220b)
- [Investing.com — Q2 2026 earnings call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-amazon-tops-q2-2026-estimates-as-aws-growth-accelerates-93CH-4826442)
- [Amazon — OpenAI strategic partnership](https://www.aboutamazon.com/news/aws/amazon-open-ai-strategic-partnership-investment) · [GeekWire](https://www.geekwire.com/2026/amazon-invests-50b-in-openai-deepens-aws-partnership-with-expanded-100b-cloud-deal/) · [Seeking Alpha — $35B final tranche](https://seekingalpha.com/news/4622936-amazon-completes-openai-investment-with-additional-35b-tranche)
- [Bloomberg Law — FTC trial rescheduled to Feb 9, 2027](https://news.bloomberglaw.com/antitrust/amazon-poised-for-late-2026-trial-in-ftc-monopoly-power-lawsuit)
- [MediaPost — advertising +26%](https://www.mediapost.com/publications/article/416930/amazon-advertising-up-26-in-q2-profits-soar-to.html)
- [stockanalysis.com — analyst forecast](https://stockanalysis.com/stocks/amzn/forecast/) · [Yahoo Finance — AMZN](https://finance.yahoo.com/quote/AMZN/) (live price $264.16)

### Schema Migration (v3.0)

- Retired legacy `Section 1 — Why Does This Company Exist?`; founding insight folded into Business Overview per Rule #11
- Merged old §3 (Geographic Revenue Mix) + §4 (Revenue Mix & Business Model) into **§2 Revenue Mix & Geographic Split**
- Renumbered old §5–§15 → **§3–§13**; old §5 retitled **Competitive Moat & Landscape** (Rule #22)
- Summary rebuilt on the Rule #17 four-part format (thesis + verbs, scenario table, KPI strip, Why/Why-not/Next read)
- Fixed stale internal cross-references to retired section numbers

### What Changed

- **Header**: Last Updated → **2026-08-19**; live price **$264.16** (Aug 19, 3:02 PM EDT), 52-wk range **$196.00–$287.20**
- **§1 (Financials)**: Q2 FY2026 added — revenue **$200.6B (+20%)**, first $200B quarter; operating income **$27.5B (+43%)**; AWS **$42.2B (+37%, fastest in 18 quarters)** with op income **$16.6B (+64%)** at a **39.4% margin**; advertising **$19.8B (+26%)**; NA op income $9.1B (7.9%), International $1.7B (4.1%); **AWS backlog $496B**; AI business and chips business each **>$25B run rate**, triple-digit growth
- **§1 (Earnings quality)** — *the analytical core of this pass*: reported net income **$62.6B** and diluted EPS **$5.75** include a **~$50.5B non-cash Anthropic revaluation** (~$62.8B across six months), roughly **2× the quarter's entire operating profit**, and explicitly removed in the operating-cash-flow reconciliation. Stripping the six-month marks at a ~20% tax assumption takes TTM EPS from $12.43 to **≈$7.82**, moving the trailing multiple from **21.3× to ≈34×**
- **§1 (Cash)**: Q2 capex **$53.1B** → quarterly FCF **–$7.7B**; **TTM FCF –$7.6B** on ~$169B TTM capex — negative for the first time since FY2022. FY2026 capex guide raised **≈$200B → ≈$220B**, partly on *memory-price inflation*. Q3 revenue guide **$197–202B vs. ~$204.1B consensus**
- **§2**: Segment table rebuilt on Q2 actuals — AWS produced **61% of operating income on 21% of revenue**
- **§3 (Moat)**: AWS row updated to the $169B run rate / $496B backlog; advertising row to ~$77B. Added **demand-funding circularity** as a named vulnerability. Tail-risk read inverted — the Azure-share bear case is materially weaker after +37%; the sharper risk is now cyclical AI demand against ~$220B/yr of committed capex
- **§4 (Management)**: **Outsider grade held at Reinvestor with a new caveat** (Rule #25 — material capital-allocation event). The **$50B OpenAI investment** is capital placed into a customer that then committed to $100B+ of AWS purchases — closer to vendor financing than the 2007–2015 AWS build, and it makes reinvestment-IRR claims hard to audit when Amazon books the revenue, holds the equity, and marks the equity. Negative FCF also removes any near-term buyback capacity. Insider section rebuilt: Jassy 10b5-1 sales (Apr 17 / May 4 / May 21), **no discretionary buying by any officer** through the $3T crossing and subsequent 8% fall
- **§5 (Growth)**: **OpenAI partnership** added as the largest new initiative — $50B invested ($15B + a **$35B tranche completed July 2026**), AWS agreement expanded **$100B over 8 years**, **2 GW Trainium** commitment; ≈$17B/yr implied ≈ **11% of AWS 2026 revenue**
- **§6 (Risks)**: Three new material risks, all tagged **not priced in** — *reported earnings quality* (investment marks dominate net income; marks can reverse), *negative FCF against compounding capex*, and *demand-funding circularity* (revenue growth and investment marks would deteriorate together, a correlation the market is not modelling). AWS-share-loss risk lowered **35% → 20%** on the +37% print. FTC row updated for the trial delay
- **§7 (Macro)**: FTC bench trial **moved October 13, 2026 → February 9, 2027**; partial dismissal granted, core monopoly-maintenance claims proceed. Pushes structural-remedy tail risk out of the current review horizon
- **§8 (Valuation)**: Rebuilt at $264.16 / ≈$2.849T. **The two-multiple problem** framed explicitly: 21.3× reported vs. **≈34× clean**, corroborated by consensus FY2027E EPS of **$10.40 sitting below** FY2026E $12.46 — the Street already models the marks rolling off. FY27E P/E ≈25.4×. FCF yield **negative**
- **§9 (Catalyst/Sentiment)**: Full refresh. Market cap **crossed $3T for the first time on August 3, 2026** then retraced 8%; **+15.32% on July 31**, one of the largest single-day gains in company history, *despite* soft Q3 guidance. Consensus **43 Strong Buy / 15 Buy / 2 Hold / 0 Sell** across 60 analysts, median **$325**; Goldman $335→$375 (Aug 10)
- **§10 (BAIT)**: **B downgraded Moderate → Weak** — zero Sell ratings across 60 analysts at a $3T crossing is consensus-long positioning, not a behavioral edge. A held Moderate-Strong, re-grounded on the earnings-quality arithmetic with an explicit falsifier (FCF inflecting positive while AWS holds >30%). Verdict Triple overlap (A+I+T; B Weak), conviction **Moderate**
- **§11/§12 (Scenarios / PW EV)**: **Migrated 3-year FY2029 → 5-year FY2031 terminal** per Rule #24, with scenario EPS restated on an **operating basis** since reported EPS is not a reliable forward anchor. Bull $400→**$550** (40%→25%) | Base $300→**$385** (45%→50%) | Bear $170→**$160** (15%→**25%**). PW EV $322 → **≈$370**; R/R 1.4:1 → **≈2.7:1**. Bear probability raised because negative FCF removes the shock absorber prior bear cases assumed
- **§13 (Recommendation)**: Verbs held **Watch / Hold**. Zones re-derived from PW EV — entry **$230–277** (spot near the top), trim **$370–550**, exit **>$550**. Two new lead thesis-break triggers: **a material downward revaluation of the Anthropic or OpenAI stakes**, and **FCF still negative through FY2027**

### Thesis Status

- **Overall**: 🟡 **Operationally strengthened, financially more complex — net Unchanged.** The operating business had its best quarter in the history of this page: AWS +37% with a $496B contracted backlog, operating income +43%, all three segments profitable. Against that, three things changed the quality of the story rather than its direction — reported earnings are now dominated by non-cash investment marks, free cash flow has gone negative against a raised ~$220B capex guide, and Amazon has become a large shareholder in two of its biggest AI customers. Conviction held at **Moderate**.
- **BAIT delta**: **B Moderate → Weak** (zero Sells across 60 analysts at $3T). A held Moderate-Strong on a re-grounded thesis; I and T held Moderate. Verdict remains Triple overlap.
- **Price target delta**: Bull $400 → **$550** | Base $300 → **$385** | Bear $170 → **$160** | PW EV $322 → **≈$370** (on a 5-year rather than 3-year terminal). R/R 1.4:1 → **2.7:1**.
- **Catalyst & Sentiment delta**: Price $265.06 → **$264.16** — essentially flat, but via a round trip through a **$3T market cap and a $287.20 high**. Consensus 42 Buy/3 Hold (avg PT $286) → **58 Buy-equivalent / 2 Hold / 0 Sell** (median $325). FTC trial pushed to Feb 2027.

### Recommendation

- **For a non-holder**: 🟡 **Watch** — unchanged verb. The operating case is strong and spot sits just inside a defensible entry band, but a ~7%/yr expected return with negative FCF, universal sell-side bullishness, and no catalyst before October 29 does not argue for urgency. Prefer initiating below **$250** or after Q3 confirms FCF is troughing.
- **For a current holder**: 🟡 **Hold** — unchanged verb. Nothing argues for reducing a business compounding operating income at 43%; nothing argues for adding at a 75th-percentile price into a quarter with three open questions.

**Next review trigger**: **Q3 FY2026 earnings — October 29, 2026**. In priority order: (1) **free cash flow — troughing or still deteriorating**, (2) **AWS growth against the +37% comp**, (3) size and direction of any new Anthropic/OpenAI revaluation, (4) whether the ≈$220B capex guide is reaffirmed, raised or cut, (5) AWS operating margin against 39.4%, (6) backlog progression from $496B, (7) advertising against +26%.

---

## [2026-05-01] — Earnings Q1 FY2026

**Trigger**: Q1 FY2026 print released April 29, 2026 (post-close) — clean operating beat across all three pillars; stock to fresh ATH $265.06 by Apr 30 close.

**Sources reviewed**:
- [Amazon Q1 2026 PR (IR)](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/)
- [Q1 2026 earnings call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/04/29/amazon-amzn-q1-2026-earnings-call-transcript/)
- [CNBC Q1 2026 recap](https://www.cnbc.com/2026/04/29/amazon-amzn-q1-earnings-report-2026.html)
- [Yahoo Finance live price](https://finance.yahoo.com/quote/AMZN) — $265.06 at Apr 30, 2026 close (fresh ATH); 52-wk $178.85–$268.00

### What Changed

- **Header**: Last Updated 2026-04-26 → **2026-05-01**; Live Price $255.08 (Apr 23) → **$265.06 (Apr 30, fresh ATH)**
- **Summary (§0)**: Refreshed under Rule #18 4-part structure — thesis line updated to reflect Q1 print; verb line 🟡 Watch / 🟡 Hold; scenario table updated (Now $265.06 ~99th %ile, PW EV $322, R/R 1.4:1); KPI strip updated (FY26E P/E ~33×, AWS Op Margin Q1 ~37%, Q1 Capex $43.2B, Next Catalyst Q2 FY26); Why/Why-not refreshed
- **Key Stats Snapshot**: Live price + market cap (~$2.85T) + Q1 actuals replacing Q1 consensus rows; added Q2 FY26 guide row; analyst PT row preserved (cluster updates pending)
- **§11 Catalyst & Sentiment Tracker**: New "Q1 FY2026 Earnings (DELIVERED ✅)" subsection with full print metrics; Recent News prepended with Q1 entry; Upcoming Catalysts table — Q1 row ~~struck~~ DELIVERED ✅ with print summary; Q2 FY26 (~late-July) elevated to next anchor
- **§13 Bull/Bear/Base**: Probabilities shifted Bull 35%→**40%**, Base 50%→**45%**, Bear unchanged 15% (AWS +28% / EPS +70% beat shifted mass toward Bull); Base price $290 → **$300**; Bull/Bear targets unchanged; CAGR math re-anchored to $265 spot
- **§14 PW EV**: **$310 → $322**; Return +22% / 7%/yr → +21% / 6.6%/yr at higher spot; **R/R 1.7:1 → 1.4:1**
- **§15 Recommendation**: Non-holder verb **Initiate (small) / Watch → Watch** (multiple has caught up to operating thesis); Holder **Hold** unchanged; entry zone $210–235 → **$220–245** (slight upshift on PW EV step); trim zone $310–340 → **$325–355**; exit zone >$370 → **≥$400** (anchored to Bull); next review trigger updated to Q2 FY26 print (~late-July) with new key items (capex pacing, AWS hold above +25%)

### Thesis Status

- **Overall**: 🟢 **Strengthened operationally** — AWS +28% (fastest in 15 quarters), EPS +70% beat, ad +24%, Q2 guide brackets Street; demand-side validation of $200B capex bet. **Asymmetry compressed** as multiple rerated to fresh ATH.
- **BAIT delta**: Triple overlap retained; Analytical edge slightly strengthened on Q1 validation; Behavioral remains weak (no fear setup at ATH). Conviction Moderate (unchanged).
- **Price target delta**: Bull $400 unchanged | Base $290 → **$300** | Bear $170 unchanged | **PW EV $310 → $322**
- **Catalyst & Sentiment delta**: Q1 print binary resolved with clean beat; AWS share-loss-to-Azure bear case partially counter-pressed (single quarter, watch sustainability)

### Recommendation

- **For a non-holder**: 🟡 **Watch** (was Initiate-small/Watch) — operating thesis confirmed but multiple has caught up; preferred entry $220–245 on any 10–15% pullback
- **For a current holder**: 🟡 **Hold** (unchanged) — let operating thesis continue to compound; trim only above $325 without commensurate re-rate

**Next review trigger**: 📅 **Q2 FY26 earnings — late-July 2026 (post-close)**. Key items: AWS YoY growth (does +28% Q1 hold above +25%), capex pacing vs. ~$200B FY26 frame, Q3 op income guide, advertising sustainability (+24% Q1), NA op margin, Trainium4 reservation pipeline.

---

## [2026-04-26] — v2.6+v2.7+v2.8 Retrofit (Primary-Source Synthesis Refresh)

**Trigger**: Schema retrofit batch under v2.8. Brings AMZN page to current schema (Rules #19, #20, #21, #22, #23, #24, #25, #26).

**Sources reviewed (new this pass)**:
- [Andy Jassy FY2025 Shareholder Letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2025-letter-to-shareholders) (Pattern A: published Apr 2026; covers FY2025)
- [Andy Jassy FY2024 letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2024-letter-to-shareholders)
- [Andy Jassy FY2023 letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2023-letter-to-shareholders)
- [Andy Jassy FY2022 letter](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2022-letter-to-shareholders)
- [Andy Jassy FY2021 letter (first as CEO)](https://www.aboutamazon.com/news/company-news/2021-letter-to-shareholders)
- [Jeff Bezos FY2020 letter (final)](https://www.aboutamazon.com/news/company-news/2020-letter-to-shareholders)
- [Q4 FY25 8-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm) — confirmed FY25 actuals: Rev $716.9B, Op Inc $80.0B, AWS Op Inc $45.6B
- [FY2024 10-K HTML](https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/amzn-20241231.htm), [FY2023 10-K HTML](https://www.sec.gov/Archives/edgar/data/1018724/000101872424000008/amzn-20231231.htm) (5-year baseline indexed in `raw/AMZN/filings/AMZN-10K-INDEX.md`)
- [Yahoo Finance live price](https://finance.yahoo.com/quote/AMZN) (verified $255.08 at Apr 23 2026 close; 52-wk $178.85–$258.79; market cap $2.74T)
- [TipRanks AMZN](https://www.tipranks.com/stocks/amzn) — Strong Buy 42/3; avg PT $286
- TradingKey / Seeking Alpha / S&P Q1 FY26 previews (consensus rev $177.2B, EPS $1.63, AWS ~$36.8B; UBS bull case +38% AWS)

### What Changed (vs. prior v2.5 page)

- **Live price refreshed** $247 → **$255.08** (Apr 23 2026 close from Yahoo Finance); 52-wk high updated to $258.79
- **FY2025 actuals now booked** — Rev $716.9B (+12%), Op Inc $80.0B, AWS Op Inc $45.6B, NA Op Inc $29.6B, Intl Op Inc $4.7B (first profitable year for International segment at scale), FCF $7.7B (compressed by capex)
- **§2 (Annual Financial Metrics)**: Added FY21 baseline column; added segment op income rows (NA, Intl, AWS); added new `### Primary Source: 10-K Segment Detail` subsection with multi-year MD&A synthesis (NA op income +$32B swing FY22→FY25; AWS op margin 24%→37%)
- **§5 (Competitive Moat)**: Standalone "Moat Assessment" block above Pivotal Question retired (Rule #23). Added mandatory `### Competitive Landscape` subsection (Rule #24) with 4-pillar peer tables (Retail / Cloud / Advertising / Logistics) and explicit framing of how AMZN's cross-pillar reinforcement differs
- **§6 (Management & Leadership)**: Added `### Recent Management Commentary — Primary Source Synthesis` subsection with 7 verbatim quotes from FY20–FY25 letters mapped to investment relevance + 5-Year Capital Allocation Arc table tracing the restraint→reaccel→AI build-out cadence (Rule #19)
- **§8 (Key Risks)**: Boilerplate dropped per Rule #25; "not priced in" tags added to AI capex ROIC and Azure share loss rows; 5-Year Risk Factor Evolution table replaced with synthesis paragraph (Rule #21) — names AI risk factor first appearing FY23 10-K, capex/data-center concentration risk added FY24, COVID logistics overcapacity language removed by FY24
- **§11 (Catalysts)**: Refreshed all analyst PTs (BMO $315, KeyBanc $325, BofA $298); added April 9 Jassy AWS AI $15B run rate disclosure; updated Q1 FY26 print 3 days out
- **§13/§14 scenarios**: Bull/Bear/Base unchanged in price targets; current price reset to $255.08 compresses R/R from prior framing — now ~1.7:1 (Bull/Bear midpoints) vs. ~3:1 at the Feb 2026 lows; PW EV $310 yields +22% / 7%/yr at $255 (vs. +26% at $247)
- **§15 (Recommendation)**: Non-holder verb softened from **Initiate** → **Initiate (small) / Watch** reflecting compressed margin-of-safety at $255 (–1.4% from 52-wk high) vs. prior $247 framing; thesis-break trigger added: "FY26 capex revised up >$250B without commensurate AWS AI revenue acceleration"
- **Summary** bullet-list rewritten under v2.8 emoji conventions; output discipline pass (no CLAUDE.md self-references; no "corrected from" language; tables time-in-columns; bullets for data-dense lines)
- **All sources linkified** per Rule #16 (eliminated [link pending] for Anthropic / Northwise / S&P)

### Thesis Status

- **Overall**: 🟡 **Unchanged → marginally weakened on price** — fundamentals strengthened (FY25 actuals beat, AWS reaccel, International profitability inflection), but $255 print compresses asymmetry vs. the $247 framing. Bear/Bull R/R now 1.7:1 vs. ~3:1 at Feb lows.
- **BAIT delta**: Triple overlap retained (A Mod-Strong + I Mod + T Mod); Behavioral remains only Moderate (no fear at near-high pricing)
- **Price target delta**: Bull $400 / Base $290 / Bear $170 unchanged from v2.5 — schema refresh, not thesis revision

### Recommendation

- **For a non-holder**: 🟡 **Initiate (small) / Watch** — preferred entry $220–235; current $255 is fair-price not value-price
- **For a current holder**: 🟡 **Hold** — let Q1 print resolve before adding; trim only above $310 without earnings re-rate

**Next review trigger**: 📅 **Q1 FY26 earnings — April 29, 2026 (post-close, 3 days out)**. Key items: AWS YoY growth (Street +22% vs. UBS +38% bull), AI revenue commentary, Q2 op income guide, FY26 capex affirmation, advertising growth rate, NA op margin.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added AMZN to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- AMZN Q4 FY25 earnings press release (AMZN IR, 2026-02-05)
- Q4 FY25 earnings call transcript (Yahoo Finance)
- Q3 FY25 ex-99.1 SEC filing
- CNBC "Amazon Q4 2025 earnings report" (2026-02-05)
- Futurum Group quarterly analyses (Q1–Q4 FY25)
- Morningstar pre-Q1 FY26 preview
- Yahoo Finance live price (2026-04-24)
- 24/7 Wall St "BofA + KeyBanc double upgrade" (2026-04-20)
- S&P Global big-tech earnings preview
- Capital.com tariff forecast piece (2026-03-30)
- Motley Fool 1-yr prediction (2026-04-15)
- Northwise Project Amazon 2030 forecast

### What Changed
- Initial compilation; no prior wiki content
- Live price verified ~$247 (Yahoo Finance / 24/7 Wall St cross-check, April 24, 2026)
- Q4 FY25: rev $213.4B (+14%); AWS $35.6B (+24%, "fastest in 13 quarters"); op income $25.0B
- **$200B FY26 capex guide** (vs. $77.7B FY24) — central thesis tension
- KeyBanc PT $285 → $325, BofA PT $275 → $298 ahead of April 29 Q1 print

### Thesis Status
- **Overall**: Initiated — Wide-moat mega-cap mid-cycle in generational AI infrastructure bet
- **BAIT signal**: Triple overlap (A Mod-Strong + I Mod + T Mod); Behavioral only Moderate; Conviction Moderate
- **PW EV**: ~$310 (3-yr) vs. spot ~$247 → +26% / ~8%/yr

### Recommendation
- **For a non-holder**: **Initiate** at $247 — quality-at-fair-price; pullback into $210–235 would offer margin of safety
- **For a current holder**: **Hold / Add modestly** into Q1 FY26 print

**Next review trigger**: Q1 FY26 earnings — April 29, 2026 (post-close). 5 days from this writeup.
