# SN — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.9 Retrofit (Schema Migration + Primary-Source Refresh)

**Trigger**: Single-ticker serial v2.9 retrofit run. Migration from v2.5 (15 sections + standalone Moat block) → v2.9 (13 sections; old §1 retired; old §3 + §4 merged into new §2; Moat consolidated into §3 with mandatory Competitive Landscape per Rule #24).

**Sources reviewed**:
- [SharkNinja Q4 2025 / FY2025 press release](https://newsroom.sharkninja.com/sharkninja-reports-fourth-quarter-and-full-year-2025-results/) (Feb 11, 2026)
- [SharkNinja Q4 2025 earnings call transcript](https://www.fool.com/earnings/call-transcripts/2026/02/11/sharkninja-sn-q4-2025-earnings-call-transcript/) — Mark Barrocas + CFO Adam Quigley prepared remarks + Q&A
- [SharkNinja Q4 2024 / FY2024 release](https://newsroom.sharkninja.com/sharkninja-reports-fourth-quarter-and-full-year-2024-results/) (FY2024 verified: net sales $5.53B +30%, adj EBITDA $951M, 17.2% margin)
- [Yahoo Finance live price](https://finance.yahoo.com/quote/SN) (2026-04-24 close $115.74; markets closed weekend Apr 25–26)
- [SEC EDGAR FY2024 20-F HTML](https://www.sec.gov/Archives/edgar/data/1957132/000195713225000006/sharkninja-20241231.htm) — direct fetch returned 403; tagged `[link pending]`
- [stockanalysis.com / MarketBeat / TipRanks / Daily Political](https://www.marketbeat.com/stocks/NYSE/SN/) — analyst consensus, short interest, insider activity refresh
- Pattern note + Q4 2025 quote file written to `raw/SN/shareholder-letters/PATTERN-NOTE.md` and `raw/SN/transcripts/Q4-2025-call-2026-02-11-key-quotes.md`

### What Changed (mirroring v2.9 §1–§13 refresh)

- **Schema header**: v2.5 → v2.9; Last Updated 2026-04-25 → 2026-04-26.
- **Summary**: rewritten to ≤10 emoji-tagged bullets per Rule #18; added moat verdict line + capital-allocation signal line (inaugural $750M buyback).
- **Business Overview**: clarified SN is a Cayman foreign private issuer (files 20-F, not 10-K) — public since July 2023 spin from JS Global Lifestyle. Brand-level franchise expanded.
- **Pivotal Investment Question**: re-framed around the *operationally de-risked* China overhang ("~100% US volume can now be made outside China") rather than open-ended tariff risk.
- **§1 Annual Financial Metrics**: refreshed FY2024 to verified $5.53B / $951M / 17.2% margin (prior wiki had ~$5.5B / ~$890M / ~16% — now corrected to primary-source numbers); added cash $777M and inaugural buyback row to Key Stats.
- **§2 Revenue Mix & Geographic Split** (merged from old §3 + §4): added forward-looking direct-operator transitions + 2H 2025 intl +23.2% vs 1H +17.3%.
- **§3 Competitive Moat & Landscape**: NEW combined section per Rule #24. Added named-peer table (NWL, HELE, WHR, IRBT, BRG, COOK, Dyson, De'Longhi, Conair) with category overlap, share, threat vector, and explicit "how SN's moat differs" framing.
- **§4 Management & Leadership**: 🔴 **CFO correction — was incorrectly listed as "Patraic Reagan" in v2.5; corrected to Adam Quigley** (verified from Q4 2025 call). Added CJ Xuning Wang chairperson role. Added Recent Management Commentary subsection with verbatim Barrocas quotes from Q4 2025 call (Pattern C — no standalone letter; sub-5-yr coverage applies). Added multi-year strategic-framework arc (FY2023 → FY2026 guide).
- **§5 Strategic Growth Initiatives**: re-anchored to "manufacturing diversification — already executed" (top initiative) rather than "in progress."
- **§6 Key Risks**: Rule #25 materiality filter applied. **Down-weighted tariff escalation** (Medium-High vs. prior High; explicitly noted operational pivot has neutralized most of risk). **Added supply-chain transition cost-overrun** as a Rule #25(d) "large discretionary investment" risk and tagged "not priced in" in Notes. Replaced 5-year RF evolution table with 2–4 sentence synthesis paragraph (Rule #21).
- **§7 Industry Macro**: re-framed China-tariff sensitivity given operational pivot.
- **§8 Valuation**: refreshed comp set with tickers (NWL / HELE / WHR / YETI / COOK / BRG); EV/EBITDA at ~12.5× (vs prior ~13×) reflecting cash-buildup.
- **§9 Catalyst & Sentiment Tracker**: refreshed price/52-wk/short interest (corrected: ~3.7% per stockanalysis.com — prior 9.6% likely a labeling artifact); insider activity (added Quigley March 2026 small open-market sale); upcoming catalysts. Q4 2025 buyback authorization moved into Recent Corporate News.
- **§10 BAIT**: A lens upgraded to Moderate-Strong on the supply-chain-out-of-China analytical edge being structurally under-modeled by sell-side.
- **§11 Bull / Bear / Base**: probabilities preserved (30 / 50 / 20). Bull narrative now includes "$750M buyback executed at <$130 average" as a precondition.
- **§12 PW EV**: PW EV ~$144 (unchanged); added Rule #26-compliant R/R interpretation (~1.9:1 Bull/Bear; honest framing — favorable but not extreme).
- **§13 Recommendation**: thesis sentence rewritten to highlight the de-risked China pivot + inaugural buyback. Thesis-break triggers updated: dropped pure tariff trigger; added "Pause / removal of $750M buyback authorization" + tariff trigger now compound-conditional.

### Thesis Status

- **Overall**: 🟢 **Strengthened** vs. pre-v2.9 baseline. Same Initiate verb, same price targets — but the underlying support is materially better understood: the central thesis-risk (China-tariff overhang) has been operationally neutralized in a way the multiple does not yet reflect.
- **BAIT delta**: A lens upgraded Moderate → Moderate-Strong (sell-side under-modeling of supply-chain pivot). Triple-lens overlap retained; conviction Moderate-High.
- **Price target delta**: Bull / Base / Bear unchanged at $185 / $145 / $80; PW EV ~$144 unchanged.
- **Catalyst & Sentiment delta**: Inaugural $750M buyback (new); CFO correction (Quigley); short-interest figure corrected to 3.7%.

### Recommendation

- **For a non-holder**: 🟢 Initiate — preferred at $115.74; entry zone $95–105 for adding on weakness.
- **For a current holder**: 🟢 Hold / Add on weakness <$105.

**Next review trigger**: Q1 2026 earnings (early May 2026, estimated). Key items: tariff impact on 1H GM; buyback execution detail; international growth rate vs 2H 2025 +23.2%; commentary on two new 2026 categories.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added SN (SharkNinja) to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- SharkNinja Q4 2025 / FY2025 press release (IR, February 11, 2026)
- Q4 2025 earnings call transcript (Motley Fool, Investing.com)
- Yahoo Finance live price (2026-04-24)
- MarketBeat short interest data (April 2026)
- Public.com / TipRanks / WallStreetZen / Investing.com analyst consensus
- JPMorgan PT cut to $144 (April 17, 2026)
- Jefferies $200 Buy reaffirmation
- stocktitan.net Form 4 filings (April 16, 2026; Feb 28, 2026)

### What Changed
- Initial compilation; no prior wiki content
- Live price verified $115.74 (Yahoo Finance, April 24, 2026 close)

### Thesis Status
- **Overall**: Initiated — Initiate verdict for non-holders; Hold/Add on weakness for holders
- **BAIT signal**: Triple-lens (A moderate-strong; B + I + T moderate); Conviction Moderate-High — strongest setup in the 5-ticker Group C batch
- **PW EV**: ~$144 (3-yr) vs. $115.74 spot → +24% (~7.5%/yr) — favorable asymmetry

### Recommendation
- **For a non-holder**: Initiate; $95–105 attractive entry on weakness
- **For a current holder**: Hold / Add on weakness below $105

**Next review trigger**: Q1 2026 earnings (early May 2026, estimated)
