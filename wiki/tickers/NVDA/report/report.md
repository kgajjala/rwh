::toc

::updates

On November 30, 2022, OpenAI released ChatGPT. Nvidia had just finished a year in which revenue went nowhere, $27.0 billion against $26.9 billion the year before, and operating margin fell to 16% after a gaming and crypto inventory hangover. Four years later it is finishing a year that should end near $410 billion of revenue, fifteen times as much, with operating margins above 60%. The stock has done well but not that well: an investor on November 30, 2022 has made about 9 times their money in total return, against about 6.4 times in AMD, 6.5 times in Broadcom and 1.9 times in the S&P 500. Revenue outran the stock because the multiple came down.

::chart since_chatgpt

The last six weeks are the part the market is trading. Nvidia's index peaked in early October. On November 5 the stock fell 9% in a sell-off of AI hardware names. On November 12 Jensen Huang, who co-founded the company in 1993 and ran it for 33 years, resigned as chief executive and director, effective immediately, after reports about his relationship with a woman suspected of ties to Chinese intelligence; the chief financial officer, Colette Kress, is interim CEO ([8-K](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm)). On November 16 the Commerce Department required export licenses for five more countries and for data centers that rent compute to Chinese firms. The stock closed that day at $156.14 and traded at $154.60 this afternoon, 36% below its 52-week high, a few hours before the company reports its third fiscal quarter.

All this time the numbers kept rising. In August management guided revenue up about 70% in fiscal 2028, the first time it had given a full-year outlook, and called that number constrained by supply, with customer forecasts pointing to demand doubling. Consensus for fiscal 2028 EPS has risen about a quarter in 90 days. At today's price the stock trades at 9.7 times that consensus.

So the question is not whether next year is good. It is what comes after it. Every large buyer of Nvidia systems now has a second chip in volume: Google's TPU, which Google now sells outright; Amazon's Trainium; AMD's Helios rack; and the custom chips Broadcom designs for six customers, whose revenue Broadcom expects to double in each of the next two years. Nvidia is also financing a growing share of its own demand. I start with the business and how it makes money per gigawatt. The key debate comes next: can a general-purpose platform hold its price and share against chips its customers design. The second debate is the balance sheet behind the growth. Then management, now without its founder, and the valuation: what $155 assumes and what 13% a year would need.

## Business Overview {#overview}

Nvidia designs accelerated-computing systems and outsources their manufacture, mainly to TSMC for chips and packaging and to the three memory makers for HBM. Since fiscal 2027 it reports two market platforms. Data Center is GPUs, CPUs, networking, the Groq LPU and software, sold as chips, boards or whole racks to cloud providers and to everyone else. Edge Computing is workstations, PCs, gaming, cars and robots. Data Center was 93% of revenue in the latest quarter, and Nvidia splits it into Hyperscale and a group it calls ACIE: AI clouds (the neoclouds), industrial and enterprise customers, sovereign programs and AI start-ups.

::table quarters

Three things stand out. First, the growth is broad: ACIE grew 25% in the quarter against 13% for Hyperscale and is now 45% of Data Center revenue. Second, margins are at a peak. Gross margin held at 75% for two quarters and management has said it will fall to 71–72% in the fourth quarter. Third, cash lagged profit. Operating cash flow was $24.1 billion against $59.7 billion of net income because receivables rose to 60 days of sales and inventory to $31.6 billion.

::chart rev_mix

The unit that explains the business is the gigawatt of data-center capacity, and management now speaks in it. Nvidia's revenue per gigawatt has gone from about $18 billion with Hopper to about $25 billion with Grace Blackwell and about $40 billion with Vera Rubin, because each generation sells more of the rack: the CPU, the scale-up switch, the network cards, now a low-latency inference chip from the Groq license. Growth is gigawatts times dollars per gigawatt.

::table drivers

A few accounting points before the debates. GAAP net income now includes large gains and losses on Nvidia's equity stakes ($7.8 billion of net gains in the second quarter), so I value the company on earnings excluding them. From fiscal 2027 Nvidia's non-GAAP figures include stock compensation, so non-GAAP and GAAP operating income are within about 1% of each other, and stock compensation is about 2% of revenue. China data-center revenue is zero in the outlook. And the fiscal year ends in late January, so fiscal 2028 is roughly calendar 2027.

## The Platform Against the Chips Its Customers Design {#platform}

