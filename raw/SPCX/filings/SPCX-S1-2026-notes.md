# SPCX (Space Exploration Technologies Corp.) — Form S-1 Extraction Notes

**Filing**: Form S-1 (IPO registration statement). Confidentially submitted April 1, 2026; publicly filed May 20, 2026; SEC declared effective June 11, 2026 (priced same day at $135/share; Nasdaq debut June 12, 2026 under ticker SPCX).
**SEC CIK**: 0001181412
**Primary source URL** (fetch blocked in this session — see Access Note): https://www.sec.gov/Archives/edgar/data/0001181412/000162828026036936/spaceexplorationtechnologi.htm

## ACCESS NOTE
Direct fetch of sec.gov (www.sec.gov) returned HTTP 403 in this research session, consistent with prior sessions in this wiki (organization/proxy-level block, not filing-specific). All data below was extracted via targeted WebSearch queries against news coverage, financial-analysis newsletters, and aggregator sites that quote the S-1 directly (Fortune, TechCrunch, CNBC, The Motley Fool, Axios, Tom Tunguz, Sacra, Morningstar, mostlymetrics, tanayj.com, vestedfinance). Every figure below is sourced from a specific citation; nothing is fabricated. A follow-up session with working SEC/IR fetch access should replace this file with a direct-source extraction and verify all figures against the primary HTML filing.

---

## Business Overview / Mission
S-1 mission statement: *"to build the systems and technologies necessary to make life multiplanetary, to understand the true nature of the universe, and to extend the light of consciousness to the stars."*

Company frames itself as operating three integrated businesses: **Launch** (Falcon 9, Falcon Heavy, Starship), **Starlink** (satellite broadband/connectivity), and — newly, following the Feb 2026 xAI merger — **AI Infrastructure/Compute** (Colossus data centers, GPU leasing).

## Total Addressable Market (S-1 claim)
S-1 states: *"We believe we have identified the largest actionable total addressable market in human history."* Quantified at **$28.5 trillion**:
- $370B — Space (space-enabled solutions)
- $1.6T — Connectivity ($870B Starlink Broadband + $740B Starlink Mobile)
- **$26.5T — AI** ($2.4T AI infrastructure + $760B consumer subscriptions + $600B digital advertising + $22.7T enterprise applications)

Analyst/independent commentary (Axios, Yahoo Finance "Peak Galaxy Brain?") is skeptical that the $22.7T "enterprise applications" bucket in particular is a defensible, near-term addressable market for SpaceX specifically rather than a category-wide AI TAM loosely associated with the business — treat the $28.5T figure as management's own framing, not an independently validated estimate. [Source: Fortune, Axios, Yahoo Finance]

