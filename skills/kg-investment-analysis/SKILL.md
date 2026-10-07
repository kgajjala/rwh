---
name: kg-investment-analysis
description: >
  Karthik's single-equity investment framework for 5–10-year holders. Turns a ticker into a
  decision (Initiate / Add / Hold / Trim / Exit / Watch / Avoid), tested against a fixed 13%
  annual hurdle on a probability-weighted five-year value. The value is built from unit
  economics, ROIC, owner earnings and a moat read. Use this skill whenever the user asks:
  "analyze [ticker]", "give me your take on [company]", "is [stock] a buy", "should I
  buy/hold/sell [ticker]", "what is [company] worth", "bull/bear case for [ticker]", "deep dive
  on [company]", "walk me through [ticker]", "what's the BAIT on [stock]", "summarize the
  earnings call for [company]", "what happened to [stock]", "price history / price action for
  [ticker]". Also use it for any request for financial, strategic, valuation or price analysis
  of a named public company, even when the word "analysis" is never used; over-triggering
  beats missing. Covers one equity at a time; peers appear only as context. Mode A writes the
  full decision report, B handles an earnings update, C news and price moves, D price history.
  It never sizes positions.
---

# kg-investment-analysis · v6.0

Every report answers one question: **what should someone do about this stock, and what would change that answer?** Each part of the report either supports that decision or is left out.

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

## Classify the request

| Request | Mode |
|---|---|
| "Analyze / deep dive / is X a buy / what is X worth" | **A**: full decision report |
| "Summarize earnings / what did X report" | **B**: earnings update |
| "What happened today / this week / why did X move" | **C**: news and price action |
| "Price history / what drove X" | **D**: price history |

---

## Mode A: the decision report

### Work order

The order matters. Grading the business before valuing it keeps the price from coloring the judgment.

1. **Gather** the sources listed under *Research protocol* below.
2. **Build the economics (§1).** Read `references/business-quality.md` and build:
   - the driver tree from the unit of value;
   - invested capital, ROIC and 3-year ROIIC;
   - the reinvestment rate;
   - **owner earnings**;
   - the quality and earnings-quality rows;
   - the **cyclical flag** and **cycle position**.
3. **Commit the grades before you value anything.**
   - Write these down, each one from its own evidence and with an outside view where one exists:
     - the §1 quality read;
     - the §3 moat rating and trend;
     - the §4 management grades;
     - the **competence** call;
     - the lifecycle **stage**.
   - Don't revise them after seeing the return unless new evidence arrives.
   - Why: one strong impression, usually the price or the story, otherwise bleeds into every other judgment. This is the mediating-assessments protocol from Kahneman, Lovallo and Sibony.
4. **Run a premortem.** Assume it is five years from now and the stock returned nothing; write down why. The top answers become the Bear's mechanism and the candidates for the three tests. People find more failure reasons by imagining a failure that already happened (Klein) than by asking what might go wrong.
5. **Value it (§5).** Read `references/valuation.md` and work through it in this order:
   1. Pick the method that fits the situation.
   2. Build the scenarios and sort them with the 3P test.
   3. Apply the floors and the special cases.
   4. Fill the return-math table.
6. **Decide.** Set the verbs, zones and flags using the *Decision rules* below.
7. **Write the three tests as kill criteria**, each with its consequence fixed now (see `references/moat-management-edge.md`).
8. **Run the bias check** if a previous report or page gave a different verb. List what changed and run the five questions in `references/moat-management-edge.md` before writing the new verb.
9. **Write the report** in Markdown from `assets/report-template.md`, then run the closing audit (*Writing rules*).

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
  - **What to show:** flag it in the header and print `—` in the Trim cell.
  - **Why:** businesses that keep earning 20%+ on new capital tend to outrun the estimates that made them look fully priced. Selling them on valuation is the costliest common mistake (Fundsmith, Akre and the 100-bagger studies).
- **Re-rating test.** If more than half of the PW return comes from re-rating, the non-holder verb is Watch, not Initiate. The compounding rate at a flat multiple is what a long-term holder actually earns.
- **Probability-fragile.** If the break-even Bear odds are within 10 points of the Bear odds you assigned, The Call says the verb is fragile and names the test that will settle it.
- **Competence: Core / Edge / Outside.**
  - **Outside** applies when the outcome turns on knowledge we lack, such as a clinical readout, frontier engineering, regulatory science or protocol economics. It **widens the scenarios**:
    - Bull and Bear each get at least 25%, and Base at most 50%;
    - the Bear includes the binary failure outcome where one exists;
    - §5 carries a one-line confidence note naming what we cannot judge.
  - **Edge** gets the confidence note only.
