::toc

::updates

On November 3, 2025, Snowflake closed at $277.14, the highest price it had seen in almost four years. Five months later, on April 10, 2026, it closed at $121.11. The company lost 56% of its value in 110 trading days. Nothing broke. In the middle of that fall Snowflake reported two quarters: product revenue up 29% and then up 30%, remaining performance obligations up 37% and then up 42%, and the strongest quarter of new customer acquisition in its history. The business did not stumble once while the stock was cut in half.

What changed was the story investors told about the next decade. Through the winter of 2025 and into the spring of 2026 the market decided that powerful agentic models were about to make the governed data warehouse an expensive middleman. Aaron Katz, the CEO of ClickHouse, put the argument crisply in public: Snowflake's engine was built for the speed at which humans click through dashboards, and agents want queries that are far faster and far cheaper than that. Databricks raised money in December 2025 at a $134 billion valuation on roughly the same revenue Snowflake had, growing twice as fast, with AI revenue about ten times larger. Snowflake's own net revenue retention had fallen from 171% at its peak to 125%. On April 9, 2026, the whole software complex repriced in a single session on fears that managed agents from Anthropic and OpenAI would absorb the workflow layer: Cloudflare fell 12%, Snowflake 9%, ServiceNow 7%. Snowflake bottomed the next day.

Then it nearly tripled. On May 27, 2026, Snowflake reported product revenue up 34%, the largest sequential dollar increase in its history, announced a $6 billion multi-year commitment from AWS and raised full-year guidance. The stock rose 36.5% the following session, from $175.26 to $239.20. On September 2 it reported a third consecutive quarter of accelerating growth, 37%, raised guidance again, and rose 16.6%. It closed on October 23, 2026 at $325.43, up 169% from the April low and 17% above the November 2025 peak.

::chart drawdown

So the bears were wrong, and loudly wrong. AI did not route around the warehouse; it drove traffic into it. Sridhar Ramaswamy told analysts on the September call that Snowflake's own AI products "contributed approximately half of the acceleration that we are seeing." That is about as clean a refutation as a thesis ever gets in public.

This piece is about what comes after being right. I want to do three things. First, work out what actually caused the round trip, because the mechanism matters more than the moral: the collapse was not a judgment about AI so much as a judgment about a guidance number, and the guidance number was wrong for a reason that was knowable at the time. Second, take the second debate seriously, which is not whether AI grows Snowflake's revenue but what that revenue costs to serve and who gets paid out of it. Third, ask the only question that is left: at $325, having bought the recovery, what does the price assume? The answer is the uncomfortable part of this report.

## Business Overview {#overview}

Snowflake sells compute and storage for enterprise data, metered. Customers buy capacity in advance under multi-year contracts and draw it down as they run queries, so revenue is consumption, not seats. In fiscal 2026, which ended January 31, 2026, product revenue was **$4,472.3 million**, up 29%, inside total revenue of $4,684 million. Professional services is the remainder and runs at about 4% of the total at roughly break-even; it exists to get workloads onto the platform, not to make money. There is one reportable segment.

::table quarters

The company's own key metrics are the best short description of the business. As of July 31, 2026 there were **14,554 customers**, up from 13,245 six months earlier; 829 of the Forbes Global 2000, who together produced about 41% of revenue; 828 customers spending more than $1 million on a trailing twelve-month basis; and net revenue retention of **126%**, which had turned up from 125% at the January year-end. Remaining performance obligations were $9.0 billion with a weighted-average remaining contract life of 2.4 years, of which management expects about 54% to convert to revenue within twelve months.

Three accounting points matter before the argument starts, and the third is the one that decides this report.

The first is that consumption revenue is recognized as customers burn capacity, not as they sign. RPO therefore leads revenue, and the gap between RPO growth and revenue growth is a genuine signal rather than an artifact. In the quarter the stock fell 11%, RPO was growing 37% against revenue at 29%.

The second is that Snowflake guides on observed consumption. Brian Robins, the CFO, said it plainly on the September call: "As always, our forecast is based on observed consumption patterns." That is a conservative and defensible method, and it has a structural blind spot that I will come back to, because it is the single best explanation for both halves of the round trip.

