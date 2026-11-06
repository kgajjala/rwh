::toc

::updates

On May 7, 2026, Akamai told investors that a frontier AI company had committed $1.8 billion over seven years to rent computing capacity on its cloud. The stock rose 26.6% the next day, its biggest one-day gain in this window, and kept going. On May 13 it closed at about $161, up more than 120% from where it stood in November. Akamai had been the content-delivery company, the one that makes websites load fast, and the security company that protects them from attack. Now Mr. Market was being asked to see it as an AI infrastructure provider.

The story kept getting bigger. In September, Akamai announced an $11.6 billion seven-year commitment from Anthropic. After the close on November 5 it said it had signed more than $14 billion of such contracts this year and guided revenue growth to accelerate to 17–22% in 2027 and past $7.0 billion in 2028, from $4.2 billion last year. The stock had already fallen 9% that day, with the market's worries about AI infrastructure, which Leighton said on the call had "dragged" Akamai down with it. On November 6, the first session after the report, it rose about 8% to $84. That is 49% below the May high.

The business and the stock have gone in different directions. Revenue in the first nine months of 2026 is up 6%. GAAP operating income is down 36%, because the company is paying for data-centre space before the contracts bill. Non-GAAP earnings per share fell 5% in the third quarter. Over a full year Akamai has returned 14.8% to a holder from last November, against 19.5% for its closest peer Cloudflare and 9.9% for the S&P 500, but the ride in between is a round trip from 100 to 221 and back to 115.

::chart since_may

The question for the next five years is whether this build earns its keep. Management says the contracts return about 13% after tax, the same number I use as my hurdle. The company is spending $3.5 billion on capex this year against about $1.5 billion of operating cash flow, and it has borrowed $7.6 billion in convertible notes to bridge the gap. The market has moved from "this changes everything" to "who pays for it", and I think both are partly right.

I begin with the business and how to read its accounts. The key debate follows: is the cloud build a business or a financing? A second debate is about the cash machine underneath, whose owner earnings have fallen while its profits looked stable. Then management, capital allocation and incentives, and finally valuation, asking what $84 already assumes and what has to be true to earn 13% a year from here. Akamai reports again in February with the full 2027 guide, so some of this will be tested soon.

## Business Overview {#overview}

Akamai runs one of the world's largest distributed networks: more than 4,000 points of presence in 130 countries, according to CEO Tom Leighton on the Q3 call. It reports a single operating segment, but since January 2026 it splits revenue into three solution categories. Security (about 55% of revenue) protects customers' web applications, APIs and internal networks, including the Guardicore microsegmentation and API-security products it bought. Delivery and other cloud applications (about 36%) is the original business of caching and delivering content, including video, for media, commerce and software customers. Cloud infrastructure services, which Akamai calls CIS (about 9% but rising fast), rents out virtual machines, Kubernetes, storage and networking, mostly from the Linode platform it bought in 2022.

::table segments

The table tells the story in three lines. Security grows 9–10% and is the engine. Delivery shrinks 3–6% a year as renewals reprice lower and large media customers optimise traffic. CIS grows in the mid-30s but is still only $109 million a quarter. Together that is 6% growth, with operating margin falling from 15% to 9% on a GAAP basis in a year.

::chart rev_mix

A few accounting points matter before the debate. Akamai guides on non-GAAP numbers that exclude stock-based compensation, amortisation of acquired intangibles and the amortisation of capitalised stock compensation. In Q3 that was a 16-point gap between the 25% non-GAAP margin and the 9.7% GAAP margin. I use GAAP margins, which charge stock compensation as the real cost it is, in the model. The company also reports capex on an accrual basis in its supplemental table ($464 million in Q3) and on a cash basis in the cash-flow statement ($605 million), so I quote which one I use. And the share count has two faces: 144 million shares are outstanding, but GAAP diluted EPS uses 151 million because the convertible notes count as if converted. Remaining performance obligations were $5.2 billion at the end of 2025, with about 55% due within a year (10-K), a figure that predates the 2026 contracts.

## Cloud Infrastructure: A Business or a Financing? {#debate}

Let me start with where things stand. Here is what management has told us about the contracts signed this year.

::table drivers

### Management's narrative

