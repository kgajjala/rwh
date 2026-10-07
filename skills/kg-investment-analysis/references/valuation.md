# Valuation: §5 and the Verdict

Contents:
1. Method by situation
2. Scenarios and the 3P sort
3. Discount rates and terminal values
4. The EPV floor
5. Cyclicals: normalized margins
6. Financials: justified P/TBV
7. Early growth: sales-to-capital, funding and the reflexive Bear
8. Ruin paths and failure odds
9. Sum of the parts
10. Return-math table (fixed row order)
11. Break-even and price-implied Bear odds
12. Base rates for sales growth
13. Worked example

---

## 1. Method by situation

| Situation | Valuation primary | Floor | Warranted-multiple check | Extra line on the page |
|---|---|---|---|---|
| Mature compounder | Owner earnings × multiple | EPV | Implied terminal growth (section 3) | — |
| Mature ex-growth | EPV, with owner earnings × multiple as a cross-check | Asset value / tangible book | Multiple ≈ 1 ÷ r plus inflation-only growth | Yield carries the return |
| Cyclical | Normalized EBIT × mid-cycle multiple | EPV on normalized earnings | On normalized earnings | Cycle position |
| Financial (bank, broker, insurer, lender) | Justified P/TBV from ROTE | Tangible book | (ROTE − g) ÷ (r − g) | ROTE vs. cost of equity |
| Early growth | Revenue × target margin × multiple, with the funding need from sales-to-capital | Failure-weighted value | Implied terminal growth ≤ 10-yr Treasury | Funding need and dilution |
| Multi-segment, different asset types | Sum of the parts | Sum of segment floors | Per segment | Gap to the consolidated multiple |
| Turnaround | EPV on restored margins × the odds they are restored | The survival case | — | Piotroski trend |

Multiples (P/E, EV/EBITDA, P/FCF, EV/sales) and a 2–3 peer table sit above the scenario table as the anchor. A multiple never stands in for the valuation.

## 2. Scenarios and the 3P sort

- **Shape.** Build three scenarios (🐂 Bull, 📊 Base, 🐻 Bear) at a five-year horizon, with probabilities that sum to 100%. Typical weights are Bull 20–30%, Base 45–55% and Bear 20–30%. Departing from them is fine; say why.
- **Driving assumption.** Each scenario names its driving assumption and its terminal math, written as `[Year] owner earnings or EPS $X × Y = $Z per share`.
- **Bear.** The Bear names a mechanism, such as "price cuts buy share but never margin", never just "macro worsens".
- **3P sort** (Damodaran: is it possible, plausible, probable?):

| Tier | Where it goes | Test |
|---|---|---|
| Possible | **Optionality line** (probability × value), outside the core | It could happen, but fewer than 5% of companies this size have done it (section 12) |
| Plausible | Bull | The growth rate clears the 5% base-rate floor |
| Probable | Base | It reconciles to the reinvestment math (ROIIC × reinvestment rate, from `business-quality.md`) or names the lever (price, mix, margin) that supplies the gap, and sits near the middle of the reference class |

  The part of a story that is only possible moves to the optionality line, so the core case can be read without it.

- **Competence = Outside.** Bull ≥ 25%, Bear ≥ 25%, Base ≤ 50%. The Bear includes the binary failure outcome, and add a confidence note.
- **Cyclical = Yes.** Every scenario's terminal value uses the normalized margin (section 5).

## 3. Discount rates and terminal values

- **Discount rate *r*** (used for EPV, implied expectations and the terminal-growth check):
  - 8%: wide-moat staples and utilities;
  - 9%: platforms and quality compounders;
  - 10–11%: cyclicals, turnarounds and capital-intensive businesses.
- **Hurdle.** The 13% hurdle is separate: it is the bar the PW return must clear.
- **Terminal values.** Prefer owner earnings per share × multiple. If the target is written in P/E, convert using the company's owner-earnings conversion, which is owner earnings ÷ core net income averaged over five years.
- **Terminal-growth check** (Damodaran caps perpetual growth at the risk-free rate). For a terminal multiple M of next-year owner earnings, the implied perpetual growth is:

  g = (M · r − 1) ÷ (M + 1)

  - g must be **≤ the 10-year Treasury yield** (FRED `DGS10`); flag any scenario that breaks this.
  - g must also be **consistent with the scenario's story**: a Bear that says "growth stops" cannot carry a multiple implying 3% growth forever.
  - Show g for every scenario in the return-math table.

## 4. The EPV floor (Greenwald)

- **Definition.** Earnings power value is sustainable earnings capitalized with no growth.
  - Equity basis (simplest): **EPV per share = normalized owner earnings ÷ r ÷ diluted shares**. Normalize by averaging five years of owner earnings, or by applying a through-cycle margin.
  - Enterprise basis (cross-check): (normalized EBIT × (1 − t) + D&A − maintenance capex) ÷ r − net debt (including leases), divided by shares.
