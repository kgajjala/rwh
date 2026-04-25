# SCHW — Changelog

Append-only record of thesis updates. Format defined in CLAUDE.md.

---

## 2026-04-17 — v2.1 Schema Migration (Consolidated Wiki Page)

**Trigger**: Wiki schema migration from v1 (4-file format: overview / thesis / financials / changelog) to v2.1 (single consolidated `[TICKER].md` page + changelog). Performed concurrently with Q1 2026 earnings absorption.

**Sources reviewed**:
- Existing v1 files (overview.md, thesis.md, financials.md)
- raw/transcripts/SCHW_Q1_2026_earnings_call_transcript.md (April 16, 2026 earnings call)
- Yahoo Finance live price (verified Apr 17, 2026)
- Prior 2026-04-05 initial ingest + 2026-04-17 Q1 entry

### What Changed
- Folded overview/thesis/financials into single `SCHW.md` matching v2.1 DASH.md template structure
- Added explicit Section 11 Catalyst & Sentiment Tracker (new in v2)
- Rewrote Section 15 with non-holder/holder split, entry/trim/exit zones, thesis-break triggers
- Removed all portfolio-sizing language (no tranche %, no allocation %, no stock/options split) per v2 Core Rule #3
- Updated price/52-wk to live data: **$88.50** (down from $93.77 prior); 52-wk low *$79.30* — printed *new* 52-wk low *the day after* the Q1 beat (counterintuitive setup)
- Q1 2026 results integrated throughout Sections 2, 4, 6, 7, 11, 13, 15 (revenue $6.5B +16%, EPS $1.43 +38%, client assets $11.8T, NNA $158B Q1 record, DARTs 9.9M, bank loans $61B, 19% div hike, $2.4B Q1 buyback, FY26 EPS guide *raised above* $5.70–$5.80)
- BAIT score *upgraded*: triple-Strong overlap (B + A + I) vs. prior v1 of A-Strong + B/I-Moderate. Behavioral lens upgraded from Moderate to Strong because the new 52-wk low *post* a clear EPS beat with raised FY26 guide is the cleanest behavioral mispricing setup SCHW has shown this cycle
- Price targets refreshed to 18-month horizon: Bull $130 (30%) / Base $108 (50%) / Bear $70 (20%) → PW EV $107 = +21% upside from $88.50
- Deleted legacy v1 files: overview.md, thesis.md, financials.md

