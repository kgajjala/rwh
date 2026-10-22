# SpaceX–Tesla: How the Exchange Ratio Gets Set

*Cross-ticker study · 2026-10-21 · prices as of the Oct 20, 2026 close. Feeds the merger optionality line in [SPCX](../tickers/SPCX/SPCX.md) and [TSLA](../tickers/TSLA/TSLA.md). Analysis, not personal investment advice; no position sizing.*

## The event

On SpaceX's Q3 2026 call on October 20, Elon Musk confirmed that both boards have formed special committees of independent directors to look at combining the companies. He is recused, and no terms exist ([transcript](../../raw/SPCX/transcripts/2026-10-20_Q3-2026_call.txt)):

> "Both SpaceX and Tesla have formed special committees to discuss this idea at the request of shareholders... because I'm a conflicted party, I can't actually be in the discussions of the special committees... some people out there assume that a SpaceX and Tesla merger is a certainty. And I think that would be overstating it... on the Tesla side, we will need a 50% vote of all shares, not just those who vote."
> — Elon Musk, SpaceX Q3 2026 earnings call, October 20, 2026

Barclays and RBC both expect SpaceX to acquire Tesla for stock ([Barclays via INDmoney](https://www.indmoney.com/blog/us-stocks/tesla-spacex-merger-barclays-shareholder-impact), [RBC via MarketWatch/iTiger](https://www.itiger.com/news/2649858934)). In that structure Tesla is the target. Its holders are the sellers whose vote decides the deal, and the premium, if there is one, goes to them. Tesla's 2026 proxy, filed October 19, sets the annual meeting for December 3 with no merger item on the agenda ([DEF 14A excerpts](../../raw/TSLA/filings/2026-10-19_DEF14A_excerpts.txt)).

## Inputs, on economic shares

Both headline share counts include unvested Musk performance shares that carry votes but not, today, economics:

| | Tesla | SpaceX |
|---|---|---|
| Price, Oct 20 close | $373.71 | $147.79 |
| Shares outstanding (headline) | 3.953B | 13.579B |
| of which unvested Musk performance shares | 423.7M (2025 CEO award, voted proportionally) | 1,302.1M Class B (Mars-colony and orbital-compute awards) |
| Diluted economic shares used here `[Derived]` | **3.54B** | **12.7B** |
| Economic market value | $1.32T | $1.88T |
| Cash and investments / net cash | $45.4B / $35.9B after debt and finance leases (Sep 30, Q3 Update) | $89.9B / $51B (Sep 30) |
| Musk's economic stake `[Derived]` | 19.8% (proxy) | ≈42% (prospectus, adjusted for Cursor) |
| Musk's voting power | 19.8% | ≈84% |

Sources: [Tesla proxy](../../raw/TSLA/filings/2026-10-19_DEF14A_excerpts.txt), [SpaceX prospectus](../../raw/SPCX/filings/2026-06-12_424B4_excerpts.txt), [SpaceX Q3 release](../../raw/SPCX/press-releases/2026-10-20_Q3-2026_release.txt), [Tesla XBRL](https://data.sec.gov/api/xbrl/companyfacts/CIK0001318605.json).

On a change in control of Tesla, the 2025 award's unearned shares vest only for market-cap milestones actually reached, the first at $2T. Everything else is forfeited. At deal values near $1.4–1.6T, none would vest. The 2018-award restricted shares accelerate, but they are already outstanding. Electrek's claim that the award would be "delivered automatically" in a merger does not match the proxy text.

## The football field (ratio = SpaceX shares per Tesla share)

| Method | Ratio | Tesla share of combined |
|---|---|---|
| Daily ratio since the SpaceX IPO (Jun 12) | 1.91 – 3.24 | 35–48% |
| VWAP, 20 to 90 trading days | 2.37 – 2.48 | 40–41% |
| **30-day VWAP (the anchor)** | **2.39** | **40%** |
| Oct 20 close / overnight indication | 2.53 / ≈2.36 | 41% / 40% |
| Analyst consensus targets ($398 / $223) | 1.79 | 33% |
| Wiki PW EVs ($295 / $221) | 1.34 | 27% |
| FY2027E revenue contribution (consensus; SpaceX at its Q1 2027 guide) | 3.0 – 3.6 | 46–51% |
| Run-rate adj. EBITDA / FY2027E net income contribution | 1.1 – 1.3 | 24–27% |

Contribution analysis brackets everything. Revenue says 50/50, while profit says Tesla deserves a quarter, because a dollar of Tesla revenue earns about a quarter of what a dollar of SpaceX revenue does. Public stock-for-stock deals are priced at **market ratio plus a negotiated premium**. The intrinsic and contribution figures are what each committee uses to argue.

## Four outcome models

| Model | How the ratio is set | Premium to Tesla | Ratio | Tesla : SpaceX | Probability |
|---|---|---|---|---|---|
| 1. At-market merger of equals | 30-day VWAP; Musk-family precedent (X/xAI 2025, SpaceX/xAI 2026 at 0.1433) was done at marks with no premium | 0–5% | 2.39–2.51 | 40–41 : 59–60 | 30% |
| **2. Market + control premium** | VWAP plus a premium for moving Tesla holders into a dual-class company Musk controls | **10–20%** | **2.63–2.87** | **42–44 : 56–58** | **45%** |
| 3. Full takeover premium | A standard public-target premium; RBC suggests 20–30% | 25–35% | 2.99–3.23 | 45–47 : 53–55 | 15% |
| 4. Earnings-based, SpaceX-favoured | Tesla priced below market on forward-profit contribution | −10% | 2.15 | 38 : 62 | 10% |

**Why I picked Model 2 as the most likely:**
- **The Tesla vote is the gate.** It needs 50% of all outstanding shares. Tesla's committee has to show its holders something for giving up one-vote stock in a company where Musk holds 19.8% for low-vote stock in one he controls.
- **Tesla has real leverage.** It brings about $36B of net cash and a profitable storage business to a company guiding to $35–40B of capex in a single quarter.
- **Three things cap the premium below a full takeover premium:**
  - No outside bidder exists.
  - Musk owns about twice as much of SpaceX as of Tesla. Each point of the combined company shifted to Tesla holders costs him roughly $7B, so his economic pull runs the other way.
  - Both companies are Texas corporations, where a committee-approved deal gets a statutory safe harbor. That weakens the litigation threat that usually pushes premiums up.

**Probability-weighted terms: about 2.66 SpaceX shares per Tesla share (an ≈11% premium), or 42/58.**
- **40/60** is approximately today's no-premium market split.
- **50/50** would need a 50% premium, which I treat as a tail outcome.

## What each side gets

I assume the combined value equals the sum of the parts. The synergies are compute, Terafab (already a three-way initiative with Intel per the prospectus), Megapacks (Tesla sold $430M of them to xAI in 2025), Starlink in vehicles, and capital access. Against them sit a controlled-company discount, index frictions, and Tesla's cash going into SpaceX's capex. I assume the two roughly offset.

| Model | Tesla holders | SpaceX holders |
|---|---|---|
| 1. At-market (+2.5%) | +1.5% | −1.0% |
| 2. Control premium (+15%) | +8.5% | −5.7% |
| 3. Full premium (+30%) | +16.1% | −10.7% |
| 4. SpaceX-favoured (−10%) | −6.3% | +4.2% |
| **Probability-weighted, if it closes** | **+6.0%** | **−4.0%** |
| If it breaks (speculation unwinds) `[Estimate]` | −6% | +2% |
| **Weighted by a 65% chance of closing** | **≈ +2%** | **≈ −2%** |

I put closing at 65%: 75% that terms get signed, times 87% that a signed deal clears the vote and CFIUS. Tesla's China plants and SpaceX's classified work make national-security review the non-trivial step. For comparison, Kalshi priced about 50% for a close before May 2027 ([NewsBytes](https://www.newsbytesapp.com/news/business/kalshi-traders-raise-tesla-spacex-merger-odds-to-56/tldr)), and Munster says 90–95% within two years.

## Conclusion

The merger moves value between the two sets of holders; it creates little on its own. If the deal closes on probability-weighted terms, Tesla holders beat SpaceX holders by about 10%. Weighted for the chance it breaks, the edge is 2–4%, smaller than either stock's typical daily move.

Each report carries this as an optionality line: about +$16 a share for Tesla and −$8 for SpaceX, each at 65%. Neither line changes a verb.

The real arbitrage starts only when definitive terms fix a ratio. Before that, owning Tesla to capture the merger is a bet on the premium. And if the deal closes, a Tesla holder's five-year return becomes the combined company's: on these two reports' models, roughly 40% Tesla and 60% SpaceX.

**What would change this:**
- Definitive terms at a premium of 5% or less remove Tesla's edge.
- A majority-of-the-minority vote condition makes Models 2–3 more likely.
- A Tesla print that resets the market ratio before signing moves the anchor itself, and it moves both sides.

*Sources: [SpaceX Q3 2026 call](../../raw/SPCX/transcripts/2026-10-20_Q3-2026_call.txt) · [CNBC live blog](https://www.cnbc.com/2026/10/20/spacex-spcx-earnings-live-updates-q3-2026html.html) · [Electrek](https://electrek.co/2026/10/20/tesla-and-spacex-take-first-step-towards-merger-would-dilute-all-shareholders/) · [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262227845-) · [xAI merger terms](https://www.implicator.ai/spacex-acquires-xai-in-1-25-trillion-deal-creating-worlds-most-valuable-private-company/) · [Yahoo SPCX](https://finance.yahoo.com/quote/SPCX/) · [Yahoo TSLA](https://finance.yahoo.com/quote/TSLA/) · [StockAnalysis TSLA forecast](https://stockanalysis.com/stocks/tsla/forecast/) · [StockAnalysis SPCX forecast](https://stockanalysis.com/stocks/spcx/forecast/). VWAPs computed from Yahoo daily closes and volumes.*