The third is stock-based compensation. Snowflake's headline profitability is non-GAAP and excludes SBC. In fiscal 2026 SBC was **$1,600 million on $4,684 million of revenue, 34% of every dollar that came in**. The company reported non-GAAP operating income of $489.7 million that year and a GAAP operating loss of $1,435.2 million. In the second quarter of fiscal 2027 the pattern held: non-GAAP net income of $235.3 million against a GAAP net loss of $191.7 million, with $456.4 million of SBC-related charges in between. Every number in this report that describes Snowflake's profit will say whether it is before or after paying the people who produce it.

## Did AI Eat the Warehouse, or Feed It? {#debate}

Let me start with where things stand.

::table roundtrip

Set the price phases against the quarterly table above and the drawdown makes no sense on fundamentals. Growth went 29%, 30%, 34%, 37% straight through it. Something other than the business was moving.

### Management's narrative

Management's case is that AI is not a competing destination for enterprise data but a reason to put more of it in one governed place and then query it far more often. Ramaswamy has been consistent about the mechanism since the Q1 call in May:

> "AI is accelerating the value that people can get from the data that they have put into Snowflake … it in turn drives more consumption on the core data platform simply because it's much easier to get projects done."
> — Sridhar Ramaswamy, CEO, Q1 FY2027 earnings call, May 27, 2026

By September he was making the stronger, structural version of the claim:

> "Customers using AI on Snowflake consume more across the data platform, creating a structural multiplier for our business … Put simply, the agentic enterprise runs on Snowflake."
> — Sridhar Ramaswamy, CEO, Q2 FY2027 earnings call, September 2, 2026

The products carrying that claim are two, both renamed at Snowflake Summit in San Francisco in June 2026. **CoCo** is Cortex Code, a coding and data-engineering agent that understands the customer's own schema and semantics. **CoWork** is the former Snowflake Intelligence, an agentic workspace for business users. By the July quarter CoCo was in more than 9,100 accounts, having added over 2,000 in three months, and CoWork was in 5,800. Neither existed eighteen months ago.

The go-to-market facts support the narrative. In the July quarter Snowflake added 692 net new customers, up 32% year over year. Net revenue retention turned up. AWS signed a $6 billion, five-year commitment, more than double the prior agreement, with expanded joint selling. And Robins was explicit about where the upside in the model came from:

> "CoCo had the largest driver to the increase in our forecast."
> — Brian Robins, CFO, Q1 FY2027 earnings call, May 27, 2026

On the bear thesis specifically, management's answer is neutrality and gravity. Christian Kleinerman, who runs product, told Karl Keirstead of UBS that model neutrality is "absolutely" a competitive advantage because customers who committed to a single model provider have regretted it, and told Tyler Radke of Citi that the reason applications will not become their own data platforms is simple: "If I use three applications, I am not going to copy my data into three different platforms." Ramaswamy's version is more elegant: "as software gets easier and easier to create, it is the data and semantics that acquire more and more importance."

I think management is substantially right, and I want to say so before I argue with them. The bear case as stated in late 2025 was a claim about query economics that turned out to be a claim about the wrong variable. Agents do want cheaper queries. They also want vastly more of them, and they want them against governed, permissioned, semantically described data that an enterprise will actually let an autonomous process touch. Snowflake charges by consumption. More queries is more revenue even if each query is cheaper. The bears modelled the price and forgot the volume.

### Poking holes in it

The first hole is that the collapse was never really about agent architecture, so the recovery does not vindicate as much as it appears to. Look at what the market was handed. On December 3, 2025 Snowflake beat on the quarter and guided Q4 product revenue to 27% growth with a 7% non-GAAP operating margin; the stock fell 11.4% the next day. On February 25, 2026 it beat again and guided **full-year fiscal 2027 product revenue to $5,660 million, 27% growth**, decelerating from the 30% it had just printed. The agentic-disruption essays were the explanation the market reached for, but the thing it was actually repricing was a guidance number that said growth was slowing. By September that same year, guidance for the same fiscal year was $6,070 million and 36%. The company beat its own initial full-year guide by $410 million and nine points of growth in six months.

