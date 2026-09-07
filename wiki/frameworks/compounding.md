# Compounding Framework — From the Unit to the Return

**Where applied**: §1 (driver tree, reinvestment and quality rows), §2 (growth levers), §5 (return decomposition, hurdle, implied expectations, base rate, year ten) of every ticker page. Governs CLAUDE.md R8 and R16.

**Sources**: Mauboussin & Rappaport, *Expectations Investing* (price-implied expectations); Mauboussin, *The Base Rate Book* (Credit Suisse HOLT, Sept 2016) and *The Economics of Customer Businesses* (in `raw/clippings/`); Zook, *Profit from the Core* (adjacency); Ansoff (growth taxonomy).

---

## 1. Driver tree

Every business is understood from one unit up. Name the unit, count it, price it, cost it, and show how the count and the per-unit economics each contribute to growth. The per-unit metrics for each asset type are fixed in [`asset-types.md`](asset-types.md) so pages are comparable.

| Row | What it is | Where it comes from |
|---|---|---|
| Unit of value | The thing the customer pays for, or the asset that earns | 10-K Item 1 |
| Units | Count at period end, and the change | 10-K, releases |
| Revenue / unit | Total revenue ÷ average units (or the disclosed per-unit metric) | Derived or disclosed |
| Contribution / unit | Segment or four-wall profit ÷ units; write `n/d` and name the proxy if undisclosed | 10-K segment note, calls |
| Return or payback / unit | New-unit capex vs. year-one contribution, or CAC vs. LTV | Investor days, calls |
| Growth split | Of last year's growth, how much was more units and how much more per unit | Derived |

Shapes by type: **store** = doors × sales/sq ft × four-wall margin · **subscriber** = subs × ARPU × contribution margin, with churn and CAC · **marketplace** = transactions × AOV × take rate, or GMV × take rate · **staples** = volume × price/mix × gross margin · **financial** = client assets or accounts × yield or ARPU · **pharma** = patients × net price per drug · **capacity** = installed base × utilization × rate.

## 2. Reinvestment economics

Growth is bought with capital. The two numbers that tell you whether the purchase is worth it:

- **ROIC** = NOPAT ÷ invested capital. NOPAT = operating income × (1 − tax rate); use the reported effective rate unless it is distorted, then a normalized rate and say so.
- **Invested capital**, two builds — state which you used and tag `[Derived]`:
  - *Financing side*: equity + debt + operating-lease liabilities − cash and non-operating investments.
  - *Operating side*: total assets − cash − non-operating investments − deferred tax assets − non-interest-bearing liabilities. Prefer this when equity is distorted by a valuation-allowance release, a large write-down, or heavy buybacks.
- **Incremental ROIC (ROIIC)** = (NOPAT this year − NOPAT three years ago) ÷ (invested capital this year − three years ago). This is the return on the *new* money, and it is the number a compounder thesis rests on. A high ROIC with a low ROIIC is a business coasting on old capital.
- **Reinvestment rate** = (capex − D&A + acquisitions + Δ working capital) ÷ NOPAT.
- **Implied organic growth** ≈ ROIIC × reinvestment rate. Compare it to the Base-case growth in §5. If the Base case needs more growth than the reinvestment math produces, the page has to say where the extra comes from (pricing power, mix, operating leverage) or lower the case.

Caveats to name on the page: goodwill from a recent acquisition inflates capital before the acquired profit arrives (compute ROIIC ex-deal as well); lease capitalization lifts both capital and operating income (add back the implied lease interest to NOPAT for consistency); a deferred-tax-asset release inflates equity and does nothing for the business.

**Quality and survivability rows** (same table): SBC as % of revenue · FCF conversion (FCF ÷ net income, or ÷ Adj. EBITDA for platforms) · net debt ÷ EBITDA · interest coverage (EBIT ÷ interest) · nearest maturity wall.

## 3. Growth levers

One table in §2 with this fixed list, so any two pages can be compared lever by lever:

| Lever | Ansoff cell | Typical evidence |
|---|---|---|
| Market growth | Penetration | Category volume, TAM growth, GDP link |
| Share gain | Penetration | Share data, competitor exits, relative growth |
| Price and mix | Penetration | Last increase vs. volume response, premium-tier mix |
| Attach / new products | Product development | Attach rate, cross-sell, new SKU contribution |
| New geographies | Market development | Country entries, international growth vs. core |
| M&A | Diversification (unless adjacent) | Deal economics, integration record |
| Margin | — | Operating leverage, productivity programs, incremental margin |
| Share count | — | Net buyback yield, dilution from SBC |

Columns: current contribution to growth · runway in years · evidence · management's stated intent · stage. **Stage vocabulary**: `proven` (in the reported numbers for 2+ years) · `scaling` (disclosed, growing, not yet material) · `option` (announced or plausible, no revenue). Options also get a valued line in §5.

**Adjacency test** (Zook): a new lever must share customers, costs or capabilities with the core. If it shares none, it is diversification and the page grades it as such, whatever management calls it.

