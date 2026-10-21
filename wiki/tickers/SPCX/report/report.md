::toc

::updates

On June 11, 2026, SpaceX priced the largest initial public offering in history at $135 a share and raised about $86 billion. The stock closed its first day at $160.95. Four trading days later it touched $225.64, on the same day the company announced an all-stock purchase of Cursor, the AI coding tool. By August 3 it had traded as low as $104.83. Yesterday, October 20, it closed at $147.79 and then jumped about 9% overnight on its third-quarter results.

The business moved faster than the stock. A year ago SpaceX was a launch company with a satellite-internet business and a money-losing AI lab bolted on in February. In the third quarter of 2026 its Super Intelligence segment, the renamed AI business, brought in $7.6 billion of revenue, up from $0.8 billion a year earlier, and became the largest of the three segments. Total revenue rose 161% to $14.6 billion. Management then guided the first quarter of 2027 to $33–37 billion of revenue, which annualizes to about $140 billion.

Measured from its first close, the stock is down about 8%. Nvidia, the company that sells SpaceX most of its chips, is up 6% over the same weeks, the S&P 500 is up 4%, and Rocket Lab, the closest listed launch company, has halved.

::chart since_ipo

So the market has been handed a lot of good news and has paid little more for it. I think the reason is the question this piece is about. SpaceX's new profits come from renting computers to AI labs at a price, about $50 a year for each watt of capacity, that exists because there are not enough of those computers. Management believes the scarcity will last and that short contracts let SpaceX capture whatever the price does next. If that is right, today's price is cheap. If compute becomes a commodity, as every rented technology before it has, the company is spending tens of billions a quarter to build a very large, very fast-depreciating landlord.

I take the compute question first, then Starlink and Starship, the part of SpaceX that already works. Then come Musk, the capital record and the incentives, which include a proposed merger with Tesla that the two boards' committees began studying this month. I finish with valuation: what $148 assumes, and what it would take to earn 13% a year from here.

## Business Overview {#overview}

SpaceX reports three segments. **Space** is the launch business: Falcon 9, Falcon Heavy, Dragon and now Starship, flying for NASA, the Pentagon, commercial customers and SpaceX itself. **Connectivity** is Starlink: broadband to 13.6 million consumers in 174 markets, plus airlines, ships, governments (Starshield) and a growing direct-to-phone business. **Super Intelligence** is what came with xAI in February: the Colossus data centers in Memphis and Southaven, the Grok models and apps, X's advertising and, since August 14, Cursor.

::table segments

The table tells the story of three different businesses. Space is roughly breakeven because Starship development runs through it. Connectivity turned from a 12% operating margin in 2023 to 45% in the third quarter, and it earns most of the company's operating profit. Super Intelligence lost $6.4 billion in 2025, then turned to a $0.4 billion operating profit in the third quarter, after $1.2 billion of Cursor stock pay, as rented capacity came online.

::chart revenue_mix

A few accounting points before the debate.

First, the 2023–2025 figures include xAI and X, which merged into SpaceX in February under common control, so the history mixes a rocket company with a social network.

Second, Q3 net income of $4.4 billion flatters the run-rate. It includes $1.0 billion of other income ($561 million from a related party), $873 million of interest income on the IPO cash and a $390 million tax benefit. Operating income was $2.8 billion.

Third, adjusted EBITDA of $8.8 billion excludes $2.4 billion of stock pay, half of it from Cursor. Of Cursor's $60 billion price, $23 billion is retention stock that will run through the income statement over about three years.

Fourth, the headline share count of 13.58 billion includes 1.3 billion restricted Class B shares granted to Musk that vest only with a million-person Mars colony or 100 terawatts of off-planet compute. They carry his votes but no economics I can value, so I use about 12.7 billion diluted economic shares.

## Super Intelligence: A Toll Road or a Commodity? {#compute}

Let me start with where things stand.

::table drivers

### Management's narrative