- **Cyclical: Yes / No.** For a Yes, every terminal value uses the **normalized (through-cycle) margin**, never the current one (`references/valuation.md`).

### Report structure

Reports are Markdown. Use `assets/report-template.md`. The front matter *is* the deliverable; the numbered sections exist to support it.

**Header** (a three-line blockquote under the `# TICKER — Company` title)
- Line 1: schema version, updated date, status.
- Line 2: price with its timestamp and source link · 52-week range · percentile · % from the high.
- Line 3: asset type · lifecycle stage · **Cyclical** Y/N · **Competence** Core/Edge/Outside · 🔁 compounder (only if it qualifies).

**Verdict**
- One sentence that carries the whole call.
- 🟢/🟡/🔴 **Non-holder: verb** · **Holder: verb**.
- A one-row table: `PW EV | PW return/yr (≥/<13%) | Compounding/yr | R/R | Entry | Trim | Avoid | primary multiple | Yield | BAIT | Moat | Next`.
- **Breaks if:** the single most load-bearing fact.

**The Call** (~200 words). What the market has priced (the price-implied Bear odds, in one number), what it has wrong, and the one number that proves it. This is the only place the argument is made; §1–§8 supply evidence and don't re-argue. Say "probability-fragile" here when the rule applies.

**What I'd Have To Be Wrong About.** Exactly three kill criteria: state, source, date, **If Fail →** a pre-committed consequence.

| § | Contents |
|---|---|
| 1. Business & Numbers | Lead with what changed. Then: the driver tree (unit, count, revenue per unit, contribution per unit, growth from units vs. per unit); a five-year table with the ROIC, ROIIC, reinvestment, **owner earnings**, quality and **earnings-quality** rows; cycle position; recent quarters; segments and geography. |
| 2. Growth Levers | One table over the fixed lever list (market growth · share gain · price and mix · attach / new products · new geographies · M&A · margin · share count). For each lever: contribution now, runway, evidence, management intent and stage. Then say which levers carry the Base and which carry the Bull, and which are optionality. |
| 3. Moat, Customer & Competition | A four-row moat table (Mechanism in 7 Powers terms · Trend with the number that decides it · Profit pool · Customer) and the rating in one sentence. Add the scale-economies-shared line where Scale is a Power. Then a competitor table, scuttlebutt findings, industry structure and TAM. |
| 4. Management & Capital | Incentives (proxy metrics and weights) · guidance grade · promises ledger (3 rows) · CEO/CFO read · capital-allocation record with the **$1 retention test** and the Outsider grade · appearances, each attributed to its venue (or a line saying there were none). |
| 5. Scenarios → PW EV | Multiples and peers as the anchor · EPV floor · one scenario table (target, probability, contribution, driving assumption, 3P tier) · the return-math table in the fixed row order from `references/valuation.md`. |
| 6. Risks & Triggers | One table: `Risk \| Impact \| Prob \| Priced in? \| Would break the thesis if…`, filtered for materiality. Name any reflexive loop or ruin path here. |
| 7. Catalysts & Sentiment | Analysts and short interest in one line each · 90 days of insiders from Form 4 XML · dated catalysts · BAIT justification only where it isn't obvious. None of it moves a verb. |
| 8. Sources | Links to every document used. |

### Research protocol

Pull these for Mode A. Log gaps; never fabricate a number.

1. **Multi-year numbers:** the SEC XBRL company-facts API.
   - Command: `curl -A "Name email@domain" https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` (CIK zero-padded to 10 digits; `www.sec.gov` blocks requests without a User-Agent).
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
8. **Market data:**
   - analyst consensus and recent rating or target changes;
   - short interest and its month-over-month change (Fintel, NASDAQ, StockAnalysis);
   - 90 days of Form 4 filings, read from the XML (codes: P = open-market buy, S = sale, A = award);
   - the 10-year Treasury yield (FRED `DGS10`).

### Writing rules

- **State each fact once.** It lives in one section; elsewhere it gets a one-clause reference, not a re-explanation.
- **Synthesis, not transcription.** Use a quote only where paraphrase would weaken it, and attribute it to its venue.
- **Budget: about 1,500 words of prose,** excluding tables and source lists. Overshooting by 10–15% to keep load-bearing evidence is fine. When a draft runs long, compress first (turn bullets into a table, collapse a restated claim into a reference); cut only the least load-bearing item.
- **Emoji carry meaning:** 🟢 bullish/add · 🔴 bearish/exit · 🟡 neutral/hold · ⚠️ material risk · ✅ resolved · 📅 dated catalyst · 💰 capital allocation · 🎯 price zone · 🔁 high-ROIIC compounder.
- **Bold only punchlines** and thesis-carrying numbers.
- **Tables run time in columns, metrics in rows.**
- **Closing audit:** any thesis-carrying figure, rate, multiple or named risk that appears more than twice gets collapsed to a reference. Then check that every number has a source or a tag.