Here is where things stand. By adding up what the chip vendors report, Nvidia takes about 83% of the money spent on AI accelerators and their networking in 2026. The companies' own guidance puts that near 80% in 2027 and 70–73% in 2028, because Broadcom's AI revenue is guided from $58 billion to about $115 billion to about $230 billion while Nvidia's guide is limited by supply.

::table share

Two rows matter more than the totals. Anthropic and OpenAI, the two labs Nvidia has invested in most heavily, have each contracted only about 40% of their announced capacity on Nvidia. Nvidia is the largest supplier to both and the majority supplier to neither.

### Management's narrative

Nvidia's answer is that it sells something different from a chip. Huang, asked on the August call about OpenAI's Jalapeño chip and Anthropic's TPU orders:

> "Well, we're building something very different. Whereas many of these XPUs are inference-specific chips for one cloud or one service, NVIDIA is a platform, an entire AI factory platform that spans the entire AI life cycle that you can use in any cloud. It's in every cloud. You can run anywhere. We'll help you set it up anywhere."
> — Jensen Huang, Q2 FY2027 earnings call, August 26, 2026

The second half of the argument is the customers who will never design a chip. Asked what drives the fiscal 2028 outlook, he split the market in two:

> "Most people see just hyperscalers. And that's half of the picture. The other half of the picture is what we call ACIE, and that's all the enterprise, the neoclouds, the sovereign AIs, that part of the world is invisible to everybody. And the reason for that is because they don't buy custom chips, they don't buy chips one at a time, they really need an entire factory platform built for them."
> — Jensen Huang, Q2 FY2027 earnings call, August 26, 2026

And Kress put the economics in one line, which is also the clearest statement of how Nvidia has grown faster than its customers' capex:

> "Since Hopper, our revenue opportunity has grown from roughly $18 billion per gigawatt to $25 billion with Blackwell, to $40 billion with Vera Rubin, which now spans Vera CPU, Rubin GPU, NVLink, InfiniBand or Ethernet and Groq LPU announced earlier this week."
> — Colette Kress, Q2 FY2027 earnings call, August 26, 2026

This is a strong case and much of it is true. Nvidia runs every major model, closed and open. Its systems are the ones lenders will finance, because they can be redeployed. The ACIE half grew 138% in a year and depends on Nvidia's full stack. And the company keeps shipping: Vera Rubin began production shipments in August, on the annual cadence it promised.

### Poking holes in it

The first hole is that the largest buyers have already split their orders. Anthropic's IPO filing describes "a multi-chip compute architecture across AWS Trainium, Google TPUs, Nvidia GPUs, and AMD GPUs," and the press reading of it is that Nvidia capacity is the easiest for Anthropic to walk away from ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ipo-filing-shows-most-of-its-compute-goes-to-r-and-d-not-serving-customers-company-details-massive-usd800-billion-in-tpu-and-gpu-contracts)). OpenAI has 10 GW of Broadcom custom chips, 6 GW of AMD and 2 GW of Trainium alongside about 12 GW of Nvidia. These are the customers whose usage is growing fastest.

The second is that the strongest alternative is no longer captive. Google Cloud's chief executive told the same Goldman conference Huang spoke at that "the size of our accelerator business, our TPU business, is more than twice that of the next largest hyperscaler," and that customers can now buy TPU systems "as a capital purchase" for their own data centers or rent them through a neocloud Google set up with Blackstone ([transcript](https://stockanalysis.com/stocks/googl/transcripts/737252-goldman-sachs-communacopia-technology-conference-2026/)). Oracle will resell them. Alphabet's inventory rose from $2.4 billion to $13.3 billion this year to stock TPU systems, and it expects most of that revenue in 2027. On SemiAnalysis's benchmark, Ironwood served tokens at $0.181 per million against $0.222 for Nvidia's B200 at one interactivity point, while Nvidia kept the lead in raw performance ([InferenceX](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam)). That is ACIE's territory, the half Huang called invisible.

The third is the price umbrella. Nvidia's $40 billion per gigawatt sits against $20–30 billion for a Broadcom custom chip, by Hock Tan's own range. A buyer that moves a gigawatt to custom silicon saves about $15 billion of capital, and the illustration below shows what that does to Nvidia if it happens at scale. The umbrella is also what funds the competition: AMD guides revenue up more than 80% in 2027, and Amazon says most of its Bedrock inference already runs on Trainium.