## Segment Revenue (FY2025, full year)
Total consolidated revenue: **$18.674 billion**. Segment split (per aggregator analysis of the S-1's segment disclosures):
- **Starlink**: $11.4B (61% of revenue) — the only segment producing meaningful operating income: $4.4B operating profit, ~$7B segment EBITDA at 63% margin
- **Launch**: ~$4.1B (22% of revenue)
- **AI/Compute**: ~$3.2B (17% of revenue) — this is pre-Anthropic/pre-Google-contract revenue (internal xAI usage transitioning to external leasing); the big external compute contracts (Anthropic from May 2026, Google from Oct 2026) will show up in FY2026 and beyond, not fully in the FY2025 base
[Source: mostlymetrics.com S-1 breakdown, tanayj.com, Morningstar 6-chart S-1 summary]

## Q1 2026 (three months ended March 31, 2026) — most recent quarter in the S-1
- Revenue: $4.694B
- Loss from operations: -$1.943B
- Adjusted EBITDA: $1.127B
- Cash & cash equivalents: $15.8B
- Total capex: $10.1B for the quarter alone (annualizing to >$40B/yr pace)
- AI-specific capex: $7,723M (vs. $2,567M in Q1 2025, a +$5,156M YoY increase) — driven by rapid expansion of terrestrial data centers (Colossus)
[Source: Kobeissi Letter (X/Twitter) citing S-1 directly; Yahoo Finance "SpaceX files IPO prospectus"]

## Starlink Metrics (subscriber growth + ARPU)
- Subscribers: 2.3M (2023) → 4.4M (2024) → 8.9M (2025) → 10.3M (Q1 2026), across 164 countries
- Monthly ARPU declining: $99 → $91 → $81 → $66 (Q1 2026) — reflects international expansion into lower-ARPU markets and cheaper tiers (Starlink Mini)
[Source: spacexchart.com, mostlymetrics.com]

## Capex Trend (multi-year)
$4.4B (2023) → [2024 not captured this pass] → $20.7B (2025) → $10.1B (Q1 2026 alone)
[Source: aggregator citing S-1 capex tables]

## Growth Projections (S-1 / management framing — treat as aspirational, not guidance in the traditional sense)
Multiple aggregators report the S-1 (or associated investor materials) laying out:
- 2028E revenue: $120–180B
- 2029E revenue: $200–300B
- 2030E revenue: $400–500B+ (with AI dominating the mix)
- Implies sustained 50–100%+ YoY revenue growth for several years, combined with 50%+ EBITDA margins
- **This is an extremely aggressive projection** (≈85–90% revenue CAGR 2025→2030) resting almost entirely on the AI/compute segment scaling far beyond Starlink/Launch combined. Treat with significant skepticism — no public launch/satellite company has ever compounded at this rate, and it depends on Starship execution (see risk factors below).
[Source: Medium "SpaceX in 2026-2030" analysis, vestedfinance.com]

## Orbital Data Center Plan (long-dated, speculative)
- Plans to begin deploying AI compute satellites in Sun-synchronous orbit "as early as 2028"
- Long-term goal: 100 gigawatts of orbital compute capacity deployed per year — would require thousands of Starship launches/year and ~1 million metric tons to orbit annually
- S-1 explicit quote: *"AI compute satellites at scale need full Starship reusability to be economically compelling."*
- SpaceX has asked the FCC for authorization to launch up to **1 million satellites** as part of this "orbital data center" concept
[Source: ai2.work, kevincrowther.com, teslarati.com]

## Risk Factors (S-1 Item 1A — ~38 pages per secondary coverage)
### Key person — Elon Musk
- No key-person insurance on Musk
- S-1 explicit: *"The loss of Mr. Musk, whether due to death, disability, or otherwise, or his inability or unwillingness to continue in his current roles, could significantly disrupt our management structure, adversely affect our ability to execute our strategic plans, and negatively impact our reputation and relationships with customers, partners, and other stakeholders."*
- S-1 discloses Musk "does not devote his full time and attention" to SpaceX — concurrently CEO of Tesla, involved in xAI/X (both now merged/related-party), Neuralink, The Boring Company
- Musk holds 94% of Class B shares (10 votes/share), translating to ~79% of total voting power
[Source: moneywise.com, singularitycapadvisors.com]

### Starship dependency (cascading single point of failure)
- Launch cadence and payload capacity increases depend on Starship succeeding at scale
- S-1 warns any failure/delay in Starship development "at scale or in achieving the required launch cadence" would cascade to next-generation Starlink satellites AND the AI data center/orbital compute plan
- *"In-orbit refueling is complex, and we have not yet demonstrated or attempted it"* — required for lunar/Mars/asteroid missions
- As of mid-2026: 11 full-stack Starship test flights completed; first Block 3 flight targeted Q2 2026
[Source: lpl.com, augment.market]

### Regulatory / national security
- Launch cadence gated by FAA licensing; company has publicly criticized regulatory review timelines as slower than rocket development itself
- FCC coordination required for Starlink spectrum
- Orbital AI compute plan requires spectrum allocation, orbital debris mitigation, and international regulatory approval — S-1 explicitly flags "no guarantee of success"
- U.S. government contracts ≈35% of total company revenue — concentration + termination-for-convenience risk (government contracts can be unilaterally terminated/reduced/delayed)
- Classified-customer disclosure carve-out: if a classified customer exceeds 10% of revenue, SpaceX can argue naming it would compromise national security and avoid standard disclosure
- Elon Musk's ~130-day tenure leading a federal cost-cutting effort (2025) that reviewed/terminated competitor contracts, while SpaceX itself is flagged as "the most financially significant target of any [that same]-era contract review" given ~$10–12B in annual government revenue — a real conflict-of-interest/political-risk factor
[Source: klover.ai, fastcompany.com, spacedaily.com]

### Financial / capital structure
- Company posted a GAAP operating loss in Q1 2026 (-$1.943B) despite positive adjusted EBITDA ($1.127B) — heavy D&A from the AI capex buildout
- Total capex run-rate (>$40B/yr annualized off Q1 2026) far exceeds FY2025 revenue ($18.7B) — company is self-funding a massive buildout via IPO proceeds + debt
[Source: same S-1 aggregator sources as above]

---

## Sources (all via WebSearch synthesis, direct SEC/IR fetch blocked)
- [Fortune — SpaceX IPO filing TAM](https://fortune.com/2026/05/20/spacex-ipo-filing-s1-total-addressable-market-make-life-multiplanetary/)
- [TechCrunch — SpaceX IPO filing has arrived](https://techcrunch.com/2026/05/20/the-spacex-ipo-filing-has-arrived/)
- [Axios — Understanding the SpaceX TAM numbers](https://www.axios.com/2026/05/24/musk-spacex-ipo-tam)
- [mostlymetrics.com — SpaceX S-1 breakdown](https://www.mostlymetrics.com/p/spacex-ipo-s1-breakdown)
- [tanayj.com — Inside the SpaceX S-1](https://www.tanayj.com/p/the-spacex-s-1-building-the-infrastructure)
- [Tom Tunguz — SpaceX's Limitless Ambition: An AI Conglomerate](https://tomtunguz.com/spacex-s1-analysis/)
- [Morningstar — 6 Charts on SpaceX's Pre-IPO Financials](https://www.morningstar.com/stocks/6-charts-spacexs-s-1-financials)
- [Sacra — SpaceX revenue, valuation & funding](https://sacra.com/c/spacex/)
- [spacexchart.com — Starlink subscribers/revenue/unit economics](https://spacexchart.com/starlink)
- [moneywise.com — SpaceX S-1 risk factors, 38 pages](https://moneywise.com/investing/stocks/spacex-ipo-s1-risk-factors-elon-musk)
- [Kobeissi Letter (X) — S-1 filing details](https://x.com/KobeissiLetter/status/2057203173069123600)
- [SEC EDGAR — SPCX S-1 primary filing](https://www.sec.gov/Archives/edgar/data/0001181412/000162828026036936/spaceexplorationtechnologi.htm) (fetch blocked)