---

## Mode B: earnings update

1. Run Step 0, then fetch the release, the 10-Q and two transcripts. Don't summarize from snippets.
2. Report:
   - headline numbers against consensus and against last year;
   - segments;
   - guidance changes and why;
   - the three to five points management emphasized;
   - notable Q&A pushback and non-answers.
3. **Score the three kill criteria** as ✅ Pass, 🔴 Fail or 🟡 Pending, each with the number that decided it.
   - Apply each pre-committed consequence exactly as written.
   - Overriding a consequence requires evidence that did not exist when the test was written; name that evidence.
   - Then write a replacement test.
4. Refresh §1 (the new quarter, trailing twelve months, owner earnings) and the §5 return math at the current price. Then:
   - re-derive the verbs and zones;
   - run the bias check before changing a verb;
   - output the updated report.

## Mode C: news and price action

- Give three to five bullets on what drove the move, classed as earnings, macro, sector or company-specific, and say whether the move looks warranted or an overreaction.
- Re-run the return math at the new price, because zones can be crossed without any news.
- If the move touches a kill criterion, say which one.
- No verb changes without the bias check.

## Mode D: price history

Run Step 0, then:
- a one-year phase table: `Phase | Period | Move | % | Tag | What happened`, with tags `INT-FUND`, `INT-PEOPLE`, `INT-STRAT`, `EXT-MACRO`, `EXT-MARKET` and `EXT-SECTOR`;
- one paragraph of five-year context against the S&P 500;
- where the price sits against the current zones, if a report exists.

Technical levels are context only. Answer in chat, or as a short Markdown note if the user wants a file; don't rewrite the report.

---

## Output

- **Format: Markdown.** Copy `assets/report-template.md` and fill it in. Use GitHub-flavored Markdown tables; no HTML.
- **Where it goes:**
  - In a research repo that keeps one page per ticker under `wiki/tickers/` (like the one this skill ships in), the report *is* `wiki/tickers/[TICKER]/[TICKER].md`. Update it in place, so it always shows the current call; git holds the history. If the folder also has a `changelog.md`, follow that repo's rules for logging the update.
  - Anywhere else, save `outputs/[TICKER]_analysis_[YYYY-MM-DD].md` in the working directory. In Cowork, save to `/mnt/user-data/outputs/` and call `present_files`.
- **Modes B and C** update the existing report in place: the sections that moved, plus the Verdict.
- **Links** to local files are relative to the report's own location.
- Show the user the file, or the diff when you updated one.
- End with the template's disclaimer line: this is analysis, not personal investment advice.

## Reference files

Read each one when you reach the step that needs it.

- `references/business-quality.md`: for **§1–§2**. Unit-of-value table by asset type, invested capital, ROIC/ROIIC, owner earnings and maintenance capex, quality rows, earnings-quality screens (accruals, Beneish, Piotroski, Altman), the cyclical flag and cycle position, lifecycle stages, the growth-lever table.
- `references/valuation.md`: for **§5 and the Verdict**. Method by situation, scenario construction and the 3P sort, discount rates, the terminal-growth check, the EPV floor, normalized margins for cyclicals, justified P/TBV for financials, sales-to-capital and the reflexive Bear, ruin paths and failure odds, sum of the parts, break-even and price-implied Bear odds, base-rate table, return-math table, worked example.
- `references/moat-management-edge.md`: for **§3, §4, §6, §7 and the tests**. 7 Powers and moat trend, the scale-economies-shared test, the customer block, the big-market check, incentives and guidance grade, the promises ledger, Outsider grades, the $1 retention test, BAIT, kill criteria and the premortem, the bias check, the risk materiality filter.

## Version history

- **v6.0 (October 2026).** Rebuilt as a decision report with a 5-year lens.
  - Added: the 13% fixed hurdle; hurdle-derived entry; owner earnings; ROIC/ROIIC; EPV floor; normalized margins for cyclicals; justified P/TBV; reflexive Bear; earnings-quality row; $1 retention test; break-even and price-implied Bear odds; 3P sort; kill criteria; mediating-assessment order; scuttlebutt; bias check; high-ROIIC compounder flag (no Trim zone); competence widening.
  - Removed: allocation %, the stock/options split, 1- and 3-year targets, and the technical verdict as a decision input.
  - Output: a Markdown report in the one-page-per-ticker shape replaces the styled HTML file.
- v5.3 (April 2026). 15-section thesis with multiples-based valuation; superseded.
