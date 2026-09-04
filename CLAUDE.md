# CLAUDE.md — kg-invest-wiki Schema (v4.0)

Operating manual for the LLM agent that maintains this wiki. **Read before touching `wiki/` or `raw/`.**

---

## 1. What This Wiki Is

A personal, position-agnostic investment knowledge base. Knowledge compounds from primary sources so every session starts from the latest synthesis, not a blank page.

**Owner**: Karthik G · **Started**: April 2026 · **Schema**: v4.0

**The deliverable is a decision.** `wiki/tickers/[TICKER]/[TICKER].md` answers one question — *what should someone do about this stock, and what would change that answer* — and is kept current in place. Everything on the page either supports that decision or does not belong.

**Schema v4.0 is mandatory for all new work.** Every Workflow A ingest and every Workflow B incremental — including a single post-earnings update to a page still written in v3 — produces the v4 page shape in §4. There is no v3 path; if you are writing to a page, you are writing v4.

**Migration is opportunistic, never bulk.** A v3 page migrates to v4 the next time a material event touches it, as part of that update — one page at a time, paid for by work you were doing anyway. Never run a mass migration, and never rewrite a page just to change its format. A quiet week does not migrate a page (it does not touch `[TICKER].md` at all). Until a page is touched, its v3 layout stands and is correct. Mixed v3/v4 pages across the wiki are the expected steady state for months; `git log` is the record of which is which.

**Not**: a portfolio tracker (never records holdings) · position sizing of any kind (price-level *valuation* ranges are fine; tranche/allocation/%-of-portfolio are not) · invented numbers (every figure traces to a primary source or carries `[Estimate]` / `[Analyst consensus]` / `[Management guidance]` / `[Derived]`).

---

## 2. Directory Layout

```
rwh/
├── CLAUDE.md                  ← this file
├── README.md                  ← ticker table (§8)
├── raw/[TICKER]/              ← immutable. NEVER modify. Store extracted text, not binaries.
│   ├── filings/ transcripts/ press-releases/
│   ├── shareholder-letters/ appearances/ investor-day/ analyst-reports/
│   └── ../clippings/          ← non-ticker-specific
└── wiki/
    ├── index.md               ← catalog (§8)
    ├── watchlist.md           ← attractiveness ranking (§8)
    ├── tickers/[TICKER]/
    │   ├── [TICKER].md        ← the deliverable
    │   └── changelog.md       ← append-only event log
    └── frameworks/            ← bait.md, moneyball.md, asset-types.md, outsiders.md
```

---

## 3. Core Rules

**R1 — `raw/` is immutable.** Add, never edit. Store extracted `.txt`, not multi-MB PDFs; link the public URL for the original.

**R2 — Position-agnostic.** Analyze the company, not the owner's holdings. Recommendations split non-holder / holder only where they diverge.

**R3 — No sizing.** No tranche %, position %, allocation, or stock/options split, anywhere.

