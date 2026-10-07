# Business & Quality: §1 and §2

Contents:
1. Unit of value by asset type
2. Driver tree
3. Five-year table rows
4. Invested capital, ROIC, ROIIC, reinvestment
5. Owner earnings and maintenance capex
6. Quality and survivability rows
7. Earnings-quality screens
8. Cyclical flag and cycle position
9. Lifecycle stages
10. Growth levers (§2)

---

## 1. Unit of value by asset type

Every company maps to one type. The unit and its per-unit rows keep two reports of the same type comparable line by line. If a company fits none of these, name a unit and explain why.

| Type | Unit of value | Driver-tree rows (per unit) | Valuation primary | Typical Power | Examples |
|---|---|---|---|---|---|
| Store-based retail | Store | Sales/sq ft · comp growth · four-wall or segment margin · new-store capex and year-one return · square-footage growth vs. comps | P/E, EV/EBIT (lease-adjusted) | Scale | HD, LOW, DKS |
| Vertical brand retail / restaurants | Store or restaurant + e-com order | Sales/sq ft or AUV · full-price sell-through · gross or restaurant-level margin · unit count · DTC mix | P/E, EV/EBITDA | Branding | LULU, SBUX, CMG |
| Franchise royalty | Franchised unit | AUV · unit growth · royalty rate · franchisee cash-on-cash return | EV/EBITDA | Branding, process | WING |
| Brand / wholesale product | Unit or pair sold | ASP · gross margin · sell-through and inventory days · DTC mix · wholesale doors | P/E, EV/EBITDA | Branding | NKE, ONON |
| Consumer staples | Case or unit volume | Organic volume vs. price/mix · gross margin · share by category · route-to-market reach | P/E + yield, EPV | Branding, scale | PEP, PG |
| Industrial materials | Tonne, board foot, unit | Volume · realized price · utilization · cost per unit | EV/EBITDA (normalized) | Scale, process | TREX, MP |
| Two-sided marketplace | Transaction | GMV · take rate · active users · frequency · AOV · contribution margin as % of GMV | FCF yield, EV/EBITDA | Network | UBER, BKNG, ABNB |
| Replenishment e-commerce | Active customer | Net adds · sales per customer · subscription share · gross profit and EBITDA per customer · CAC proxy | EV/EBITDA, FCF after SBC | Switching (habit), scale | CHWY |
| Commerce platform | Merchant | GMV · attach rate · merchant count and cohort GMV growth | P/FCF, EV/gross profit | Switching, network | SHOP |
| Subscription / streaming | Subscriber | ARPU · churn · content cost per sub · paid net adds | P/FCF, EV/EBITDA | Scale, branding | NFLX, SPOT |
| Software | Seat or customer | ARR · NRR and gross retention · ARPU · CAC payback | P/FCF, EV/ARR | Switching | MSFT, ADBE |
| E-commerce + cloud | Active customer; cloud capacity | Spend per customer · fulfillment cost per order · membership share · cloud backlog, capex per $ revenue | FCF yield, sum of the parts | Scale, network | AMZN, CPNG |
| Brokerage / fintech | Funded account | Client assets · net new assets · NII per $ of assets · ARPU | Justified P/TBV, P/E | Switching, scale | SCHW, HOOD |
| Mortgage / housing finance | Loan originated | Origination volume · gain-on-sale margin · servicing UPB and MSR yield · recapture | P/TBV, normalized P/E | Process, brand | RKT |
| Conglomerate / insurer | Float and book value per share | Float growth and cost · look-through earnings · operating EPS | P/B, look-through P/E, sum of the parts | Cornered resource | BRK.B |
| Pharma / diagnostics | Patient or dose | Scripts or doses · net price · gross-to-net · pipeline milestones · patent cliff | P/E; EV/sales pre-profit | Cornered resource (IP) | LLY |
| Managed care | Member | Members · premium yield · medical loss ratio · opex ratio | P/E, P/FCF | Scale | UNH |
| Capital-intensive OEM | Delivered unit | Deliveries · ASP · gross margin per unit · utilization · capex per unit of capacity · backlog | EV/EBITDA (normalized) | Scale, process | TSLA, DELL |
| People-based services | Billable head | Revenue per head · utilization · bookings and book-to-bill · attrition | P/E, P/FCF | Process, switching | ACN |
| Logistics network | Package | Volume · yield per package · cost per package · utilization | EV/EBITDA (normalized) | Scale | FDX |
| Contracted infrastructure | Installed capacity | Fleet · utilization · $/unit/month · contract length · maintenance capex per unit | EV/EBITDA, FCF yield | Scale | KGS |

If a per-unit figure is not disclosed, write `n/d` and name the proxy you used instead. Examples: segment profit per sq ft standing in for four-wall margin; loyalty share of sales standing in for retention.

