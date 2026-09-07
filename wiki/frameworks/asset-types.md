# Asset Types — Unit of Value, Per-Unit Metrics, Valuation Primary

Fixes the **unit of value** and the **driver-tree rows** for each business type (CLAUDE.md R16), so two pages of the same type are comparable line by line. Every ticker maps to one type below; add a row when a new type appears, never a one-off unit on a page.

| Type | Unit of value | Driver-tree rows (per unit) | Valuation primary | Typical Power | Tickers |
|---|---|---|---|---|---|
| Store-based retail | Store (door) | Sales / sq ft · comp growth · four-wall or segment margin · new-store capex and year-one return · sq ft growth vs. comp | P/E, EV/EBIT (lease-adjusted) | Scale, cornered resource (allocation) | DKS, HD, LOW, RH |
| Vertical brand retail | Store + e-com order | Sales / sq ft · full-price sell-through · gross margin · store count · DTC mix | P/E, EV/EBITDA | Branding | LULU, SBUX (company stores), CMG (restaurant: AUV, restaurant-level margin) |
| Franchise royalty | Franchised unit | AUV · unit growth · royalty rate · franchisee cash-on-cash return | EV/EBITDA | Branding, process power | WING |
| Brand / wholesale product | Unit or pair sold | ASP · gross margin · sell-through and inventory days · DTC mix · wholesale door count | P/E, EV/EBITDA | Branding | NKE, ONON, SN, CELH (cases) |
| Consumer staples | Case / unit volume | Organic volume vs. price/mix · gross margin · share by category · DSD reach | P/E + yield | Branding, scale | PEP, PG |
| Industrial materials | Tonne, board foot, unit | Volume · realized price · capacity utilization · cost per unit | EV/EBITDA | Scale, process power | TREX, AMCR, MP (NdPr tonnes) |
| Two-sided marketplace | Transaction (trip, order, night, listing) | GMV or GB · take rate · active users (MAPCs) · frequency · AOV · contribution margin as % of GB | FCF yield, EV/EBITDA | Network economies | UBER, DASH, BKNG, ABNB, EBAY, ZG |
| Commerce platform | Merchant | GMV · attach rate (payments, capital, shipping) · merchant count and cohort GMV growth | P/FCF, EV/gross profit | Switching costs, network | SHOP |
| Subscription / streaming | Subscriber (member) | ARM or ARPU · churn or retention · content or delivery cost per sub · paid net adds | P/FCF, EV/EBITDA | Scale (content), branding | NFLX, SPOT, DIS (plus parks: attendance × per-cap) |
| Software | Seat / customer | ARR · NRR and gross retention · ARPU · CAC payback · seats per customer | P/FCF, EV/ARR | Switching costs | MSFT, ADBE, INTU, FIG |
| E-commerce + cloud | Active customer; cloud capacity | Spend per active customer · fulfillment cost per order · Prime/membership share · cloud utilization, backlog, capex per $ of revenue | FCF yield, EV/EBITDA (sum of parts) | Scale, network, switching (cloud) | AMZN, CPNG |
| Brokerage / fintech | Client account (funded customer) | Client assets · net new assets · NIM or NII per $ asset · ARPU · accounts | P/E, P/TBV | Switching costs (custody), scale | SCHW, HOOD |
| Mortgage / housing finance | Loan originated | Origination volume · gain-on-sale margin · servicing UPB and MSR yield · recapture rate | P/TBV, P/E (normalized) | Process power, brand | RKT |
| Conglomerate / insurer | Float and book value per share | Float growth and cost · look-through earnings · operating earnings per share · investment yield | P/B, look-through P/E | Cornered resource (capital), process | BRK.B |
| Pharma / diagnostics | Patient or dose | Scripts or doses · net price per unit · gross-to-net · pipeline milestones · patent cliff dates | P/E, EV/sales (pre-profit) | Cornered resource (IP) | LLY, LNTH |
| Managed care | Member | Members · premium yield · medical loss ratio · operating cost ratio | P/E, P/FCF | Scale, switching | UNH |
| Capital-intensive OEM | Delivered unit (vehicle, tool, server) | Deliveries · ASP · gross margin per unit · capacity utilization · capex per unit of capacity · backlog | EV/EBITDA, P/E | Scale, process power | TSLA, RIVN, DELL, ACLS, SPCX (launches; Starlink subs) |
| People-based services | Billable headcount | Revenue per head · utilization · bookings and book-to-bill · attrition | P/E, P/FCF | Process power, switching | ACN |
| Logistics network | Package / shipment | Volume · yield per package · cost per package · network utilization | EV/EBITDA, P/E | Scale | FDX |
| Contracted infrastructure | Horsepower / installed capacity | Fleet size · utilization · $/hp/month · contract duration · maintenance capex per hp | EV/EBITDA, FCF yield | Scale, cornered resource | KGS |

**Lifecycle stage** (header field) is set per ticker, not per type: `early growth · scaling · mature compounder · mature ex-growth · turnaround · declining`, defined in [`compounding.md`](compounding.md).

**Where a per-unit figure is not disclosed**, the page writes `n/d`, names the proxy it used, and lists the gap in `index.md` Pending Data Gaps. Common proxies: segment profit per sq ft for four-wall margin; loyalty share of sales for retention; member vs. non-member spend for LTV.