**R4 — Primary sources, verified.** SEC filings, earnings releases, IR pages, transcripts. Non-primary content carries a tag (R above). **Verify live price before any valuation work** — [Yahoo Finance](https://finance.yahoo.com/quote/) first, then CNBC / Google Finance / MarketWatch. Never trust a search snippet; click through. Same for any number that moves the decision.

**R5 — Every source is a real Markdown link.** `[Human-readable label](url-or-relative-path)`, pointing at the *specific* document. Relative path when stored locally, absolute when public. Unresolvable → append `[link pending]`. Never a bare `[Source: …]` tag.

**R6 — Date discipline.** Run `date -u +%Y-%m-%d` before writing any date-stamped artifact. Never infer today's date from context or file contents.

**R7 — State once.** *(replaces v3 rules 20, 21, 22, 26)*
- Every fact has exactly one home. Elsewhere it is **referenced in a clause**, never re-explained. Canonical homes: price/range → header · multiples, scenarios, PW EV, R/R → §4 · sentiment, analysts, insiders, short interest → §6 · capital allocation + Outsider grade → §3 · the argument → The Call.
- **Synthesis, not transcription.** A verbatim quote must earn its place — use one only where paraphrase would weaken it. Never a chronological table of source extracts where 2–3 sentences would do.
- **No schema mechanics on the page.** No references to this file, no "corrected from" / "prior framing" / "previously we said". Git is the audit trail.
- **Budget: ≤1,500 words of prose** for a full page, **≤250 words** for a changelog entry — both measured on prose only, **excluding tables and source lists** (a page's Sources section, a changelog's Trigger/Sources block). Citing sources properly must never cost you budget. Both figures are calibrated against real output, not aspiration — below ~1,200 a page starts losing the evidence that makes its argument credible, and below ~250 a changelog starts dropping metrics that a later reader needs. An entry that also records a schema migration sits at the top of that range; a routine earnings entry should come in well under it. Tables must earn their place — a table with one meaningful row is a sentence.
- **Closing audit, required**: scan for any thesis-carrying *claim* — a figure, a rate, a named risk, a valuation multiple — appearing more than twice, and collapse the extras to a reference. Proper nouns are exempt: naming an initiative, a segment or a person in three places is not duplication, **restating what it proves is**.

**R8 — Valuation: one 5-year forward lens.** *(v3 rule 24, unchanged in substance)*
- §4 scenarios always use a 5-year terminal horizon; Bull/Base/Bear probabilities sum to 100%.
- **PW EV is the sole buy/sell anchor.** Entry = price ≤ PW EV − 15–25% MoS · Trim = PW EV → Bull · Avoid = ≥ Bull.
- **One R/R figure**, cited identically everywhere: (Bull % upside) ÷ (Bear % downside) vs. spot.
- Analyst targets and 12–18-month re-rating math are *inputs to probabilities*, never anchors for the zones.

**R9 — Management primary sources: letters *and* appearances.** *(v3 rule 18, condensed)*
Management speaks off-script at conferences, on CNBC/Bloomberg, on podcasts, and discloses strategy and pricing detail that never reaches the press release.
- **Letters** — 5 fiscal years. Pattern A (standalone annual): 5. Pattern B (quarterly letters): 5× Q4 + 3 most recent, min 8. Pattern C (no standalone): chairman's letter in the annual report or DEF 14A; if neither exists, log the gap. Store as `shareholder-letters/YYYY_letter.txt` by fiscal year covered.
- **Appearances — sweep every ingest and every Workflow B window**, in order: (a) IR events/calendar page — also confirms *upcoming* appearances; (b) earnings-day CEO/CFO media hit, which routinely reframes the print; (c) podcasts / non-financial shows, where CEOs are least guarded; (d) conference transcripts. Fetch the transcript or a substantive write-up, never a headline. Store as `appearances/YYYY-MM-DD_<venue>_<who>.txt`.
- When an IR prepared-remarks PDF won't parse, cross-check **two independent transcripts plus one trade-press write-up** — secondary transcripts truncate, and pricing/product/partnership detail is what they drop.
- Attribute every quote to *where* it was said. An off-script claim carries different weight than a scripted one.
- **If a window genuinely had no appearances, say so.** An unstated absence is indistinguishable from an unchecked one.

**R10 — 10-K MD&A and Risk Factors are required.** Last 5 fiscal years on first ingest.

| 10-K Item | Lands in | Extract |
|---|---|---|
| 1 Business | §1, §2 | Founding insight, segment definitions |
| **1A Risk Factors** | **§5** | Verbatim language for the highest-impact few; flag *new* vs. prior year |
| **7 MD&A** | **§1, §2** | Segment drivers, competitive dynamics, macro sensitivity |
| 7A Market Risk | §5 | Quantified rate/FX/commodity sensitivities |
| 8 Statements & Notes | §1, §3 | Segment data, contingencies, debt, share count |
| 15 / DEF 14A | §3 | Exec comp, board, insider ownership |

EDGAR HTML > IR PDF > analyst summaries. The **[SEC XBRL company-facts API](https://data.sec.gov/api/xbrl/companyfacts/CIK[##########].json)** is the fastest reliable source for multi-year series — prefer it over parsing HTML tables. Workflow B diffs Item 1A year-over-year; new risks get a `[NEW in FY[N] 10-K]` tag.

**R11 — Risk materiality filter.** §5 covers risks material to the *decision*, not every Item 1A line.
- **Drop** boilerplate: "revenue could fluctuate", generic cyber, generic key-personnel, generic third-party reliance.
- **Keep** only risks meeting ≥1 test: (a) materially worse here than for peers; (b) **not priced in** — say so explicitly; (c) tied to a quantified thesis-break trigger the page commits to monitor; (d) tied to a specific large discretionary bet with an uncertain outcome.
- Multi-year risk evolution is 2–3 sentences of prose, never a table.

**R12 — Outsiders lens.** §3 carries a one-line grade per [`outsiders.md`](wiki/frameworks/outsiders.md), anchored on countercyclical buyback discipline. Vocabulary: `Outsider · Outsider-leaning · Reinvestor · Steward (not Outsider) · Anti-Outsider`. One sentence of evidence. Surface it to the Verdict **only on a material capital-allocation event** (buyback authorization/execution, dividend init/raise/cut, M&A, large debt action). Keep the ticker's row in `outsiders.md` in sync.

**R13 — One page per ticker; changelog is the event log.** The folder holds exactly `[TICKER].md` and `changelog.md`. Every material update writes a changelog entry stating **Thesis Status** (Strengthened / Weakened / Unchanged) and an **action verb** (Initiate / Add / Hold / Trim / Exit / Watch / Avoid — *Trim* and *Reduce* are the same action; prefer *Trim*, matching the §4 zone name). Cross-ticker and schema-only events live in **commit messages**, not in any wiki file.

**R14 — Active / Paused.** Header carries `**Status**: Active` or `**Status**: Paused — since YYYY-MM-DD`. README, `index.md` and `watchlist.md` mirror it; Workflow B skips Paused entirely. Quiet ≠ paused: an Active quiet week still logs; a Paused ticker writes nothing.

**R15 — Style.** Emoji carry meaning, never decoration: 🟢 bullish/add · 🔴 bearish/exit · 🟡 neutral/hold · ⚠️ material risk · ✅ resolved (pair with `~~strikethrough~~`) · 📅 dated catalyst · 💰 capital allocation · 🎯 price zone. **Bold** only punchlines and thesis-carrying numbers — if half a paragraph is bold, none of it is. Tables run time in columns, metrics in rows.

---

## 4. The Page

Seven sections. The front matter *is* the deliverable; the sections exist to support it.

```markdown
# TICKER — Company Name

> **Schema** v4.0 · **Updated** YYYY-MM-DD · **Status** Active
> **Price** $X.XX verified <date, time> ([Yahoo](url)) · 52-wk $L–$H · Nth %ile · ±X% from high
> **Type** <one-line asset class>

## Verdict
<One sentence. The whole call — what this is and what to do.>

🟢 **Non-holder: <verb>** · 🟡 **Holder: <verb>**

| PW EV | vs. spot | R/R | Entry | Trim | Avoid | <primary multiple> | Yield | BAIT | Moat | Next |
|---|---|---|---|---|---|---|---|---|---|---|
(one row)

**Breaks if**: <the single most load-bearing fact — if this goes, the thesis goes.>

## The Call
≤200 words. What the market has priced, what it has wrong, and the one number that
proves it. This is the ONLY place the argument is made — sections 1–7 supply evidence,
they do not re-argue.

## What I'd Have To Be Wrong About
Exactly 3 bullets. Each is a *disconfirming test*: what I would look for, where it
would show up, and by when. Not a hazard list — that is §5.

## 1. Business & Numbers      ← v3 §1 + §2 + §5 growth
## 2. Moat & Competition      ← v3 §3 + §7 macro/industry
## 3. Management & Capital    ← v3 §4, incl. Outsider grade + letters/appearances
## 4. Scenarios → PW EV       ← v3 §8 valuation + §11 + §12, one table
## 5. Risks & Triggers        ← v3 §6 + §13 triggers, one table
## 6. Catalysts & Sentiment   ← v3 §9
## 7. Sources
```

**Section notes**

- **§1** — 5-year table + recent quarters + segment detail + where growth comes from. Lead with what changed, not what is.
- **§2** — Wide / Narrow / None + why + what breaks it. Must name direct competitors with market share and a one-line threat read each; state how *this* company differs and the evidence. Structurally unique businesses get a line, not a table. Industry structure and TAM live here.
- **§3** — CEO/CFO read, capital-allocation record, Outsider grade (R12), and the letters/appearances synthesis (R9). Attribute quotes to venue. State explicitly when a window had no appearances.
- **§4** — **One table**: scenario, 5-yr target, probability, contribution, plus the assumption that drives it. PW EV is the sum. Multiples and the peer read sit here as the *anchor* for the scenarios, not as a separate valuation section.
- **§5** — **One table**: `Risk | Impact | Prob | Priced in? | Would break the thesis if…`. The trigger column replaces the old standalone trigger list. Front-matter bullets state the *test*; this table states the *hazard and odds* — different objects, no restatement.
- **§6** — Analyst consensus + rating changes; short interest with WoW/MoM delta; insider activity (last 90 days, Form 4 verified); recent news; **management appearances (R9)**; upcoming catalysts with dates. Move delivered items to `✅ Delivered`.
- **BAIT** is one cell in the Verdict table (`Triple (B+A+T)`). Justify a lens in §6 only where the rating is non-obvious. It is a scoring overlay, not a section.

---

## 5. Frameworks

- **BAIT** (Mauboussin) — Behavioral / Analytical / Informational / Technical, each Strong / Moderate / Weak. Triple+ overlap = highest conviction. → [`bait.md`](wiki/frameworks/bait.md)
- **Moneyball** — 5-year terminal scenarios; PW EV per R8. → [`moneyball.md`](wiki/frameworks/moneyball.md)
- **Asset Types** — per-asset-class key metrics and valuation primary. → [`asset-types.md`](wiki/frameworks/asset-types.md)
- **Outsiders** (Thorndike) — five tests, R12. → [`outsiders.md`](wiki/frameworks/outsiders.md)

---

## 6. Workflow A — First-Run Ingest

Trigger: *"ingest [TICKER]"* / *"add [TICKER]"* / *"build a page for [TICKER]"*. If the folder exists, switch to Workflow B.

1. **Verify the date** (R6) and **the live price** (R4).
2. **Fetch the raw set** into `raw/[TICKER]/` — 5 annual 10-Ks · last 4 quarterly transcripts and press releases · 12 months of 8-Ks · latest DEF 14A · 5 years of letters (R9) · 12 months of appearances plus scheduled forward dates (R9) · latest investor-day deck · user-supplied PDFs. Log gaps; never fabricate. Store extracted text (R1).
3. **Pull the numbers** — SEC XBRL company facts for the multi-year series (R10); then 52-wk range, market cap, EV, net debt, operating leases, float, short interest, analyst consensus, 90-day insider activity from Form 4 XML.
4. **Synthesize the page** per §4, applying R7–R12.
5. **Write** `[TICKER].md` + a `changelog.md` initial entry. Delete any legacy `overview.md` / `thesis.md` / `financials.md`.
6. **Run the closing audit** (R7) — duplication scan and word budget.
7. **Update the cross-file layer** (§8) — including the `index.md` Summary cell with its verb and fresh upside/downside pair, and the `Updated` date in the same edit. Then **commit and push** (§9).

## 7. Workflow B — Incremental Update

Trigger: *"weekly update"* / *"update [TICKER]"*.

1. **Baseline** — read `**Status**:`. Paused → skip entirely. Active → baseline is the latest changelog entry date; the lookback window is everything since.
2. **Scan** the Meaningful Events list (§10) across IR (including the events calendar), SEC EDGAR, the earnings calendar, the appearance sweep (R9), analyst actions, short interest, Form 4s, and news.
3. **Material events** → fetch new raw material, then refresh **only what moved**:

   | Always | On the right trigger |
   |---|---|
   | §1 on earnings (new quarter row, roll TTM) | §2 — only on a moat-altering event or true strategic pivot |
   | §4 — re-verify multiples, scenarios, PW EV, R/R | §3 — on management change, capital allocation, a new letter or a material appearance |
   | §5 — mark resolved risks `~~struck~~ DE-RISKED [date]`, add new under R11 | |
   | §6 — price, consensus, insiders, news, appearances, upcoming | |
   | **Verdict** — thesis, verbs, zones, "Breaks if" | |

   §2 rarely moves on a single earnings print. Do not touch a section the news did not touch.
4. **Quiet week** → write only a `[YYYY-MM-DD] — No Material Events` changelog entry with a price / short-interest / consensus snapshot. **Do not modify `[TICKER].md` and do not bump any dates.**
5. **Changelog** entry mirroring the sections refreshed, ≤200 words (R7). Then §8 — re-derive the `index.md` Summary against the new price and scenario set, since both the verb and the upside/downside pair move whenever §4 or the price does — and §9.

## 8. Cross-File Layer

Three files summarize the ticker set. **Each carries only what is unique to it** — the same sentence must not appear in two of them. All history lives in commit messages (R13), never as append-only prose.

| File | Carries | Hard cap |
|---|---|---|
| `README.md` | `Ticker \| Status \| Updated \| Punchline`, alphabetical; `*N tickers.*` counter below | **Punchline ≤ 30 words** — the verdict and the one number behind it |
| `wiki/index.md` | `Ticker \| Status \| Company \| Moat \| Conviction \| Updated \| Summary` + a price/BAIT/recommendation table + pending data gaps. **Summary format below.** | **Summary ≤ 40 words.** No "last refresh" narrative — a bare `*Last updated: YYYY-MM-DD*` line only |
| `wiki/watchlist.md` | Attractiveness ranking: `Rank \| Ticker \| Conviction \| BAIT \| PW EV vs. price \| Recommendation \| Next catalyst` + price-target table + earnings calendar + macro watch items. Active only; Paused in a footer | **Ranking cell ≤ 40 words.** No header changelog |

### The `index.md` Summary cell

The one place a reader can scan the whole book and see, per ticker, *what to do and what it is worth*. Three parts, in this order, ≤40 words total:

1. **The action verb**, leading — 🟢 Initiate / Add · 🟡 Hold / Watch · 🔴 Trim / Exit / Avoid. Where non-holder and holder diverge, give both (`Initiate / Hold-Add`).
2. **One or two lines on the opportunity** — what the setup is, in plain words. Not a metrics dump.
3. **Upside and downside**, always as a pair and always defined the same way:
   - **Upside** = **PW EV vs. spot** — what the probability-weighted case is worth from here.
   - **Downside** = **Bear case vs. spot** — what it costs if the thesis fails.
   - Write it as `PW EV $204: +49% up / −27% down`. Both legs come from the §4 scenario set, so they always reconcile to that page's R/R (R8) without restating it.

**These percentages are point-in-time and go stale as the price moves.** That is expected and disclosed by the `Updated` column in the same row — which is why the two must never drift apart. Refresh the Summary, the percentages and the `Updated` date **in the same edit**, on every Workflow A ingest and every Workflow B incremental that touches the page. **A quiet week refreshes none of them** — it does not touch `[TICKER].md`, so the row keeps its old date and its old numbers, correctly labelled as of that date.

⚠️ **The v3 failure mode this replaces**: the same ~400-word block written three times, plus `index.md` accreting a single 4,000-word "last refresh" line. If a reader needs the full story, they open the ticker page. These three files are indexes, not summaries.

## 9. Commit & Push

`git commit` with a subject naming the ticker and the finding, then **`git push origin main` — always** (R13). Surface push failures to the user.

- Ingest: `INGEST [TICKER]: <headline finding>`
- Update: `WEEKLY YYYY-MM-DD: [N] events / [M] quiet — <headline>`
- Pause/resume: `PAUSE [TICKER]: <reason>` / `RESUME [TICKER]: catch-up over [N] days — <headline>`
- Schema: `SCHEMA: vX.Y — <what changed and why>`

The commit body is where rationale, migration history and cross-ticker context live.

## 10. Workflow C — Pause / Resume

**Pause** — verify Active, get the date (R6), set the header, append a changelog entry with the reason and last baseline, update the three cross-files (README/index Status → Paused, watchlist → Paused footer; do **not** bump Updated), commit `PAUSE`.

**Resume** — a multi-quarter pause spans earnings, analyst clusters and macro events; reconstruct them, don't just re-price. Scan the full window (all 10-Q/10-K, earnings and transcripts, 8-Ks, the full analyst-action record noting clusters, current short interest / insiders / consensus, plus management, M&A, regulatory and capital-allocation events). Apply the Workflow B refresh; §6 enumerates each earnings print in order before settling on the current state. Set Active, bump Updated, append a `## [date] — Resumed (Catch-Up)` entry, update cross-files, commit `RESUME`.

---

## 11. Meaningful Events

Earnings (10-Q/10-K, release, transcript) · annual shareholder letter · **material C-suite appearance** (R9 — material when it discloses strategy, pricing, product, partnership or competitive detail not in the filings, or reframes a print) · shareholder meeting and proxy outcomes · strategic announcements (launch, market entry/exit, divestiture, restructuring) · M&A and JVs · capital allocation (buyback, dividend, debt, equity issuance) · analyst rating changes (**a cluster of ≥3 firms in a week gets special attention**) · short interest >10% MoM or a sustained 3-week trend · insider Form 4 >$1M, any cluster, or a CEO/CFO sale into a decline · major regulatory action · material litigation · CEO/CFO/COO or board changes · credit rating actions.

Extensible — add types when encountered.

## 12. Data Sources

| Data | Primary | Fallback |
|---|---|---|
| Live price | [Yahoo Finance](https://finance.yahoo.com/quote/) | CNBC, Google Finance, MarketWatch |
| Filings | SEC EDGAR (HTML; `curl` with a UA header) | Company IR |
| Multi-year financials | **SEC XBRL company-facts API** | 10-K tables |
| Transcripts | IR prepared remarks, Motley Fool, Seeking Alpha | Investing.com, AlphaStreet, Benzinga — cross-check ≥2 (R9) |
| Appearances | IR events page, conference transcripts | CNBC/Bloomberg, podcast notes, trade press |
| Analyst ratings | Research-firm releases | User PDFs in `analyst-reports/`, TipRanks, StockAnalysis |
| Short interest | Fintel, ChartExchange, NASDAQ | FINRA twice-monthly |
| Insiders | **SEC Form 4 XML direct** | OpenInsider |
| Options | CBOE, Yahoo chain | Barchart |

## 13. changelog.md Format

Append-only, newest first. **Record what changed and why — never restate the thesis; the page carries that.**

```markdown
## [YYYY-MM-DD] — <Event type>

**Trigger**: <what caused this; link the primary source>
**Sources**: <files in raw/ or URLs>

### Changed
- <metric or thesis element — direction and magnitude, one bullet each>

### Status
- **Thesis**: Strengthened / Weakened / Unchanged
- **PW EV**: $X → $Y · **R/R**: A → B · **BAIT**: <delta if any>
- **Verbs**: non-holder <verb> · holder <verb>

**Next trigger**: <event or date>
```

Quiet week:

```markdown
## [YYYY-MM-DD] — No Material Events

**Window**: <baseline> → <today>
**Snapshot**: price $X (±Y%) · 52-wk %ile · short interest A% (±B% MoM) · consensus $C
**Dismissed**: <headlines scanned and why they don't matter>

**Recommendation**: Unchanged. **Next trigger**: <default or specific>.
```

## 14. Parallelization

- Workflow A fetch: optional fan-out of 3–4 agents split by source type; one synthesizer reads the aggregate.
- Weekly across N tickers: one agent per Active ticker, dispatched in a single message.
- **Within a ticker: single agent.** §4 depends on §5 depends on §1 — section-level parallelism costs more in merge than it saves.
- **Never parallel-write** `README.md`, `index.md` or `watchlist.md`.
- Only spawn agents when the user asks for them.

## 15. Schema Co-Evolution

This file **does not grow by default.** R7 applies to it as much as to a ticker page.

1. **Find the home first.** Edit where the concept already lives. A new rule only when no home exists.
2. **Replace, don't append.** A change that adds lines deletes the lines it supersedes in the same commit.
3. **Rationale goes in the commit message**, never as residue in the text.
4. **Apply on next material touch** (§1). Never backfill untouched pages, and never bulk-migrate — git is the record.
5. **Consolidate when rules sprawl.** Bump the major version and rewrite rather than patch.

`git log --oneline CLAUDE.md` · `git log -p CLAUDE.md` · `git blame CLAUDE.md`
