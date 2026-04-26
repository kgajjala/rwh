# FIG — Changelog

*Append-only. Most recent entry first. Format defined in CLAUDE.md.*

---

## [2026-04-26] — v2.6+v2.7+v2.8 Retrofit — Primary-source synthesis + output discipline pass

**Trigger**: Per CLAUDE.md retrofit batch — apply v2.6 (shareholder-letter + 10-K MD&A primary-source synthesis), v2.7 (5-year baselines / quarterly-letter substitution), and v2.8 (synthesis discipline + ticker-page output discipline + competitive landscape + risk-factor materiality filter + R/R discipline). Sub-5-year coverage acknowledged: Figma IPO'd 2025-07-31, so available primary-source set is one 10-K (FY2025), three quarterly prints (Q2 stub / Q3 / Q4 2025), and the S-1 founder letter — fetched all available since IPO per Rule #19 sub-5-year provision.

**Sources reviewed**:
- [Figma S-1 prospectus (2025-07)](https://www.sec.gov/Archives/edgar/data/1579878/000162828025033742/figma-sx1.htm) + [S-1/A amendment](https://www.sec.gov/Archives/edgar/data/1579878/000162828025035381/figma-sx1a.htm)
- [Figma IPO founder letter (blog excerpt)](https://www.figma.com/blog/figma-ipo-founder-letter/) — Dylan Field's S-1 letter
- [Figma FY2025 10-K (2026-02-18)](https://s206.q4cdn.com/973901332/files/doc_financials/2025/q4/fig-20251231.pdf) — first 10-K as a public company
- [Figma Q4 2025 / FY2025 release](https://investor.figma.com/news-events/news/news-details/2026/Figma-Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx) and [Q4 2025 transcript via Yahoo](https://finance.yahoo.com/news/figma-fig-q4-2025-earnings-234316909.html)
- [Figma Q3 2025 transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2025/11/05/figma-fig-q3-2025-earnings-call-transcript/) and [Q3 2025 10-Q](https://s206.q4cdn.com/973901332/files/doc_financials/2025/q3/FIG-Q3-2025-10Q.pdf)
- [Yahoo Finance live price (2026-04-24)](https://finance.yahoo.com/quote/FIG)
- [Fortune Dylan Field volatility commentary (2025-09)](https://fortune.com/2025/09/25/dylan-field-figma-stock-share-price-volatility-ipo/)

### What Changed (vs. v2.5 baseline)
- **Header**: Schema v2.5 → **v2.8**; Last Updated 2026-04-25 → 2026-04-26.
- **Summary**: Refreshed; moat-verdict line elevated (Rule #23) — "Narrow but Widening" with explicit drivers; R/R figure (~5:1) now anchored to Section 13 Bull/Bear (Rule #26).
- **Business Overview**: Rule #23 — standalone Moat Assessment block retired; moat content consolidated into §5. Added Q3 2025 + Q4 2025 + S-1 primary-source detail (Make adoption progression, customer cohort growth, $1B termination-fee history).
- **§2**: Added `### Primary Source: 10-K / S-1 Segment Detail (FY2025)` per Rule #20 — verbatim FY26 op-margin guidance framed against Field's S-1 *"AI spend will potentially be a drag on our efficiency for several years"* commitment; quarterly trajectory table reformatted with time in columns (Rule #22). Adds Q3 2025 row that v2.5 was missing.
- **§5**: Added required `### Competitive Landscape` subsection (Rule #24) — 7-row peer comparison (Adobe / Canva / Microsoft Designer / Sketch / Penpot / Cursor-v0-Lovable-Stitch / Miro-Mural) with explicit moat-differentiator framing and honest tail-risk read on Canva + Google Stitch.
- **§6**: Added `### Recent Management Commentary — Primary Source Synthesis` per Rule #19 — 7 verbatim Field quotes (S-1 founder letter + Q3 + Q4 transcripts + Fortune Sept 2025 interview) mapped to investment relevance + 3-print Strategic Framework Arc (synthesis paragraph per Rule #21, not table).
- **§8**: Refactored under Rule #25 materiality filter — dropped boilerplate; kept AI-disruption (not priced in), lock-up cascade, Adobe/MSFT/GOOG bundle competition (not priced in), FY26 op-margin compression (Rule #25(d) discretionary-investment risk), Krieger departure, recession, dual-class governance. Replaced 5-Year Risk Factor Evolution Arc table with synthesis paragraph (Rule #21 — public history is one 10-K, table would be misleading bulk).
- **§11**: Refreshed to 2026-04-26; lock-up final-expiration date called out as proximate technical inflection.
- **§13/§14**: Scenarios preserved (Bull $55 / Base $25 / Bear $7; PW EV $28.60). **§14 Interpretation now explicitly states R/R = ~5:1** anchored to Section 13 (Rule #26) — fixes v2.5 surface that did not state R/R figure.
- **Cleanup**: Removed all "v2.X" / CLAUDE.md self-references from page body per Rule #22 (light references retained in changelog only); removed retrospective "corrected from" framing per Rule #22; tables reoriented to time-in-columns convention.

### Thesis Status
- **Overall**: **Unchanged** — recommendation verbs hold (Initiate small / Hold-Add).
- **BAIT delta**: Triple overlap preserved (B Strong + A Moderate + I Moderate; T Weak-Moderate). Conviction Moderate-High.
- **Price target delta**: Bull $55 / Base $25 / Bear $7 unchanged; PW EV $28.60 unchanged.
- **Catalyst & Sentiment delta**: No new events vs. v2.5 entry — refresh primarily synthesis-discipline, not data-driven.

### Recommendation
- **For a non-holder**: Initiate (small, contrarian) — entry $15–18.
- **For a current holder**: Hold / Add — add on dips into $14–16; trim into $35+.

### Data Gaps Persisting
- Precise diluted share count and fully-diluted market cap
- Specific firm-by-firm analyst rating cadence
- Exact short interest %
- Country-level geographic revenue split
- Specific Form 8-K URL for Krieger board resignation

**Next review trigger**: 📅 Q1 2026 earnings — 2026-05-14 (post-close).

---

## [2026-04-24] — v2.2 Initial Ingest (Workflow A) — ⚠️ Limited Public History

**Trigger**: User added FIG to wiki on 2026-04-24 as part of a 25-ticker expansion batch. Note: FIG IPO'd July 31, 2025 — limited multi-year public-company data.

**Sources reviewed**:
- Figma Q4 2025 / FY2025 press release and earnings call transcript (~2026-02-17, IR / Yahoo Finance / Stocktitan / Fortune)
- Figma IPO disclosures (S-1, July 31, 2025)
- Perplexity Finance / IPOScoop / InvestorPlace coverage of post-IPO price action
- Sherwood News on lock-up expiration mechanics
- Yahoo Finance JSON API live price (2026-04-24)
- News reports on Mike Krieger board resignation (April 14, 2026)

### What Changed
- Initial compilation; no prior wiki content for this ticker.
- Live price verified at $17.47 (Yahoo Finance, April 24, 2026) — **–88% from $142.92 first-day post-IPO peak**, –47% from $33 IPO price.
- FY2025 confirmed: revenue $1.056B (+41%), Q4 NDR 136% (highest in 10 quarters), 67 customers >$1M ARR (+68% YoY).
- FY26 guide: Q1 $315–317M (+38% midpoint); FY $1.366–1.374B (+30% midpoint).
- 8 products (from 4); Make weekly adoption >50% of $100K+ customers.
- Mike Krieger (Anthropic CPO) resigned from Figma board April 14, 2026 — modest negative signal.
- Lock-up dynamics dominant: 54.1% of shares under extended lock-ups expiring in tranches through August 2026.
- 3-year PW EV ~$28.60 vs. spot $17.47 = +64% return — high asymmetry, high AI-disruption tail risk.

### Thesis Status
- **Overall**: Initiated — Initiate (small, contrarian) for non-holder; Hold/Add for holder.
- **BAIT signal**: Triple-overlap (B Strong + A Moderate + I Moderate); Conviction Moderate-High but elevated existential risk.
- **PW EV**: $28.60 vs. spot $17.47 (+64% over 3 years, ~18%/yr).

### Recommendation
- **For a non-holder**: Initiate (small) — entry zone $15–18; explicitly contrarian; AI-disruption tail risk real.
- **For a current holder**: Hold / Add — fundamentals don't support price collapse this severe. Add on $14–16; trim into $35+.

### Data Gaps Flagged
- Precise diluted share count and resulting market cap
- Exact short interest % (likely elevated given lock-up dynamics)
- Geographic revenue split (full disclosure pending FY26 10-Q)
- Insider activity Form 4 cadence not retrieved

**Next review trigger**: Q1 2026 earnings on May 14, 2026 (post-close). Key items: revenue vs. guide, NDR ≥125%, Make adoption metrics, FY26 guide reaffirmation, AI competitive commentary.
