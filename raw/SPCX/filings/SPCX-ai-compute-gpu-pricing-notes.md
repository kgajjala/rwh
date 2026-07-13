# SPCX — AI/Compute GPU Chip Mix & Market Pricing Extraction Notes

**Coverage**: Chip-generation detail for the Anthropic/Google/Reflection Colossus leases, plus third-party GPU cloud-rental price trackers, gathered to back-calculate implied $/GPU-hour and capacity-share estimates for `wiki/tickers/SPCX/SPCX.md` §2 AI/Compute funnel deep dive.
**Access note**: WebSearch-synthesized; direct fetch of several tracker sites not attempted (aggregator summaries used). Cross-referenced across multiple independent queries per session convention.

---

## Colossus 1 (Anthropic, 100% exclusive)
- Reported mix: **≈150,000 H100 + ≈50,000 H200 + ≈30,000 GB200** = ≈230,000 GPUs total (commonly rounded to "220,000+" in press).
- 300MW+ power. Location: Memphis, TN.
- Deal: $1.25B/month, signed May 6, 2026, through May 2029 (≈$45B total). Exclusive access — Anthropic took the *entire* cluster.
[Source: HotHardware "Anthropic Leases SpaceXAI's 220,000 NVIDIA GPU Colossus Cluster"; Tom's Hardware; letsdatascience.com; x.ai/news/anthropic-compute-partnership]

## Colossus 2 (Google + Reflection, partial allocations; also xAI's own Grok training)
- Went live Jan 2026; expanded to ≈555,000 total Colossus GPUs (combined C1+C2) / ≈2GW power / ≈$18B GPU capex as of the most recent consistently-cited report (~Feb 2026).
- Reported as predominantly **GB200 and GB300** (Blackwell-generation) accelerators.
- Note: one source (abit.ee) describes "550,000 GB200/GB300 nodes" for Colossus 2 alone, "each node housing two GPUs" implying >1M accelerators — this conflicts with the more commonly repeated "555,000 GPUs total (C1+C2)" figure. Treated the latter (555,000 total) as the primary estimate in the wiki page given it's the more consistently cross-referenced number; flagged the discrepancy rather than silently picking one.
[Source: Introl Blog "xAI Colossus Hits 2GW: 555,000 GPUs, $18B, Largest AI Site"; abit.ee; basenor.com]

## Google deal
- $920M/month at full rate; ramps through Sept 2026 at a reduced fee first; full rate Oct 2026 – June 2029 (≈$30B total / ≈33 months).
- ≈110,000 Nvidia GPUs, CPUs, memory, "and other related components" — chip generation not separately disclosed in sources captured.
- Contract flexibility: Google may terminate immediately (after a 1-month grace period past Sept 30, 2026) or accept a reduced GPU count/fee if SpaceX under-delivers the committed count.
[Source: TechCrunch "Google will pay SpaceX $920M per month for compute"; DataCenterDynamics; MLQ News; CNBC 2026-06-05; Memphis Flyer "$30B Rent Deal"]

## Reflection AI deal
- $150M/month starting July 1, 2026; ≈$6.3B if the deal runs through 2029 (≈42 months × $150M ≈ $6.3B, consistent).
- Chip type confirmed: **Nvidia GB300** (Blackwell Ultra, Nvidia's newest chip generation) — "immediate access to Nvidia GB300s."
- Contract flexibility: 90-day termination clause after an initial 3-month commitment — the loosest-locked-in of the three deals.
- GPU count NOT disclosed in any source captured this pass — back-calculated in the wiki page from the monthly fee and GB300 market pricing.
[Source: CNBC "SpaceX signs computing power deal with open-source AI startup Reflection worth up to $6.3 billion"; Forbes (Jon Markman); MLQ News; TechFundingNews; Mezha.net; Axios]

---

## GPU Cloud Rental Price Trackers (market benchmarks, ~July 2026)

| Chip | Range | Cohort median / representative on-demand | Notes |
|---|---|---|---|
| H100 | $1.49/hr (Vast.ai) – $12.29/hr (Azure) | ≈$2.99/hr median | Thunder Compute / Vast.ai / RunPod at the low end; Azure / Google Cloud at the high end |
| H200 | $2.30/hr (FluidStack) – $13.78/hr (Azure) | ≈$4.00/hr median | Google Cloud Spot $3.72/hr (preemptible); AWS/Azure on-demand ≈$10.60/hr |
| GB200 / B200 | $4.95/hr – $18.00/hr | Spheron: spot $5.34/hr, on-demand $6.02/hr | Wide range reflects provider/region/commitment-term variance |
| GB300 | $4.00/hr (Runcrate, low-end listing) – $9.16+/hr | Verda $8.62/hr; Spheron $9.16/hr on-demand (as of 2026-07-05) | Newest chip; pricing "firming up" toward the $8.60–$9.20 band as of early July 2026 |

Aggregator/tracker sources used: Spheron Network (blog + GPU rental pages), IntuitionLabs (H100 comparison), Lambda pricing page, aimultiple GPU Index, GetDeploying (H100 + B300 comparison pages), Jarvislabs (H200 price guide), gpuperhour.com (29-provider live tracker), cloudgputracker.com, Thunder Compute market-trends blog, Runcrate (GB300 pricing page), gpus.io, CoreWeave pricing, Nebius AI Cloud pricing, tech-insider.org (Blackwell pricing).

---

## Back-of-the-envelope back-calculation methodology (see SPCX.md §2 for full output)

Assumptions: 720 hours/month (24/7, 100% utilization — a simplifying assumption; actual could be lower due to maintenance/ramp, which would mean implied real rates are even higher than shown). Market-rate comps use the table above's representative on-demand mid-points, weighted by each cluster's reported chip mix where known.

- **Anthropic**: $1.25B ÷ (230,000 × 720) ≈ $7.55/GPU-hr implied, vs. ≈$3.61/GPU-hr mix-weighted market comp → ≈2.1× premium.
- **Google**: $920M ÷ (110,000 × 720) ≈ $11.62/GPU-hr implied, vs. ≈$6.00–7.50/GPU-hr assumed GB200/GB300 blend → ≈1.5–1.9× premium.
- **Reflection**: solved in reverse — $150M ÷ (720 × assumed $/hr) → GPU count. At pure market GB300 rate ($9.00/hr): ≈23,100 GPUs. At an Anthropic/Google-like premium (1.5–2.1×, i.e. $13.50–$18.90/hr): ≈11,000–14,000 GPUs. Presented as a range, not a point estimate, since neither the GPU count nor the actual premium Reflection pays is disclosed.

**Caveat carried into the wiki page**: this is a back-calculation built on trade-press-reported chip mixes (not S-1/10-Q disclosure), a simplifying 100%-utilization assumption, and third-party tracker data that itself varies by provider/region/term. Directional, not precise unit economics — SpaceX does not disclose AI-segment margin or per-GPU pricing.