## 2. Driver tree

Build the business from the unit up: units × revenue per unit × contribution per unit → segment profit → consolidated → per share.

| Row | What it is |
|---|---|
| Unit of value | The thing the customer pays for, or the asset that earns |
| Units | Count at period end, and the change |
| Revenue / unit | Total revenue ÷ average units, or the disclosed per-unit metric |
| Contribution / unit | Segment or unit profit ÷ units; `n/d` plus the proxy if not disclosed |
| Return or payback / unit | New-unit capex against year-one contribution, or CAC against LTV |
| Growth split | Of last year's growth, how much came from **more units** and how much from **more per unit** (price/mix) |

## 3. Five-year table rows

Columns are fiscal years, plus the current-year estimate. Rows:
- net revenue;
- organic growth;
- operating income, GAAP and core;
- diluted EPS and core EPS;
- operating cash flow, capex, FCF;
- **owner earnings** and owner earnings per share;
- dividends and buybacks;
- invested capital, **ROIC**, **3-year ROIIC**, reinvestment rate;
- SBC % of revenue, FCF conversion, owner-earnings conversion (÷ core net income);
- net debt/EBITDA, interest coverage, nearest maturity wall;
- the **earnings-quality** row.

State each source, and tag every derived row `[Derived]`.

## 4. Invested capital, ROIC, ROIIC, reinvestment

- **NOPAT** = operating income × (1 − tax rate). Use the reported effective rate unless it is distorted; then use a normalized rate and say so. Show GAAP and core NOPAT side by side when restructuring or impairments are large.
- **Invested capital**: state which build you used and tag it `[Derived]`.
  - Financing side: equity + debt + operating-lease liabilities − cash and short-term investments.
  - Operating side: total assets − cash − non-operating investments − non-interest-bearing liabilities. Prefer this when equity is distorted (large buybacks, write-downs, valuation-allowance releases).
- **ROIC** = NOPAT ÷ invested capital.
- **3-year ROIIC** = (NOPAT_t − NOPAT_t−3) ÷ (IC_t − IC_t−3). This is the return on the *new* money, and it is what a compounder thesis rests on. A high ROIC with a low ROIIC means the business is coasting on old capital. Compute it excluding acquisitions as well when goodwill from a recent deal inflates capital.
- **Reinvestment rate** = (capex − D&A + acquisitions + Δ working capital) ÷ NOPAT.
- **Implied organic growth** ≈ ROIIC × reinvestment rate. Compare it with the Base case's growth. If the Base needs more growth than this produces, name the lever that supplies the rest (pricing power, mix, margin), or lower the Base.
- **High-ROIIC compounder flag (🔁)**, all of:
  - ROIC ≥ 20% in at least 4 of the last 5 years;
  - 3-year ROIIC ≥ 20%;
  - reinvestment rate ≥ 25%;
  - a §2 lever with at least 5 years of runway at stage proven or scaling.

  A flagged company has no Trim zone (see SKILL.md).

## 5. Owner earnings and maintenance capex

**Owner earnings** is the cash a business can pay out while keeping its competitive position and unit volume (Buffett, 1986 letter). It is the cash number the report compounds:

**Owner earnings = CFO − SBC − maintenance capex − finance-lease principal**

- **SBC** counts as a real cost. SBC is added back to CFO, so leaving it in would credit the company for paying people in shares.
- **Maintenance capex**, using Greenwald's estimate:
  - growth capex = (5-year average net PP&E ÷ revenue) × Δ revenue, floored at 0;
  - maintenance capex = total capex − growth capex;
  - cross-check against D&A, and state which figure you used.
  - Over five years, sum the capex and Δ revenue across the whole period. A single year is noisy.
- **Growth capex** belongs in the reinvestment rate, not in owner earnings.
- **Owner-earnings conversion** = owner earnings ÷ core net income, averaged over five years. Use it to turn core-EPS targets into owner-earnings multiples.
- **Compounding/yr** in the Verdict = Base growth in owner earnings per share + shareholder yield.
- **Coverage check.** If dividends plus buybacks exceed owner earnings over five years, the gap was funded with debt or asset sales. Say so, and show the change in net debt.

## 6. Quality and survivability rows

A decade-long holding has to survive a recession. The report says whether it can.
- SBC as % of revenue.
- FCF conversion (FCF ÷ net income, or ÷ adjusted EBITDA for platforms).
- Owner-earnings conversion.
- Net debt (including leases) ÷ EBITDA, GAAP and core.
- Interest coverage (EBIT ÷ interest).
- The nearest maturity wall, measured against cash and FCF.

## 7. Earnings-quality screens