Management's case is that compute is scarce, will stay scarce, and that SpaceX can build it faster than anyone. Musk said he spends four days a week in Memphis and that the company is turning on about 20,000 Nvidia GB300s a month. He said he is "highly confident" of 10 more gigawatts in 2027, for about 13 in total, and that there is a non-zero chance of more than 20. On pricing, he was explicit about the strategy:

> "Our approach is to rent at the — effectively the spot market rate as opposed to sign these long-term deals. Our belief is that the value of compute per watt will increase over time, not decrease... And if you look at, say, how are our short-term contracts renewing? Are they renewing at higher dollars per watt or lower? And we see them renewing at higher dollars per watt, not lower dollars per watt. We are also, frankly, hounded relentlessly by every hyperscaler and by dozens of smaller companies to rent more of our compute. So we could rent out our compute several times over if we said yes to everyone."
> — Elon Musk, Q3 2026 earnings call, October 20, 2026

CFO Bret Johnsen put numbers on it:

> "At current pricing, new compute deployments are generating a payback of less than a year. Pricing is currently tracking slightly above the high end of the $30 to $50 per watt range we were discussing just last quarter."
> — Bret Johnsen, CFO, Q3 2026 earnings call, October 20, 2026

Musk also explained why SpaceX can build faster than rivals. The bottleneck in new gas turbines is the cast blades and vanes, which turbine makers deliver 12–18 months after the rest of the machine. SpaceX already casts rocket-engine parts, so it is casting its own. If that works, it is the kind of advantage that is hard to copy. The backlog rose to $63 billion, $42 billion of it due within a year. Demand is not the problem.

### Poking holes in it

The first hole is that short contracts cut both ways. Renting at spot is a great strategy while prices rise, and SpaceX says renewals are repricing upward. But it means none of today's revenue is protected when prices fall, and in rented technology they always have. The GPU price trackers this wiki follows put the median H100 rental near $3 an hour in mid-2026, against roughly $8 at the 2023 peak `[Estimate]`. The fall happened because more supply arrived, and supply is exactly what SpaceX, Oracle, CoreWeave and the hyperscalers are all building as fast as they can. Musk's argument that better models make each watt more valuable is plausible. It is also an argument that the AI labs keep most of that value, since they own the models and the landlord only owns the building.

The second hole is the size of the bill. Industry estimates put a gigawatt of GB300 or Vera Rubin capacity, including power and cooling, at about $40 billion `[Estimate]`. Ten more gigawatts in 2027 would therefore cost on the order of $400 billion. SpaceX ended September with $90 billion of cash and securities, after spending $19.6 billion on capex in the third quarter, and it has guided the fourth quarter to $35–40 billion. Johnsen named the sources: operating cash flow, the investment-grade debt market, and partners "on the vendor and customer side." Even if the guide comes in, I doubt operating cash flow in 2027 exceeds $70–80 billion `[Estimate]`. Somebody else's money has to pay for the rest, and the price of that money depends on the stock.

The third hole is depreciation. A payback of under a year is an EBITDA statement. GPU generations now turn over every 12–18 months, and SpaceX's own 2027 build is "primarily Rubin." A cluster that pays back in one year at today's price needs to keep renting near today's price for its whole useful life to earn a real return, and that life may be closer to four years than six.

The fourth hole is who the customers are. About half of the capacity serves SpaceX's own Grok and Grok Bot, which earn revenue only to the extent consumers and enterprises pay for them. Grok Bot has 800,000 paid weekly users, a good start but a small one. The rented half goes to a short list of AI labs, two of which (Anthropic and Google) compete with Grok. SpaceX is renting its rivals the tools to beat its own model, at a premium, for as long as there is no alternative.

Here is the arithmetic for a single gigawatt:

::table compute

At today's price a gigawatt earns a 95% pre-tax return on its capital. If the price halves, it is still a good business. If it falls 75% and the chips last four years, the gigawatt loses money. The last row is what actually happened in Q3. Blended across rented and internal capacity, Super Intelligence earned about $16.6 billion per gigawatt-year, a third of the headline rate, because half the capacity serves Grok and new halls take time to fill.