That is not a forecasting accident; it is the predictable output of the method. Robins told analysts in May that CoCo was new, so there was no observed consumption behaviour to forecast from, and that the company now layers it into the model. A guidance philosophy anchored on observed consumption cannot, by construction, include a product that has not been consumed yet. In February 2026 Snowflake guided a year that excluded the contribution of the products its CEO was simultaneously describing as the future of the company, and the market read the resulting number as evidence that the future was not arriving. Both the fall and the recovery were the market marking to a forecast that was never trying to answer the question being asked of it.

The second hole is that the clean refutation is also a short one. We have three quarters of acceleration. Three quarters is a trend in a press release and a data point in a five-year thesis. Koji Ikeda of Bank of America asked the right question in September — whether AI consumption represents higher lifetime consumption or projects pulled forward — and Ramaswamy's answer was that "this is not merely projects being pulled forward," citing breadth and depth of use cases, while declining to share uplift numbers. That is an assertion, not a disclosure. Snowflake has not quantified AI revenue, has not given an AI net revenue retention figure, and has not said what share of the raised full-year guide is CoCo and CoWork beyond "approximately half of the acceleration." A migration burst, in which every large enterprise rebuilds its data foundation for agents over three or four years and then stops, looks exactly like this for exactly this long.

The third hole is that the adoption curve of the two breakout products is already diverging. CoCo went from roughly 7,100 accounts in April to 9,100 in July, up about 28% in a quarter. CoWork went from roughly 5,200 to 5,800, which Ramaswamy described on the call as "up nearly 11% quarter-over-quarter." CoCo is a developer tool, sold into the people who were already Snowflake's users. CoWork is the one that was supposed to put the platform in front of every business user in the enterprise, and it is the one decelerating. The bull case for a structural multiplier rests more on CoWork than on CoCo, because an engineering productivity tool makes existing workloads cheaper to build while a business-user agent creates new ones.

The fourth hole is competitive and has not gone away because Snowflake's quarter was good. Databricks was raising at $134 billion in December 2025 on about $4.8 billion of run-rate revenue growing over 55%, with net revenue retention above 140% and AI revenue above $1 billion against Snowflake's roughly $100 million at the time. Those are not numbers that get refuted by one good Snowflake quarter; they say the category is growing fast enough for both and that the faster grower is taking the harder workloads. Ramaswamy himself conceded the point at Summit, acknowledging that differentiating data platforms is getting harder.

So let me turn the debate into arithmetic. Snowflake does not disclose unit economics, so the table below builds an illustrative customer from what the company does disclose, and then asks what AI does to it.

::table unit

The illustration says something the narrative does not. AI adds revenue per customer, and it adds it at a lower gross margin, so the gross profit per customer grows meaningfully less than the revenue does. Management has now put that in the guidance: Robins cut the full-year non-GAAP product gross margin outlook to 74.0% from 75.0%, and said why — "This revised outlook includes a higher revenue mix from fast-growing AI workloads … which carry a lower contribution margin today." The word doing the work is *today*. The bull case needs inference costs to fall faster than AI mix rises. Ramaswamy's August 18 appearance on Bloomberg, where he argued that the next phase of enterprise AI is about economics and model routing rather than always reaching for the largest model, is management telling you they know this is the fight.

Where I come out: the bears lost the argument they picked, and they picked the wrong one. AI is a genuine demand tailwind for a consumption-priced data platform, and I would now underwrite high-teens-to-twenties revenue growth for several years with reasonable confidence. The debate that is actually open is not whether the revenue comes. It is what fraction of it ever reaches an owner, which is the subject of the next chapter.

### Rings of profit {#rings}

It helps to sort Snowflake's gross profit by how exposed each part is to the agentic thesis.

::table rings

The reassuring reading is that roughly three-quarters of gross profit sits in core warehousing and engineering workloads that are sticky, governed and growing, and that the AI ring is additive rather than substitutive. The uncomfortable reading is that the ring growing fastest is the one with the worst margin, and the ring with the best margin — storage and the data-sharing network — is the one most exposed to open table formats. Snowflake's own answer to Iceberg has been to embrace it: Iceberg v3 support and bidirectional read/write through the Horizon Catalog on Apache Polaris, announced at Summit. That is the right strategic call and it is also an admission that storage lock-in is finished as a profit engine. What replaces it has to be the context and governance layer, which is exactly what Ramaswamy says he is building.