- **Franchise test.** If invested capital is close to reproduction cost, EPV ÷ invested capital ≈ ROIC ÷ r. A ratio well above 1 means a franchise. Near 1 means returns have been competed away, and then **growth is worth nothing**, because new capital earns only its cost.
- **Growth share of price** = 1 − EPV ÷ price. This is how much of today's price pays for growth.
- **Rules for the Bear:**
  - A Bear at EPV says growth stops and the franchise holds. That is the natural floor for a business with a moat.
  - A Bear that says growth stops must be valued at or near EPV. If it sits above EPV, the scenario must state the growth it still assumes (for example "inflation-only, 2%, after year five") and pass the terminal-growth check.
  - A Bear below EPV must name what damages today's earnings power: a lost customer, a price war, a structural reset in margins.
  - On a Moat: None page, the Bull cannot be built on growth alone.
- **Mature ex-growth.** For this stage, EPV is the valuation primary.

## 5. Cyclicals: normalized margins

- **Flag.** Set Cyclical = Yes when either holds:
  - the asset type is cycle-exposed: industrial materials, capital-intensive OEM, semiconductor equipment, mortgage and housing finance, logistics, housing-linked retail, energy, commodities;
  - over the last ten years, operating margin swung by more than half of its median (max − min > 0.5 × median), or revenue fell 10% or more in any year for macro reasons.
- **Cycle position.** This is a §1 line: the current operating margin as a percentile of its 10-year range, with the median. Use a scaled ratio (margin), not an average of absolute earnings.
- **Terminal values.** All three scenarios apply the **normalized margin** (10-year median, or the sector's through-cycle average when the company's history is short) to terminal revenue.
  - The scenarios differ in the normalized *level* (a structural improvement in the Bull, a structural reset in the Bear), not in where year five happens to fall in the cycle.
  - A Bull that keeps an above-median margin must point to the §2 lever that makes it structural.
- **Commodity prices.** Use the futures curve for the near term, and a normalized real price for the terminal year, rather than your own forecast.
- **Multiples row.** Show P/E and EV/EBIT on normalized earnings next to the reported ones. A cyclical looks cheapest on reported P/E at the peak (Lynch).

## 6. Financials: justified P/TBV

- **Why it differs.** For banks, brokers, insurers and lenders, debt is raw material, so EV multiples and ROIC break down. Value the equity instead.
- **Formula:** **P/TBV = (ROTE − g) ÷ (r − g)**, where g = ROTE × retention and reinvestment is the capital regulators require.
- **Examples** at r = 10%: ROTE 12% with g 4% → 1.33×; ROTE 18% with g 5% → 2.6×; ROTE 25% with g 6% → 4.75×.
- **Terminal multiple.** Each scenario's terminal P/TBV is the one that scenario's terminal ROTE justifies.
- **Insurers.** Add float growth and the cost of float to the driver tree.

## 7. Early growth: sales-to-capital, funding and the reflexive Bear

- **Reinvestment need.** Reinvestment = Δ revenue ÷ (sales ÷ invested capital). Use the company's or the sector's sales-to-capital ratio, which is steadier than capex. For example, revenue from $5B to $15B at a ratio of 1.5 needs about $6.7B of reinvestment.
- **Funding need** = reinvestment − cumulative operating cash flow over the period. If it is positive, the scenario needs outside capital.
- **Reflexive loops (Soros).** In some businesses a falling share price damages the business itself:

| Loop | Mechanism |
|---|---|
| Funding | Equity has to be raised; the lower the price, the more shares it takes. |
| Talent | High SBC; underwater awards mean more shares or more cash pay. |
| Activity | Revenue tracks market prices or trading (brokers, exchanges). |
| Confidence | Customers, suppliers or lenders treat the price as a signal of viability. |
| Currency | The acquisition strategy is funded with stock. |

  Where any loop applies, the Bear must be reflexive:
  - **Bear value per share = (Bear equity value − outside capital the Bear requires) ÷ current shares.**
  - If the capital would have to be raised below value, the cost is higher. For example: Bear equity of $6B, 1.0B shares and $2B to raise give $4.00 per share, not $6.00; a forced raise at $3 gives $3.60.
  - Name the loop in the §6 risk table.

## 8. Ruin paths and failure odds

- **Ruin paths.** A ruin path is an irreversible outcome that wipes out the equity:
  - an unfunded debt maturity inside five years;
  - a covenant;
  - a license that could be lost;
  - a customer whose loss would take most of the profit with it.
- **Bear value.** Where a ruin path exists, the Bear's value is what the equity would be worth after the ruin, often close to zero, not a trough multiple applied to trough earnings.
- **Explicit failure odds.** For early-growth or heavily levered companies, add a separate failure line: value = going-concern value × (1 − p_fail) + distress value × p_fail.

## 9. Sum of the parts

Use this when segments fall under different asset types.
1. For each segment, build its driver tree and use the valuation primary for its type.
2. Capitalize corporate costs at the consolidated multiple and deduct them.
3. Deduct net debt.
4. Apply a holding-company discount only where capital is trapped or governance blocks its release.
5. Reconcile the total to the consolidated multiple and explain the gap.

