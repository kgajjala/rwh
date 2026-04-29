# Richer Wiser Happier (rwh)

Personal investment knowledge base — maintained by Claude Code following the
[Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## What This Is

A structured, compounding wiki of investment analyses. Unlike RAG or chat history,
knowledge accumulates here permanently — every earnings update, every new article,
every thesis revision is integrated into the wiki and versioned with Git.

The wiki is **position-agnostic** — it analyzes companies, not portfolio holdings.
Recommendations split into "for a non-holder" vs. "for a current holder" framings.
Schema and operating rules live in [`CLAUDE.md`](CLAUDE.md).

## How It Works

1. **Add raw sources** → drop earnings transcripts, 10-Ks, or clipped articles into `raw/`
2. **Claude Code compiles** → reads `raw/`, updates `wiki/` with structured analysis
3. **Obsidian displays** → open this folder as a Vault to browse with graph view + backlinks
4. **Git tracks everything** → full diff history of every thesis change
5. **Friday cron auto-refreshes** → `kg-invest-wiki-weekly` routine fires every Friday 22:00 UTC, scans every ticker for material events, writes a cross-ticker summary to `outputs/weekly/`, commits, pushes

## Tickers Covered

*Alphabetical. Maintained per CLAUDE.md Core Rule #14 — every Workflow A ingest, Workflow B material update, or ticker removal must update this table in the same commit.*

| Ticker | Status | Last Updated | Punchline |
|--------|--------|--------------|-----------|
| [ABNB](wiki/tickers/ABNB/ABNB.md) | Active | 2026-04-24 | Wide-moat global lodging marketplace at $142.82 (near 52-wk high); Q4 2025 GBV inflection (+16%, highest in 2 years), FCF $4.6B / 38% margin; PW EV +13% over 3yr. **Watch / Hold; attractive entry $120–130**. |
| [ACLS](wiki/tickers/ACLS/ACLS.md) | Active | 2026-04-24 | Semi capital-equipment specialist at $143 (+186% trailing year) on SiC + memory cycle inflection; B. Riley $150 PT but FY26 guide flat; PW EV +8% — momentum-late, low forward asymmetry. **Watch / Hold**. |
| [ADBE](wiki/tickers/ADBE/ADBE.md) | Active | 2026-04-24 | High-conviction asymmetric setup at $245.44 (–42% from high) — sub-11× FY26E NGAAP P/E + 9% FCF yield + AI-first ARR tripled YoY = "great business at a fair price"; Triple-overlap BAIT; PW EV $348 (+42%). **Initiate / Add**. |
| [AMZN](wiki/tickers/AMZN/AMZN.md) | Active | 2026-04-24 | Three-pillar Wide-moat mega-cap mid-cycle in $200B/yr AI capex bet; Triple BAIT; PW EV ~$310 (+26% / ~8%/yr); April 29 Q1 FY26 print is the binary catalyst. **Initiate / Hold-Add**. |
| [BKNG](wiki/tickers/BKNG/BKNG.md) | Active | 2026-04-24 | Wide-moat global travel platform post-25-for-1 split (~$180); Triple BAIT (B+A-Strong); FCF compounder with the Connected Trip reinvestment thesis intact. **Initiate / Hold-Add**. |
| [BRK.B](wiki/tickers/BRK.B/BRK.B.md) | Active | 2026-04-25 | Wide-moat $1.01T fortress at $469.32 (–13.4% from high, near 52-wk low); first post-Buffett year under Greg Abel (CEO Jan 2026); $373B cash + $176B float; **first buyback since May 2024 resumed Mar 4, 2026** at this zone — credible soft floor. Triple BAIT (B+I-Strong, A-Mod); PW EV ~$543 (+15.7% over 3yr). **Initiate (small/scaled) / Hold-Add**. |
| [CELH](wiki/tickers/CELH/CELH.md) | Active | 2026-04-24 | Three-brand functional energy (CELSIUS + Alani Nu + Rockstar via PepsiCo) at $35.25 (–47% drawdown); Triple BAIT (B Strong + A/T Mod); event-driven into May 11 Q1; PW EV ~$52 (+47% / ~14%/yr). **Initiate small / Hold-Add**. |
| [CPNG](wiki/tickers/CPNG/CPNG.md) | Active | 2026-04-24 | Wide-moat Korean e-commerce + logistics at $20.58 (–40% drawdown); cleanest Triple BAIT (B+A Strong + I/T Mod); PW EV ~$28 (+36% / ~11%/yr); May 12 Q1 print on Korea margin is the catalyst. **Initiate / Add modestly**. |
| [DASH](wiki/tickers/DASH/DASH.md) | Active | 2026-04-25 | Dominant U.S. food-delivery (60-67% share, 3× Uber Eats) + global local-commerce post-Deliveroo $3.9B; FY2025 GAAP NI $935M (7.6×); v2.9 competitive landscape surfaces vertical-depth differentiator (only platform building food + grocery + retail + restaurant CRM); Wolt-precedent de-risks Deliveroo integration. **Watch / Hold (Add bias <$155); Q1 May 6 binary**. |
| [DELL](wiki/tickers/DELL/DELL.md) | Active | 2026-04-24 | AI-server beneficiary at $214.65 (near 52-wk high); FY27 +23% guide intact, but consensus median $185 sits *below* spot and Michael Dell entities sold ~$150M+ near highs in mid-April; PW EV $229 ≈ flat to spot. **Watch**. |
| [EBAY](wiki/tickers/EBAY/EBAY.md) | Active | 2026-04-24 | Re-accelerating marketplace at $97.94 (–8.8%, near highs); Q4 GMV +10% with ~6% combined buyback + dividend yield; fair value at consensus median; modest +17% PW EV asymmetry. **Watch / selective Initiate / Hold**. |
| [FIG](wiki/tickers/FIG/FIG.md) | Active | 2026-04-24 | Design-collaboration platform at $17.47 (–88% from post-IPO peak) under lock-up overhang + AI-disruption fear despite NDR 136% and 41% revenue growth; triple-overlap BAIT, PW EV +64% over 3yr; real existential AI risk. **Initiate (small, contrarian) / Hold-Add**. |
| [INTU](wiki/tickers/INTU/INTU.md) | Active | 2026-04-26 | Wide-moat vertical SaaS (TurboTax + QuickBooks + Credit Karma) at $395.95 trading at 17× FY26E NGAAP EPS — decade-low multiple driven by AI-horizontal fear primary-source data contradicts. Triple BAIT; PW EV $566 (+43%). **Initiate / Add**; Q3 FY26 May 21. |
| [KGS](wiki/tickers/KGS/KGS.md) | Active | 2026-04-26 | #1 U.S. contract compression (4.35M HP, 97.7% util) + AI-data-center power optionality (DPS close Apr 1) at $66 (52-wk high); R/R ~1:1 — bull case adequately priced. **Watch / Hold**; entry $50–55. |
| [LLY](wiki/tickers/LLY/LLY.md) | Active | 2026-04-26 | Tirzepatide franchise (~$40B FY25) + **orforglipron FDA-approved Apr 1, 2026** + retatrutide Phase 3; ~26× FY26E EPS on +46–53% growth; Triple BAIT (A+I-Strong). Q1 prints Apr 30. **Initiate / Hold-Add on pullback**; entry $750–850. |
| [LNTH](wiki/tickers/LNTH/LNTH.md) | Active | 2026-04-26 | PYLARIFY-concentrated PET radiodiagnostic franchise navigating FY26 –6 to –9% revenue trough; binary 2026 PDUFA event-setup (LNTH-2501 June 29, MK-6240 Aug 13); PW EV +16% (3yr). **Watch / Hold**; entry $65–78. |
| [LULU](wiki/tickers/LULU/LULU.md) | Active | 2026-04-26 | Premium athleisure at $143.80 (–58% from high, 52-wk low) — 2014-style executional trough vs. structural brand-cycle peak question; new ex-Nike CEO O'Neill starts Sept 8, 2026; PW EV $192 (+34%). **Watch / Initiate <$135 / Hold**. |
| [MP](wiki/tickers/MP/MP.md) | Active | 2026-04-26 | U.S. indispensable rare-earth + magnetics platform at $60.73 with DoD 10-yr offtake + $110/kg NdPr floor + Apple/GM offtakes + 10X campus 2028 ramp; Triple BAIT; PW EV $85 (+40%). **Initiate / Hold-Add**; Q1 May 7. |
| [MSFT](wiki/tickers/MSFT/MSFT.md) | Active | 2026-04-26 | Deepest-moat mega-cap (productivity + Azure + AI) at $424.62 (–23.5% drawdown); **Quadruple BAIT** (B+A+T Strong, I Mod); PW EV ~$565 (+31% / ~10%/yr). **Initiate / Add**; Q3 FY26 binary Apr 29. |
| [NFLX](wiki/tickers/NFLX/NFLX.md) | Active | 2026-04-26 | Wide-and-widening global streaming at $93.24 (–30% post-split); FY26 op-margin guide 31.5% (+200bps); ad revenue inflecting $1.5B → $3B → $7B+ by 2028E; Triple BAIT; PW EV $119.50 (+28%, 3yr); R/R ~2.4:1. **Initiate (small, scaled)**; entry $80–88. |
| [NKE](wiki/tickers/NKE/NKE.md) | Active | 2026-04-26 | Wide-moat global brand at $44.69 (12-year low, 3.67% yield, 20-yr high yield); **CEO Hill bought $1M April 14**; first NA re-acceleration signal in Q3 FY26 (+3%); Triple BAIT; PW EV ~14%/yr total. **Initiate / Add**; entry $40–48. |
| [ONON](wiki/tickers/ONON/ONON.md) | Active | 2026-04-26 | Premium Swiss athletic brand compounding +23% c-c at record 62.8% GM at $36.25, mispriced by FX + tariff + leadership-transition (co-CEOs Mar 26); PW EV $53 (+46%); median analyst $60. **Initiate / Add**; Q1 May 12. |
| [PG](wiki/tickers/PG/PG.md) | Active | 2026-04-26 | Dividend King post-Q3 FY2026 print (Apr 24): first companywide volume growth in over a year cautiously validates Jejurikar recovery, but 6 consecutive quarters of GM compression keep conviction moderate; PW EV ~10% total return. **Watch / Hold**; Q4 late July. |
| [RH](wiki/tickers/RH/RH.md) | Active | 2026-04-26 | Luxury-home retailer at $137.51 (–46.5%) at deep cyclical trough; 2030 mgmt vision $5.4–5.8B revenue / 25–28% margins; weak Q1 FY26 guide + 35.6% short interest amplify both ways; PW EV $208 (+51%, 4yr). **Watch / selective Initiate / Hold**; entry <$115. |
| [RIVN](wiki/tickers/RIVN/RIVN.md) | Active | 2026-04-26 | Pre-scale EV OEM (Narrow moat) at $16.54; FY25 print revealed structural mix-shift — software & services (largely VW JV) ~30% of revenue at high GM; R2 production started Apr 22; Triple BAIT; PW EV ~$18.50 (+12%, 2yr); R/R ~3.4:1. **Watch / small Initiate**; Q1 Apr 30. |
| [RKT](wiki/tickers/RKT/RKT.md) | Active | 2026-04-26 | Most complete U.S. homeownership super-platform (Redfin + Rocket + Mr. Cooper, Narrow-to-Emerging Wide moat) at ~13–15× FY26E EBITDA; market pricing the bear case while operating data confirms bull. PW EV $22.65 (+45%, 2–3yr); R/R ~3:1. **Initiate (Speculative) / Hold-Add**; Q1 May 7. |
| [SBUX](wiki/tickers/SBUX/SBUX.md) | Active | 2026-04-28 | **Niccol turnaround confirmed** — Q2 FY26 (Apr 28) printed +7.1% U.S. comp on **+4.3% transactions** with reduced discounting + op margin +110 bps; **FY26 guide raised to ≥5% comp / $2.25–$2.45 adj EPS**. PW EV ~$132 (+36% / ~11%/yr + 2.5% div); R/R ~3.2:1. 🟢 **Initiate-on-dip / Hold**; entry $90–97. |
| [SCHW](wiki/tickers/SCHW/SCHW.md) | Active | 2026-04-26 | Largest U.S. retail brokerage post-cash-sorting + TDA integration at $91.71; Q1 2026 BEAT with FY26 EPS guide raised >$5.70–$5.80; 19% dividend hike, $2.4B buyback executed; **Wide moat post-TDA**. Triple BAIT (B+A+I Strong); PW EV ~$108 (+18%, 18mo). **Initiate / Add**. |
| [SHOP](wiki/tickers/SHOP/SHOP.md) | Active | 2026-04-25 | Wide-and-widening moat commerce-infrastructure at $125.83 (30% US share, 3× Wix global); Q4 +30% rev / +29% GMV; **first-ever $2B buyback** at this zone is cleanest Tobi-Lütke intrinsic-value signal in 11 yrs; UCP + Agentic Storefronts = AI-commerce standard-setter. Triple BAIT; PW EV $212 (+68% 3yr); ~10:1 R/R. **Initiate / Add-Hold**. |
| [SN](wiki/tickers/SN/SN.md) | Active | 2026-04-26 | Serial-innovation consumer-products platform (Shark + Ninja) compounding +24% (FY24) / +18% (Q4 25) at expanding 17%+ adj EBITDA margins; ~100% US volume now manufacturable outside China — central tariff overhang largely de-risked; PW EV $144 (+24%); inaugural $750M buyback. **Initiate**. |
| [SPOT](wiki/tickers/SPOT/SPOT.md) | Active | 2026-04-28 | Wide-moat global audio super-platform (32% global streaming share, 761M MAU, 293M Premium); FY2025 op-inc +61% / FCF €2.87B; today's –13% on Q1 2026 op-inc guide miss creates first attractive entry in 12 months; PW EV $540 (+26%) at $429; R/R ~3.2:1. **Watch / Initiate $400–450; Hold**. |
| [TREX](wiki/tickers/TREX/TREX.md) | Active | 2026-04-26 | Dominant U.S. composite-decking franchise (Narrow-and-widening moat, 50–60% composite share) at $41.90 (housing-cyclical trough); $200M buyback compounding at the bottom; PW EV $57 (+36%); R/R ~3.6:1. **Initiate (patient) / Hold**; entry $30–42. |
| [TSLA](wiki/tickers/TSLA/TSLA.md) | Active | 2026-04-26 | Three-engine platform (Auto + Energy + AI/Robotics optionality) at $376.30 / ~125× FY26E P/E — substantial autonomy success already priced; PW EV ~$393 ≈ spot, R/R ~1.4:1; widest dispersion in mega-cap U.S. equities ($24.86–$600 analyst range). **Hold / Watch**; entry $280–320. |
| [UNH](wiki/tickers/UNH/UNH.md) | Active | 2026-04-28 | Wide-moat #1 managed care with **two reinforcing de-risks**: Q1 2026 BEAT (Apr 21, MCR 83.9%, FY26 guide >$18.25) **plus CMS 2027 MA Final Rate Notice ≈+2%** (Apr 28) — multi-billion FY27 EBIT tailwind; stock +≈14% in a week to ≈$368. Quadruple BAIT preserved; PW EV ~$447 (+21% / 24mo). **Initiate / Add**. |
| [WING](wiki/tickers/WING/WING.md) | Active | 2026-04-26 | Best-in-class asset-light franchise royalty (Narrow moat) at $189 — first SSS decline in 22 years (–3.3% FY25; Q4 –5.8%); $300M buyback authorized + 27/27 analyst Strong-Buy + Smart Kitchen rollout signal investing through trough. Triple BAIT; PW EV ~$215 (+14%, 18mo); R/R ~3:1. **Watch / Hold**; Q1 SSS Apr 29 binary. |
| [ZG](wiki/tickers/ZG/ZG.md) | Active | 2026-04-26 | Dominant U.S. real-estate marketplace at $45.41 (–51.6% from high) executing credible super-app pivot — Q4 25 rev +18%, FY25 +16%, Adj EBITDA margin 24%, FCF $420M; market pricing Rocket-Redfin narrative partly contradicted by $100M Zillow-Redfin rental syndication deal. Triple BAIT; PW EV ~$68 (+50%); R/R ~3:1. **Initiate / Add**. |

*36 tickers above. Last refresh: 2026-04-28 (SPOT initial v2.9 ingest added; prior 2026-04-26 v2.9 retrofit batch covered 22 tickers; 11 tickers preserved at v2.8 per user direction; SHOP and DASH at v2.9 from prior session).*

## Frameworks Used

- **BAIT** (Mauboussin) — Behavioral / Analytical / Informational / Technical
- **Moneyball** — Probability-weighted scenario scoring
- **15-Section thesis** — Full bottoms-up equity analysis framework
- **Asset Type Rules** — Valuation primary varies by business model (capital-light platform, three-sided marketplace, financial / brokerage, pharma / biotech, managed care, mortgage / housing, consumer staples, semiconductor capital equipment, real-estate marketplace, EV / auto, hyperscaler, etc.)

See `wiki/frameworks/` for full detail and `CLAUDE.md` for the schema.

## Quick Start (Claude Code)

Open this folder in Claude Code and say:
> "Read CLAUDE.md, then ingest [TICKER] under Workflow A."

Or for a specific update:
> "Refresh [TICKER] with the latest earnings transcript I dropped in raw/[TICKER]/transcripts/."

## Scheduled Updates

**Friday weekly cron**: `kg-invest-wiki-weekly` (`trig_01R1X9aCDwHQDfUmkSii1bWb`).
Runs every Friday at 22:00 UTC (6pm EDT / 5pm EST) on Anthropic's cloud
infrastructure. Each run executes Workflow B (incremental update for every
ticker), generates `outputs/weekly/YYYY-MM-DD_weekly_summary.md`, commits
and pushes. Manage at https://claude.ai/code/routines/trig_01R1X9aCDwHQDfUmkSii1bWb.

See [`wiki/summaries.md`](wiki/summaries.md) for the reverse-chron index of
all weekly summaries.

## Repo Map

```
rwh/
├── CLAUDE.md                     ← Schema and operating rules. Read first.
├── README.md                     ← This file. Top-level orientation + ticker table.
├── raw/                          ← Immutable source material (filings, transcripts, clippings)
├── wiki/
│   ├── index.md                  ← Master ticker catalog
│   ├── log.md                    ← Append-only event log
│   ├── watchlist.md              ← Cross-ticker attractiveness ranking
│   ├── summaries.md              ← Weekly summaries index
│   ├── tickers/[TICKER]/         ← One folder per ticker ([TICKER].md + changelog.md)
│   └── frameworks/               ← BAIT, Moneyball, Asset Types
└── outputs/
    ├── [TICKER]/                 ← Polished initial analysis reports
    └── weekly/                   ← Friday cross-ticker summaries
```

---
