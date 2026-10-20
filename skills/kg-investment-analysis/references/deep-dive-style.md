# Deep-dive style: structure, voice, devices and updates

Read this before writing or updating any report. It describes the long-form style (modelled on MBI Deep Dives' *Uber: The Aggregator on Trial*) that v7 uses for every full report and every incremental update. The framework's rules (hurdle, verbs, kill criteria, R16 ground truth) do not change; this file says how they are told.

Contents:
1. What the style is
2. The chapter structure
3. Recurring devices
4. Where the framework's required content goes
5. Voice and copy rules
6. Charts and tables
7. Incremental updates (Modes B and C)
8. Length
9. Checklist before building

---

## 1. What the style is

A deep dive is an argued essay by one analyst, in the first person, that ends in a decision. It reads like a smart person thinking out loud with the numbers in front of them:

- It **starts from history and the stock's record**, not from a definition of the company: what happened, what the stock did, and why the market is unsure now.
- It **names the one debate** that decides the stock and spends most of its length there.
- It **lets management make its case in its own words** (long, attributed quotes from calls, conferences and letters), then **pokes holes** in it, with numbers.
- It **builds an illustrative unit-economics table** to turn the debate into arithmetic.
- It **judges management by its record**, including the CEO's previous job, the deal history, the capital-allocation table and the incentive plan.
- It **values the company backwards**: what does the price already assume, and what has to be true to earn the hurdle?
- It **ends with a plain verdict** and the evidence that would change it.

Two habits make it work. Every claim that matters has a number next to it. And the writer admits uncertainty and past mistakes rather than hiding them.

## 2. The chapter structure

Use these chapters in this order. Rename them to fit the company (e.g. "North America: Traffic Is Back. The Margin Isn't."), but keep the job of each.

| # | Chapter | Its job | Typical length |
|---|---|---|---|
| — | **Front matter** (generated from data.json) | Header, Verdict, The Call, the three tests, latest update with scorecard; then the essay title and dek | — |
| — | `::toc` | A contents line linking the chapters | — |
| 0 | **Opening** (no heading) | The history in 3–5 paragraphs: a dated, concrete moment (a CEO hire, an IPO, a crash); what the business did since; what the stock did, against a named rival and the S&P 500 (`::chart`); the question the market can't answer; a roadmap paragraph listing the chapters and ending with the valuation question | 400–700 words |
| 1 | **Business Overview** | Segments in one table (revenue, operating income, margin across 3–5 periods); the profit mix (`bar100` chart); "a few accounting points" the reader needs before the debate (non-GAAP adjustments, one-offs, deconsolidations) | 400–700 |
| 2 | **The key debate** | Where things stand (a table) → **Management's narrative** (h3; 1–3 long quotes, attributed) → **Poking holes in it** (h3; 3–4 numbered-in-prose holes, each with a number) → the illustrative unit-economics table → "Where I come out" paragraph | 1,200–2,000 |
| 2b | **Rings of profit** (h3) | Profit split into 3–4 rings by exposure to the debate, as a table, with one paragraph on what is safe and what is not | 250–400 |
| 3 | **The second debate** | The other segment or strategic question (beverages vs. Coke, international and an acquisition, the ad business). Same pattern, shorter | 600–1,200 |
| 4 | **Management, Capital Allocation and Incentives** | CEO background and **prior-tenure record** (chart + table when there is one); the deal list with verdicts; the capital-allocation table with cumulative row; the incentive table; "Is X the right manager?" paragraph | 1,000–1,800 |
| 5 | **Valuation and Model Assumptions** | Method in one paragraph; `::model_build Base`; one paragraph walking the Base; `::scenarios`; the **Priced-in** paragraph (what spot assumes); the **Hurdle** paragraph (what 13% needs); PW value, return, entry; the EPV floor cross-check | 700–1,100 |
| 6 | **Final Words** | The conclusion in plain language: what the market has right, what it has wrong, the verdict, and the three things (= the kill criteria) that would change it, with dates | 300–500 |
| 7 | **Appendix: The Numbers** | Required R16 tables that don't fit the narrative (five-year record with ROIC/ROIIC/owner earnings, driver tree, growth levers, moat table, risks table, catalysts) | tables |
| — | **Sources** `{#sources}` + `::sources`, `::disclaimer` | Every document used | — |

## 3. Recurring devices

**The stock-versus-business opener.** Contrast operating growth with shareholder return over a meaningful window ("revenue +45%, the stock +14%"). Chart total return (`prices.py`) against the most relevant rival and the S&P 500. Pick the window that tells the story: a CEO's tenure, the period since an event, or before vs. after.

**Management's narrative, then the holes.** Quote management at length where its own words carry the argument best: earnings calls, sell-side conferences, investor days, interviews, letters. Attribute every quote to a person, venue and date. Then write "Poking holes in it" as a sequence: "The first hole is…", "The second hole is…". Each hole needs a number or a source. Be fair: say where management is right.

**The illustrative unit-economics table.** Build the economics of one unit (a trip, a $1 of snack revenue, a store, a subscriber) from disclosed figures plus clearly labelled estimates. Then show how the profit per unit moves under the debate's scenarios: price cut, take-rate cut, labor reinvestment, refurbishment. The last row compares the illustration with the actual reported number. Label the estimates in the note.

**Rings of profit.** Order the profit pool by how exposed each part is to the central risk, with share of profit, margin, the threat and the exposure. The rings usually show that the risk is real but concentrated.

**The prior-tenure test.** If the CEO or the strategy has a track record elsewhere, chart it and table it: what grew, what the stock did, how much came from earnings versus multiple, and what's different now.

**The deal list.** Every material acquisition and divestiture of the era: year, price, what happened, verdict (Good / Mixed / Poor / Unclear / Too early).

**The capital-allocation table.** Fiscal years in rows: revenue, YoY, EPS, operating cash flow, SBC, capex, FCF, FCF margin, dividends and % of FCF, buybacks and % of FCF, acquisitions, debt and diluted shares, plus the latest partial year and a cumulative row. Write two paragraphs on what the cumulative row says.

**The incentive table.** Component, weight or size, what it pays for, latest outcome. Always include a "Return on invested capital" row, even when it is 0%. Then say how the plan is likely to shape behaviour.

**Priced-in and Hurdle cases.** These come from the model's diagnostics (`model.py` solves them along a case path at a fixed exit multiple). Write them as two short paragraphs: "To earn an ordinary [discount rate] … the price needs EPS of [[Priced-in.eps]]…" and "To earn 13% a year … it would need [[Hurdle.eps]]…". Then compare each with the Base and Bull cases.

## 4. Where the framework's required content goes

Nothing the framework requires is dropped; it moves to where it reads best.

| Framework item (v6 section) | Deep-dive home |
|---|---|
| Verdict, verbs, zones, PW EV, R/R, Breaks if, The Call | `data.json` (verdict, call); rendered in the generated front matter. The Call is also the backbone of Final Words; don't restate it word for word |
| Three kill criteria with pre-committed consequences | `data.json` tests (with `shift` so consequences compute); rendered in the front matter; `::tests` in Final Words places a pointer to them |
| Driver tree (R16) | The key-debate chapter ("where things stand") or the Appendix |
| Five-year record with ROIC, 3-yr ROIIC, reinvestment, owner earnings, quality and earnings-quality rows | Appendix table (required). Its conclusions are argued in Management & Capital |
| Growth levers | Appendix table; the Base/Bull lever sentence goes in Valuation |
| Moat table (mechanism, trend, profit pool, customer) | The debate chapters argue it; the four-row table goes in the Appendix |
| Incentives, guidance grade, promises ledger, $1 retention test, Outsider grade | Management & Capital (incentive table, capital-allocation table, promises ledger as a table, grade in one sentence) |
| Appearances (R9) | Quoted in the debate chapters; the list of appearances (or "none") goes in the update note or the Appendix |
| Scenarios, return math, EPV floor, break-even and price-implied Bear odds, terminal-growth check, base rate, year ten | Valuation (`::model_build`, `::scenarios`, prose) plus a return-math table in the Appendix |
| Risks table, catalysts, analysts, short interest, insiders, BAIT | Appendix tables; analysts and insiders get one line each |

## 5. Voice and copy rules

- **First person, plain words.** "I think", "my worry is", "I would not underwrite". Short declarative sentences. Talk to the reader like a smart colleague.
- **Concrete over abstract.** A date, a price, a percentage, a name. "The stock rose 24.5% that day, from $77.03 to $95.90" beats "the market welcomed the news".
- **Fair to management.** State their case at full strength before arguing with it; credit what's working.
- **Admit uncertainty and past errors.** "I was skeptical about X; that was a mistake." "There may be too much noise to conclude anything."
- **Mr. Market** is fine, used sparingly. No hype words, no "game-changer".
- **No mannered devices**: no em-dash asides, no "not X, but Y" constructions, no colon-then-reveal, no scare quotes, no "worth noting".
- **Numbers that matter come from the model or data** through `[[tokens]]`, so they stay consistent across the essay, the tables and the front matter.
- **Tags still apply**: estimates are labelled in the table note or the sentence (`[Estimate]`, "author's estimate"), consensus as `[Analyst consensus]`.
- **Every source is a link** in the sentence or the table note, and in `data.json` sources.

## 6. Charts and tables

- **Charts** are rendered as static SVG images (light and dark backgrounds both work), each followed by its note and a small data table.
- **Chart types**: `line` for total-return comparisons (one to four series, from `prices.py`); `bar100` for profit or revenue mix over periods. One chart per point. Two or three charts per report is typical. Each has a note with the definition, base date and source, and an automatic data table.
- **Palette**: the four categorical slots in fixed order; the subject company is always slot 1. Never more than four series.
- **Tables**: years or periods in columns, metrics in rows. `grp` for segment headers, `sub` for indented detail rows, `tot` for totals. `in` marks model inputs. `neg`/`pos` mark the cells that carry the point. A leading `~` on a column name makes it a wrapping text column. Every table has a note with the source.
- **Accent color** (`meta.accent`) applies only to the optional `--html` page.

## 7. Incremental updates (Modes B and C)

An update keeps the deep dive true and puts the news on top. It never starts a new essay unless the thesis changed.

1. **Write the update note** as `updates/YYYY-MM-DD.md` and add it to `data.json` `updates` with a title and the **scorecard** (each standing test: `pass`, `fail` or `pending`, plus the number that decided it).
   - **Mode B (earnings or a material event): 600–1,200 words.** What was reported against what was expected. Management's three to five points, quoted where it matters. Q&A pushback and non-answers. What it does to the debate. The scorecard consequences, applied as pre-committed. The verb, and why.
   - **Mode C (news or price move): 200–500 words.** What drove the move, whether it touches a test, and the return math at the new price.
2. **Refresh the data, not just the note.**
   - New quarter rows go into the tables.
   - Move `model.json` `spot` to the verified price and re-run `model.py`.
   - Update `meta` (price, date, range) and `verdict`.
   - Replace a resolved test with a new one.
3. **Edit body prose that is now false.** Any sentence the news contradicts gets rewritten in place, so the essay stays true on its own. Don't leave a contradiction for the update note to explain. Git holds the old text.
4. **Rebuild with `--check`** and read the result once. If the report is shared as an Artifact, republish it to the same URL.
5. **Full rewrite (Mode A again) when the thesis changes**, a year has passed since the last full report, or more than four update notes have accumulated. Older notes stay in `updates/`; the report links them under "Earlier updates".

## 8. Length

- Full deep dive: **about 4,000–7,000 words of prose**, excluding tables, quotes and the Appendix. The Uber piece that set the style runs about 11,000 words including long quotes; aim shorter.
- The budget guards against sprawl. When a draft runs long, cut restated claims and second examples before cutting evidence.
- Update notes: 600–1,200 words (Mode B) or 200–500 words (Mode C).
- Front matter: generated; about 400–700 words including the latest update's scorecard.
- **Closing audit**: no thesis-carrying number or claim more than twice in the prose (tables and tokens excepted); every number sourced or tagged; `build_report.py --check` clean.

## 9. Checklist before building

- [ ] Opening has a dated moment, a stock-vs-business contrast and a chart
- [ ] The key debate has management's case quoted and attributed, then numbered holes
- [ ] One illustrative unit-economics table, with estimates labelled
- [ ] Rings of profit
- [ ] Management: prior record, deal list, capital-allocation table, incentive table with a ROIC row
- [ ] Valuation: `::model_build`, `::scenarios`, Priced-in and Hurdle paragraphs, PW return and entry, EPV floor
- [ ] Final Words names the three tests and dates
- [ ] Appendix has the five-year record with ROIC, ROIIC and owner earnings, plus the risks and catalysts tables
- [ ] Sources section, `--check` clean, one read of the Markdown and each chart SVG
