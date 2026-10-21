---
name: kg-investment-analysis
description: >
  Karthik's single-equity investment framework for 5–10-year holders. Writes a long-form deep dive in the MBI Deep Dives style (history, the key debate argued from management's own words, unit economics, management and incentives, a segment model with priced-in and hurdle cases) that ends in a decision (Initiate / Add / Hold / Trim / Exit / Watch / Avoid) tested against a fixed 13% hurdle on a probability-weighted five-year value. Use whenever the user asks "analyze [ticker]", "is [stock] a buy", "should I buy/hold/sell [ticker]", "what is [company] worth", "deep dive on [company]", "update [ticker]", "summarize the earnings call for [company]", "what happened to [stock]" or "price history for [ticker]", or for any valuation or price analysis of a named public company. Mode A writes the deep dive; B and C update it in place; D is price history. Writes one Markdown report with SVG charts. Never sizes positions.
---

# kg-investment-analysis · v7.0

Every report answers one question: **what should someone do about this stock, and what would change that answer?** In v7 the answer is told as a long-form deep dive. It is an argued essay that starts from the company's history, works through the debate that decides the stock using management's own words and the numbers, and ends in a verdict. **The output is one Markdown file, `[TICKER].md`, as in v6.0.** The decision front matter comes first (header, Verdict, The Call, the three tests, the latest update), then the deep dive and its appendix. All of it is generated from one set of sources, so the verdict, zones and tests never drift from the essay.

## The lens: why the rules exist

- **The reader holds for 5–10 years and wants the business to compound at a teens rate.**
  - **The hurdle is fixed at 13% a year** total return on the probability-weighted case. It is not tied to interest rates; the 10-year Treasury yield is shown only as context.
  - **Re-rating is upside, never the thesis.** Momentum, sentiment, analyst targets and technicals are context, never the reason for a verb.
- **Analyze the company, not anyone's portfolio.** Give a verb for someone who doesn't own the stock and one for someone who does.
- **No position sizing of any kind.** That means no allocation %, no tranches, no position %, and no stock/options split. Sizing depends on a portfolio the analysis cannot see. If asked, say the framework doesn't size, and give the price zones instead.
- **Every number traces to a primary source or carries a tag:** `[Estimate]`, `[Analyst consensus]`, `[Management guidance]` or `[Derived]`.
  - Every source is a Markdown link to the specific document (relative path for a local file, absolute URL otherwise). If a source can't be resolved, write `[link pending]`.
  - Primary means SEC filings, company releases, IR pages and transcripts. Search snippets are leads, not sources; click through.
- **Dates come from the clock:** run `date -u +%Y-%m-%d` before writing anything dated, and never infer today's date from context.

## Step 0: date and live price (always first)

1. Run `date -u +%Y-%m-%d`.
2. Fetch the live price from `https://finance.yahoo.com/quote/[TICKER]/`, and cross-check it on `https://stockanalysis.com/stocks/[ticker]/statistics/` (or CNBC, Google Finance or MarketWatch).
   - Record the price with its timestamp, the 52-week range, market cap, EV, net debt and the forward dividend.
   - If Yahoo looks stale (a banner, or data more than 3 days old), say so and use the cross-check.
3. Re-verify the price before computing any multiple if much time has passed since step 2.

## What a report is (v7)

A report is a folder of source files that builds into one Markdown file:

| File | What it holds | Who writes it |
|---|---|---|
| `report.md` | The essay in Markdown, with directives (`::table`, `::chart`, `::model_build`, `::scenarios`, `::tests`, `::updates`, `::toc`, `::sources`, `::disclaimer`) and `[[tokens]]` for model numbers | You |
| `data.json` | `meta` (ticker, price, dates, type, stage, flags, accent, artifact URL), `verdict`, `call`, `tests` (with `shift` so consequences compute), `updates` (with scorecards), `tables`, `charts`, `sources`, `vars` | You |
| `model.json` | Segment model: base year (with SBC % and owner-earnings conversion), cases (role, probability, growth and terminal margin per segment, dilution and buybacks, exit multiple and its basis, story, 3P tier), optionality lines, risk-free rate, diagnostics (Priced-in, Hurdle) | You |
| `updates/YYYY-MM-DD.md` | Dated update notes (Modes B and C) | You |
| `series/*.json` | Total-return series for line charts | `scripts/prices.py` |
| `model_out.json` | Cases, PW EV, return, entry, R/R, Bear odds, solved diagnostics | `scripts/model.py` |
| `../TICKER.md` | **The report**: decision front matter, then the deep dive and appendix, in GitHub-flavored Markdown with no HTML | `scripts/build_report.py` |
| `charts/*.svg` | Static chart images referenced from the report (legend, end labels, a data table follows each) | `scripts/build_report.py` |
| `TICKER-deep-dive.html` | Optional interactive page, built only with `--html`, for publishing | `scripts/build_report.py --html` |