The fourth is software. CUDA was the lock. AMD's third-quarter remarks say an Anthropic engineer used Claude to bring a new model up on AMD racks over a weekend, a job that used to take months. Google is opening a PyTorch backend for TPUs and Amazon has open-sourced one for Trainium. For a lab with a few models and many engineers, the lock is now a few weeks of work. For an enterprise it is still a lock.

::table unit

Here is what that arithmetic says. A 15% price cut takes a fifth off Nvidia's gross profit per gigawatt. Losing 40% of the gigawatts to custom chips takes two-fifths. Both together halve it, and Nvidia would then need gigawatts to double just to stand still. That is the mechanism of my Bear and why my Base already concedes a few points of margin.

Where I come out: the platform argument holds where customers cannot build alternatives, and that half is the faster-growing one today. At the six or seven largest buyers the argument has already been partly lost, by the companies' own contracts. My Base has Nvidia's share of spending falling to about 58% by 2030 and gross margin to 69%. The first evidence will be Hyperscale revenue: Kress said it would reaccelerate in the fourth quarter as Vera Rubin supply grows. If it falls instead while Broadcom meets its guide, the share-break case is arriving.

### Rings of profit

::table rings

The point of the rings is that the threat is real and concentrated. About 45% of Data Center revenue goes to buyers who do not design chips, and attach products ride along with the GPU. The exposed ring is inference at the largest buyers, which is the fastest-growing workload and the one every alternative chip targets first. From 2027 the protection around the first ring also thins, because Google and Amazon start selling their chips to the same neoclouds and sovereigns.

## Financing the Customers {#financing}

The second debate is quieter and, for a ten-year holder, nearly as important. Nvidia is now part of how its customers pay for Nvidia systems.

::table financing

### Management's narrative

Kress addressed it directly in August, which I give the company credit for:

> "We recognize the scale of this support, and we know some will call this circular financing. We see it differently. ... And our risk is limited. The NVIDIA Compute platform is fungible and durable and can be redeployed to support other customers. For context, we expect demand from the AI labs for which we expect to leverage our balance sheet to contribute toward roughly a quarter of our business next year."
> — Colette Kress, Q2 FY2027 earnings call, August 26, 2026

