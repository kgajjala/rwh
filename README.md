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
| [DASH](wiki/tickers/DASH/DASH.md) | Active | 2026-04-25 | Dominant U.S. food-delivery + global local-commerce platform at $176.78 (–38% from $285 peak); FY2025 GAAP NI $935M (7.6×); Deliveroo $3.9B closed Oct 2025; v2.6 letter arc + 10-K MD&A confirms thesis (Wolt-precedent execution lowers integration risk to 12–15%). **Watch / Hold (Add bias <$155); Q1 May 6 binary**. |
| [DELL](wiki/tickers/DELL/DELL.md) | Active | 2026-04-24 | AI-server beneficiary at $214.65 (near 52-wk high); FY27 +23% guide intact, but consensus median $185 sits *below* spot and Michael Dell entities sold ~$150M+ near highs in mid-April; PW EV $229 ≈ flat to spot. **Watch**. |
| [EBAY](wiki/tickers/EBAY/EBAY.md) | Active | 2026-04-24 | Re-accelerating marketplace at $97.94 (–8.8%, near highs); Q4 GMV +10% with ~6% combined buyback + dividend yield; fair value at consensus median; modest +17% PW EV asymmetry. **Watch / selective Initiate / Hold**. |
| [FIG](wiki/tickers/FIG/FIG.md) | Active | 2026-04-24 | Design-collaboration platform at $17.47 (–88% from post-IPO peak) under lock-up overhang + AI-disruption fear despite NDR 136% and 41% revenue growth; triple-overlap BAIT, PW EV +64% over 3yr; real existential AI risk. **Initiate (small, contrarian) / Hold-Add**. |
| [INTU](wiki/tickers/INTU/INTU.md) | Active | 2026-04-24 | Wide-moat vertical SaaS at $395.95 (17× FY26E EPS after –51% AI-fear drawdown); PW EV $566 (+43%). **Initiate / Add**. |
| [KGS](wiki/tickers/KGS/KGS.md) | Active | 2026-04-24 | Scale-leader U.S. compression (4.35M HP, 98% util) at $62.16 (fair value near 52-wk high after +83% 6-mo run); Single-overlap BAIT (A only); PW EV ~$72 (+15%, ~7–8%/yr incl. div). **Watch / Hold**. |
| [LLY](wiki/tickers/LLY/LLY.md) | Active | 2026-04-24 | Tirzepatide franchise (Mounjaro + Zepbound = $36.5B in 2025) with raised FY26 guide $80–83B; Triple BAIT (A+I-Strong). Q1 2026 prints April 30. **Initiate measured / Hold-Add on pullback**. |
| [LNTH](wiki/tickers/LNTH/LNTH.md) | Active | 2026-04-24 | Radiopharmaceutical / imaging at $84.33 (–22.6%); binary 2026 PDUFA event-setup (LNTH-2501 June, MK-6240 August) on PYLARIFY commoditization trough; modest +17% PW EV; 8.89% rising short interest. **Watch / Hold**. |
| [LULU](wiki/tickers/LULU/LULU.md) | Active | 2026-04-24 | Premium athleisure at $143.80 (–58% from high, at 52-wk low); brand-cycle vs. executional-trough question with new ex-Nike CEO O'Neill (Sept 8, 2026); Maestrini insider buy + China +29% constructive but FY26 EPS declining. **Watch / Initiate <$135 / Hold**. |
| [MP](wiki/tickers/MP/MP.md) | Active | 2026-04-24 | U.S. indispensable rare-earth platform at $60.73 with DoD 10-yr offtake + $110/kg floor + Apple/GM customers; PW EV $85 (+40%). **Initiate / Hold-Add**. |
| [MSFT](wiki/tickers/MSFT/MSFT.md) | Active | 2026-04-24 | Deepest-moat mega-cap (productivity + Azure + AI) at $432.92 (–22% drawdown); **Quadruple BAIT overlap (B/A/T Strong + I Mod) — likely cleanest mega-cap setup in wiki**; PW EV ~$565 (+31% / ~10%/yr); April 29 Q3 FY26 print. **Initiate / Hold-Add**. |
| [NFLX](wiki/tickers/NFLX/NFLX.md) | Active | 2026-04-24 | Subscription video at $93.24 (post-10:1-split, –30% from highs); Q1 2026 rev $12.25B beat, 325M+ subs, $3B 2026 ad target on track; light Q2 guide drove –9.7% selloff April 17; PW EV $119.50 (+28%) over 3 years. **Initiate (small, scaled)**. |
| [NKE](wiki/tickers/NKE/NKE.md) | Active | 2026-04-24 | Athletic-footwear icon at $44.69 (12-year low, –44% from high); Hill turnaround Q3 NA +3% early signal, **CEO bought $1M April 14**; 3.6% dividend yield (20-yr high); triple-overlap BAIT, PW EV ~14%/yr total return. **Initiate / Add**. |
| [ONON](wiki/tickers/ONON/ONON.md) | Active | 2026-04-24 | Premium athletic brand at $36.25 compounding 23%+ c-c at 63% gross margin, mispriced by FX/tariff macro; PW EV $53 (+46%). **Initiate / Add**. |
| [PG](wiki/tickers/PG/PG.md) | Active | 2026-04-24 | Dividend King in "show me" mode under new CEO Jejurikar mid-restructuring; **Q3 FY2026 earnings April 24 = TODAY** — the binary catalyst that confirms or refutes execution. **Watch / Hold pre-print**. |
| [RH](wiki/tickers/RH/RH.md) | Active | 2026-04-24 | Luxury-home retailer at $137.51 (–46.5%); deep cyclical trough with 2030 management vision of $5.4–5.8B / 25–28% margins; PW EV $225 (+64% over 4 yrs); leverage amplifies both ways. **Watch / selective Initiate / Hold**. |
| [RIVN](wiki/tickers/RIVN/RIVN.md) | Active | 2026-04-24 | EV maker at $16.95; R2 production started April 22 days after a tornado hit Normal, IL; Q1 deliveries 10,365 beat 9,678 cons; VW JV implicitly worth ~$5/share; PW EV $19.40 (+14%); 13.55% short interest creates squeeze potential on April 30 print. **Watch / small Initiate**. |
| [RKT](wiki/tickers/RKT/RKT.md) | Active | 2026-04-24 | Integrated homeownership platform (Redfin + Mr. Cooper + Rocket Mortgage) post-Up-C collapse at $15.60; PW EV $22.65 = +45% over 2–3yr. Q1 print April 30. **Initiate (Speculative) / Hold-Add on weakness**. |
| [SBUX](wiki/tickers/SBUX/SBUX.md) | Active | 2026-04-24 | Coffee-retail icon at $98.67 (+30% off low, ~3% off 52-wk high); Niccol turnaround mid-stride with Q1 FY26 inflection (first U.S. txn growth in 8 quarters); PW EV +17% over 3yr, BAIT single-overlap. **Watch / Hold** ahead of binary April 28 print. |
| [SCHW](wiki/tickers/SCHW/SCHW.md) | Active | 2026-04-24 | Q1 2026 BEAT (Apr 16) with FY26 EPS guide raised >$5.80; record revenue/NNA/DARTs. Stock printed a fresh 52-wk low *the day after* the beat — cleanest behavioral mispricing in the wiki. Triple BAIT (B+A+I-Strong). **Initiate / Add**. |
| [SHOP](wiki/tickers/SHOP/SHOP.md) | Active | 2026-04-25 | Wide-and-widening moat commerce-infrastructure at $125.83; Q4 +30% rev / +29% GMV; **first-ever $2B buyback** at this zone is cleanest Tobi-Lütke intrinsic-value signal in 11 yrs as public co; v2.7 5-yr Item 1A arc surfaces 2023 AI-risk addition as 1-yr leading indicator of Agentic Storefronts. Triple BAIT; PW EV $212 (+68% 3yr). **Initiate / Add-Hold**. |
| [SN](wiki/tickers/SN/SN.md) | Active | 2026-04-24 | Consumer-products / appliances at $115.74 (–14% from highs); FY26 guide +10–11% sales / $5.90–6.00 adj EPS; consensus median ~$148 (+28%); 9.6% short interest; 3-year PW EV $144 (+24%) with bull asymmetry. **Initiate**. |
| [TREX](wiki/tickers/TREX/TREX.md) | Active | 2026-04-24 | Composite-decking category leader at $41.90 (housing-cyclical trough) with $200M buyback; PW EV $57 (+36%). **Initiate / Hold**. |
| [TSLA](wiki/tickers/TSLA/TSLA.md) | Active | 2026-04-24 | EV/AI leader at $376.30 (–25% from highs); Q1 2026 GM 21.1% + FCF $1.44B beat (vs. –$1.57B cons), but 50K inventory build is yellow flag; Cybercab production "officially begun" April 24; PW EV $393 ≈ flat to spot — coin-flip risk-reward. **Hold / Watch**. |
| [UNH](wiki/tickers/UNH/UNH.md) | Active | 2026-04-24 | Q1 2026 BEAT (Apr 21) — Adj EPS $7.23 vs. $6.59 cons. (+9.7%); MCR 83.9% (vs. 84.8%); FY26 adj EPS guide raised >$18.25. Quadruple BAIT preserved with B-compressed post-recovery. **Initiate / Add**. |
| [WING](wiki/tickers/WING/WING.md) | Active | 2026-04-24 | Asset-light franchise QSR at $189 (–51% from $388 peak); Q3 (–5.6%) + Q4 2025 (–5.8%) SSS technically activated the prior thesis-break trigger, but Citi upgraded to $230 on H2 recovery. Q1 print April 29 = binary. **Watch / Hold**. |
| [ZG](wiki/tickers/ZG/ZG.md) | Active | 2026-04-24 | Dominant U.S. real-estate marketplace at $45.63, mispriced by Rocket-Redfin narrative while Mortgages +39% / Rentals +45%; PW EV $69 (+51%). **Initiate / Add**. |

*35 tickers above. Last refresh: 2026-04-25 (BRK.B initial ingest under Workflow A).*

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
