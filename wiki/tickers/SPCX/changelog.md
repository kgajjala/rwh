# SPCX — Changelog

*Append-only. Most recent entry first.*

---

## [2026-07-13] — AI/Compute Deep Dive: Chip Mix + GPU Market Pricing Back-Calculation

**Trigger**: User-requested deep dive on the GPU-compute-leasing business, same day as initial ingest — (1) identify the specific Nvidia chip generations leased to Anthropic, Google, and Reflection; (2) research third-party GPU cloud-rental price trackers for hourly rates; (3) back-calculate implied capacity-share and $/GPU-hour pricing for each customer against those market benchmarks; (4) add as a subsection to the AI/Compute Top-to-Bottom funnel.

**Sources reviewed**: New raw note file `raw/SPCX/filings/SPCX-ai-compute-gpu-pricing-notes.md` — full source list there. Key outlets: HotHardware, Tom's Hardware, Introl Blog, TechCrunch, MLQ News, CNBC, Mezha.net (chip-mix and deal-term confirmation); Spheron Network, IntuitionLabs, GetDeploying, Jarvislabs, aimultiple, Runcrate (GPU cloud price trackers).

### What Changed
- **§2 AI/Compute funnel, point 2 (Contracting)**: added chip-generation detail per customer — Anthropic/Colossus 1 confirmed as a mixed ≈150K H100 + ≈50K H200 + ≈30K GB200 fleet (≈230,000 GPUs, not a single chip generation as the initial ingest implied); Google's ≈110,000-GPU allocation confirmed as drawn from Colossus 2 (chip generation undisclosed, cluster reported predominantly GB200/GB300) with new detail on its Sept 2026 fee-ramp and under-delivery termination clause; Reflection's terms fully specified for the first time on this page — $150M/month from Jul 1, 2026, confirmed **Nvidia GB300** chips, ≈$6.3B total, 90-day termination clause (previously "[link pending]").
- **New subsection added**: "Deep Dive — Chip Mix, Market Rental Pricing & Back-of-the-Envelope Capacity/Rate Analysis" — a chip-mix table, a GPU market-pricing-benchmark table (H100/H200/GB200/GB300, sourced to live cloud-GPU price trackers), and a back-calculation table implying: Anthropic ≈$7.55/GPU-hr (≈2.1× the mix-weighted market comp), Google ≈$11.62/GPU-hr (≈1.5–1.9× an assumed GB200/GB300 blend), and a reverse-solved Reflection GPU-count estimate of ≈11,000–23,000 GB300s depending on the assumed premium. Capacity-share estimate: the three customers combined account for ≈63–65% of total reported Colossus capacity (555,000 GPUs), leaving roughly a third for xAI's own Grok training and buffer.
- **Consistency pass**: the page's headline AI run-rate figure was previously stated as "≈$26B/yr (Anthropic + Google only; Reflection unquantified)" in four places (Summary, §5, §6 risk table, §13 thesis sentence). Updated to **≈$27.8B/yr** (all three contracts) now that Reflection's $150M/month is a known, disclosed figure rather than "further, unquantified upside." Left the §8 valuation P/S multiple (≈42×) untouched — the ≈4% denominator shift doesn't move the multiple at the precision shown.
- **New raw source file**: `raw/SPCX/filings/SPCX-ai-compute-gpu-pricing-notes.md` — full chip-mix and price-tracker extraction notes, plus the back-calculation methodology and its stated caveats (100%-utilization assumption, trade-press-not-SEC-disclosed chip mixes, tracker-data variance).

### Thesis Status
- **Overall**: Unchanged (Watch / entry <$110) — this was a data-depth addition, not a new catalyst. The back-calculated ≈1.5–2.1× pricing premium over market on-demand GPU rates is a modestly *positive* data point for the segment's potential margin profile (exclusive/reserved/bundled-power-and-networking capacity commanding a premium over shared spot pricing is a defensible structural explanation), but remains inference — SpaceX does not disclose AI-segment margin separately, so this does not change the recommendation.
- **BAIT delta**: None.
- **Price target delta**: None — §11/§12 scenario prices unchanged; only the AI run-rate figure feeding narrative context was refreshed ($26B→$27.8B).

### Recommendation
- **For a non-holder**: Unchanged — Watch; entry <$110
- **For a current holder**: Unchanged — Hold if positioned pre-IPO

**Next review trigger**: Unchanged — first public-company earnings report and/or the August 11, 2026 lockup unlock, whichever lands first.

---

## [2026-07-13] — v3.0 Initial Ingest (Workflow A)