Management's case is that it is not building a bare-metal GPU farm. It is selling a cloud of ordinary CPU servers, packed into many small leased data-centre footprints that it can get when large sites are scarce, on contracts that guarantee revenue for seven years. Here is how Leighton put it on the Q3 call:

> "We sell compute capacity through our Infrastructure as a Service platform, which consists of virtual machines, managed Kubernetes, storage and networking. This keeps our capacity elastic across customers and generates substantially more revenue per megawatt or dollar of CapEx than a bare metal contract. In particular, we expect to generate about $22 million of revenue per megawatt of contracted power for the large deals we signed this year."
> — Tom Leighton, CEO, Q3 2026 earnings call, November 5, 2026

CFO Ed McGowan then gave the return numbers that investors had asked for, posted on a slide: about $2.2 billion of annual revenue from the $14 billion of contracts, a 75% adjusted EBITDA margin, a 30% non-GAAP operating margin, a 13% after-tax IRR and an average adjusted return on invested capital of about 15%. His answer on the pricing was the most revealing part of the call:

> "These are the lowest prices you're going to see on a unit economic basis. So look at that as sort of your floor as far as what pricing is. So somebody is going to commit to half the amount or 1/3 of the amount and 1/10 of the volume, they're not going to get anywhere near those prices."
> — Ed McGowan, CFO, Q3 2026 earnings call, November 5, 2026

And on funding, he said Akamai expects "to fund our CIS expansion and broader growth investments through 2028 as well as address our 2027 convertible note maturity, primarily from our existing cash balance and expected operating cash flows, which may be supplemented by measured incremental financing activities as appropriate."

I take much of this at face value. The company has secured the data-centre space and power for the whole $11.6 billion contract, about 70% of the hardware, and a price-adjustment clause for the rest. Two of the first three large deals are billing. The 2028 revenue target excludes any use of the $9 billion Anthropic option. Management also says it is walking away from deals that do not meet its return threshold. This is a more careful build than the AI infrastructure story the market has been worrying about.

### Poking holes in it

The first hole is that the return is the hurdle, not above it. A 13% after-tax IRR on the largest customer's best price is a fair return on capital, and I fully believe management that smaller deals pay more. But the biggest deals are where the money is: $11.6 billion of the $14 billion. Using management's own ratios, I build the return on a dollar of capex below. The as-guided case needs servers to be worth 15 cents on the dollar after seven years to reach 12.7%.

::table unit

A 10% price cut takes the return to 9.4%. A 20% rise in hardware costs without a pass-through takes it to 8.6%. The price-adjustment clause protects the roughly 30% of hardware not yet ordered, and memory prices are the thing everyone is watching. There is upside too: later deals "coming in higher" lift the return to 15.9% at a 10% price premium. But there is little margin of safety in the base contract, and the company is paying for that capex up front.

The second hole is the financing. Capex guidance for 2026 is $3.46–3.66 billion. Operating cash flow was $1.07 billion in the first nine months. Cash and securities were $4.24 billion on September 30, and Q4 capex alone is guided to $2.45–2.65 billion, including $1.7 billion to pre-buy memory for the Anthropic contract. By my arithmetic cash falls to about $2 billion at year-end. Convertible notes stand at $7.64 billion in par value across five issues, at coupons of 0–1.125%, with $1.15 billion due on September 1, 2027. The notes carry hedges and warrants that offset dilution only up to a point. If Akamai's stock is still below $93.01 in May 2031, holders of the $1.725 billion 2033 notes can demand cash back. The CFO's "measured incremental financing" is a polite phrase for more of this, and it comes with a goal to "maintain investment grade as long as we certainly can."

The third hole is the counterparty. Anthropic is 83% of the signed commitments, is privately held, and the 8-K describes the $11.6 billion as "subject to termination terms and service delivery requirements." At about $1.66 billion of revenue a year, it would be roughly a quarter of 2028's $7.0 billion, in a company that reported no customer above 10% of revenue in 2023–2025. The warrant is a clever structure: Anthropic gets up to 5% of the stock at $111.33, with 2% vesting on the commitment and about 1% for each further $3 billion bought. McGowan said the warrant gives Anthropic "an incentive for them as our stock goes higher," so he does not expect them to exercise the $9 billion option soon. That is honest, and it tells you the equity value is a bargaining chip.