## What AI Costs, and Who Gets Paid {#margin}

Here is the second debate, and in my view the one that decides the stock.

Snowflake generated $1,222 million of operating cash flow in fiscal 2026 and spent $102 million on property and equipment, for $1,120 million of free cash flow at a 24% margin. On that basis it is a cash machine with no capital needs. In the same year it issued **$1,600 million** of stock to its employees. Subtract the stock from the cash and the business consumed $480 million.

That is not a one-year artifact. Owner earnings, defined as operating cash flow less SBC less capital expenditure, have been negative in every year of Snowflake's public life and were more negative in fiscal 2026 than in fiscal 2024.

::chart revenue_dollar

::table owner

The trend inside that table is genuinely improving: SBC has fallen from 49.6% of revenue in fiscal 2022 to 34.2% in fiscal 2026 and is running near 29% in the first half of fiscal 2027. Operating leverage is real — the non-GAAP operating margin went 6% in fiscal 2025, 10% in fiscal 2026, and is guided to 14.5% this year, with the September raise taking it up a point mid-year. Management deserves credit for this; it is a disciplined company now in a way it was not three years ago.

But the gap has to close a very long way. For Snowflake to earn the 13% a year this framework requires, the arithmetic is not that the margin keeps improving. It is that a business which has never produced a dollar of owner earnings produces several billion of them inside five years.

There is a second cost, related and easier to see. Snowflake has spent **$3,398 million on buybacks since fiscal 2024** — $592 million, then $1,932 million, then $874 million — and the diluted share count has gone up every year anyway, from 300 million in fiscal 2022 to 337 million in fiscal 2026, with 352.8 million shares outstanding as of August 21, 2026. The buyback is not returning capital. It is paying, partially, for the dilution the compensation plan creates. In fiscal 2025 the company spent $1,932 million on repurchases against $1,479 million of SBC, bought back 131% of its own stock issuance, and still ended the year with more shares than it started. Then in September 2026 it raised **$3.75 billion of 0% convertible notes**, $2 billion due 2029 convertible at about $500.38 and $1.75 billion due 2031 at about $483.98, spending $383.5 million on capped calls to push effective dilution out to $820.30 and $548.3 million to retire part of the 2027 notes. A company with $4.3 billion of cash and investments and no capital needs borrowed $3.75 billion. The honest description of Snowflake's capital structure is that it funds its compensation bill with a mix of cash flow, buybacks and convertible paper, and manages the share count at the margin.

None of this makes Snowflake a bad business. It makes it an unusual one. The conventional compounder frame does not apply here, and the Appendix shows why: invested capital, built the standard way as equity plus debt plus operating leases less cash and investments, was **negative $120 million** at the fiscal 2026 year-end and $584 million at the July quarter-end. Snowflake's customers fund it through deferred revenue; it needs essentially no capital to grow. Return on invested capital is not a meaningful number on a base that straddles zero, and there is no reinvestment-rate-times-incremental-return engine to underwrite. The constraint on this business has never been capital. It is the income statement, and specifically what it costs to employ the people who build the product.

So the second debate reduces to one question: is 34% of revenue going to employees in stock a feature of a company that is still scaling, which falls to 12% as it matures, or a feature of competing with Databricks, OpenAI and every hyperscaler for the same few thousand engineers, which does not fall nearly that far? The last five years say the first. The AI talent market says the second. I have assumed something between them, closer to the first, and it is the most consequential assumption in this report.

## Ramaswamy, Capital Allocation and Incentives {#mgmt}

Sridhar Ramaswamy became CEO on February 28, 2024, in one of the more abrupt successions in enterprise software. Frank Slootman retired the day the company also cut its guidance; the stock fell about 20%. Ramaswamy had joined only through Snowflake's acquisition of Neeva, the search startup he founded after fifteen years at Google, where he ran the advertising business as it grew into the largest cash engine in technology. He had been at Snowflake for less than a year.