Compute these on every Mode A run, and mention them in the text only when one trips. They are reasons to look harder, never reasons to buy.

- **SBC-adjusted accruals** = (net income − (CFO − SBC)) ÷ average total assets. Negative means cash earnings exceed accounting earnings, which is good.
  - Flag it if it is positive and rising, or sits in the top decile for the sector.
  - Subtracting SBC matters because high-SBC companies otherwise look high-quality on an accrual test. (Sloan 1996; the return anomaly has faded since publication, so treat this as a quality flag only.)
- **Beneish M-score** (1999): flag anything above −1.78.

  M = −4.84 + 0.920·DSRI + 0.528·GMI + 0.404·AQI + 0.892·SGI + 0.115·DEPI − 0.172·SGAI + 4.679·TATA − 0.327·LVGI

  Each index compares year t with year t−1:

  | Index | Definition |
  |---|---|
  | DSRI | (receivables ÷ sales)_t ÷ (receivables ÷ sales)_t−1 |
  | GMI | gross margin_t−1 ÷ gross margin_t |
  | AQI | [1 − (current assets + net PP&E) ÷ total assets]_t ÷ [same]_t−1 |
  | SGI | sales_t ÷ sales_t−1 |
  | DEPI | [dep ÷ (dep + net PP&E)]_t−1 ÷ [same]_t |
  | SGAI | (SG&A ÷ sales)_t ÷ (SG&A ÷ sales)_t−1 |
  | LVGI | [(current liabilities + LT debt) ÷ total assets]_t ÷ [same]_t−1 |
  | TATA | (net income − CFO) ÷ total assets_t |

  Fast growers trip the score through SGI. When it trips, read DSRI and TATA before concluding anything.
- **Piotroski F-score** (2000): for `turnaround`-stage companies only, tracked in Mode B as a check on direction. It scores nine binary tests:
  - ROA > 0, CFO > 0, ROA rising, CFO > net income;
  - long-term debt ratio falling, current ratio rising, no new shares issued;
  - gross margin rising, asset turnover rising.
- **Altman Z** (1968): only for levered manufacturers.

  Z = 1.2·WC/TA + 1.4·RE/TA + 3.3·EBIT/TA + 0.6·MVE/TL + 1.0·Sales/TA

  Below 1.81 is distress and above 2.99 is safe. For everything else, the survivability rows do the job better.

## 8. Cyclical flag and cycle position

- **Set Cyclical = Yes** when either holds:
  - the asset type is cycle-exposed (see `valuation.md` section 5);
  - over 10 years, operating margin max − min exceeds half the median, or revenue fell 10% or more in a year for macro reasons.
- **Cycle position** (§1 line): current operating margin, its percentile within the 10-year range, and the median.
- **Normalized margin** = the 10-year median (or the sector's through-cycle average). For a Yes, every terminal value uses it.
- For a non-cyclical company, show the 10-year margin range anyway when today's margin sits at an extreme, and say what caused it (for example impairments versus structural).

## 9. Lifecycle stages

The header's `Stage` field. The stage sets the prior for what a Base case may assume.

| Stage | Definition |
|---|---|
| early growth | Units growing >20%; negative or thin margins |
| scaling | Units growing 10–20%; margins expanding |
| mature compounder | Units growing <10%; ROIIC still above the cost of capital; buybacks |
| mature ex-growth | ROIIC at or below the cost of capital; the return is the yield |
| turnaround | Margins below the company's own history, with a named recovery plan |
| declining | Units shrinking structurally |

Two of Lynch's categories cut across stage: **cyclical** is handled by the flag above, and **asset plays** by sum of the parts.

## 10. Growth levers (§2)

The lever list is fixed:

| Lever | Typical evidence |
|---|---|
| Market growth | Category volume, TAM growth, link to GDP |
| Share gain | Share data, competitor exits, relative growth, scuttlebutt |
| Price and mix | Last price increase and what volume did; premium-tier mix |
| Attach / new products | Attach rate, cross-sell, contribution from new SKUs |
| New geographies | Country entries; international growth vs. the core |
| M&A | Deal economics, integration record, ROIIC with and without the deal |
| Margin | Operating leverage, productivity programs, incremental margin |
| Share count | Net buyback yield after SBC dilution |

- **Columns for each lever:** contribution now · runway in years · evidence · management's stated intent · stage. The stage is one of:
  - `proven`: in the reported numbers for two or more years;
  - `scaling`: disclosed and growing, but not yet material;
  - `option`: announced or plausible, with no revenue yet. An option also gets a valued line in §5.
- **Adjacency test (Zook).** A new lever must share customers, costs or capabilities with the core business. If it shares none, grade it as diversification, whatever management calls it.
- **After the table:** two or three sentences on which lever carries the Base and which the Bull.