The fourth hole is the track record. Piper Sandler's James Fish said it directly on the call: "we've kind of missed compute or only been in line on virtually every quarter that you've had this business." The company's FY2026 CIS growth guide has gone from at least 50% in May (secondary reports) to 40–42%, and about $30 million of Q4 revenue now slips into 2027 because of supply-chain and third-party data-centre delays. Management says the delays are a "punch list on a construction project" and I believe it, but the 2027 CIS guide of $1.1–1.3 billion requires 70–75% of the year's revenue in the second half.

Where I come out: management is right that this is a better-designed build than most, and probably right that it will deliver the 2028 revenue. But a fair return is not a bargain, and the financing, concentration and execution risk all sit with shareholders. The burden of proof is on the next four quarters.

### Three rings of profit {#rings}

Akamai gives no profit by solution, so I sort revenue by how exposed it is to this debate.

::table rings

Rings 1 and 2 are 91% of today's revenue and nearly all of today's profit. They are not exposed to the AI build except that they pay for it. Ring 4 is zero today and about 30% of 2028 revenue. The whole question is whether a new ring earning a 28% operating margin (before SBC) on heavy capital is worth more or less than the old rings it is displacing in the mix. Delivery capacity is already being redirected: "we're much better off investing that CapEx into our CIS business," Leighton said.

## The Cash Machine Underneath {#cash}

The second debate is quieter and I think it matters just as much. Is the core still the cash machine it looks like?

Akamai's non-GAAP earnings suggest a steady company. Non-GAAP EPS was $6.99 in 2025 and is guided to $6.47–6.68 in 2026, a dip. At $84 that is 12.8 times. Cheap, if you believe it. But non-GAAP excludes stock compensation, which is now 10.9% of revenue, up from 5.9% in 2021. In 2026 it will be about $540 million, roughly $3 a share after tax, or close to half of non-GAAP EPS. The GAAP profit looks very different: $3.07 per share in 2025, down from $3.93 in 2021, and about $2.50 this year. At $84 that is 33 times.

Free cash flow tells the same story from another side. Reported free cash flow was $0.70 billion in 2025, a healthy 1.55 times net income. But subtract stock compensation, which is a real cost paid in shares that the company then spends cash buying back, and owner earnings were $0.24 billion. In 2021 they were $0.66 billion.

::table five_year

The five-year table has three uncomfortable numbers. Return on invested capital, built from equity, convertible debt and leases less cash, fell from 11.3% to 5.2%. Three-year incremental ROIC is negative. And the reinvestment rate was 95%, 136%, 76%, 142% and 43% of NOPAT, which means that Akamai has been putting most of its profits into acquisitions and servers for five years while its NOPAT fell from $0.63 billion to $0.45 billion. Some of this was deliberate and good. Guardicore and Noname gave Akamai the security products now growing 10%. Restructuring charges ($95 million in 2024, $58 million in 2025) and rising amortisation also depressed GAAP profit. But the pivot to AI compute is the third big reinvestment in five years, and the first two have not yet shown up in returns.

This is why I do not flag Akamai as a compounder. It fails the ROIC test in all five years and the ROIIC test in both years that can be computed. The business still earns a real return on its older capital, which is why security can be a 20% margin business, but it has not earned a return on the new capital. The AI contracts are the bet that fixes that. If they earn the 13% that management says, the new capital will earn more than the 5.2% the old capital is earning now.

Delivery, the oldest ring, still pays. It is shrinking by a low-to-mid single digit each year, but management says "we're probably holding pricing better now than we have for a long period of time." Security adds $12–13 million of sequential revenue every quarter. If that is the pattern, the core grows about 6% a year, with margins that depend on how much of the cost base the AI build absorbs. I model that.

## Leighton, Capital Allocation and Incentives {#mgmt}

Tom Leighton co-founded Akamai and has been CEO since 2013. He draws a $1 salary, takes his bonus in stock, and owned 1.9% of the company in February (2,759,456 shares), so he is paid in the stock, not around it. The company has pivoted before, from content delivery to security and now to cloud. This is his biggest bet, and he has been consistent in public about it: "I've never been more confident in Akamai's ability to power and protect an AI-driven world." I have not found a prior-tenure record elsewhere to chart, so the test is what he has done with the cash.

