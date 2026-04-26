# LNTH — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Schema Retrofit

**Trigger**: v2.9 schema retrofit — section renumbering (15→13 sections), structural consolidation, shareholder letter pattern identification, material updates from post-v2.2 events (PYLARIFY TruVu approval, SPECT divestiture completion, CEO transition, securities litigation, Evergreen + Life Molecular acquisitions)

**Sources reviewed**:
- [Lantheus Q4 2025 & FY2025 PR — GlobeNewswire](https://www.globenewswire.com/news-release/2026/02/26/3245408/0/en/Lantheus-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results-and-Provides-Business-Update.html)
- [PYLARIFY TruVu FDA approval PR (March 6, 2026)](https://www.globenewswire.com/news-release/2026/03/06/3251298/0/en/Lantheus-Announces-FDA-Approval-of-PYLARIFY-TruVu-piflufolastat-F-18-Injection.html)
- [LNTH-2501 PDUFA extension to June 29, 2026](https://lantheusholdings.gcs-web.com/news-releases/news-release-details/lantheus-announces-three-month-extension-pdufa-date-lnth-2501-ga)
- [MK-6240 PDUFA August 13, 2026](https://lantheusholdings.gcs-web.com/news-releases/news-release-details/lantheus-announces-fda-acceptance-new-drug-application-mk-6240)
- [Evergreen Theragnostics acquisition completion](https://www.globenewswire.com/news-release/2025/04/01/3053408/0/en/Lantheus-Completes-Acquisition-of-Evergreen-Theragnostics.html)
- [Leadership transition announcement](https://lantheusholdings.gcs-web.com/news-releases/news-release-details/lantheus-announces-leadership-transition-plan)
- [Securities class action filing](https://www.globenewswire.com/news-release/2025/11/04/3180375/0/en/Lantheus-Holdings-Inc-Sued-for-Securities-Law-Violations-Contact-the-DJS-Law-Group-to-Discuss-Your-Rights-LNTH.html)
- [Q1 2026 earnings call set for May 7, 2026](https://www.stocktitan.net/news/LNTH/lantheus-to-host-first-quarter-2026-earnings-conference-call-and-2zbgrwlpfvsk.html)
- [stockanalysis.com — LNTH financials](https://stockanalysis.com/stocks/lnth/financials/) (FY2021–FY2025 annual + 8 quarters)
- [stockanalysis.com — LNTH forecast](https://stockanalysis.com/stocks/lnth/forecast/) (analyst consensus)
- [MarketBeat — LNTH short interest](https://www.marketbeat.com/stocks/NASDAQ/LNTH/short-interest/) + price
- [StockTitan — CCO Form 4 April 17, 2026](https://www.stocktitan.net/sec-filings/LNTH/form-4-lantheus-holdings-inc-insider-trading-activity-ea818ab503d9.html)
- [Yahoo Finance — Q4 2025 earnings call transcript](https://finance.yahoo.com/news/lantheus-lnth-q4-2025-earnings-195852869.html)
- [FNArena — Telix competitive update](https://fnarena.com/index.php/2026/01/22/focus-on-telix-guidance-post-annus-horribilis/)

**Shareholder letter pattern**: Pattern C — Lantheus does not publish standalone annual or quarterly shareholder letters. CEO commentary sourced from earnings releases and 10-K annual report preambles. No `raw/LNTH/shareholder-letters/` files populated (gap logged).

### What Changed

- **Header**: Schema version bumped from v2.5 → v2.9; live price updated to $82.91 (2026-04-26)
- **Summary**: Refreshed under v2.9 Rule #18 (≤10 emoji-tagged bullets); added CEO vacancy, litigation, and Posluma TPT dynamics as new elements
- **Business Overview**: Substantially updated — SPECT divestiture (effective Jan 1, 2026), Life Molecular Imaging (Neuraceq) and Evergreen Theragnostics acquisitions, CEO transition, PYLARIFY TruVu approval incorporated
- **Pivotal Investment Question**: Updated to reflect CEO vacancy + litigation as compounding factors to the original PDUFA binary question
- **Key Stats Snapshot**: Updated price ($82.91), FCF ($354M actual FY2025), analyst consensus, Q1 2026 earnings date confirmed May 7, 2026
- **§1 retired** (v2.9 schema): Founding-insight content folded into Business Overview; Pivotal Investment Question elevated to header subsection
- **§1 (Annual Financial Metrics)**: Added full FY2021–FY2025 annual table from primary sources; added 8-quarter recent quarterly table; added multi-year narrative synthesis
- **§2 (Revenue Mix & Geographic Split)**: Merged old §3 (Geographic) + §4 (Revenue Mix) per v2.9; updated with Neuraceq Q4 2025 contribution, SPECT divestiture impact, PYLARIFY TruVu forward shift
- **§3 (Competitive Moat & Landscape)**: Added Competitive Landscape subsection per v2.9 Rule #24; named Posluma (Blue Earth/Bracco), Illuccix/Gozellix (Telix), Curium, Novartis Locametz, Eli Lilly/POINT; added Posluma TPT pass-through mechanism as the primary pricing threat
- **§4 (Management & Leadership)**: Updated with Markison retirement, Heino interim CEO appointment, CEO search status, Blanchfield as CFO; added Pattern C management commentary subsection from Q4 2025 earnings call + FY2024 annual letter
- **§5 (Strategic Growth Initiatives)**: Updated with PYLARIFY TruVu (approved March 6, 2026), LNTH-2503 + Evergreen CDMO, Meilleur Technologies AI dosimetry, Neuraceq AD platform; all sourced from primary press releases
- **§6 (Key Risks)**: v2.9 materiality filter applied (Rule #25); added CEO vacancy and securities class action as NEW material risks not priced in; removed boilerplate; added Posluma TPT expiration as a specific dated catalyst; risk factor evolution synthesis paragraph added
- **§7 (Industry-Specific Macro Analysis)**: Updated with Posluma TPT mechanism detail, Lu-177 supply chain context, theranostics secular trend; Neuraceq + anti-amyloid therapy connection added
- **§8 (Valuation)**: Updated multiples to current $82.91 / ~$5.31B market cap; updated peer set with Telix; refreshed fair value range
- **§9 (Catalyst & Sentiment Tracker)**: Live price $82.91, short interest 8.89%, PYLARIFY TruVu approval on Mar 6 marked ✅ delivered; Posluma TPT expiration Sept 30, 2026 added; Q1 2026 earnings date May 7, 2026 confirmed; CEO search as ongoing catalyst added
- **§10 (BAIT)**: Updated — CEO vacancy and litigation add to Behavioral signal; Posluma TPT expiration date added to Analytical edge; Neuraceq AD platform added to Informational edge
- **§11 (Bull/Bear/Base)**: Scenarios updated — bear case probability raised to 25% (from 25%) incorporating CEO + litigation risk; bull case probability lowered to 25% (from 30%); base case stable at 50%; terminal year 2028 (vs. 2029 prior)
- **§12 (PW EV)**: Recomputed — PW EV ~$94 (vs. prior ~$99); R/R ~1.5:1 Bull/Bear; horizon stated as 3 years to 2028
- **§13 (Recommendation)**: Updated thesis sentence to include CEO vacancy + litigation; entry zone maintained $65–78; trim zone maintained $110–130; thesis-break triggers updated (added CEO search unresolved past Q3, litigation >$200M)
- All section cross-references updated to v2.9 numbering (§9 was §11; §13 was §15, etc.)
- All sources converted to Markdown links per Rule #16

### Thesis Status

- **Overall**: **Unchanged** vs. v2.2 initiation — Watch/Hold framing maintained. However, thesis is modestly *weakened* vs. the original v2.2 by two new risk factors not present at initiation: CEO vacancy (execution gap at a critical pipeline launch window) and securities class action (disclosure credibility + capital overhang). PW EV revised down slightly from ~$99 to ~$94 reflecting these new risks.
- **BAIT delta**: Behavioral edge reduced slightly (not extreme fear setup at $82.91); Analytical edge maintained (Posluma TPT expiration + AD platform underappreciated); no material I or T change
- **Price target delta**: Bull $145 → $140 | Base $95 → $95 | Bear $50 → $45 (reflecting CEO + litigation risk in the bear scenario)

### Recommendation

- **For a non-holder**: Watch — wait for LNTH-2501 PDUFA outcome (June 29, 2026) or $65–78 entry zone
- **For a current holder**: Hold — FY26 trough largely priced; add on weakness toward $70

**Next review trigger**: Q1 2026 earnings — May 7, 2026, 8:00 a.m. ET

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added LNTH to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Lantheus Q4 2025 earnings release (2026-02-26, stocktitan / Investor Relations)
- Lantheus FY2026 guidance summary (Seeking Alpha)
- Yahoo Finance live price endpoint (2026-04-24)
- MarketBeat, TipRanks, stockanalysis — analyst consensus April 2026
- Truist + Mizuho PT raises (April 2026)
- FDA PDUFA notices (GeneOnline, OncLive, Lantheus IR)
- stocktitan / SEC Form 4 — insider activity April 2026
- Merlintrader 2026 outlook commentary

### What Changed
- Initial compilation; no prior wiki content
- Live price verified at $84.33 (Yahoo Finance, April 24, 2026)
- Established LNTH as Pharma / radiopharmaceutical asset type
- Recorded –22.6% from 52-wk high, +78.5% above 52-wk low
- Documented FY26 guide: revenue $1.4–1.45B (–6 to –9%), adj EPS $5.00–5.25
- Three 2026 PDUFA dates flagged: New PYLARIFY F-18 (Mar 6 — outcome to verify), LNTH-2501 (June, extended), MK-6240 tau PET (Aug 13)
- Short interest at 8.89% rising — bear-side conviction on PYLARIFY commoditization

### Thesis Status
- **Overall**: Initiated — Cautious / Watch
- **BAIT signal**: Moderate — A + I both Moderate; binary-event setup (3 PDUFAs)
- **PW EV**: ~$99 (3-yr) vs. $84.33 spot = +17% / +5.4% annualized — modest

### Recommendation
- **For a non-holder**: Watch — Wait for PDUFA outcomes or drawdown into $65–75 zone.
- **For a current holder**: Hold — FY26 trough largely priced; pipeline catalysts skew positive.

**Next review trigger**: Q1 2026 earnings (early May 2026, est.) + LNTH-2501 PDUFA (June 2026).
