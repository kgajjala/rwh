# CLAUDE.md — kg-invest-wiki Schema

This is the instruction file for the LLM agent (Claude Code or equivalent) that
maintains this wiki. Read this file at the start of every session before making
any changes to the wiki/ directory.

---

## What This Wiki Is

A personal investment knowledge base maintained by an LLM agent. It accumulates
and compounds knowledge from raw source material over time — replacing the need
to re-derive analysis from scratch on every session.

**Owner**: Karthik G  
**Started**: April 2026  
**Model**: Karpathy LLM Wiki pattern (gist: karpathy/442a6bf555914893e9891c11519de94f)

---

## Directory Layout

```
kg-invest-wiki/
├── CLAUDE.md              ← This file. Read before every session.
├── raw/                   ← Immutable source material. NEVER modify.
│   ├── transcripts/       ← Earnings call transcripts (.md or .txt)
│   ├── filings/           ← 10-Ks, 10-Qs, proxy statements
│   ├── clippings/         ← Web-clipped articles (via Obsidian Web Clipper)
│   └── analyses/          ← Prior full analyses exported from Claude sessions
├── wiki/                  ← LLM-owned. You write and maintain everything here.
│   ├── index.md           ← Master catalog. Update on every ingest.
│   ├── log.md             ← Append-only event log. Never delete entries.
│   ├── tickers/           ← One folder per company
│   │   └── [TICKER]/
│   │       ├── overview.md       ← Business description, moat, pivotal question
│   │       ├── thesis.md         ← Full investment thesis (15 sections condensed)
│   │       ├── financials.md     ← Key metrics table, updated each earnings
│   │       └── changelog.md      ← What changed and whether action is warranted
│   ├── frameworks/        ← Analytical frameworks used across all tickers
│   └── watchlist.md       ← Cross-ticker ranking, conviction, allocation
└── outputs/               ← Generated HTML reports, exported analyses
```

---

## Core Rules