Judged on operations, the appointment has worked. The company he inherited was growing 29% with a 6% non-GAAP operating margin, a declining retention rate and no credible AI product. It is now growing at the rate shown in the quarterly table above, with a 15% operating margin, retention that has turned up, and two AI products that between them touch roughly 15,000 accounts. He shipped over 430 new capabilities in fiscal 2026 and more than 330 in the first half of fiscal 2027. Whatever one concludes about the stock, the product and go-to-market execution over the last two years has been very good.

### The deals

::table deals

The pattern is consistent and sensible: small, capability-led acquisitions that plug directly into the platform rather than buying revenue. Natoma, announced with the Q1 print, brought an enterprise Model Context Protocol platform and twenty employees, and is already shipping inside the Cortex AI Gateway. Observe is the exception and deserves a flag. It was a $50-billion-market entry into observability, and Jeremy Burton, Observe's CEO, sat on Snowflake's board until he resigned on January 30, 2026 in connection with the deal. The company handled it correctly — a special committee of independent and disinterested directors plus the audit committee approved it — but a related-party acquisition that takes the company into an adjacent market is the kind of thing worth watching rather than nodding through. On Chris Zook's adjacency test it passes on customers and data gravity and is unproven on capabilities.

### The cash

::table capital

The cumulative row is the argument. Since fiscal 2022, Snowflake has produced about $3.6 billion of free cash flow and issued about $5.7 billion of stock. It has spent $3.4 billion buying stock back and the share count has risen 12% anyway. It pays no dividend, which is correct. It now carries $3.75 billion of new convertible debt against $4.3 billion of cash and investments before that raise. There is no capital-allocation record here in the Thorndike sense, because there has been no free capital to allocate: the cash flow has gone to offsetting dilution. On the Outsiders vocabulary I grade Snowflake **Reinvestor, not Outsider** — the reinvestment is in people and product rather than plant, it has produced real growth, and the one countercyclical test that matters was failed rather than passed. In the quarter the stock bottomed near $121, Snowflake was not buying aggressively; the largest repurchase year was fiscal 2025, at prices well above today's lows.

### The incentives

::table incentives

Two things stand out, and they point in opposite directions.

The first is that the annual plan is well constructed for this company's actual problem. The fiscal 2027 PRSU program sets product revenue at 70%, non-GAAP operating margin at 15% and non-GAAP adjusted free cash flow at 15%, on a three-year cliff, with the cash bonus moved onto total revenue so the two plans do not duplicate a metric. Margin and cash flow at 30% combined is a real counterweight to a growth metric, and the three-year cliff is a genuine improvement. There is no return-on-invested-capital metric, which for once is defensible, because invested capital is approximately zero.

The second is the grant that arrived on July 15, 2026. The Compensation Committee gave Ramaswamy a **1,000,000-share performance award**, 0.29% of the company, in five tranches with stock-price hurdles of $324, $375, $427, $479 and $531 over two to seven years, designed, in the filing's own words, "to culminate in adding up to $100 billion of stockholder value." The stock closed at $271.87 that day. Run the arithmetic on the tranches and the picture is unflattering: the first requires a 9.2% annual return over two years, the second 11.3% over three, the third 9.4% over five, the fourth 8.4% over seven and the top tranche 10.0% over seven. **Every tranche of the CEO's maximum payout pays out at a shareholder return below this framework's 13% hurdle**, and the largest tranches require the least. At today's price the first tranche is already effectively earned.

The context makes it worse rather than better. Snowflake's shareholders voted down executive compensation in 2025, and the proxy says why: the magnitude of the new CEO's grants and the fact that three-quarters of the value was in options the holders did not regard as performance-based. Then on June 29, 2026 they voted it down again — 96,340,999 for, 124,481,663 against, 44% support — and approved, against the board's position, a shareholder proposal requiring majority voting for directors. Sixteen days after that second rejection, the committee granted the mega-award. I do not think this is a company being looted; the grant has a ninety-day averaging test, deferred delivery, and a clawback. But a board that has twice been told its pay practices are wrong and responds within a month with a $100 billion milestone award is telling you where it thinks the balance of power sits.