Where I come out: management is right that demand exceeds supply today and right that SpaceX builds faster than anyone. The business is real and, for now, highly profitable. But the price SpaceX is earning is a scarcity price, the contracts are designed to follow the market, and the build is so large that SpaceX will be part of the supply that ends the scarcity. My Base case assumes compute revenue per gigawatt falls to about a third of today's headline rate by 2031. That is roughly where Q3's blended number already sits.

### Four rings of profit {#rings}

It helps to sort SpaceX's profit by how exposed it is to that question.

::table rings

More than half of segment EBITDA now sits in the two rings most exposed to compute pricing. A year ago it was none. Starlink and launch, 44% of Q3 EBITDA, are the parts I would underwrite with the most confidence, and they are also the parts the market priced at the IPO, before the compute business existed in its current form.

## Starlink and Starship: The Part That Already Works {#starlink}

Starlink is one of the best businesses in the world, and the third quarter made it look better. Consumer subscribers rose 89% in a year to 13.6 million. Consumer ARPU, which fell in every period the IPO prospectus disclosed (from $99 a month in 2023 to $66 in Q1 2026), rose 5% to $69. Johnsen attributed the rise to mix, as growth came from developed markets. Enterprise and government revenue rose 91% to $2.1 billion. Connectivity's operating margin reached 45%, including about three points of one-time tariff refunds.

The growth levers are visible. Shotwell said Starlink is contracted on about 12,000 aircraft, nearly a quarter of the world's fleet, with three of the four major U.S. carriers signed. Starshield won more than $6 billion of multi-year Space Force contracts in the second quarter. Starlink Mobile reaches 22 million monthly users through carrier partners. SpaceX bought EchoStar's AWS-4 and H-block spectrum in 2025 and has now agreed to buy 800 MHz low-band spectrum, with a stated goal of becoming "a major mobile carrier in the United States" by early 2028. Musk went further:

> "I can say we do see a clear path to several hundred billion dollars a year in connectivity revenue."
> — Elon Musk, Q3 2026 earnings call, October 20, 2026

I don't underwrite that. But even my Base case has Connectivity compounding about 17% a year from its $26 billion run-rate at a 45% margin. That is a business worth several hundred billion dollars by itself.

What Starlink needs is capacity, and capacity depends on Starship. Flight 14 in September reached orbit for the first time and deployed 26 V3 satellites, adding about 26 terabits per second of downlink, roughly ten Falcon 9 launches' worth on a half-loaded rocket. Flight 15, expected in November, will try to catch both the booster and the ship. Musk called success "more likely than not" and said Starship should fly weekly in the first half of 2027. His Starship timelines have slipped before: the first operational flights were expected years earlier than September 2026. So I treat the 2027 cadence as Bull-case material and make full reuse by mid-2027 my third test.

The Space segment itself matters less than what it enables. Its revenue grew 6% in the third quarter to $1.8 billion and it lost $7 million. SpaceX flew 90% of the world's mass to orbit, China about 6%, everyone else 4%. The segment's job is to make satellites and, eventually, orbital data centers cheap to deploy. On that, its record is the best of any company in this wiki.

## Musk, Capital Allocation and Incentives {#mgmt}

Musk founded SpaceX in 2002, and his record here is the strongest part of his record anywhere. Reusable boosters took the cost of reaching orbit from about $18,500 a kilogram, the historical average, to about $2,700 with the first Falcon 9 and lower since. Starlink went from nothing to the most profitable satellite business ever built. Gwynne Shotwell has run operations since the early years.

The record as a capital allocator for public shareholders is four months long, and it is mostly deals.

::table deals

Two of these were struck at moments that suited the seller. The xAI merger valued Musk's own AI company at $250 billion against SpaceX's $1 trillion, with no premium either way, four months before the IPO. Cursor was announced on June 16, the day SpaceX hit its all-time high, paid in stock at that price, and $23 billion of it is retention pay. I don't know yet whether Cursor was a good purchase. Grok Enterprise customers above $1 million of run-rate revenue rose 50% in a quarter including Cursor, and the bundle with Grok and X Premium is sensible. What I do know is that the deal's cost to shareholders is closer to $60 billion of stock plus three years of dilution than to the $37 billion that the purchase accounting attributes to the business.