### The deals

::table deals

Four of the five deals have worked or are working, which is a better record than most acquisitive software companies. The biggest, Linode, took four years to become the foundation of a business that is growing in line with the pivot. The deal list is not where my worry sits.

### The cash

::table capital

From 2021 to 2025 Akamai generated $3.83 billion of free cash flow, spent $2.07 billion on acquisitions, paid $1.60 billion of stock compensation and bought back $3.14 billion of stock, or 82% of free cash flow. Diluted shares fell 11%, from 166 million to 147 million, which is a good result. But owner earnings per share still fell from $3.96 to $1.63, because the stock compensation, capex and acquisitions grew faster than the buyback shrank the count.

2026 changed the pattern. In the first half the company repurchased about 5 million shares for $616 million at an average of $123.19, higher than today's price. It spent nothing in the third quarter as the price dropped below $100 and capex rose. That is pro-cyclical: it bought at the top and stopped at the bottom. It also issued $3.5 billion of new convertibles in May, with note hedges and warrants. I grade capital allocation Steward, not Outsider, because buybacks followed the price rather than the value. The rest of the discipline is intact. Debt is cheap, with an effective rate on the new notes of 0.23–0.35%, and capex is tied to signed contracts. It does leave a $565 million authorisation and no plan to use it before 2028.

### The incentives