Insiders have been selling into the recovery with both hands. In the ninety days to October 23, 2026, Form 4 filings show **$521.6 million of open-market sales and not one open-market purchase**. Frank Slootman, now a director, sold roughly $190 million across September 16–21 and October 19. Benoit Dageville, the co-founder, sold 50,000 shares on each of five separate occasions. Michael Speiser of Sutter Hill, Christian Kleinerman and the new CRO all sold. Most of this is almost certainly scheduled under 10b5-1 plans, and founders of a six-year-old public company diversifying is not a scandal. But the direction of travel is one-way, and it is happening at prices between $280 and $380.

So is Ramaswamy the right manager? On product and operations, clearly yes, and the last three quarters are his vindication as much as they are a refutation of the bears. On the question this report cares about — whether value created by the business reaches the people who own it rather than the people who work there — the record is not yet there, and the incentive architecture is not obviously pointed at fixing it.

## Valuation and Model Assumptions {#val}

I value Snowflake on owner earnings, not on the non-GAAP earnings the company reports, because the non-GAAP measure excludes stock-based compensation and SBC is this company's largest single expense. The model builds product revenue and professional services separately, each with a gross margin, deducts operating expense as a percentage of revenue, adds net interest income and taxes down to non-GAAP net income, then applies a cash-conversion factor of 1.30 to reflect that cash taxes are far below the book rate and capital expenditure is under 1% of revenue, and finally deducts stock-based compensation after tax. What is left is what an owner earned. Fiscal 2027 is calibrated to the guided $6,070 million of product revenue, a 74.0% product gross margin and a 14.5% non-GAAP operating margin. Here is the Base case, with inputs highlighted:

::model_build Base

In the Base case product revenue compounds **21% a year** to about $15.7 billion in fiscal 2032, the product gross margin holds at 75%, the non-GAAP operating margin reaches roughly 29%, and SBC falls from 29% of revenue to 13.5%. Every one of those is an extension of the trend of the last five years rather than a break from it. Non-GAAP earnings per share reach [[Base.eps]] and owner earnings per share reach [[Base.owner_eps]]. At 25 times owner earnings the stock is worth [[Base.value]] in fiscal 2032, against the current price.

::scenarios

::return_math

Two things in that table need saying out loud.

The first is the exit multiple, because it is doing more work than any other input and I have constrained it deliberately. At a 9% cost of equity, a multiple of 25 times owner earnings implies perpetual growth of 4.96%, which is exactly the current ten-year Treasury yield of 4.96%. Anything higher implies a business growing faster than the risk-free rate forever. The Bull case at 28 times already breaches that test, which the model flags. A reader who thinks Snowflake should exit at 40 or 50 times owner earnings will get a very different answer from this model, and that reader should know that is the assumption they are making, not a view about AI.

The second is that there is no compounding rate to report, in the ordinary sense. The return-math table shows the compounding row as not meaningful because Snowflake's owner earnings per share are **negative today**, at about −$0.86 in the base year. You cannot compute a growth rate from a negative base. The entire Base case value rests on a swing from −$0.86 to [[Base.owner_eps]] of owner earnings per share in five years. That is the thesis, stated without decoration.

Now the two diagnostic cases. **To earn an ordinary 9% a year from here**, at that same exit multiple, Snowflake needs fiscal 2032 owner earnings of about [[Priced-in.owner_eps]] a share, against [[Bull.owner_eps]] in my Bull case. That is 41% above the Bull, and the solver only reaches it by extrapolating 74% of the way beyond Bull along the Base-to-Bull path. **To earn 13% a year**, it needs [[Hurdle.owner_eps]], about 70% above the Bull, which is 116% beyond it along the same path. Put differently: the price today does not merely assume the bulls were right about AI. It assumes they were right by a margin the model cannot reach without inventing a case I would not write down.

This produces the starkest output I have had from this framework. Weighting the cases 30% Bull, 45% Base and 25% Bear, and adding [[optionality_value]] a share for Observe reaching scale in the IT-operations market at 30% odds, gives a probability-weighted value of **[[pw_ev]]** and an annual return of **[[pw_return]]**. The break-even Bear probability is negative and so is the price-implied Bear probability, which is the model's way of saying that **even with no Bear case at all, a 30/45 mix of Bull and Base does not earn even 9% a year from here**. My Bull case alone, if it happened with certainty, returns [[Bull.return]] a year. The price at which the probability-weighted case clears the hurdle is **[[entry]]**, about where the stock traded in April.