1. **Never modify raw/**. It is the immutable source of truth.
2. **Always update index.md** when adding or substantially changing a wiki page.
3. **Always append to log.md** with a timestamped entry for every session action.
4. **Never delete from log.md**. It is append-only.
5. **Source data only from published sources**: SEC filings, earnings releases,
   official IR pages. Never invent or estimate financials without labeling them
   clearly as `[Estimate]` or `[Analyst consensus]`.
6. **Live price always verified first**: Before any valuation work, fetch from
   `https://finance.yahoo.com/quote/[TICKER]` — never trust search snippet prices.
7. **changelog.md is the action layer**: After every update to a thesis, write
   a changelog entry that explicitly states whether the thesis is Strengthened /
   Weakened / Unchanged, and whether action is warranted (Buy more / Trim / Hold / Watch).

---

## Investment Framework (Applied to All Tickers)

### 15-Section Analysis Structure

Every ticker's `thesis.md` follows this structure (condensed from full HTML output):

1. Why Does This Company Exist? + Pivotal Investment Question
2. Annual Financial Metrics (4–6 year trend + recent quarters)
3. Geographic Revenue Mix
4. Revenue Mix & Business Model
5. Competitive Moat (Wide / Narrow / None + sources)
6. Management & Leadership (CEO/CFO assessment + capital allocation)
7. Strategic Growth Initiatives
8. Key Risks (Impact × Probability)
9. Industry-Specific Macro Analysis
10. Valuation & Comparable Analysis
11. Position Building Strategy (stock % vs. options %, staged tranches)
12. BAIT Framework (Behavioral / Analytical / Informational / Technical)
13. Bull / Bear / Base Cases with price targets and probabilities
14. Bottom Line (1-yr + 3-yr targets, portfolio %, monitoring trigger)

### BAIT Framework (Mauboussin)

Applied in Section 12 of every full thesis. Four lenses:

- **B — Behavioral**: Is there identifiable sentiment/fear driving mispricing?
  Is the fear empirically supported by operating data, or narrative-only?
- **A — Analytical**: What is consensus missing? (buyback compounding, AI leverage,
  attach rate acceleration, hidden FCF). What does a rigorous model yield vs. price?
- **I — Informational**: Is there primary data (transcript, filing, conference)
  underappreciated because most investors rely on media summaries?
- **T — Technical**: Converging mechanical catalysts — index inclusion, short squeeze,
  buyback acceleration, options expiry, institutional flow.

**BAIT Verdict**: Triple or quadruple overlap = highest-conviction signal.

### Moneyball Probability Scoring

All scenario price targets carry explicit probabilities summing to 100%.
Example: Bull $X (30%) + Base $Y (50%) + Bear $Z (20%) = weighted EV of $W.
Use this to compute expected return vs. current price.

### Asset Type Rules

| Type | Key Metrics | Valuation Primary |
|------|-------------|-------------------|
| Capital-light platform (BKNG) | GBV, Take Rate, Room Nights | FCF yield, EV/EBITDA |
| Franchise royalty (WING) | SSS, AUV, Unit Count, Royalty Rate | EV/EBITDA |
| Financial/Brokerage (SCHW) | NII, NIM, AUM, Net New Assets | P/TBV, P/E |
| Pharma/Biotech (LLY) | Revenue by drug, pipeline milestones | P/E, EV/Sales |
| Managed Care (UNH) | MLR, membership, premium yield | P/E, P/FCF |

---

## Update Operations

### On New Earnings (Mode B)

When a new earnings transcript or press release is added to `raw/transcripts/`:

1. Read the new file
2. Extract: headline numbers vs. consensus, guidance update, management tone,
   key Q&A moments, any thesis-altering disclosures
3. Update `wiki/tickers/[TICKER]/financials.md` with the new quarter's data
4. Update `wiki/tickers/[TICKER]/thesis.md` Sections 2, 8, 13, 14 if materially changed
5. Write a new entry in `wiki/tickers/[TICKER]/changelog.md`
6. Update `wiki/watchlist.md` if conviction or allocation has changed
7. Update `wiki/index.md` with new last-updated date
8. Append to `wiki/log.md`

### On New Clipping (web article, research note)

1. Read the file in `raw/clippings/`
2. Determine which ticker(s) it affects
3. Integrate relevant data points into the appropriate `thesis.md` or `overview.md`
4. Note the source in the relevant section with a `[Source: filename, date]` tag
5. Append to `wiki/log.md`

### Weekly Lint Pass

Run this when asked to "lint the wiki" or on the weekly cron trigger:

1. Check every ticker's `financials.md` — is the data stale (>90 days since earnings)?
   Flag with `⚠️ STALE — next earnings: [date]`
2. Check `watchlist.md` — are all BAIT signals and conviction levels current?
3. Check `index.md` — are all pages listed and summaries current?
4. Append a lint summary to `log.md`

---

## changelog.md Format (Per Ticker)

```markdown
## [YYYY-MM-DD] — [Event Type: Earnings Q[X] / Price Action / New Clipping / Lint]

**Trigger**: [What caused this update]
**Data points reviewed**: [List of sources read]

### What Changed
- [Specific metric or thesis element that changed]
- [Direction and magnitude of change]

### Thesis Status
- **Overall**: Strengthened / Weakened / Unchanged
- **BAIT delta**: [Any change in B/A/I/T signals]
- **Price target delta**: Bull $X → $Y | Base $X → $Y | Bear $X → $Y

### Action
- [ ] Buy more — [rationale + suggested tranche]
- [ ] Trim — [rationale + suggested %]
- [x] Hold — [rationale]
- [ ] Watch — [specific trigger to monitor]

**Next review trigger**: [Specific event or date]
```

---

## log.md Format

Each entry starts with a fixed prefix for Unix parseability:

```
LOG [YYYY-MM-DD HH:MM] [ACTION] [SCOPE] — [description]
```

Examples:
```
LOG 2026-04-05 14:30 INGEST WING — Added Q1 2026 earnings transcript to raw/transcripts/
LOG 2026-04-05 14:35 UPDATE WING — Updated financials.md and changelog.md post Q1 earnings
LOG 2026-04-06 09:00 LINT ALL — Weekly lint pass; flagged UNH financials as stale
LOG 2026-04-06 09:05 UPDATE index.md — Refreshed last-updated dates for all tickers
```

---

## Co-Evolution Note

This schema file (`CLAUDE.md`) should be updated collaboratively over time.
When a new framework is added, a new ticker type is encountered, or a new
update operation is needed, update this file first, then apply the change.
Version history is tracked via Git — every meaningful schema change should be
committed with a descriptive message.