## 10. Return-math table (fixed row order)

| Row | Content |
|---|---|
| PW return/yr vs. hurdle | `(PW EV ÷ spot)^(1/5) − 1 + yield`, marked `≥13%` or `<13%`. Then Entry. Then, as context, the 10-year Treasury and the spread from 13% to it. |
| Compounding at a flat multiple | Owner-earnings (or core EPS) growth per share in the Base case, plus shareholder yield (dividend + net buyback). State what share of the Base return comes from re-rating. Re-rating above half the return means Watch. |
| Optionality | Probability × value per share, so the core reads without it; or "none". |
| Price-implied expectations | Perpetual: g = r − (unlevered FCF ÷ EV). Or two-stage: the 5-year growth that, followed by inflation-level terminal growth, equates PV to EV. State r. |
| EPV floor | EPV per share, growth share of price, and where the Bear sits relative to EPV. |
| Base rate / 3P | Where the Bull growth rate sits in section 12, and the 3P tier of each scenario. |
| Terminal-growth check | Implied g for each scenario versus the 10-year Treasury, and whether each fits its story. |
| Break-even and price-implied Bear odds | Section 11. Flag "probability-fragile" when the break-even odds are within 10 points of the assigned odds. |
| Year ten | One sentence: is the business still growing at year ten (runway from §2), or is the terminal multiple doing the work? |
| R/R | (Bull % upside) ÷ (Bear % downside) against spot. Use this one figure everywhere. Note when it is mechanically flattered, for example when spot sits just above the Bear. |

## 11. Break-even and price-implied Bear odds

Scenario probabilities are the least reliable input on the page, yet the verb depends on them. These two numbers show how far the probabilities can move before the verb changes.

Hold the Bull-to-Base mix fixed and let only the Bear's share vary:

- V_nb = (p_bull · Bull + p_base · Base) ÷ (p_bull + p_base)
- p*_bear(h) = (V_nb − spot · (1 + h − y)^5) ÷ (V_nb − Bear)

Read it two ways:
- **Break-even Bear odds** (h = 13%): the highest Bear probability at which the PW case still clears the hurdle.
- **Price-implied Bear odds** (h = r, the page's discount rate): the Bear probability at which today's price earns an ordinary return. This is a reverse DCF expressed in scenario terms, and it is The Call's one-number statement of what the market is pricing.

Results above 100% or below 0% mean that no Bear probability makes the equation hold; report them as ">100%" or "<0%".

## 12. Base rates for sales growth

The table shows the share of companies that achieved each **real** compound sales growth rate, by starting sales bucket. Source: Mauboussin, *The Base Rate Book* (Credit Suisse HOLT, 2016). The 10-year sample has about 59% survivorship, so the true odds are lower than shown.

| Sales bucket | Horizon | ≥5% | ≥10% | ≥15% | ≥20% | Median |
|---|---|---|---|---|---|---|
| $2–3B | 5-yr | 50.7% | 23.8% | 11.8% | 6.4% | n/a |
| $3–4.5B | 5-yr | 47.8% | 22.6% | 10.3% | 5.1% | n/a |
| $4.5–7B | 5-yr | 43.9% | 20.8% | 10.3% | 4.7% | 4.1% |
| $7–12B | 5-yr | 40.6% | 17.1% | 7.6% | 3.6% | 3.5% |
| $12–25B | 5-yr | 36.1% | 15.0% | 6.8% | 3.2% | 2.9% |
| >$25B | 5-yr | 31.8% | 13.7% | 5.2% | 2.0% | 2.0% |
| >$50B | 5-yr | 27.2% | 10.3% | 3.3% | 1.0% | 1.5% |
| Full universe | 5-yr | 51.3% | 27.1% | 14.5% | 8.5% | 5.2% |

How to use it: find the company's current sales bucket, read across at the Bull case's real growth rate, and write one line: "the Bull assumes X% real growth for five years; Y% of companies this size have done it." Under 5% means the growth is *possible*, not *plausible*.

## 13. Worked example (illustrative)

Inputs: Bull $330 at 20%, Base $215 at 50%, Bear $100 at 30%; spot $139; yield 3.6%.

1. **PW EV:** 0.2 × 330 + 0.5 × 215 + 0.3 × 100 = **$203.5**.
2. **PW return:** (203.5 ÷ 139)^0.2 − 1 + 0.036 = 7.9% + 3.6% = **11.5%**. That is below 13%, so the non-holder verb is Watch.
3. **Entry:** 203.5 ÷ (1.094)^5 = **$130**.
4. **Bear odds:**
   - V_nb = (66 + 107.5) ÷ 0.7 = $247.86.
   - Break-even at 13%: spot must grow to 139 × 1.094^5 = $217.82, so p* = (247.86 − 217.82) ÷ (247.86 − 100) = **20%**, against 30% assigned.
   - Price-implied at 9%: spot must grow to 139 × 1.054^5 = $180.81, so p = **45%**.
5. **The Call reads:** "we think the Bear is 30% likely; the price implies 45%; the hurdle needs ≤20%."