A complete worked example lives in `examples/SBUX/report/`; copy its shape. `assets/skeleton/` has empty starting files.

### Pipeline

Run the scripts with `python3 -I` (standard library only), from the report folder:

```
python3 -I SKILL_DIR/scripts/prices.py series/NAME.json TICK,RIVAL,SPY --start YYYY-MM-DD --interval 1mo --names "TICK=Company,SPY=S&P 500"
python3 -I SKILL_DIR/scripts/model.py model.json
python3 -I SKILL_DIR/scripts/build_report.py . --check
python3 -I SKILL_DIR/scripts/build_report.py .
```

`--check` lists unresolved tokens and missing tables, charts or update files; fix everything it reports. Then read the rendered Markdown once (a preview, or the file), and look at each chart SVG. Fix what you see.

---

## Classify the request

| Request | Mode |
|---|---|
| "Analyze / deep dive / is X a buy / what is X worth", or no report exists yet | **A**: full deep dive |
| "Summarize earnings / what did X report / update X" after a print or material event | **B**: incremental update |
| "What happened today / this week / why did X move" | **C**: news and price update |
| "Price history / what drove X" | **D**: price history |

---

## Mode A: the full deep dive

### Work order

The order matters. Grading the business before valuing it keeps the price from coloring the judgment.

1. **Gather** the sources listed under *Research protocol* below.
2. **Build the economics** (the Appendix tables and the Business Overview). Read `references/business-quality.md` and build:
   - the driver tree from the unit of value;
   - invested capital, ROIC and 3-year ROIIC;
   - the reinvestment rate;
   - **owner earnings**;
   - the quality and earnings-quality rows;
   - the **dilution** rows (diluted shares, net share change, SBC ÷ owner earnings, buybacks against SBC);
   - the **cyclical flag** and **cycle position**.
3. **Commit the grades before you value anything.**
   - Write these down, each one from its own evidence and with an outside view where one exists:
     - the quality read;
     - the moat rating and trend;
     - the management grades;
     - the **competence** call;
     - the lifecycle **stage**.
   - Don't revise them after seeing the return unless new evidence arrives.
   - Why: one strong impression, usually the price or the story, otherwise bleeds into every other judgment. This is the mediating-assessments protocol from Kahneman, Lovallo and Sibony.
4. **Run a premortem.** Assume it is five years from now and the stock returned nothing; write down why. The top answers become the Bear's mechanism and the candidates for the three tests. People find more failure reasons by imagining a failure that already happened (Klein) than by asking what might go wrong.
5. **Value it.** Read `references/valuation.md` and work through it in this order:
   1. Pick the method that fits the situation.
   2. Build the scenarios and sort them with the 3P test.
   3. Apply the floors and the special cases.
   4. Fill the return-math table.
6. **Decide.** Set the verbs, zones and flags using the *Decision rules* below.
7. **Write the three tests as kill criteria**, each with its consequence fixed now (see `references/moat-management-edge.md`).
8. **Run the bias check** if a previous report or page gave a different verb. List what changed and run the five questions in `references/moat-management-edge.md` before writing the new verb.
9. **Write the deep dive** as `report.md` + `data.json` + `model.json` in the report folder, following `references/deep-dive-style.md`. Run the pipeline below, then the closing audit (*Writing rules*).