The earnings-power floor is consistent with that. Capitalizing five-year average owner earnings at 9% gives no positive value at all, because the five-year average is negative. On the kindest cash-based floor, fiscal 2027 adjusted free cash flow of roughly $1.45 billion capitalized at 9% with no growth gives about $16 billion, or $43 a share, against a $114.7 billion market capitalization. Essentially all of today's price is paying for growth and for a margin structure that does not exist yet.

A confidence note, since the competence call here is Edge rather than Core. What I cannot judge from outside is how fast inference costs fall relative to AI revenue mix, and therefore whether the product gross margin troughs at 74% or keeps sliding. That single variable moves the Base case's terminal owner earnings by more than any other assumption except SBC.

## Final Words {#final}

Snowflake is a better business than it was two years ago and a much better business than the market believed it was in April. The bears picked a specific, falsifiable fight — that agentic AI would route enterprise queries around the governed warehouse — and they lost it in public, three quarters running. Consumption pricing turned out to be the right business model for an agent-driven world, because agents generate volume and Snowflake bills for volume. Ramaswamy has earned the credit he is getting for seeing that early and shipping against it.

The problem is that the market has now paid for all of it and then some. At $325.43 Snowflake trades at about eighteen times this year's guided product revenue and at no meaningful multiple of owner earnings, because owner earnings are still negative. To justify the price at an ordinary 9% return, the company needs fiscal 2032 owner earnings about 40% above my Bull case. The compensation structure that makes owner earnings negative is not obviously on a path to normality: shareholders have rejected the pay plan twice, the board responded with a 1,000,000-share award whose every tranche pays out below a 13% shareholder return, and insiders have sold $521.6 million into the rally without buying a share.

The round trip of the last year should make anyone humble about forecasting this stock, me included. I was not writing about Snowflake in April, and the honest thing to say is that the framework would have had me buying near the low and would now have me selling into the high, which is the correct behaviour for a method that anchors on value rather than narrative, but is also exactly the pattern that looks foolish if the business keeps surprising upward. It may. Three quarters of acceleration is not nothing.

What would change my mind? Three things, and the first of them resolves on December 2 when Snowflake reports the October quarter. A fourth consecutive acceleration with the product gross margin holding at or above 74% would tell me the AI mix is not structurally dilutive and would move weight from Bear to Bull. A fiscal 2028 guide above 30% growth, given a year earlier than the equivalent guide was given this year, would tell me management has fixed the forecasting blind spot that caused the round trip. And a fiscal 2027 10-K in March showing SBC below 26% of revenue with the share count flat would be the first evidence in this company's history that the gap between cash flow and owner earnings is actually closing. Until then the business is one I would like to own and the price is one I would not pay.

Here are the three tests written as kill criteria, each with its consequence fixed in advance:

::tests

## Appendix: The Numbers {#numbers}

The tables below carry the framework's required numbers. The argument for each is made in the chapters above.

### Five-year record

::table five_year

Cycle position: not cyclical in the commodity sense, but consumption revenue is geared to enterprise IT budgets and to the AI capital-expenditure cycle, which is late-expansion. The October 16, 2026 selloff, when Snowflake fell 8.4% alongside Cloudflare and Datadog on AI-financing worries with no company-specific news, is a reminder that the whole complex now trades as one macro expression.

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

Reflexive loop: yes, and it is worth naming. Snowflake pays a third of its revenue in stock and funds the offsetting buyback partly with convertible debt struck off the share price. A sustained fall in the stock raises the share count needed to pay the same people, raises cash compensation demands, and makes the converts harder to settle in stock. The April 2026 drawdown was not long enough to test this. No ruin path: $4.3 billion of cash and investments before the September raise, no coupon on the convertible notes, and the nearest maturity is the 2027 notes, which have been partially retired.

### Catalysts

::table catalysts

### Sentiment and positioning

::table sentiment

Analysts are near-unanimously positive: the consensus twelve-month target is $425.14 across 52 analysts, 31% above spot, with UBS at a street-high $500. Insiders sold half a billion dollars of stock in the last ninety days and bought nothing. Neither fact is a reason for a verb; both are recorded because they describe who is on which side of this trade.

## Sources {#sources}

::sources

::disclaimer
