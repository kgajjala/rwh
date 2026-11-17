---
title: Nvidia against the field in training and inference
date: 2026-11-17
tags: [nvda, ai, accelerators, custom-silicon, tpu, amd, broadcom, networking, insights]
status: snapshot, written before the fiscal Q3 2027 print (due 2026-11-17 after the close)
data_as_of: 2026-11-16 close ($156.14); company data through fiscal Q2 2027 (quarter ended 2026-07-26)
---

# Nvidia against the field: training, inference, and what the competition is worth

This study maps each Nvidia data-center product family to the chips that compete with it now and the ones arriving through 2028, sizes the shares, and turns the competitive outcomes into revenue, market-cap and return ranges on a five-year view. It is a competitive study with a valuation read. It is not a full ticker page: the five-year filing record, incentive table and promises ledger are not built here.

## Read this first: three things changed in the last five days

1. **Jensen Huang resigned on November 12**, effective immediately, as CEO, President and director. CFO Colette Kress is interim CEO and the board has opened a search ([8-K, Nov 12, 2026](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm)). An independent board investigation continues, and congressional inquiries are expected ([CNBC, Nov 16](https://www.cnbc.com/2026/11/16/nvidia-jensen-huang-return-tech.html); [NBC News](https://www.nbcnews.com/tech/tech-news/nvidia-investigation-jensen-huang-continue-departure-sources-say-rcna609136)). Every roadmap date and every management quote below was made under Huang.
2. **Commerce published an interim final rule on November 16** requiring licenses for advanced-chip exports to Indonesia, Malaysia, Singapore, Thailand and Brazil and for data centers serving China-headquartered firms remotely ([Fortune](https://fortune.com/2026/11/16/new-commerce-rule-nvidia-chip-singapore-malaysia-china/); [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-16/us-moves-to-limit-remote-access-to-advanced-ai-chips)). No source quantifies the revenue effect yet.
3. **Fiscal Q3 2027 results are due tonight**, after this was written. The print will confirm or reset the two numbers this study leans on most: the fiscal 2028 growth outlook and the gross-margin floor. Treat every forward figure here as pre-print.

The stock closed at **$156.14** on November 16, inside a 52-week range of $148.80 to $243.37, for a market value of about $3.76 trillion on 24.1 billion shares ([Yahoo Finance](https://finance.yahoo.com/quote/NVDA/)).

## The short answer

- **Position today.** Nvidia takes roughly **83%** of the money spent on AI accelerators and their networking outside China `[Derived]`, and more than 95% of merchant GPUs. Outside estimates run 75% to 85%. By units and by packaging capacity its share is lower, about 55% to 60%.
- **Where it is strong.** Training of frontier models outside Google, and everything bought by customers who do not design chips: neoclouds, sovereigns, enterprises. That group is about 45% of data-center revenue and is growing faster than the hyperscalers.
- **Where it is losing ground.** Inference at the six or seven largest buyers. Anthropic and OpenAI have each contracted only about 40% of their announced capacity on Nvidia. Google sells its TPU as a system to outsiders from 2027, AMD ships a rack-scale system to five of the largest buyers, and Broadcom has guided its AI revenue to double in each of the next two years.
- **What that does to share.** On the companies' own guidance, Nvidia's share of spend drifts from about 83% in 2026 to about 80% in 2027 and to roughly 70% to 73% in 2028 `[Derived]`. Nvidia's own guide is constrained by supply, so unmet demand is what feeds the alternatives.
- **What it means for revenue.** Fiscal 2028 revenue is guided to about $697 billion. After that, my probability-weighted path is flat: about $745 billion in fiscal 2029 and about $706 billion in fiscal 2031. Market growth and share loss roughly cancel.
- **What it means for value.** Probability-weighted value in five years is **$273 a share**, about $5.8 trillion of market value, a **12.5% annual return** against the wiki's 13% hurdle. Bull $489, Base $253, Bear $98. The return is almost all earnings and buybacks, with next to nothing from a higher multiple. On the rule, that is a Watch with an entry at or below $153. Spot is 2% above it.

## 1. Where Nvidia stands

| ($ billions) | Q2 FY26 | Q1 FY27 | Q2 FY27 | Q3 FY27 guide |
|---|---|---|---|---|
| Revenue | 46.7 | 81.6 | 96.2 | 108.0 ± 2% |
| Data Center | 41.1 | 75.2 | 89.0 | n/d |
| of which Hyperscale | 24.2 | 43.1 | 48.7 | n/d |
| of which AI clouds, industrial and enterprise | 16.9 | 32.2 | 40.3 | n/d |
| Edge Computing | 5.6 | 6.4 | 7.2 | n/d |
| Gross margin (non-GAAP) | 72.5% | 75.0% | 75.0% | 74.0% ± 0.5 pt |

Source: [CFO commentary, Q2 FY27](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf) (text in [`raw/NVDA/press-releases/`](../../raw/NVDA/press-releases/2026-08-26_Q2FY27_CFO_commentary.txt)).

Fiscal 2026 revenue was $215.9 billion ([SEC XBRL company facts](https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json)). Fiscal 2027 lands near $410 billion if Q3 meets guidance and Q4 meets the roughly $124 billion consensus `[Derived from guidance and analyst consensus]`. On the August 26 call Kress gave a full-year outlook for the first time: revenue up about 70% in fiscal 2028, which she called supply-constrained, against customer forecasts that point to demand doubling ([Q2 FY27 call transcript](../../raw/NVDA/transcripts/2026-08-26_Q2FY27_earnings_call.txt)). That implies about $697 billion `[Management guidance, derived]`; consensus sits at about $692 billion and $15.91 of EPS `[Analyst consensus]` ([Yahoo Finance, Nov 2026](https://finance.yahoo.com/markets/stocks/articles/nvidia-fiscal-2028-revenue-estimate-132028810.html)).

Four facts from that call and filing shape the competitive question:

- **Margins are already giving ground.** Management guided gross margin to bottom at 71% to 72% in Q4 and settle at 72% to 73% in fiscal 2028, citing memory prices, with price increases taking effect in Q1.
- **Revenue per gigawatt keeps rising.** Management put Nvidia's content at about $18 billion per gigawatt for Hopper, $25 billion for Blackwell and $40 billion for Vera Rubin. Broadcom's Hock Tan put custom-chip content at $20 billion to $30 billion per gigawatt ([Broadcom Q3 FY26 call summary](https://finance.yahoo.com/technology/ai/articles/broadcom-inc-avgo-q3-2026-110030403.html)). That gap is the size of the incentive to switch.
- **Growth is partly bought with the balance sheet.** Commitments were $366 billion (of which $279 billion supply and capacity), plus $56 billion of AI-cloud agreements and third-party leases, plus guarantees with a maximum exposure of $108.5 billion. Receivables rose to 60 days of sales from 45. Kress said the AI labs Nvidia supports with its balance sheet should be about a quarter of the business next year. The wiki's [circular-deals snapshot](ai-circular-deals-2026-10-27.md) carries the deal detail.
- **China is zero in the outlook.** H200 shipments were under 1% of data-center revenue.

## 2. Nvidia's families and roadmap

| Family | What it is | Status | Job |
|---|---|---|---|
| Blackwell / Blackwell Ultra (GB200, GB300 NVL72) | Grace CPU + Blackwell GPU rack, NVLink 72 | The vast majority of revenue in Q2 FY27 | Training and inference |
| Vera Rubin NVL72 | Vera CPU + Rubin GPU rack | Production shipments began August 2026; about 20% of data-center revenue guided for Q3 FY27 | Training and inference; pitched at agentic inference |
| Rubin Ultra (Kyber NVL144) | New rack, 144 GPUs | Public target 2H 2027; outside reports flag a possible slip to 2028 | Same, at higher density |
| Feynman | New GPU, Rosa CPU, LP40 LPU, co-packaged optics between racks | 2028 | Same |
| Groq 3 LPX | 256-LPU rack from the roughly $20 billion Groq license and team hire | Full production; volume to early adopters in Q3 FY27, Nebius first | Low-latency inference, bolted onto GPU racks |
| Vera / Grace CPUs | Arm server CPUs, sold alone as well as in racks | Grace above $5 billion trailing revenue; CPU revenue expected to more than double in FY28 | Agent and head-node compute |
| Networking | NVLink (inside the rack), Spectrum-X Ethernet and InfiniBand (between racks) | Revenue up 18% sequentially in Q2 FY27; Spectrum-X up 2.6x year over year | Connects all of the above |
| China SKUs (H200) | Licensed Hopper parts | Under 1% of data-center revenue | Inference and training in China |

Sources: [Q2 FY27 call transcript](../../raw/NVDA/transcripts/2026-08-26_Q2FY27_earnings_call.txt); [SemiAnalysis on GTC 2026](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands); [HPCwire on the roadmap](https://www.hpcwire.com/2026/03/17/huang-shares-nvidia-roadmap-showing-more-chips-nvl1152-scale-up-cpo/); [10-Q for Q2 FY27](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm) for the Groq license.

The cadence is one platform a year. The strategic move since 2024 is that Nvidia sells the whole rack and now the whole site design, which is why its content per gigawatt has more than doubled in two generations.

## 3. The market and who holds it

No audited share table exists for AI accelerators. The cleanest view adds up what the vendors themselves report. Hyperscalers' in-house chips show up as their design partners' revenue, so nothing is counted twice.

| Vendor revenue, $ billions | 2026 | 2027 | 2028 |
|---|---|---|---|
| Nvidia Data Center (fiscal year ending the following January) | ~379 `[Derived]` | ~645 `[Derived from guidance]` | 750 to 850 `[Estimate]` |
| Broadcom AI semiconductors (fiscal year ending about November 1) | 58 `[Management guidance]` | ~115 `[Management guidance]` | ~230 `[Management guidance]` |
| AMD data-center AI | ~13 `[Estimate]` | ~35 `[Estimate]` | ~60 `[Estimate]` |
| Marvell, MediaTek, Alchip custom, and specialists | ~7 `[Estimate]` | ~13 `[Estimate]` | ~25 `[Estimate]` |
| **Total** | **~457** | **~808** | **~1,065 to 1,165** |
| **Nvidia share** | **~83%** | **~80%** | **~70% to 73%** |

Sources and method: Nvidia from the tables above at a 92.5% data-center mix. Broadcom from its [Q3 FY26 release](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial) and call; Tan said the 2027 and 2028 figures rest on secured supply and data-center timing, and 73% of AI revenue in the quarter was custom accelerators, the rest networking. AMD from its [Q3 2026 prepared remarks](../../raw/clippings/2026-11-03_AMD_Q3_2026_prepared_remarks.txt): AMD does not disclose AI GPU revenue, so the row is my estimate from a segment that more than doubles in 2026, a Q4 in which AI passes server CPUs, and a 2027 guide of total revenue up more than 80% with data center above 80% of the total. Marvell from its [fiscal Q2 2027 call](https://www.tradingkey.com/news/transcripts/262137259-tradingkey). Fiscal years do not line up, so read the shares as ±3 points.

Other ways to cut the same market:

| Measure | Nvidia | Others | Source |
|---|---|---|---|
| Merchant GPUs, revenue | >95% | AMD under 5% | `[Derived]` from the table |
| All accelerators, revenue, third-party range | 75% to 85% | Custom 12% to 18%, AMD 5% to 8% | [Presenc AI](https://presenc.ai/research/ai-chip-market-share-2026), [Silicon Analysts](https://siliconanalysts.com/analysis/nvidia-ai-accelerator-market-share-2024-2026) `[Estimate, secondary]` |
| AI server shipments | GPU-based ~72%, Nvidia and AMD together | Custom ASIC systems 27.8% in 2026 | TrendForce via [Safeguard](https://safeguard.sh/resources/blog/ai-chip-market-share-2026-nvidia-custom-silicon-training-vs-inference) `[Estimate, secondhand]` |
| TSMC CoWoS packaging, 2026 | 55% to 60% | Broadcom ~15%, AMD ~10% to 11% | Morgan Stanley and DigiTimes via [ClusterBid](https://clusterbid.com/blog/gpu-supply-chain-2026-tsmc-cowos-nvidia-allocation-lead-times) `[Estimate, secondary]` |
| Inference only | 60% to 75% | Not split | [Flowverify](https://www.flowverify.co/blog/nvidia-inference-market-share-custom-silicon-2026) `[Estimate, low quality]` |
| China accelerators | 8% to 34% | Huawei 28% to 62%, Cambricon 5% to 14% | Bernstein, IDC, Morgan Stanley via [Startup Fortune](https://startupfortune.com/huaweis-ascend-chips-have-overtaken-nvidia-in-chinas-ai-market/) `[Estimate, secondhand, conflicting]` |
| Data-center Ethernet switching, Q2 2026 | 20.4%, first | Arista 18.7% | [IDC](https://www.idc.com/resource-center/blog/ethernet-switch-market-surges-43-4-to-18-9b-in-2q26-as-ai-infrastructure-demand-drives-record-datacenter-spending/) |
| Anthropic contracted capacity (~11 GW) | ~42% | TPU ~41%, Trainium ~11%, AMD ~7% | [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262241466-anthropic-ipo-reveals-11gw-compute-footprint-nvidia-accounts-42-tradingkey) `[Estimate]`; the S-1 gives no split |
| OpenAI announced capacity (~30 GW) | ~40% (12 GW) | Broadcom custom 10 GW, AMD 6 GW, Trainium 2 GW | `[Derived]` from the Nvidia call and deal announcements |

Three readings matter. Revenue share overstates Nvidia's share of compute because Nvidia charges more per gigawatt. Packaging share is the better guide to where 2027 and 2028 land, and one forecast has AMD and Broadcom each near 500,000 CoWoS wafers in 2027 against about 1.2 million for Nvidia `[Estimate, secondary]`. And the two largest AI labs, which Nvidia finances, have already split their orders so that Nvidia is the largest supplier but not the majority.

## 4. Competitors mapped to each Nvidia family

| Nvidia family | Competing now | Arriving 2027 to 2028 | Threat |
|---|---|---|---|
| Blackwell / Blackwell Ultra | Google TPU v7 Ironwood (1 GW to Anthropic in 2026); Amazon Trainium 2 and 3; AMD MI355X; Meta MTIA 300/400; Microsoft Maia 200 | Superseded by the row below | High in inference at the large buyers, low elsewhere |
| Vera Rubin NVL72 | AMD MI455X in Helios racks (volume since Q3 2026 at Anthropic, Meta, Microsoft, OpenAI, Oracle) | Google TPU 8t (training) and 8i (inference), broad external availability late 2027; OpenAI Jalapeño with Broadcom, ramping 2027; Trainium 4; MTIA 450/500; Maia 300 | High. This is the generation where every large buyer has a second source in volume |
| Rubin Ultra / Kyber | Nothing shipping | AMD MI500 (2027, multi-gigawatt talks with frontier labs); next TPU and Trainium generations | Medium to high; a slip to 2028 would hand AMD a window |
| Feynman | Nothing shipping | Successors of all of the above | Unknown; too early |
| Groq 3 LPX | Cerebras (OpenAI contract above $20 billion for 750 MW; 2026 revenue guided to about $860 million); SambaNova | AMD with Taalas (acquisition closing by year-end 2026); Jalapeño on latency | Low in dollars; this is Nvidia's own defensive move |
| Vera / Grace CPUs | AMD EPYC Turin and Venice; Intel Xeon; in-house Arm (Graviton, Axion, Cobalt) | AMD Helion all-CPU racks | Nvidia is the challenger; AMD expects server revenue to double in 2027 |
| NVLink (inside the rack) | AMD Helios scale-up; Broadcom Tomahawk Ultra | UALink 1.0 products in 2027 | Medium; the open standard runs one to two generations behind |
| Spectrum-X and InfiniBand (between racks) | Broadcom Tomahawk 6 through Arista, Cisco, Celestica and white boxes | Tomahawk 7 | Medium; Nvidia is already the largest data-center Ethernet vendor, but Broadcom silicon sits inside most rivals' switches |
| China SKUs | Huawei Ascend 950; Cambricon | Ascend 960 | Lost for now; upside only |
| CUDA and the software stack | AMD ROCm 10; Google JAX and TorchTPU; Amazon TorchNeuron | AI-written ports | Rising; see section 6 |

Sources: [AMD Q3 2026 prepared remarks](../../raw/clippings/2026-11-03_AMD_Q3_2026_prepared_remarks.txt); [The Next Web on TPU 8](https://thenextweb.com/news/google-ironwood-tpu-inference-cloud-next); [Tom's Hardware on Jalapeño](https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-openais-jalapeno-ai-asic-unpacked-accelerator-developed-using-ai-achieves-efficiency-and-throughput-gains-against-power-hungry-blackwell); [Meta on MTIA](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/); [Cerebras Q1 2026 results](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-announces-strong-first-quarter-2026-results); [BofA note on NVLink Fusion and UALink, via X](https://x.com/jukan05/status/1926211761541206524) `[Analyst, 2025]`.

## 5. The competitors, one at a time

**Google TPU, built with Broadcom and MediaTek.** This is the most dangerous rival because it is no longer captive. Thomas Kurian told the Goldman conference on September 8 that Google's accelerator business is more than twice the size of the next-largest hyperscaler's, and that Google now sells TPUs three ways: as cloud capacity, as systems bought outright for the customer's own data center, and through a neocloud set up with Blackstone ([transcript](https://stockanalysis.com/stocks/googl/transcripts/737252-goldman-sachs-communacopia-technology-conference-2026/)). Oracle will also offer TPUs ([CNBC, Oct 28](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)). Alphabet's inventory rose to $13.3 billion from $2.4 billion at year-end to stock TPU systems, and management expects the bulk of contracted TPU revenue in 2027. Analyst estimates of 2027 external TPU sales run from $51 billion to $99 billion `[Analyst estimates]` ([Yahoo Finance](https://uk.finance.yahoo.com/news/alphabet-cloud-forecast-raised-piper-115900092.html)); much of that overlaps Broadcom's revenue, so it is not additive to the table above. On cost, SemiAnalysis measured Ironwood at $0.181 per million tokens against $0.222 and $0.276 for Nvidia's B200 and B300 at one interactivity point, and noted Nvidia keeps the raw-performance lead and the lead at 4-bit precision ([InferenceX preview](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam)). The limits are software for outside users, which is in beta, and a matrix unit that penalizes some model shapes.

**Amazon Trainium.** Jassy said on the October 29 call that most of Bedrock now runs on Trainium, that Trainium commitments are up more than 20-fold in a year, and that Amazon plans to sell Trainium outside AWS from late 2027 ([Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)). Anthropic has up to 5 GW of Trainium and OpenAI at least 2 GW. Amazon is also Nvidia's customer for 2 million more GPUs through mid-2028, so this is substitution at the margin, concentrated in inference for Amazon's own services.

**AMD.** The only merchant rival with a full rack. The MI455X and Helios entered volume production in Q3 2026 and five of the largest buyers brought racks online. AMD guided Q4 data-center revenue up about 50% sequentially and 2027 total revenue up more than 80%, and said data-center AI will grow faster than it projected 90 days earlier. Contracted demand is up to 6 GW each at OpenAI and Meta and up to 2 GW at Anthropic; the OpenAI and Meta deals each carry warrants over roughly 10% of AMD. AMD is small against Nvidia, about 3% of spend in 2026 rising to perhaps 4% to 5% in 2027 `[Derived]`, but it is the price check on every Nvidia negotiation, and it sells to the same OEM channel that serves Nvidia's enterprise customers.

**Custom chips at OpenAI, Meta and Microsoft.** OpenAI's Jalapeño, built with Broadcom, claimed 1.5 to 1.9 times the throughput per watt of GB200 and GB300 systems in OpenAI's own tests, with small volumes at the end of 2026 and a real ramp in 2027; the comparison is against the generation Nvidia is now replacing. Meta has MTIA 300 in production and 400, 450 and 500 aimed at generative inference into 2027. Microsoft's Maia 200 serves Copilot and OpenAI models, with Maia 300 due in 2027. Broadcom counts six custom customers. Marvell targets more than $10 billion of custom revenue in fiscal 2029.

**Inference specialists.** Cerebras is public and tied to OpenAI. Nvidia answered this group by licensing Groq. Huang's own description on the August call was that the LPU gives very fast tokens at lower throughput and higher cost per token, for premium services, and that most data centers will simply be Vera Rubin. Intel's Crescent Island and Qualcomm's AI200 have no confirmed volume shipments ([Tom's Hardware on Intel](https://www.tomshardware.com/tech-industry/semiconductors/intel-chip-roadmap-2026-2028); [Bloomberg on Qualcomm](https://www.bloomberg.com/news/articles/2025-10-27/qualcomm-unveils-chip-to-rival-nvidia-in-ai-accelerator-market)). None of these moves the numbers before 2028.

**China.** Beijing has blocked most licensed H200 purchases and Huawei has taken the lead by most estimates ([Bloomberg, Aug 26](https://www.bloomberg.com/news/articles/2026-08-26/nvidia-steps-back-into-china-market-with-first-h200-chip-sales); [CNBC, Jul 14](https://www.cnbc.com/2026/07/14/nvidia-h200-ai-chips-china.html)). The new remote-access rule closes the route by which Chinese firms rented Nvidia capacity in Southeast Asia. China is an option, valued separately in section 9.

## 6. Training against inference

Nvidia does not split revenue by workload, and no reliable outside split exists. What can be said from the sources:

- **Training.** Frontier training outside Google runs mainly on Nvidia. The exceptions are large: Google trains Gemini on TPUs, and Anthropic's first million TPUs were mainly for training. Anthropic's S-1 shows about two-thirds of its compute going to research and training rather than serving customers ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ipo-filing-shows-most-of-its-compute-goes-to-r-and-d-not-serving-customers-company-details-massive-usd800-billion-in-tpu-and-gpu-contracts)), so the training market at the labs is bigger than the inference narrative suggests, and it is where Nvidia's lead is widest.
- **Inference.** Every custom chip in section 4 is aimed here first, because inference at one company runs a narrow set of models at huge volume, which is the case an ASIC serves best. Huang's reply to the custom-chip question on the August call was that those chips are inference-specific parts for one cloud or one service, while Nvidia runs every model in every cloud and can be redeployed. That is true and it is why Nvidia is financeable collateral. It is also an admission that at the largest services the single-purpose chip is good enough.
- **Agentic inference.** Nvidia's case for Vera Rubin is that agents need long context, tool calls and fast tokens, and that one fungible system across training and inference holds its value longer. SemiAnalysis' work supports a large Rubin advantage at high interactivity ([Rubin against GB200](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference)). No independent test yet compares Rubin with TPU 8i, MI455X or Jalapeño. That test is the most important missing fact in this study.

The software moat is thinning at the top end. AMD said in its Q3 remarks that an Anthropic engineer used Claude to bring up Anthropic's latest model on AMD racks over a weekend. Google is opening a PyTorch backend for TPUs and Amazon open-sourced one for Trainium. For a lab with a few models and many engineers, CUDA is no longer a lock. For an enterprise or a sovereign buyer with neither, it still is.

In 7 Powers terms: scale economies in R&D and supply (the $279 billion of pre-committed capacity is close to a cornered resource in memory and packaging), switching costs through CUDA, and counter-positioning against the hyperscalers as the one supplier that does not also run a competing cloud. **Trend: narrowing at hyperscalers and labs, stable in the rest of the market, with Google, AMD and Amazon all entering that second half during 2027.**

## 7. How the field changes, year by year

| | 2026 | 2027 | 2028 | 2029 to 2030 |
|---|---|---|---|---|
| Nvidia | Blackwell Ultra is the volume part; Vera Rubin and Groq 3 LPX ramp | Rubin dominant; Rubin Ultra targeted 2H; supply-constrained growth guide; new CEO | Feynman | First SB Energy site for OpenAI ready (fiscal 2029); upgrade cycles |
| Google / Broadcom | 1 GW of Ironwood to Anthropic; TPU 8 in Google Cloud | 3.5 to 5 GW more to Anthropic; external system sales scale; Broadcom AI ~$115B | Broadcom AI ~$230B; $125B to $150B of further TPU deliveries to Anthropic begin | Custom share set by how 2027 and 2028 racks performed |
| AMD | MI455X and Helios in volume | Revenue up >80%; first Anthropic gigawatt in 1H; MI500 | MI500 multi-gigawatt | OpenAI and Meta 6 GW programmes complete by 2030 |
| Amazon | Trainium 3 nearly sold out; most of Bedrock on Trainium | External Trainium sales late in the year | Trainium 4 | |
| OpenAI, Meta, Microsoft | Jalapeño in very small volume; MTIA 400; Maia 200 | Jalapeño ramps; MTIA 450/500; Maia 300 | Second generations | OpenAI's 10 GW Broadcom programme completes end of 2029 |
| Open standards | UALink silicon in labs | UALink 1.0 products | | |

The pattern: 2026 was the last year in which Nvidia was the only volume option at rack scale. In 2027 every large buyer has at least two. 2028 is the first year the alternatives' guided dollars are large enough to move Nvidia's share by ten points.

## 8. Scenarios

Revenue is market size times share, so I set probabilities on each separately and then combine them. Market size is 2030 spending on AI accelerators and their networking at vendor revenue, outside China's domestic chips; the 2028 level on current guidance is about $1.1 trillion.

**Competitive outcomes (Nvidia's share of that spend in 2030):**

| Outcome | Share | Probability | What has to happen |
|---|---|---|---|
| Platform holds | ~68% | 25% | Rubin and Feynman keep a clear cost-per-token lead in independent tests; custom programmes stay confined to their owners' internal inference; the non-hyperscaler half keeps growing fastest; the roadmap survives the leadership change |
| Share bleeds | ~58% | 45% | TPU and AMD systems are good enough for most inference; labs stay split as contracted; Google and AMD win a minority of neocloud and sovereign deals; Nvidia holds training and the long tail |
| Share breaks | ~45% | 30% | Custom chips reach training parity at the labs; Google and Amazon sell systems broadly; AI-written ports remove the software lock; a roadmap slip or talent loss after Huang; pricing follows |

**Demand outcomes (2030 market):**

| Outcome | Market | Probability | What has to happen |
|---|---|---|---|
| Boom | $1.7 trillion | 25% | Agent usage keeps compute scarce; hyperscaler capex holds above the $1.3 trillion Nvidia cites for 2027 and grows |
| Grind | $1.25 trillion | 45% | Spending plateaus near the 2028 level and grows with revenue from AI services |
| Digestion | $0.75 trillion | 30% | A financing or returns shock; capex falls about a third from the peak, in line with past semiconductor cycles |

**Nvidia data-center revenue in 2030, $ billions (joint probability):**

| | Holds (68%) | Bleeds (58%) | Breaks (45%) |
|---|---|---|---|
| **Boom $1.7T** | 1,156 (6%) | 986 (11%) | 765 (8%) |
| **Grind $1.25T** | 850 (11%) | 725 (20%) | 563 (14%) |
| **Digestion $0.75T** | 510 (8%) | 435 (14%) | 338 (9%) |

Probability-weighted, that is about $686 billion `[Derived]`. The two axes are not independent: a bust makes hyperscalers favour their own chips and hits the financed customers first, so I weight the bear case above what independence gives.

Collapsed into three cases for valuation, with about $40 billion of edge revenue added:

| | FY2028 | FY2029 (waypoint) | FY2031 (terminal) | Probability |
|---|---|---|---|---|
| **Bull** revenue, $B | 697 | 850 | 1,015 | 25% |
| **Base** revenue, $B | 690 | 780 | 695 | 50% |
| **Bear** revenue, $B | 640 | 570 | 420 | 25% |
| **Probability-weighted** | 679 | 745 | 706 | |

Fiscal 2027 is about $410 billion, so growth is about 66% probability-weighted in fiscal 2028 and about 10% in fiscal 2029, then slightly negative. The Bull grows 13% a year after fiscal 2028. The Base peaks in fiscal 2029 and returns to the fiscal 2028 level as share loss offsets a growing market. The Bear misses the fiscal 2028 guide and falls 13% a year afterwards.

## 9. What it is worth

| | Bull | Base | Bear |
|---|---|---|---|
| FY2031 revenue, $B | 1,015 | 695 | 420 |
| Net margin | 52% | 48% | 38% |
| Net income, $B | 528 | 334 | 160 |
| Diluted shares, billions | 21.6 | 21.1 | 21.3 |
| EPS | $24.47 | $15.81 | $7.50 |
| Multiple | 20x | 16x | 13x |
| Value per share | **$489** | **$253** | **$98** |
| Against $156.14 | +213% | +62% | −38% |
| Market value, $ trillions | 10.6 | 5.3 | 2.1 |
| Probability | 25% | 50% | 25% |

All rows `[Derived]`. Assumptions: gross margin of roughly 72%, 69% and 61% in the three cases, reflecting how much price Nvidia gives up; 45% of net income spent on buybacks at prices along each path, less 0.4% a year of stock-compensation dilution; a 17% tax rate. Today's base is the fiscal 2027 consensus EPS of $9.31 `[Analyst consensus]`, on which the stock trades at 16.8 times, or 9.8 times fiscal 2028.

- **PW EV: $273 a share**, 75% above spot, about $5.8 trillion of market value against $3.76 trillion today.
- **PW return: 12.5% a year** (11.8% from price plus a 0.6% dividend yield), against the 13% hurdle.
- **Compounding at a flat multiple: 11.9% a year**, being 11.3% EPS growth, which already contains the buyback, plus the dividend. Multiple change adds 0.5% a year. Almost none of the return is re-rating.
- **Hurdle-derived entry: $153.** Trim from $273. Avoid at or above $489.
- **R/R: 5.7**, Bull upside over Bear downside.
- **On the wiki's rule the non-holder verb is Watch**, by half a point of return and 2% of price. This is analysis against a stated hurdle, not personal advice, and it says nothing about how much to own.

**How fragile that conclusion is:**

| PW return per year | Base multiple 14x | 16x | 18x |
|---|---|---|---|
| Bull probability 20% (Base 55%) | 10.1% | 11.5% | 12.8% |
| Bull probability 25% (Base 50%) | 11.3% | **12.5%** | 13.7% |
| Bull probability 30% (Base 45%) | 12.4% | 13.4% | 14.5% |

Bear held at 25% throughout. With Bull at 20%, Base at 45% and Bear at 35%, the return is 10.1%. The answer sits within one notch of the hurdle in either direction, and 45% of the value comes from a Bull case that needs a $10 trillion company. That is the honest state of it: the price is fair to slightly cheap for the base outcome, and the decision turns on whether you believe the Bull is one chance in four.

**Price-implied expectations.** At a 10% discount rate, $3.76 trillion equals about $376 billion of earnings held flat forever. That is fiscal 2028 consensus net income with no growth after it. The market is pricing fiscal 2028 as the peak.

**Base-rate check.** The Bull needs revenue to compound about 25% a year for four years from $410 billion. Two percent of companies with sales above $25 billion have grown 20% a year in real terms for five years, and none started this large. Most of the Bull's growth, however, is the already-guided and supply-committed fiscal 2028; after that it needs 13% a year.

**Year ten.** By 2035 this is a replacement-cycle business: installed gigawatts refreshed every four to six years, with Nvidia holding about half. In the Base it is not growing at year ten, and the 16 times multiple is carried by buybacks and cash returns, not by growth.

**Valued separately, outside the figures above:**

| Line | Value | Basis |
|---|---|---|
| Equity stakes in AI labs and partners | about +$4 a share at carrying value | $47.9 billion non-marketable plus $47.8 billion public at July 26, 2026 (10-Q); two labs may list, so marks could move either way |
| China | about +$1 a share | 20% chance of $20 billion a year of licensed revenue `[Estimate]` |
| Guarantees and take-or-pay | about −$1.50 a share in the Bear | 30% loss on $108.5 billion maximum exposure `[Estimate]` |
| Retained cash | not credited | About half of cumulative earnings is neither bought back nor paid out in the model |

## 10. What would change the read

In order of how soon the evidence arrives:

1. **Tonight's print.** The fiscal 2028 outlook of about 70% growth is reaffirmed or it is not. A cut moves the Base toward the Bear path. Gross margin guided below the 71% to 72% floor says price is already being conceded.
2. **Hyperscale against the rest.** Hyperscale grew 13% sequentially in Q2 against 25% for everything else. Hyperscale flat or down while Broadcom doubles is the first hard sign of the share-breaks outcome.
3. **Broadcom's December report.** A raise to the $115 billion fiscal 2027 AI outlook, or named gigawatts above the 5 GW for Anthropic, shifts 2028 share toward the low end of the range.
4. **An independent Rubin against TPU 8i, MI455X and Jalapeño benchmark** on agentic workloads. A Rubin lead of more than about 30% in cost per token supports Platform holds. Parity supports Share bleeds or worse.
5. **Google's 2027 external TPU revenue.** Above about $75 billion means TPUs are winning outside the labs, in Nvidia's stronger half.
6. **Rubin Ultra and Kyber timing.** A slip into 2028 with MI500 on time is AMD's opening.
7. **The successor, and who leaves.** A named CEO from inside the roadmap team keeps Platform holds at 25%. Departures among the architecture and systems leads lower it.
8. **The balance sheet.** Receivables above 60 days, guarantees above the current maximum, or supply commitments rising faster than revenue mean growth is being bought.

## 11. Gaps and caveats

- Written before the fiscal Q3 2027 release and call. Nothing here reflects them.
- Nvidia does not disclose networking, CPU or training-versus-inference revenue. AMD does not disclose AI GPU revenue. Every share figure is derived or third-party and good to a few points at best.
- The Broadcom 2027 and 2028 figures, the Jassy and Kurian remarks, the Anthropic S-1 detail and the Goldman conference remarks were read through transcripts and summaries from secondary publishers. Broadcom's own release was not opened for the outlook figures. Nvidia's and AMD's figures come from their own documents.
- Huang's September 10 Goldman appearance ([transcript](https://stockanalysis.com/stocks/nvda/transcripts/740955-goldman-sachs-communacopia-technology-conference-2026/)) and the October 21 GTC Berlin keynote ([Nvidia blog](https://blogs.nvidia.com/blog/gtc-berlin-2026-keynote/)) were checked. Neither added competitive detail beyond the August call. No appearance by Kress as interim CEO was found before tonight's call.
- The 10-Q risk factors, the fiscal 2026 10-K competition section and the proxy were not read for this study. A full ticker page would need them.
- Several market-share sources are aggregators quoting research firms secondhand, marked as such in the tables. Where two disagreed I gave the range.
- The effect of the November 16 export rule is not in any scenario as a separate line; it sits inside the demand probabilities.

## 12. Sources

Primary: [Nvidia Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf) · [Nvidia Q2 FY27 call transcript (IR-hosted)](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf) · [Nvidia 10-Q, quarter ended July 26, 2026](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm) · [Nvidia 8-K on the CEO transition](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm) · [SEC XBRL company facts, Nvidia](https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json) · [AMD Q3 2026 prepared remarks](https://newsroom.amd.com/documents/2026/11/84f4476b-f064-4f0f-957c-fe484853e178.pdf) · [Broadcom Q3 FY26 release](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial) · [Alphabet 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm) · [Meta on MTIA](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/) · [Cerebras Q1 2026 results](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-announces-strong-first-quarter-2026-results)

Transcripts and appearances: [Amazon Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/) · [Broadcom Q3 FY26 call summary](https://finance.yahoo.com/technology/ai/articles/broadcom-inc-avgo-q3-2026-110030403.html) · [Alphabet at Goldman Communacopia, Sep 8](https://stockanalysis.com/stocks/googl/transcripts/737252-goldman-sachs-communacopia-technology-conference-2026/) · [Nvidia at Goldman Communacopia, Sep 10](https://stockanalysis.com/stocks/nvda/transcripts/740955-goldman-sachs-communacopia-technology-conference-2026/) · [Marvell fiscal Q2 2027 call](https://www.tradingkey.com/news/transcripts/262137259-tradingkey)

Research and press: [SemiAnalysis, GTC 2026](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands) · [SemiAnalysis, TPU InferenceX](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) · [SemiAnalysis, Rubin against GB200](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference) · [IDC Ethernet switch tracker, Q2 2026](https://www.idc.com/resource-center/blog/ethernet-switch-market-surges-43-4-to-18-9b-in-2q26-as-ai-infrastructure-demand-drives-record-datacenter-spending/) · [Tom's Hardware on Anthropic's S-1](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ipo-filing-shows-most-of-its-compute-goes-to-r-and-d-not-serving-customers-company-details-massive-usd800-billion-in-tpu-and-gpu-contracts) · [Tom's Hardware on Jalapeño](https://www.tomshardware.com/tech-industry/artificial-intelligence/hot-chips-2026-openais-jalapeno-ai-asic-unpacked-accelerator-developed-using-ai-achieves-efficiency-and-throughput-gains-against-power-hungry-blackwell) · [CNBC on Google's TPU partners](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html) · [CNBC on calls for Huang's return](https://www.cnbc.com/2026/11/16/nvidia-jensen-huang-return-tech.html) · [Fortune on the export rule](https://fortune.com/2026/11/16/new-commerce-rule-nvidia-chip-singapore-malaysia-china/) · [Yahoo Finance quote, NVDA](https://finance.yahoo.com/quote/NVDA/) · [Yahoo Finance on fiscal 2028 consensus](https://finance.yahoo.com/markets/stocks/articles/nvidia-fiscal-2028-revenue-estimate-132028810.html)