From the [2026 proxy](https://www.sec.gov/Archives/edgar/data/1086222/000108622226000042/akam-20260330.htm):

::table incentives

Every financial metric in the plan is non-GAAP: revenue, non-GAAP operating income and non-GAAP EPS. None charges management for the capital it uses or the stock it issues. The 2025 bonus paid at 151% of target, with the operating income leg paying 190%, in a year in which owner earnings fell by almost half. The relative-TSR grant is the best-aligned piece, since it pays only if Akamai's stock beats peers through 2027, but it measures the stock rather than the returns behind it. A manager paid on revenue and non-GAAP EPS will take $14 billion of revenue at a 13% return more readily than shareholders would at the same price. That does not make it a bad decision. It means the check on the decision has to come from the board and from investors.

So is Leighton the right manager for this build? The operating plan looks careful and the commercial wins are real. What I cannot see yet is the discipline on capital: the proxy contains no return-on-capital goal, the buyback followed the price, and the financing comes after the contracts, not before. The three tests on my page are aimed at exactly that.

## Valuation and Model Assumptions {#val}

As with other pages, I ask what has to be true to earn 13% a year from today's price, and what the price already assumes at a 9% cost of equity. The model builds security, delivery and cloud infrastructure separately, each with revenue growth and a GAAP operating margin after stock compensation, then deducts corporate and net financing costs, tax and the share count. 2026 is calibrated to guidance and nine-month results, at GAAP EPS of about $2.52. The 2031 value is GAAP EPS times an exit multiple. Here is the Base case, with inputs highlighted:

::model_build Base

In the Base, security grows 8% a year with its margin rising to 20%, delivery shrinks 3% a year at a 6% margin, and cloud infrastructure grows to about $3.2 billion by 2031 at a 24% margin, which is the $2.2 billion of signed contracts holding plus another $1 billion of other cloud revenue. Revenue reaches about $8.2 billion, close to the $7.0 billion 2028 target plus a few years of ordinary growth. GAAP EPS grows [[Base.cagr]] a year to [[Base.eps]], though that starts from a 2026 year depressed by costs running ahead of revenue. Net shares rise about 2% a year, since buybacks resume only partly and stock compensation continues. At 18 times, which I think is fair for a security business attached to a capital-heavy infrastructure one, the stock is worth about [[Base.value]] in 2031.

::scenarios

::return_math

The market's expectations are close to my Base, and slightly above it. To earn an ordinary 9% a year at an 18 times exit, Akamai needs 2031 GAAP EPS of about [[Priced-in.eps]], [[Priced-in.cagr]] growth a year from [[Base.eps0]], a shade more than my Base. Put in scenario terms, the price implies a Bear weight of about [[implied_bear]]. I give the Bear [[Bear.prob]]: the contracts are delivered but returns are thin, cloud revenue stops near $2.2 billion, and refinancing dilutes. So the market is ten points more optimistic than I am, and this is not a stock to buy on the theory that the sell-off over-reacted.

To earn 13% a year, Akamai would need about [[Hurdle.eps]] of GAAP EPS in 2031, [[Hurdle.cagr]] growth a year, halfway between my Base and my Bull. That requires cloud revenue around $3.8 billion at a 25% margin with buybacks restarting, which means a second set of large contracts. Weighting the cases [[Bull.prob]] Bull, [[Base.prob]] Base and [[Bear.prob]] Bear gives a value of about [[pw_ev]] and an annual return of [[pw_return]]. The R/R is [[rr]]: the Bull is worth [[Bull.value]] and the Bear [[Bear.value]]. The price at which the same case clears 13% is about [[entry]]. Even with no Bear weight at all (break-even [[breakeven_bear]]) the stock would not clear 13%. The compounding rate at a flat multiple, [[compounding]], looks high but is mostly the recovery from a depressed 2026, and the multiple itself compresses from 33 to 18 times, taking [[rerating]] off the return.

The earnings-power value is a useful floor to look at. Capitalising five-year average owner earnings of $0.45 billion at 9% gives about $5.0 billion, or $35 a share. That says about 40% of the price pays for what Akamai earns today after stock compensation and capex, and 60% pays for the contracts. Management is asking for the 60% to be real, and so far the bill for it is on the balance sheet.

Confidence note: this is an Edge case. I can read the security and delivery businesses and the financing. I cannot judge how long AI-compute demand and pricing hold, Anthropic's ability to pay for seven years, or where memory prices go. The scenario ranges are wide for that reason. The funding need is real: roughly $2–3 billion of new capital through 2027 on my numbers `[Estimate]`.

## Final Words {#final}

Akamai is better than the market gave it credit for in November 2025 and not as good as the market thought in May. The security business is growing 10%. The cloud business has landed customers that matter, on contracts with real take-or-pay features, at returns near 13%, with space and power secured. The management team has been candid about the economics. If you asked me whether I would rather own Akamai's business in 2031 than today's, I would say yes.

But what I would be buying is a company that has changed from an unlevered cash machine into a levered builder, and the price of $84 already pays for most of the likely outcome. At 33 times GAAP earnings, with owner earnings at a five-year low, a 13% project return, a single large counterparty and a financing plan I can describe only as "measured," the probability-weighted case compounds at [[pw_return]], not 13%. A buyer at today's price is paid for taking the execution and financing risk with a good chance of a fair return and a poor chance of an excellent one. The stock reaches my hurdle at [[entry]], about 23% below the price. Until then I will watch.

What would change my mind? Three things, each with a date. Cloud revenue of at least $120 million in Q4 and $180 million a quarter by Q2 2027 would show the contracts ramp as promised. A margin guide for 2027 at or above 24% non-GAAP, with GAAP margin turning up by Q4 2027, would show costs peaking in the first half as management says. And the $1.15 billion of notes repaid from cash in September 2027, without more than $2 billion of fresh paper, would show the build is funded. Failing any one moves the numbers by an amount I have fixed in advance:

::tests

## Appendix: The Numbers {#numbers}

The tables below carry the framework's required numbers. The argument for each is made in the chapters above.

### Growth levers

::table levers

### Moat, customer and profit pool

::table moat

### Competitors

::table competitors

### Promises ledger

::table promises

### Risks and triggers

::table risks

There is a reflexive loop: the financing depends on the stock and on the credit rating, and the customer warrant is worth more if the stock rises. A stranded-capex ruin path exists only in the Bear, where contracts are delivered on thin returns and financing costs rise; with $4.2 billion of cash and securities, $1.5 billion of annual operating cash flow and coupons near zero, I see no ruin path inside the five-year window.

### Catalysts

::table catalysts

### Sentiment and positioning

::table sentiment

Appearances: in the window I found no conference or media appearances by Leighton or McGowan beyond the Q1, Q2 and Q3 calls and the September 24 Anthropic call. I could not retrieve the investor-relations events page. Akamai publishes no shareholder letter; the proxy and the 10-K are the substitutes.

## Sources {#sources}

::sources

::disclaimer