**Trigger**: User-requested new ticker addition. SpaceX IPO'd June 12, 2026 (largest IPO in history, ~$1.8T valuation) — user specifically requested S-1-focused analysis covering (1) segment revenue funnels (Starlink, Launch, and any new segments), (2) company growth projections including new segments like GPU-compute leasing to Anthropic/Google, and (3) business risks.

**Sources reviewed**: SEC EDGAR S-1 (CIK 0001181412) — direct fetch returned HTTP 403 this session; all data WebSearch-synthesized from primary press coverage and financial-analysis newsletters that quote the S-1 directly. Full source list and raw extraction notes in `raw/SPCX/filings/` (SPCX-S1-2026-notes.md, SPCX-post-IPO-events-notes.md, SPCX-management-and-launch-ops-notes.md). Key outlets: CNBC, Bloomberg, Forbes, The Motley Fool, TechCrunch, Fortune, Axios, Benzinga, Yahoo Finance, Al Jazeera, plus specialist S-1-analysis newsletters (mostlymetrics.com, tanayj.com, Tom Tunguz, Morningstar).

### What Changed (initial ingest — full page created)
- **Business Overview / §1–§2**: Established the three-segment structure (Starlink 61% / Launch 22% / AI-Compute 17% of FY2025's $18.674B revenue) and built explicit top-to-bottom funnels for each segment per the user's request — Starlink (capacity → 10.3M subscriber base → declining-ARPU monetization, the only profitable segment), Launch (manifest/backlog → ~140-145 launches/2026 cadence → per-launch + government-contract monetization), and AI/Compute (Colossus GPU capacity → signed Anthropic/Google/Reflection contracts → ~$26B/yr run-rate once fully ramped).
- **§4/§5**: Captured the Feb 2026 xAI merger (the structural origin of the AI segment), the Anthropic ($1.25B/mo through May 2029) and Google ($920M/mo from Oct 2026) compute contracts by name and dollar value, the company's own aggressive 2028-2030 revenue targets ($120-180B → $200-300B → $400-500B+), and the long-dated orbital-data-center ambition (targeted 2028+, explicitly gated on Starship reusability per the S-1's own language).
- **§6**: Built a materiality-filtered risk table covering Musk key-person risk (no key-person insurance, ~79% voting control, explicitly not full-time per the S-1), Starship as a single point of failure for the entire multi-segment thesis, capital intensity (>$40B/yr capex run-rate vs. $18.7B FY2025 revenue), bond-market skepticism (a $25B investment-grade offering trading at junk-like levels within days), extreme float/short-interest fragility (~4-5% float, ~31% of that float short), the staggered lockup-unlock schedule (starting Aug 11, 2026), government customer concentration (~35% of revenue), AI-segment customer concentration (two names), the unexplained $60B Cursor/Anysphere acquisition, and political/regulatory conflict-of-interest exposure tied to Musk.
- **§9**: Full IPO-to-date timeline — debut, ATH ($225.64, Jun 16), the Cursor/Anysphere deal announced the same day, the $25B bond sale and its junk-like secondary pricing, the broader tech selloff, the fresh all-time low ($145.07, Jul 10), and the post-quiet-period analyst-initiation wave (27 analysts, $131-$800 target range).
- **§11/§12**: Built 5-year scenarios with a deliberately wider Bear-probability weight (30%, vs. this wiki's more typical 20-25%) reflecting the concentration/execution risk profile unique to this name. PW EV ≈$185; R/R ≈2.3:1 — modest by this wiki's usual standard, an honest reflection of the risk balance rather than a manufactured asymmetry.

### Thesis Status
- **Overall**: N/A (initial ingest)
- **BAIT delta**: N/A — established at Double overlap (B Strong + I Moderate-Strong; A Mixed; T Weak), Conviction Low-Moderate
- **Price target delta**: N/A — established at Bull $340 (25%) / Base $185 (45%) / Bear $60 (30%); PW EV ≈$185

### Recommendation
- **For a non-holder**: Watch — underlying businesses (Starlink, Launch) are genuinely high-quality, but a 5-week-old listing with no earnings report yet, a fresh all-time low, an unexplained $60B acquisition, and a lockup unlock 3-4 weeks out argue for waiting on the next two catalysts before sizing a position. A deep-discount starter position below $110 is defensible for risk-tolerant investors.
- **For a current holder**: N/A / Hold if positioned pre-IPO — same catalyst-driven framing applies.

**Next review trigger**: First public-company earnings report (targeted late July–August 2026, unconfirmed) and/or the August 11, 2026 lockup unlock — whichever lands first.

---