### Thesis Status
- **Overall**: **Strengthened** (driven by Q1 print + lower entry price)
- **BAIT delta**: B Moderate → **Strong**; A Strong → Strong (now with FY26 EPS bar *raised*); I Moderate → **Strong** (CFO's explicit guide-raise statement); T Weak → **Moderate** (fresh 52-wk low + buyback floor)
- **Price target delta**: Base $110 → $108 (slightly lower target, but lower entry preserves upside); Bull $137 → $130 (narrower 18-mo horizon); Bear $70 → $70 (unchanged)
- **Catalyst & Sentiment delta**: Stock at fresh 52-wk low *despite* clear Q1 beat; 19% dividend raise + $2.4B Q1 buyback represent step-change capital return; FY26 EPS bar raised >$5.80; Q2/July guide refresh now the next hard catalyst

### Recommendation
- **For a non-holder**: **Initiate** — at $88.50 / ~15× FY26E EPS the stock sits below historical band with strengthening fundamentals
- **For a current holder**: **Add** — the post-beat 52-wk low is a rare add opportunity in a high-quality compounder

**Next review trigger**: Q2 2026 earnings + FY26 formal guidance refresh (~July 2026).

---

## 2026-04-17 — Q1 2026 Earnings Update

**Trigger**: SCHW reported Q1 2026 earnings on April 16, 2026 (yesterday). Strong beat on EPS; FY2026 guidance raised materially.

**Data points reviewed**:
- Q1 2026 earnings call transcript (Motley Fool, Yahoo Finance)
- SCHW investor relations press release
- CFO commentary on NIM trajectory, capital management, growth initiatives

### What Changed
- **EPS**: Q1 $1.43 (+38% YoY) beat consensus $1.42; implies FY2026 EPS will exceed prior guidance of $5.70–$5.80
- **Revenue**: Q1 $6.5B (+16% YoY); record revenue
- **Client Assets**: $11.8T (+19% YoY); core net new assets $158B (Q1 record)
- **NIM Trajectory**: Management signaling "upward momentum" with potential lack of Fed rate cuts; client cash deposits +$8B sequentially
- **Trading Volume**: Record 9.9M daily average trades (+34% YoY); however, revenue per trade declined (smaller positions, shorter duration)
- **Managed Investing**: +46% net flows, Schwab Wealth Advisory reached $10B (+90% YoY)
- **Lending**: Bank loans $61B (+29% YoY), all-time high; long-short lending demand strong
- **Capital Actions**: 19% dividend increase; $2.4B share buybacks; Tier 1 leverage 6.8% (within target)

### Thesis Status
- **Overall**: STRENGTHENED — Q1 execution confirms thesis; FY2026 EPS guidance raised above prior range
- **BAIT delta**: A-STRONG (TD synergies + NIM expansion visible now, not just projected) + I-STRONG (management commentary on rate environment + internal cash growth) + B-MODERATE (no significant behavioral signal; execution affirms fundamentals)
- **New EPS guidance**: FY2026 tracking >$5.80 (vs. prior $5.70–$5.80) — implies multiple expansion opportunity if guidance raised in July
- **Price target delta**: Base case $105–115 may be conservative if FY2026 EPS reaches $5.90+; implies upside re-rating

### Action
- [x] Hold — Tranche 1 position confirmed; Q1 execution validates thesis
- [ ] Buy more — If Fed signals rate cuts, this would be a Tranche 2 entry (NIM hedge)
- [ ] Trim — Not warranted

**Key Monitoring Items**:
1. FY2026 formal guidance (July 2026) — will it be raised above $5.80?
2. Federal Reserve rate path — any cut signals are immediate re-assessment triggers
3. NIM trajectory in Q2 (due ~July 20) — should show continued upward momentum if cash deposit trends hold
4. AI/digital assets/alternatives monetization — early indicators of "next leg" growth
5. Trading revenue per-transaction trend — is this structural decline or temporary?

**Thesis-break triggers** (unchanged):
- Federal Reserve cuts rates 150+bps in 2026 AND cash sorting re-emerges
- NIM falls below 2.5% for two consecutive quarters

**Next review trigger**: FY2026 formal guidance expected July 2026 (post-Q2 earnings ~July 20)

---

## 2026-04-05 — Initial Thesis Compilation

**Trigger**: First full wiki import — thesis compiled from live data (Yahoo Finance,
stockanalysis.com, pressroom.aboutschwab.com FY2025 results, web search).
**Data points reviewed**:
- FY2021–FY2025 annual financials (revenue, NII, NIM, net income, EPS)
- FY2025 full year results: $23.9B revenue (+22%), NII $11.75B (+28.5%), EPS $4.65 (+55%),
  net income $8.4B (+54%), NIM 2.90% (up from ~2.33% trough)
- Client assets: $11.9T (record), net new assets $519B (5.1% organic growth)
- High-cost debt reduction: FHLB + CDs peaked at ~$97B (2023) → $5.1B by Q4 2025
- TD Ameritrade integration: declared complete; "new era of asset monetization"
- FY2026 guidance: revenue +9.5-10.5%; NIM target 2.85-2.95%; expenses +5.5-6.5%
- Stock: $93.77 (13% off 52-week high $107.50; well off 52-week low $65.88)

### What Changed
- First-time compilation — no prior thesis to compare against
- Key thesis established:
  - Cash sorting (the defining 2023-2024 headwind) is FULLY RESOLVED
  - $91.9B in high-cost debt retired — permanent balance sheet improvement
  - TD Ameritrade integration complete — $2B+ synergy run-rate available
  - NIM recovery from 2.33% to 2.90% is structural, not temporary
  - $11.9T AUM at 5.1% organic growth = compounding fee revenue regardless of rates
- Primary risk: Federal Reserve rate cuts could compress NIM back to 2.0-2.3%
- Stock is 13% off high — not a distressed entry, but a quality compounder at fair value

### Thesis Status
- **Overall**: Established — **Medium Conviction** (solid fundamentals; lower BAIT score)
- **BAIT delta**: A-STRONG (TD synergies + NIM expansion not in consensus) + B-MODERATE
  (rate-cut fear overstated vs. balance sheet transformation) + I-MODERATE (FHLB
  debt cleanup structural significance underappreciated) = Double-Triple Overlap
- **Price targets**:
  - Bull: $130–$145 (30%) | Base: $105–$115 (50%) | Bear: $65–$75 (20%)
  - Probability-weighted EV: ~$110 (~+17% from $94)

### Action
- [x] Buy more — Tranche 1: 40% of position at $88–$96; current $94 is in range
- [ ] Trim — N/A (establishing position)
- [ ] Hold — N/A
- [ ] Watch — Federal Reserve rate decisions and NIM trend each quarter

**Data gaps to resolve**:
- ⚠️ Full cash flow statement from SCHW 10-K (FCF, capex, buyback amounts)
- ⚠️ Detailed revenue breakdown by segment (NII vs. fees vs. trading) for quarterly trend
- ⚠️ P/TBV calculation (requires tangible book value from balance sheet)

**Next review trigger**: Q1 2026 earnings (expected April 2026) — NIM trend is key.
Also watch: any Federal Reserve meeting signaling rate cuts would be an immediate
Tranche 2 entry opportunity on any share price decline.

**Thesis-break triggers**:
- Federal Reserve cuts rates 150+bps in 2026 AND cash sorting re-emerges
- NIM falls below 2.5% for two consecutive quarters

---

## 2026-04-05 — INIT

**Trigger**: Wiki initialization — stub created.
**Thesis Status**: Pending first import
**Next review trigger**: Import from raw/analyses/
