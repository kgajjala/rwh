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
| [AMZN](wiki/tickers/AMZN/AMZN.md) | Active | 2026-05-01 | Q1 FY26 print confirmed thesis — AWS +28% (fastest in 15 quarters), EPS +70% beat, advertising +24%. At fresh ATH $265 / ~37× FY25 P/E quality is operationally proven; R/R compressed to ~1.4:1; PW EV $322. **Watch / Hold**; preferred re-entry $220–240. |
| [BKNG](wiki/tickers/BKNG/BKNG.md) | Active | 2026-05-01 | Q1 EPS/revenue beat but Q2 guide cut on Iran/Hormuz travel disruption — stock −6.6% to $168, mid-attractive-entry-zone. $3.6B Q1 buyback (130% pace acceleration) is unmistakable Fogel response; PW EV $192. **Initiate / Add**; R/R ~3.7:1. |
| [BRK.B](wiki/tickers/BRK.B/BRK.B.md) | Active | 2026-04-25 | Wide-moat $1.01T fortress at $469.32 (–13.4% from high, near 52-wk low); first post-Buffett year under Greg Abel (CEO Jan 2026); $373B cash + $176B float; **first buyback since May 2024 resumed Mar 4, 2026** at this zone — credible soft floor. Triple BAIT (B+I-Strong, A-Mod); PW EV ~$543 (+15.7% over 3yr). **Initiate (small/scaled) / Hold-Add**. |
| [CELH](wiki/tickers/CELH/CELH.md) | Active | 2026-04-24 | Three-brand functional energy (CELSIUS + Alani Nu + Rockstar via PepsiCo) at $35.25 (–47% drawdown); Triple BAIT (B Strong + A/T Mod); event-driven into May 11 Q1; PW EV ~$52 (+47% / ~14%/yr). **Initiate small / Hold-Add**. |
| [CPNG](wiki/tickers/CPNG/CPNG.md) | Active | 2026-04-24 | Wide-moat Korean e-commerce + logistics at $20.58 (–40% drawdown); cleanest Triple BAIT (B+A Strong + I/T Mod); PW EV ~$28 (+36% / ~11%/yr); May 12 Q1 print on Korea margin is the catalyst. **Initiate / Add modestly**. |
| [DASH](wiki/tickers/DASH/DASH.md) | Active | 2026-04-25 | Dominant U.S. food-delivery (60-67% share, 3× Uber Eats) + global local-commerce post-Deliveroo $3.9B; FY2025 GAAP NI $935M (7.6×); v2.9 competitive landscape surfaces vertical-depth differentiator (only platform building food + grocery + retail + restaurant CRM); Wolt-precedent de-risks Deliveroo integration. **Watch / Hold (Add bias <$155); Q1 May 6 binary**. |
| [DELL](wiki/tickers/DELL/DELL.md) | Active | 2026-04-24 | AI-server beneficiary at $214.65 (near 52-wk high); FY27 +23% guide intact, but consensus median $185 sits *below* spot and Michael Dell entities sold ~$150M+ near highs in mid-April; PW EV $229 ≈ flat to spot. **Watch**. |
| [EBAY](wiki/tickers/EBAY/EBAY.md) | Active | 2026-05-01 | Q1 2026 print (rev +19%, GMV +14% FXN, EPS $1.66) extends multi-quarter Focus-Category inflection; ~6% combined buyback + dividend yield intact, but post-print rerate to $103 compressed R/R to ~1.0:1. **Watch / selective Initiate / Hold-Trim into $115+**; entry $78–90. |
| [FIG](wiki/tickers/FIG/FIG.md) | Active | 2026-04-24 | Design-collaboration platform at $17.47 (–88% from post-IPO peak) under lock-up overhang + AI-disruption fear despite NDR 136% and 41% revenue growth; triple-overlap BAIT, PW EV +64% over 3yr; real existential AI risk. **Initiate (small, contrarian) / Hold-Add**. |
| [HOOD](wiki/tickers/HOOD/HOOD.md) | Active | 2026-04-29 | Multi-stream financial super-app (FY25 rev +52%, adj EBITDA +76%); Q1 2026 confirmed diversification (NII +24%, event contracts +320%, Gold +36%) absorbing crypto –47%; post-Q1 sell-off to **$70.29 (–14% session)** brings stock to entry zone low end; R/R improves to ≈5.5:1 at $70 vs. ~2.4:1 at $84. **Initiate / Add** at $65–80. PW EV ~$108 (+54%). |
| [INTU](wiki/tickers/INTU/INTU.md) | Active | 2026-04-26 | Wide-moat vertical SaaS (TurboTax + QuickBooks + Credit Karma) at $395.95 trading at 17× FY26E NGAAP EPS — decade-low multiple driven by AI-horizontal fear primary-source data contradicts. Triple BAIT; PW EV $566 (+43%). **Initiate / Add**; Q3 FY26 May 21. |
| [KGS](wiki/tickers/KGS/KGS.md) | Active | 2026-04-26 | #1 U.S. contract compression (4.35M HP, 97.7% util) + AI-data-center power optionality (DPS close Apr 1) at $66 (52-wk high); R/R ~1:1 — bull case adequately priced. **Watch / Hold**; entry $50–55. |
| [LLY](wiki/tickers/LLY/LLY.md) | Active | 2026-05-01 | Q1 2026 print confirmed franchise build-out — revenue +56% to $19.8B, **Mounjaro $8.66B (+125%)**, EPS $8.55 (+25% beat); FY26 guide raised to $82–85B / $35.50–$37.00 EPS. Triple BAIT (A+I-Strong); PW EV $1,264 (+30% 18mo); +10% post-print to ~$974. **Initiate / Hold-Add**; entry $830–900. |
| [LNTH](wiki/tickers/LNTH/LNTH.md) | Active | 2026-04-26 | PYLARIFY-concentrated PET radiodiagnostic franchise navigating FY26 –6 to –9% revenue trough; binary 2026 PDUFA event-setup (LNTH-2501 June 29, MK-6240 Aug 13); PW EV +16% (3yr). **Watch / Hold**; entry $65–78. |
| [LULU](wiki/tickers/LULU/LULU.md) | Active | 2026-05-01 | Decade-low P/E (~11.5×) on a brand mid-turnaround at new 52-wk low ~$138; Wilson DFAN14A proxy fight (Apr 29) + Bracey board appointment (Apr 28) add governance overhang into the 2026 Annual Meeting. PW EV $192 unchanged; R/R 2.6:1 at lower spot. **Watch / Initiate <$135 / Hold**. |
| [MP](wiki/tickers/MP/MP.md) | Active | 2026-05-01 | Strategic-asset rare-earth + magnetics platform at $66.04 (+9% post-Wedbush OP $90 + MS PT cut cluster); DoD 10-yr offtake + Apple/GM offtakes + 10X campus 2028 ramp intact; PW EV $80.50 unchanged but R/R compressed to ~1.7:1. **Initiate on dips $52–62; Hold at $66**; Q1 May 7. |
| [MSFT](wiki/tickers/MSFT/MSFT.md) | Active | 2026-05-01 | Q3 FY26 print confirmed Azure +40% / EPS $4.27 (+23%) but FY26 capex guide ~$190B (vs. ~$80–90B Street) drove –5–6% post-print sell-off to ~$414; Q3 thesis-break trigger DE-RISKED ✅. Quadruple BAIT preserved; PW EV $499 (+20% 3yr); R/R 1.7:1. **Initiate / 🟢 Hold-Add below $420**. |
| [NFLX](wiki/tickers/NFLX/NFLX.md) | Active | 2026-04-26 | Wide-and-widening global streaming at $93.24 (–30% post-split); FY26 op-margin guide 31.5% (+200bps); ad revenue inflecting $1.5B → $3B → $7B+ by 2028E; Triple BAIT; PW EV $119.50 (+28%, 3yr); R/R ~2.4:1. **Initiate (small, scaled)**; entry $80–88. |
| [NKE](wiki/tickers/NKE/NKE.md) | Active | 2026-04-26 | Wide-moat global brand at $44.69 (12-year low, 3.67% yield, 20-yr high yield); **CEO Hill bought $1M April 14**; first NA re-acceleration signal in Q3 FY26 (+3%); Triple BAIT; PW EV ~14%/yr total. **Initiate / Add**; entry $40–48. |
| [ONON](wiki/tickers/ONON/ONON.md) | Active | 2026-04-26 | Premium Swiss athletic brand compounding +23% c-c at record 62.8% GM at $36.25, mispriced by FX + tariff + leadership-transition (co-CEOs Mar 26); PW EV $53 (+46%); median analyst $60. **Initiate / Add**; Q1 May 12. |
| [PG](wiki/tickers/PG/PG.md) | Active | 2026-04-26 | Dividend King post-Q3 FY2026 print (Apr 24): first companywide volume growth in over a year cautiously validates Jejurikar recovery, but 6 consecutive quarters of GM compression keep conviction moderate; PW EV ~10% total return. **Watch / Hold**; Q4 late July. |
| [RH](wiki/tickers/RH/RH.md) | Active | 2026-04-26 | Luxury-home retailer at $137.51 (–46.5%) at deep cyclical trough; 2030 mgmt vision $5.4–5.8B revenue / 25–28% margins; weak Q1 FY26 guide + 35.6% short interest amplify both ways; PW EV $208 (+51%, 4yr). **Watch / selective Initiate / Hold**; entry <$115. |
| [RIVN](wiki/tickers/RIVN/RIVN.md) | Active | 2026-05-01 | Q1 2026 print delivered EPS beat (−$0.33 vs. −$0.63 Street), R2 saleable, $4.5B DOE loan + $2.55B VW+Uber capital lifting available liquidity to ~$8B; bear-tail dilution risk materially de-risked but stock −8% to ~$15.15 on R2 demand focus. Triple BAIT; PW EV ~$21.10 (+39% over 2yr); R/R 2.1:1. **Watch / Hold**. |
| [RKT](wiki/tickers/RKT/RKT.md) | Active | 2026-04-26 | Most complete U.S. homeownership super-platform (Redfin + Rocket + Mr. Cooper, Narrow-to-Emerging Wide moat) at ~13–15× FY26E EBITDA; market pricing the bear case while operating data confirms bull. PW EV $22.65 (+45%, 2–3yr); R/R ~3:1. **Initiate (Speculative) / Hold-Add**; Q1 May 7. |
| [SBUX](wiki/tickers/SBUX/SBUX.md) | Active | 2026-04-28 | **Niccol turnaround confirmed** — Q2 FY26 (Apr 28) printed +7.1% U.S. comp on **+4.3% transactions** with reduced discounting + op margin +110 bps; **FY26 guide raised to ≥5% comp / $2.25–$2.45 adj EPS**. PW EV ~$132 (+36% / ~11%/yr + 2.5% div); R/R ~3.2:1. 🟢 **Initiate-on-dip / Hold**; entry $90–97. |
| [SCHW](wiki/tickers/SCHW/SCHW.md) | Active | 2026-04-26 | Largest U.S. retail brokerage post-cash-sorting + TDA integration at $91.71; Q1 2026 BEAT with FY26 EPS guide raised >$5.70–$5.80; 19% dividend hike, $2.4B buyback executed; **Wide moat post-TDA**. Triple BAIT (B+A+I Strong); PW EV ~$108 (+18%, 18mo). **Initiate / Add**. |
| [SHOP](wiki/tickers/SHOP/SHOP.md) | Active | 2026-04-25 | Wide-and-widening moat commerce-infrastructure at $125.83 (30% US share, 3× Wix global); Q4 +30% rev / +29% GMV; **first-ever $2B buyback** at this zone is cleanest Tobi-Lütke intrinsic-value signal in 11 yrs; UCP + Agentic Storefronts = AI-commerce standard-setter. Triple BAIT; PW EV $212 (+68% 3yr); ~10:1 R/R. **Initiate / Add-Hold**. |
| [SN](wiki/tickers/SN/SN.md) | Active | 2026-04-26 | Serial-innovation consumer-products platform (Shark + Ninja) compounding +24% (FY24) / +18% (Q4 25) at expanding 17%+ adj EBITDA margins; ~100% US volume now manufacturable outside China — central tariff overhang largely de-risked; PW EV $144 (+24%); inaugural $750M buyback. **Initiate**. |
| [SPOT](wiki/tickers/SPOT/SPOT.md) | Active | 2026-05-01 | Q1 2026 print reset stock to $442 entry zone; post-print analyst cluster of 6+ target cuts (median $668→$607) compresses upside band but all revised targets remain above spot. Wide-moat fundamentals + BAIT + PW EV $540 unchanged; R/R ~3.5:1. **Watch / Initiate $400–450; Hold**. |
| [TREX](wiki/tickers/TREX/TREX.md) | Active | 2026-04-26 | Dominant U.S. composite-decking franchise (Narrow-and-widening moat, 50–60% composite share) at $41.90 (housing-cyclical trough); $200M buyback compounding at the bottom; PW EV $57 (+36%); R/R ~3.6:1. **Initiate (patient) / Hold**; entry $30–42. |
| [TSLA](wiki/tickers/TSLA/TSLA.md) | Active | 2026-04-26 | Three-engine platform (Auto + Energy + AI/Robotics optionality) at $376.30 / ~125× FY26E P/E — substantial autonomy success already priced; PW EV ~$393 ≈ spot, R/R ~1.4:1; widest dispersion in mega-cap U.S. equities ($24.86–$600 analyst range). **Hold / Watch**; entry $280–320. |
| [UBER](wiki/tickers/UBER/UBER.md) | Active | 2026-05-06 | Q1 2026 print (rev $13.2B slight miss / GB $53.7B +25% / Adj EBITDA $2.5B +33%; Q2 GB guide $56.3–57.8B above consensus) drove +5.93% pre-market to $77.32 from $72.95 (52-wk range $68–$102). Wide-moat platform at ~14× FY26E EV/EBITDA + 6.2% FCF yield while market prices AV-disintermediation that 30+ partnerships (Waymo/Zoox/Hertz-Nuro) actively defuse; record $3B Q1 buyback at 52-wk-low. Triple BAIT (B+A+I); PW EV $195 (+153% 5yr); R/R ~9:1 (~14:1 with Bull+ tail). **Initiate / Add**; entry <$85. |
| [UNH](wiki/tickers/UNH/UNH.md) | Active | 2026-04-28 | Wide-moat #1 managed care with **two reinforcing de-risks**: Q1 2026 BEAT (Apr 21, MCR 83.9%, FY26 guide >$18.25) **plus CMS 2027 MA Final Rate Notice ≈+2%** (Apr 28) — multi-billion FY27 EBIT tailwind; stock +≈14% in a week to ≈$368. Quadruple BAIT preserved; PW EV ~$447 (+21% / 24mo). **Initiate / Add**. |
| [WING](wiki/tickers/WING/WING.md) | Active | 2026-05-01 | Post-Q1 5-firm analyst cluster confirms thesis-weakening (Goldman Buy→Neutral $190; Mizuho/BMO/Wells Fargo PT cuts); consensus center-of-gravity reset to $190–$200, aligning with already-cut §11 Base. EBITDA/EPS resilience preserved but cyclical-vs-structural debate intact. **Watch / Reduce on bounce >$180**; next read = Q2 print late July. |
| [ZG](wiki/tickers/ZG/ZG.md) | Active | 2026-04-26 | Dominant U.S. real-estate marketplace at $45.41 (–51.6% from high) executing credible super-app pivot — Q4 25 rev +18%, FY25 +16%, Adj EBITDA margin 24%, FCF $420M; market pricing Rocket-Redfin narrative partly contradicted by $100M Zillow-Redfin rental syndication deal. Triple BAIT; PW EV ~$68 (+50%); R/R ~3:1. **Initiate / Add**. |

*38 tickers above. Last refresh: 2026-05-06 (UBER Workflow A ingest — Q1 2026 print: rev $13.2B / GB $53.7B +25% / Adj EBITDA $2.5B +33% / Q2 GB guide above consensus; +5.93% pre-market to $77.32; PW EV $195, R/R ~9:1, Initiate <$85). Prior weekly: 2026-05-01 (10 material / 27 quiet).*

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