### The cash

::table capital

Since 2023 SpaceX has generated about $30 billion of operating cash flow and spent $84 billion on capital projects. It has raised $138 billion from outside: the IPO, $25 billion of investment-grade bonds in June, preferred stock before the IPO and other debt. It has also issued stock for xAI, Cursor and EchoStar. Free cash flow in the first nine months of 2026 was minus $35 billion, and the fourth quarter alone will be worse. Management describes the spending as demand-led and fast-paying, and it may be. Either way, for at least the next two years the compute plan depends on capital markets staying open to SpaceX at good prices. The only repurchases, $4.4 billion of common and preferred stock in the first nine months of 2026, are not explained in the release.

**Outsider grade: Reinvestor, Anti-Outsider-leaning on M&A.** All cash goes back into the business, which is right if returns are as described. But the two large deals were paid in stock near peak valuations, and no capital is ever returned, the opposite of the countercyclical discipline the [Outsiders](../../frameworks/outsiders.md) test rewards.

### The incentives

::table incentives

Musk's two awards are the most unusual incentive plans I have seen. Both pay only for things no company has done: a million people living on Mars, or 100 terawatts a year of compute in space. Both also require market-cap milestones that run to $7.5 trillion. Because the shares are issued now and Musk votes them, they give him about 84% of SpaceX's votes on about 42% of its economics. Like Tesla's 2025 award, they reward scale and ambition, and nothing in any SpaceX plan measures return on capital. For a company about to spend several hundred billion dollars, that gap matters more here than almost anywhere.

### The Tesla question

On the Q3 call, Musk confirmed that SpaceX and Tesla have each formed special committees of independent directors to study a combination, at shareholders' request, and that he is recused:

> "Some people out there assume that a SpaceX and Tesla merger is a certainty. And I think that would be overstating it. Do I think it would be a good idea, yes... the special committees have not reached agreement on the terms of any transaction. And obviously, there's no guarantee that they will."
> — Elon Musk, Q3 2026 earnings call, October 20, 2026

For SpaceX holders the deal is mostly about price. SpaceX would most likely be the acquirer, and Tesla's holders control the vote that matters (50% of all outstanding Tesla shares). So any premium would flow from SpaceX's public holders to Tesla's. In the [exchange-ratio study](../../insights/SPCX-TSLA-merger-exchange-ratio-2026-10-21.md), I put the most likely terms at the market ratio plus a 10–20% premium. The probability-weighted outcome is about 2.66 SpaceX shares per Tesla share, a 42/58 split, and a 65% chance of closing. On those terms SpaceX holders give up about 4% of value if it closes. I carry that as an optionality line in the valuation. Musk owns about 42% of SpaceX and about 20% of Tesla, so his own money favors a SpaceX-friendly ratio; the Tesla vote pulls the other way.

The strategic case is real but overlapping: Terafab is already a three-way chip initiative with Tesla and Intel, Tesla sold xAI $430 million of Megapacks in 2025, and the two companies are building the Macrohard agent platform together. Most of those benefits are available by contract. My test for the deal is whether Tesla's committee insists on a majority-of-the-minority vote and SpaceX's committee holds the premium under 20%. If both happen, the committees did their jobs.

### Promises

::table promises

Management's financial promises have been kept so far, for two quarters, and the 2028 revenue target now looks conservative. Its engineering timelines have run late for years, but Starship reached orbit with a paying payload. So is Musk the right manager? For building, without question. For capital, the evidence is thin and points toward stock-funded expansion, and his incentives reward exactly that.

## Valuation and Model Assumptions {#val}

SpaceX is an early-growth company with three businesses of very different quality, so I build each segment separately: revenue growth and an operating margin, down to GAAP EPS after stock pay and dilution. I start from the exit run-rate (the Q1 2027 guide annualized, with Q3 margins) rather than from calendar 2026, whose $48 billion of revenue the company will have outgrown by January. The 2031 value is EPS times an exit multiple, 30× in the Base. Competence is Outside: Starship's reuse and the long-run price of compute are questions I can't answer with an edge. So Bull and Bear each get 25%, and the Bear includes the funding loop: equity sold low to finish the build. Here is the Base:

::model_build Base

In the Base, Super Intelligence grows about 19% a year to roughly $250 billion of revenue at a 25% operating margin. That is about 15 GW renting near $16 billion per GW-year, management's 13 GW arriving a year late with prices a third of today's. Starlink compounds about 17% a year at 45%, and Space grows slowly as Starship costs settle. Net dilution runs 2% a year. Run-rate EPS of [[Base.eps0]] grows to [[Base.eps]] in 2031, about [[Base.cagr]] a year, and at 30× the stock is worth about [[Base.value]]. That is roughly today's price.

::scenarios

::return_math

At a 10% cost of equity and a 30× exit, the price needs FY2031 EPS of about [[Priced-in.eps]], roughly [[Priced-in.cagr]] growth a year from the run-rate. That is about 40% of the way from my Base to my Bull: a compute business that keeps most of today's pricing while it quadruples in size. In scenario terms, the price implies a [[implied_bear]] chance of the Bear against my 25%.

To earn 13% a year, SpaceX would need about [[Hurdle.eps]] of EPS, more than halfway to the Bull. Weighting the cases 25/50/25 and adding the two option lines (Musk's $500 billion-plus revenue path at 2%, the Tesla premium at minus) gives about [[pw_ev]] a share and [[pw_return]] a year. The price that clears the hurdle on the same cases is about [[entry]]. The Bull returns [[Bull.return]] a year and carries almost all of the upside; R/R is [[rr]], but the Base earns nothing. Capitalizing today's earnings with no growth gives about $20–25 a share, so about 85% of the price pays for growth.

*Confidence note: I cannot judge Starship's path to rapid reuse, or how fast AI-compute rental prices normalize; both are frontier questions, which is why the scenario weights are wide.*

## Final Words {#final}

SpaceX is better than the market thought in July, when I first wrote about it at $145. The compute business turned profitable a quarter early, Starlink's prices turned up, and management's own revenue targets now look conservative. If you asked me which company in this wiki has the most remarkable set of businesses, I would probably say this one.

But the stock is back near where it was, so the improvement went into a higher bar. At $148 the price already assumes the compute business keeps a good part of its scarcity pricing while it grows several times over, and that it gets funded on good terms. That is possible. Management believes it, and it has delivered on everything financial it has promised so far. It is not a case I would pay for in advance, because the contracts that capture rising prices will also pass on falling ones, and the build is large enough to help make prices fall.

What would change my mind? The Q4 and Q1 prints will show whether $33–37 billion of quarterly revenue arrives with its margins intact. The next three quarters will show how a $35–40 billion capex quarter gets financed. Flight 15 and its successors will show whether Starship becomes the cheap, reusable rocket that every long-run plan here assumes. The price at which I would buy on today's cases is about [[entry]]. Until then I'll watch, and I'll watch the merger terms as closely as the rockets.

Here are the three tests written as kill criteria, each with its consequence fixed in advance:

::tests

## Appendix: The Numbers {#numbers}

The tables below carry the framework's required numbers. The argument for each is made in the chapters above.

### Five-year record

::table five_year

Cycle position: not meaningful; the company has reported positive operating income in one full year of three, and its current margin reflects a business that did not exist eighteen months ago.

### Growth levers

::table levers

### Moat, customer and profit pool

::table moat

### Competitors

::table competitors

### Risks and triggers

::table risks

Reflexive loop: **funding**. The compute plan needs outside capital for at least two years, and the lower the stock, the more shares that capital costs. The Bear carries 4.5% a year of dilution for this reason. Ruin path: none within five years. $51 billion of net cash and an investment-grade rating cover the bonds; the risk is dilution, and default is remote.

### Catalysts

::table catalysts

### Sentiment and positioning

::table sentiment

## Sources {#sources}

::sources

::disclaimer
