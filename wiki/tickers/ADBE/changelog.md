# ADBE — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.6 + v2.7 + v2.8 Retrofit + Material Thesis Refresh

**Trigger**: Schema retrofit pass to bring ADBE from v2.5 to v2.8, combined with two material events that materially shift the thesis since the v2.2/v2.5 ingest:
1. **CEO succession announced March 12, 2026** — Shantanu Narayen to step down once successor named
2. **$25B share repurchase authorized April 21, 2026** — largest in Adobe's history, replaces prior

**Sources reviewed**:
- Yahoo Finance live price (2026-04-25): $245.44, market cap $99.2B, P/E 14.3, EPS TTM $17.16
- Adobe FY2025 + FY2024 stockholder letters (Pattern A annual letter publisher; brief 1–2 pages — substantive commentary in earnings calls)
- FY2024 10-K SEC EDGAR PDF (Item 1A risk factors — AI competition language expanded materially FY2023→FY2025)
- Q1 FY2026 earnings press release + transcript (Mar 12, 2026): $6.40B revenue +12%, NGAAP EPS $6.06 +19%, AI-first ARR more than tripled YoY, Firefly ARR >$250M (+75% QoQ)
- Adobe news + CNBC + BusinessWire on CEO succession and $25B buyback
- Programming Helper / SaaStr / Sacra for Figma market share (40.65%, 13M MAU) and Canva ($3.5B revenue, 260M MAU, $42B valuation)
- MarketBeat / stockanalysis.com / Public.com / Benzinga for analyst consensus ($329–$362 median; RBC Outperform $350 reiterated April 22, 2026)
- Yahoo Finance for confirmation of Michael Burry long position
- Raw indices written to raw/ADBE/shareholder-letters/SOURCES.md and raw/ADBE/filings/SOURCES.md (PDF binary fetches timed out on Adobe CDN; URLs confirmed valid for subsequent curl-based archival)

### What Changed (vs. v2.5)

- **Schema upgraded to v2.8** with all v2.6 + v2.7 + v2.8 mandates applied:
  - Standalone "Moat Assessment" block retired (Rule #23) — moat verdict line in Summary; full detail in §5
  - §5 gains mandatory `### Competitive Landscape` subsection (Rule #24) with Figma / Canva / AI-natives / Microsoft peer table including market share + moat differentiation framing
  - §8 Risk Factors filtered for materiality (Rule #25) — boilerplate dropped; "not priced in" tagging applied; CEO-succession overhang and OpenAI/Microsoft Designer added as differentiated risks
  - 5-Year Risk Factor Evolution collapsed from table to synthesis paragraph (Rule #21)
  - §6 RMC subsection added with FY2024 + FY2025 letter quotes + multi-year strategic-framework arc (Adobe Magic → age of AI → succession-handoff)
  - §2 gains `### Primary Source: 10-K Segment Detail (FY2024–FY2025)` with multi-year MD&A synthesis
  - §14 R/R figure (3.1:1) explicitly anchored to §13 Bull/Bear (Rule #26)
- **Summary section refreshed** — new bullets for $25B buyback, Burry long, CEO succession overhang
- **§6 Management** — full refresh; CEO transition added as the primary management-track narrative, succession-arc framing, $25B buyback recorded
- **§7 Strategic Initiatives** — DICK's partnership added as 2026 enterprise-content-supply-chain proof point
- **§10 Valuation** — combined FCF + buyback yield ~15% computed; market cap refined to $99.2B per Yahoo; FY2026E NGAAP P/E ~10.5×
- **§11 Catalyst Tracker** — refreshed with $25B buyback + CEO succession + Burry + Q1 FY26 + RBC $350 target. Upcoming catalysts now include CEO successor announcement
- **§13 / §14** — bull/base/bear preserved; PW EV $348 unchanged; R/R ~3.1:1 anchored to §13 per Rule #26
- **§15 Recommendation** — thesis sentence rewritten to incorporate the three convergent intrinsic-value signals (AI-first ARR triple, $25B buyback, Burry long); thesis-break triggers expanded to include succession-related triggers (extended search, non-AI-native external hire) and Microsoft Designer / Copilot escalation

### Thesis Status

- **Overall**: 🟢 **Strengthened** vs. v2.5 — the $25B buyback + Burry confirmation + Q1 FY26 AI-ARR concretization (Firefly ARR >$250M disclosed) all materially reinforce the asymmetric-entry thesis. The CEO succession adds offsetting overhang risk but does not invalidate the thesis.
- **BAIT delta**: B Strong (Burry adds capstone signal); A Strong (buyback yield + Firefly ARR disclosure strengthen analytical edge); I Moderate (unchanged); T Weak→Moderate (buyback creates mechanical floor)
- **Price target delta**: Bull / Base / Bear unchanged at $480 / $340 / $170; PW EV $348; R/R ~3.1:1
- **Catalyst & Sentiment delta**: $25B buyback (Apr 21); CEO transition (Mar 12); Burry long (April); RBC reiteration $350 (Apr 22) all new

### Recommendation

- **For a non-holder**: 🟢 **Initiate** at $245.44 — sub-11× FY26E NGAAP P/E + ~9% FCF + ~6% buyback yield + AI-first ARR tripled + Burry long + the largest share repurchase in Adobe's history at a multi-year multiple bottom = Buffett-style asymmetric entry.
- **For a current holder**: 🟢 **Add** — drawdown is sentiment-driven; operating data + capital allocation both intact. Add aggressively below $230.

**Next review trigger**: Q2 FY2026 earnings (June 2026, est.) — first earnings post-buyback announcement and second under the active CEO search.

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A)

**Trigger**: User added ADBE to wiki on 2026-04-24 as part of a 25-ticker expansion batch.

**Sources reviewed**:
- Adobe Q1 FY2026 earnings release (2026-03)
- Adobe Q4 FY2025 / FY2025 earnings release (2025-12-10, BusinessWire)
- Yahoo Finance live price endpoint (2026-04-24)
- MarketBeat, TipRanks, Public.com — analyst consensus April 2026
- Fintel / MarketBeat — short interest April 2026
- Quartr ADBE earnings summary

### What Changed
- Initial compilation; no prior wiki content
- Live price verified at $245.44 (Yahoo Finance, April 24, 2026)
- Established ADBE as Capital-light software platform asset type
- Recorded –42% drawdown from 52-wk high of $422.95
- Documented Q1 FY26: $6.40B revenue +12%, NGAAP EPS $6.06 +19%, AI-first ARR more than tripled YoY

### Thesis Status
- **Overall**: Initiated — Constructive (Buy / Initiate)
- **BAIT signal**: Strong — Triple overlap (B + A + I all Strong/Moderate); High conviction
- **PW EV**: ~$348 (3-yr) vs. $245.44 spot = +42% / +12.4% annualized

### Recommendation
- **For a non-holder**: Initiate — Sub-11× FY26E NGAAP P/E + 9% FCF yield + AI-first ARR tripling = Buffett-style asymmetric entry. Attractive entry zone $220–260.
- **For a current holder**: Add — Drawdown is sentiment-driven; operating data intact.

**Next review trigger**: Q2 FY2026 earnings (June 2026, est.).