Huang made the same point at the Goldman conference more briefly: "we put a little bit of money in, and a lot of money comes back," and the aim is to turn Nvidia compute into an "investable asset" financed by institutional capital ([transcript](https://stockanalysis.com/stocks/nvda/transcripts/740955-goldman-sachs-communacopia-technology-conference-2026/)). Nvidia has also arranged partnerships with six large asset managers to raise more than $500 billion of outside capital for lab infrastructure, so most of the money is not its own.

### Poking holes in it

The first hole is size. The guarantees alone, $108.5 billion at their maximum, are about a quarter of this year's revenue, and they arrive from fiscal 2029, exactly when my Base has demand flattening. A guarantee on a data-center lease is called when the tenant cannot pay, which is the case where GPUs are also hardest to redeploy at a good price.

The second is the supply commitments. They rose from $95 billion in January to $279 billion in July, mostly memory, and $175 billion of them fall due in fiscal 2028 and 2029. Nvidia has been here in miniature: it took a $4.5 billion charge in the first quarter of fiscal 2026 when export controls stranded H20 inventory and purchase obligations. The same commitments that secure supply in a boom fix costs in a bust.

The third is quality of revenue. Receivables went from 45 to 60 days of sales in one quarter on extended terms for large buyers, and Kress's "roughly a quarter of our business next year" means roughly a quarter of fiscal 2028 revenue goes to customers who rely on Nvidia's balance sheet. That does not make the revenue fake. It does make it more cyclical than the headline growth suggests, and it means the equity stakes, worth about $96 billion, rise and fall with the same customers.

Where I come out: this is vendor financing at a scale I have not seen in a technology hardware company, and I treat it as a Bear amplifier, not a Base cost. In the Base it costs nothing, because the labs keep growing and pay. In the Bear it costs about $1.50 a share in guarantee losses, valued as an option line, and it is part of why the Bear multiple is 13 times. The test I would watch is receivables: above 70 days of sales would say the terms are doing the selling.

## Management, Capital Allocation and Incentives {#mgmt}

For 33 years management was Jensen Huang. He set the bets that made the company, CUDA in 2006, the data center long before it paid, the purchase of Mellanox in 2020, and the move from chips to whole racks, and he was its public voice on every one. The record since ChatGPT is in the opening chart: revenue up fifteen-fold, the stock up about nine. He resigned on November 12. The board has an independent investigation under way, a search for internal and external candidates, and, by the Financial Times's account, has approached Arm's chief executive, Rene Haas; Nvidia says it has not formally engaged anyone ([CNBC](https://www.cnbc.com/2026/11/16/nvidia-jensen-huang-return-tech.html)). The board chair said operations, customer commitments and the roadmap should "continue without interruption." Kress, the interim CEO, has been CFO since 2013 and is also keeping that job.

I cannot judge from outside how much of the roadmap lived in one person. I can say what to watch: whether the architecture and systems leads stay, whether Rubin Ultra ships in the second half of 2027, and who is named. Until then I treat the leadership change as a risk to the Bull, not as a change to the Base.

::table deals

::table capalloc

The cumulative column says two things. Nvidia generated $196 billion of free cash flow in five fiscal years and issued $19 billion of stock compensation, so owner cash was about $177 billion, and it returned $96 billion of it, mostly in buybacks, while the diluted share count fell only 3.3% because the price rose so fast. And the most countercyclical thing it did was the earliest: in fiscal 2023, the trough year, it bought back $10 billion, more than two and a half times that year's free cash flow, at prices I estimate near $16 a share on today's split basis. Since then the buyback has followed cash flow, $40 billion in fiscal 2026 at about $143 a share and $20 billion in the second quarter alone, with a policy of returning half or more of free cash flow.

What changed in 2026 is where the rest of the cash goes. About $96 billion now sits in equity stakes in customers and partners, and the balance sheet backs the guarantees described in the financing chapter. I grade Nvidia **Steward (not Outsider)**: one strong trough-buying year, then programmatic returns, with the marginal dollar going into financing demand rather than into its own shares at low prices.

### The incentives

::table incentives

The plan paid for revenue, operating income and relative stock return, and nothing in it paid for returns on capital. The goals were set well below what happened, so every component paid at or near its maximum. The plan did not encourage the build-up of commitments and guarantees, but nothing in it discouraged it either. With Huang gone, the next CEO's package is the first chance to add a capital-efficiency measure, and I will read it when it is filed.

Against its own guidance, management is a **consistent beater**: revenue and EPS have beaten consensus six quarters running, and the second quarter came in at $96.2 billion against about $91.7 billion expected.

::table promises

Is this the right team? Through November 12, yes, on every operating measure in this report. The question now is whether the system Huang built runs without him. The best evidence for it is the depth of the bench that delivered Rubin on time and the fact that customers' purchase orders for it are already placed. The best evidence against is that the company was organized around one person to an unusual degree.

## Valuation and Model Assumptions {#val}

I value Nvidia at the end of fiscal 2032 (about January 2032), five fiscal years after the current one, on earnings per share excluding gains on equity stakes, which are close to its non-GAAP EPS and already charge stock compensation. The model builds revenue from Data Center and Edge Computing, applies one gross margin to both because Nvidia does not report margin by platform, and subtracts operating expenses as a share of revenue. It adds about $2 billion of net interest income, taxes at 16.5% rising to 17–18%, and divides by diluted shares after buybacks. The base year is fiscal 2027 at about $410 billion of revenue: two reported quarters, the third-quarter guide and fourth-quarter consensus. Nvidia is cyclical, so the terminal margins are through-cycle margins below today's: 72% gross in the Bull, 69% in the Base and 61% in the Bear, against about 74% for fiscal 2027.

::model_build Base

The model grows each segment at a constant rate, but the Base I have in mind is lumpy: revenue jumps about 70% in fiscal 2028 as guided, then grows little, as a market that keeps growing is offset by share falling to about 58% of spending. Data Center reaches about $655 billion and total revenue about $694 billion in fiscal 2032. Operating margin falls from about 65% to 58.5% as gross margin gives up five points and operating expenses rise to 10.5% of revenue. Buybacks retire a net 2.4% of shares a year. EPS rises from [[Base.eps0]] to [[Base.eps]], and at 16 times that is [[Base.value]]. Sixteen times is about where the stock trades on this year's earnings, and an ordinary multiple for a business that has stopped growing but returns most of its cash.

::scenarios

The Bull is boom demand plus a platform that holds: spending reaches about $1.7 trillion by 2030 and Nvidia keeps about two-thirds, so revenue passes $1.1 trillion, gross margin settles at 72%, and the stock is worth [[Bull.value]] at 20 times. Its implied perpetual growth is below the risk-free rate, so it is a high case rather than an impossible one, but only about 2% of companies above $25 billion of sales have grown this fast for five years. The Bear is digestion plus a share break: capex falls about a third from its peak after fiscal 2028, custom chips reach parity in training at the labs, revenue drifts back to about $420 billion, gross margin falls to 61% as supply commitments are absorbed, and at 13 times it is worth [[Bear.value]]. That is close to the company's earnings power on this year's numbers.

The option lines sit outside the cases: the equity stakes at their carrying value, about $4 a share; a 20% chance of China sales resuming under license; and a 25% chance of guarantee losses in a bust.

::return_math

Here is where the price stands. To earn an ordinary 10% a year from [[price]], the stock needs fiscal 2032 EPS of [[Priced-in.eps]] at 16 times, a little below my Base: the fiscal 2028 guide, held roughly flat for four years. To earn 13% it needs [[Hurdle.eps]], a fifth of the way from my Base to my Bull.

Weighted 25% Bull, 50% Base and 25% Bear, plus the option lines, the value is [[pw_ev]] and the return is [[pw_return]] a year. The price that returns exactly 13% is [[entry]], just above today's price. The return is nearly all compounding: EPS grows [[Base.cagr]] a year in the Base and the dividend adds 0.6%, while the multiple contributes nothing. That passes the re-rating test easily. It does not pass the fragility test. The break-even Bear probability is [[breakeven_bear]], one point above the 25% I assign, and the market's price implies [[implied_bear]]. Ten points moved from Base to Bear take the return to about 12.5%. So the verb is Initiate by the rules, with the strongest possible warning attached: the answer depends on whether the Bear is one chance in four or one in three.

This is an Edge case for me. I can judge the unit economics, the customer contracts and the financing. I cannot judge from outside whether Nvidia's next two architectures keep a cost-per-token lead over TPU 8 and Jalapeño, or how much of the roadmap depended on Huang, and those two things decide the Bull.

Bias check, because the wiki's competition study written this morning read Watch: the change is driven by method and price, not by new evidence. That study ran the same scenarios to fiscal 2031, one year short of a five-year horizon; extending to fiscal 2032 adds a year of buybacks, and the study left out the option lines. The stock is also $1.50 lower. No input came from someone paid to hold the view, the verb does not follow analysts (who were bullish both times) or the price fall, and the five-year record carries more weight here than any quarter.

## Final Words {#final}

Nvidia is the best-positioned company in the most important buildout in computing, and its stock is down 36% because the market has started to price what happens after the buildout peaks. The market has that right. Every large buyer now has a credible second chip, the alternatives are cheaper per gigawatt, Nvidia is financing a quarter of next year's demand, and the person who made every big bet just left.

What I think the price gets slightly wrong is how much is left even in an unexciting outcome. My Base has Nvidia losing about a third of its share and growing almost nothing after next year, and it still compounds EPS at about 11% a year through buybacks on a balance sheet with net cash. At [[price]] the probability-weighted case just clears the 13% hurdle.

The verb is Initiate for someone who does not own it, at or below [[entry]], and Add for someone who does. It is probability-fragile, and I would say so to anyone acting on it. Tonight's report is the first test. The three that would change my mind, with consequences fixed in advance:

::tests

## Appendix: The Numbers {#numbers}

The tables carry the framework's required numbers. The argument for each is in the chapters above.

### Five-year record

::table five_year

### Growth levers

::table levers

### Moat, customer and profit pool

::table moat

### Competitors by product family

::table competitors

### Risks and triggers

::table risks

Reflexive loops: the labs Nvidia finances buy Nvidia systems, and their ability to raise money depends partly on the value of AI infrastructure, which Nvidia's results set; a fall in either feeds the other. Stock compensation is small at about 2% of revenue, so a lower share price does not create a dilution spiral. Ruin path: none within five years. Nvidia has net cash, and even fully called guarantees are less than one year of free cash flow at the fiscal 2027 run rate.

### Catalysts

::table catalysts

### Sentiment and positioning

::table sentiment

## Sources {#sources}

::sources

::disclaimer