**Lifecycle stage** (header `Stage` field): `early growth` (units growing >20%, negative or thin margins) · `scaling` (units growing 10–20%, margins expanding) · `mature compounder` (units growing <10%, ROIIC still above cost of capital, buybacks) · `mature ex-growth` (ROIIC at or below cost of capital, return is yield) · `turnaround` · `declining`. The stage sets the prior for what a Base case may assume.

## 4. Return decomposition, hurdle and entry

Expected annual return ≈ **growth in FCF (or EPS) per share** + **shareholder yield** (dividend + net buyback) **± multiple change**.

- The first two terms are the **compounding rate at a flat multiple**. It goes in the Verdict table as `Compounding/yr`. It is what a 5–10-year holder actually earns if the market never changes its mind.
- The third term is re-rating. State its share of the PW return in one clause. A thesis whose return is mostly re-rating is a Watch.
- **PW return/yr** = (PW EV ÷ spot)^(1/5) − 1 + dividend yield. **Hurdle: 13%.** Initiate requires PW return/yr ≥ 13%.
- **Entry price** = PW EV ÷ (1 + 0.13 − yield)^5 — the price at which the PW case returns exactly the hurdle. Trim = PW EV → Bull. Avoid ≥ Bull.

Worked example: PW EV $204, spot $139, yield 3.6% → PW return = (204/139)^0.2 − 1 + 0.036 = 8.0% + 3.6% = **11.6%**, below the hurdle → Watch. Entry = 204 ÷ (1.094)^5 = **$130**.

## 5. Price-implied expectations

One line in §5. Two acceptable methods; state the discount rate.

- *Perpetual*: implied growth g = r − (FCF ÷ EV). At r = 9% and a 6.3% FCF yield, spot implies ~2.7% growth forever.
- *Two-stage*: solve for the five-year FCF growth that, followed by 3% terminal growth, equates PV to EV.

Discount rates: 8% wide-moat staples and utilities · 9% platforms and quality compounders · 10–11% cyclicals, turnarounds, capital-intensive. Use steady-state FCF (NOPAT less maintenance capex) when reported FCF is depressed by a growth-capex cycle, and say so.

## 6. Base rates for sales growth

Mauboussin, *The Base Rate Book*, Exhibit 4 — top 1,000 global companies by market cap, 1950–2015, **real (inflation-adjusted)** sales CAGR; add roughly 2–3 points for a nominal comparison. Sorted by prior-year sales. Share of companies achieving at least the stated real CAGR:

| Sales bucket | Horizon | ≥5% | ≥10% | ≥15% | ≥20% | Median |
|---|---|---|---|---|---|---|
| $2–3B | 5-yr | 50.7% | 23.8% | 11.8% | 6.4% | n/a |
| $2–3B | 10-yr | 44.9% | 16.1% | 6.3% | 2.2% | n/a |
| $3–4.5B | 5-yr | 47.8% | 22.6% | 10.3% | 5.1% | n/a |
| $3–4.5B | 10-yr | 41.3% | 13.2% | 4.5% | 1.3% | n/a |
| $4.5–7B | 5-yr | 43.9% | 20.8% | 10.3% | 4.7% | 4.1% |
| $4.5–7B | 10-yr | 38.4% | 11.9% | 4.2% | 1.5% | 3.7% |
| $7–12B | 5-yr | 40.6% | 17.1% | 7.6% | 3.6% | 3.5% |
| $7–12B | 10-yr | 34.6% | 9.5% | 3.2% | 1.1% | 3.2% |
| $12–25B | 5-yr | 36.1% | 15.0% | 6.8% | 3.2% | 2.9% |
| $12–25B | 10-yr | 30.5% | 9.7% | 3.4% | 0.9% | 2.7% |
| >$25B | 5-yr | 31.8% | 13.7% | 5.2% | 2.0% | 2.0% |
| >$25B | 10-yr | 27.5% | 7.3% | 1.5% | 0.2% | 1.8% |
| >$50B (mega) | 5-yr | 27.2% | 10.3% | 3.3% | 1.0% | 1.5% |
| >$50B (mega) | 10-yr | 21.1% | 3.9% | 0.9% | 0.0% | n/a |
| Full universe | 5-yr | 51.3% | 27.1% | 14.5% | 8.5% | 5.2% |
| Full universe | 10-yr | 48.9% | 20.6% | 9.0% | 4.5% | 4.9% |

Use: find the bucket for the company's *current* sales, read across at the Bull case's real growth rate, and write one line — "the Bull assumes X% real sales growth for five years; Y% of companies this size have done it." The 10-year sample has ~59% survivorship, so the true odds are somewhat lower than shown. Buckets below $2B and the margin- and ROIC-persistence tables are not yet transcribed; extend this file from the [source PDF](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf) when a page needs them.

## 7. Year ten

One sentence in §5. The scenarios stop at year five; the holder does not. Say whether the business is still growing at year ten and why (runway from §2), or whether the terminal multiple is carrying the value. A terminal multiple above the market's for a business whose levers are exhausted by year seven is the most common way a five-year page flatters a ten-year hold.