10. **Write in the deep-dive style.** Chapter structure, devices, voice, charts and length are in `references/deep-dive-style.md`; the framework's required content and where it goes are in its section 4. In short:
    - an opening built on a dated moment and a stock-vs-business chart;
    - Business Overview with a segment table and a profit-mix chart;
    - the key debate (management's case quoted, then the holes, then an illustrative unit-economics table, then rings of profit);
    - the second debate;
    - Management, Capital Allocation and Incentives (prior record, deal list, capital-allocation table, incentive table);
    - Valuation (model build, scenarios, Priced-in and Hurdle);
    - Final Words;
    - Appendix: The Numbers (five-year record with ROIC, ROIIC and owner earnings, levers, moat, risks, catalysts);
    - Sources.

### Decision rules

The definitions behind each line are in `references/valuation.md`.

- **PW EV** = Σ (probability × 5-year target), plus any optionality lines valued as probability × value.
- **PW return/yr** = (PW EV ÷ spot)^(1/5) − 1 + dividend yield. **Initiate requires ≥ 13%.**
- **Entry** = PW EV ÷ (1 + 0.13 − yield)^5. This is the price at which the PW case returns exactly the hurdle.
- **Zones and verbs:**

| Price zone | Non-holder | Holder |
|---|---|---|
| At or below Entry | Initiate | Add |
| Entry → PW EV | Watch | Hold |
| PW EV → Bull | Watch | Trim |
| At or above Bull | Avoid | Trim |
| A kill criterion fails with a pre-committed exit | Avoid | Exit |

- **🔁 High-ROIIC compounder: no Trim zone.**
  - **Criteria (all must hold):**
    - ROIC ≥ 20% in at least 4 of the last 5 years;
    - 3-year ROIIC ≥ 20%;
    - a reinvestment rate ≥ 25% of NOPAT;
    - at least one growth lever with ≥ 5 years of runway at stage proven or scaling.
  - **What changes:** the holder verb is Add at or below Entry and Hold everywhere above it. The holder exits only when a kill criterion fails, never on valuation alone. The non-holder zones are unchanged: don't buy above Bull.
  - **What to show:** set `meta.compounder: true`; the report header flags it and prints `—` in the Trim cell.
  - **Why:** businesses that keep earning 20%+ on new capital tend to outrun the estimates that made them look fully priced. Selling them on valuation is the costliest common mistake (Fundsmith, Akre and the 100-bagger studies).
- **Re-rating test.** If more than half of the PW return comes from re-rating, the non-holder verb is Watch, not Initiate. The compounding rate at a flat multiple is what a long-term holder actually earns.
- **Probability-fragile.** If the break-even Bear odds are within 10 points of the Bear odds you assigned, The Call says the verb is fragile and names the test that will settle it.
- **Competence: Core / Edge / Outside.**
  - **Outside** applies when the outcome turns on knowledge we lack, such as a clinical readout, frontier engineering, regulatory science or protocol economics. It **widens the scenarios**:
    - Bull and Bear each get at least 25%, and Base at most 50%;
    - the Bear includes the binary failure outcome where one exists;
    - the Valuation chapter carries a one-line confidence note naming what we cannot judge.
  - **Edge** gets the confidence note only.
- **Cyclical: Yes / No.** For a Yes, every terminal value uses the **normalized (through-cycle) margin**, never the current one (`references/valuation.md`).

### Report structure

The essay's structure is set by `references/deep-dive-style.md`. The front matter at the top of `[TICKER].md` is generated, so its shape is fixed by the build script:

- **Header**: schema, updated date, status; price with timestamp and source, 52-week range, percentile, distance from the high; type, stage, Cyclical, Competence, 🔁 if it qualifies; a link to the deep dive.
- **Verdict**: one sentence, the two verbs, the one-row table (`PW EV | PW return/yr | Compounding/yr | R/R | Entry | Trim | Avoid | multiple | Yield | BAIT | Moat | Next`), **Breaks if**.
- **The Call** (~200 words, from `data.json` `call`). What the market has priced, what it has wrong, the one number that proves it; say "probability-fragile" when the rule applies.
- **What I'd Have To Be Wrong About**: exactly three kill criteria, each with source, date and a pre-committed consequence (give the test a `shift` so its PW EV, return and entry are computed).
- **Latest update** with its scorecard, then a rule and **Deep Dive: [title]** with the essay, Appendix and Sources (chapters one heading level down).

### Research protocol

Pull these for Mode A. Log gaps; never fabricate a number.

1. **Multi-year numbers:** the SEC XBRL company-facts API, via `scripts/xbrl.py CIK out.json "Name email"` (or `curl -A "Name email@domain" https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`; `www.sec.gov` blocks requests without a User-Agent).
   - Pull 10 years of revenue, operating income, net income, operating cash flow, SBC, capex, D&A, dividends, buybacks, receivables, current assets and liabilities, PP&E, total assets, debt, cash, leases and equity.
   - Prefer annual `frame` values (`CY2025`, `CY2025Q4I`).
2. **Latest 10-K:**
   - Item 1 (business, segments, unit of value).
   - Item 1A (risk factors; flag ones that are new versus last year).
   - Item 7 (MD&A: volume versus price/mix, segment drivers).
   - Item 7A (quantified sensitivities).
   - Item 8 notes (segments, debt maturities, leases).
3. **Latest earnings:**
   - The release and the 10-Q.
   - The transcript, cross-checked against a second source. Secondary transcripts drop pricing and product detail.
4. **DEF 14A:** CEO incentive metrics and weights from the CD&A, board composition and insider ownership.
5. **Letters and investor days:** about 5 years of shareholder letters, plus the latest investor-day targets for the promises ledger.
6. **Appearances sweep:**
   1. the IR events page (it also shows upcoming appearances);
   2. the CEO/CFO media hit on earnings day;
   3. podcasts and non-financial shows;
   4. conference transcripts.

   Fetch the substance, not the headline. If there were none, say so.
7. **Scuttlebutt.** This is where informational edge comes from (Fisher).
   - Competitors' latest results and transcripts: what they say about this company and the category.
   - Suppliers' and customers' 10-K disclosures of 10%-of-revenue customers.
   - Public pricing pages, captured with a date.
   - Third-party app, web or hiring data is allowed only with a tag.
8. **Price history** for the charts: `scripts/prices.py` (total return, dividend-adjusted) for the company, its closest rival and the S&P 500 over the window the opening argues about, plus any prior-tenure window.
9. **Market data:**
   - analyst consensus and recent rating or target changes;
   - short interest and its month-over-month change (Fintel, NASDAQ, StockAnalysis);
   - 90 days of Form 4 filings, read from the XML (codes: P = open-market buy, S = sale, A = award);
   - the 10-year Treasury yield (FRED `DGS10`).

### Writing rules

- **State each fact once.** It lives in one chapter; elsewhere it gets a one-clause reference. Model numbers go through `[[tokens]]` so the essay, tables and front matter agree.
- **Quote management where its own words carry the argument**, at length if needed, always attributed to person, venue and date. Paraphrase everything else.
- **Budget**: about 4,000–7,000 words of prose for a full deep dive, excluding tables, quotes and the Appendix; 600–1,200 words for a Mode B note; 200–500 for Mode C. The budget guards against sprawl, not against evidence.
- **Tables run time in columns, metrics in rows**; every table and chart has a sourced note.
- **Emoji** stay out of the essay; they appear only in the generated front matter, with their usual meanings (🟢 🔴 🟡 ⚠️ ✅ 📅 💰 🎯 🔁).
- **No HTML** anywhere in the sources; the build emits plain GitHub-flavored Markdown.
- **Closing audit**: no thesis-carrying figure, rate, multiple or named risk more than twice in the prose; every number sourced or tagged; `--check` clean.

---

## Mode B: incremental update (earnings or a material event)

1. Run Step 0, then fetch the release, the 10-Q (or 8-K) and two transcripts. Don't summarize from snippets.
2. **Score the three kill criteria** as `pass`, `fail` or `pending`, each with the number that decided it. Record them as the update's `scorecard` in `data.json`.
   - Apply each pre-committed consequence exactly as written.
   - Overriding a consequence requires evidence that did not exist when the test was written; name that evidence.
   - Write a replacement for each resolved test.
3. **Write the update note** `updates/YYYY-MM-DD.md` (600–1,200 words) in the deep-dive voice. Cover:
   - the numbers against consensus and last year;
   - segments;
   - guidance and why it changed;
   - management's three to five points, quoted where it matters;
   - Q&A pushback and non-answers;
   - what it does to the debate;
   - the verdict.
4. **Refresh the data**:
   - add the new quarter to the tables and roll the Appendix's five-year record when a fiscal year closes;
   - re-base `model.json` (spot, base year when a year closes, case inputs only where evidence moved them) and re-run `model.py`;
   - update `meta`, `verdict` and `call`.
5. **Edit body prose that the news made false**, in place. The essay must stay true on its own.
6. Re-derive verbs and zones; run the bias check before changing a verb. Rebuild with `--check` and read the result once.

## Mode C: news and price update

- Write a 200–500-word update note covering what drove the move (earnings, macro, sector or company-specific) and whether the move looks warranted.
- Set the new spot in `model.json` and re-run the model, because zones can be crossed without news. Say if a kill criterion is touched.
- Refresh `meta` and anything the news made false. No verb change without the bias check. Rebuild.

## Mode D: price history

Run Step 0, then:
- a one-year phase table: `Phase | Period | Move | % | Tag | What happened`, with tags `INT-FUND`, `INT-PEOPLE`, `INT-STRAT`, `EXT-MACRO`, `EXT-MARKET` and `EXT-SECTOR`;
- one paragraph of five-year context against the S&P 500 (a `prices.py` series helps);
- where the price sits against the current zones, if a report exists.

Answer in chat or as a short note; don't rebuild the deep dive.

---

## Output

- **Where it goes:**
  - **Format: Markdown.** The report is `[TICKER].md`; charts are SVG files beside it in `report/charts/`, linked as images. No HTML.
  - In a research repo with one folder per ticker under `wiki/tickers/` (like the one this skill ships in), the sources live in `wiki/tickers/[TICKER]/report/` and the report is `wiki/tickers/[TICKER]/[TICKER].md`. Follow the repo's rules for the changelog and its cross-files.
  - Anywhere else: `outputs/[TICKER]/report/` with the report at `outputs/[TICKER]/[TICKER].md`. In Cowork, use `/mnt/user-data/outputs/` and call `present_files`.
- **Sharing (optional):** to share a page, publish `[TICKER].md` as an Artifact with its `report/charts/*.svg` as supporting files, or build the interactive page with `--html` and publish that. Store the URL in `meta.artifact_url` so the header links it.
- Links inside the essay are absolute URLs. Local `raw/` files are cited in the changelog.
- Show the user the page or the diff, and end with the disclaimer: this is analysis, not personal investment advice.

## Reference files

Read each one when you reach the step that needs it.

- `references/deep-dive-style.md`: **for every report and update.** Chapter structure, recurring devices, where each framework item goes, voice, charts, update notes, length, checklist.
- `references/business-quality.md`: unit-of-value table by asset type, invested capital, ROIC/ROIIC, owner earnings and maintenance capex, quality and earnings-quality rows, cyclical flag, lifecycle stages, growth levers.
- `references/valuation.md`: method by situation, scenarios and the 3P sort, discount rates, terminal-growth check, EPV floor, normalized margins, justified P/TBV, reflexive Bear, ruin paths, sum of the parts, break-even and price-implied Bear odds, the Priced-in and Hurdle diagnostics, base rates, the return-math table.
- `references/moat-management-edge.md`: 7 Powers and moat trend, scale economies shared, customer block, incentives and guidance grade, promises ledger, Outsider grades, the $1 retention test, BAIT, kill criteria and the premortem, the bias check, the risk materiality filter.

## Version history

- **v7.0 (October 2026).** The deep dive becomes the report.
  - Long-form essay in the MBI Deep Dives style, built from `report.md` + `data.json` + `model.json` into one Markdown report (decision front matter + essay + appendix) with SVG charts; an optional interactive HTML page via `--html`.
  - New scripts: `model.py` (cases, PW maths, solved Priced-in and Hurdle diagnostics), `build_report.py`, `prices.py`, `xbrl.py`.
  - Kill-criteria consequences computed from the model; incremental updates as dated notes with scorecards plus in-place edits; worked SBUX example.
  - The decision rules and the 13% hurdle are unchanged from v6.0.
- v6.0 (October 2026). A one-page Markdown decision report with a 5-year lens, owner earnings, EPV floor, kill criteria and Bear odds; superseded as the output format, rules retained.
- v5.3 (April 2026). 15-section thesis with multiples-based valuation; superseded.
