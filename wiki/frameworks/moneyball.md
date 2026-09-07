# Moneyball Framework — Probability-Weighted Scenario Scoring

Applied in §5 of every ticker page. All price targets carry explicit probabilities that sum to 100%, enabling a calculated expected value to compare directly against the current price.

---

## Core Formula

```
PW EV              = (Bull Price × Bull %) + (Base Price × Base %) + (Bear Price × Bear %) [+ optionality lines]
PW return / yr     = (PW EV ÷ Current Price)^(1/5) − 1 + dividend yield
Asymmetry (R/R)    = Bull Upside % ÷ Bear Downside %
```

A position clears the bar when **PW return/yr ≥ 13%** (CLAUDE.md R8). The entry price is the level at which the PW case returns exactly the hurdle: `Entry = PW EV ÷ (1 + 0.13 − yield)^5`. R/R is a secondary check on shape, not the anchor. The flat-multiple compounding rate and the re-rating share are reported alongside per [`compounding.md`](compounding.md).

---

## Scenario Definitions

### 🐂 Bull Case
- Everything that *could* go right, goes right — but check the growth rate against the base-rate table in `compounding.md` and say where it sits
- Key assumptions: best-case growth rate, margin expansion, multiple re-rating
- Include terminal math: `[Year] EBITDA $X × [Y]x multiple = $Z/share`
- Typical probability: 20–30%

### Base Case
- Continuation of current trajectory with no major surprise; growth should reconcile to the reinvestment math in §1 or the page says where the extra comes from
- Key assumptions: consensus or slight beat, stable multiple
- Include terminal math at the same multiple as bull (or slightly lower)
- Typical probability: 45–55%

### 🐻 Bear Case
- What has to go wrong, and what is the floor?
- Key assumptions: thesis breaks on 1–2 named risks materializing
- Include terminal math: `[Year] EBITDA $X × [Y]x multiple = $Z/share`
- Be specific — the bear case should name the mechanism, not just "macro worsens"
- Typical probability: 20–30%

### Optionality
- A segment, stake or product not in the core case gets its own line: probability × value per share. It is added to PW EV and shown separately so the core can be read without it.

---

## Template (§5)

```
| Scenario | 5-yr target | Prob. | Contribution | Driving assumption |
|---|---|---|---|---|
| 🐂 Bull  | $X | X% | $ | … |
| 📊 Base  | $Y | Y% | $ | … |
| 🐻 Bear  | $Z | Z% | $ | … |
| Optionality (if any) | $ | | $ | … |
| | | | PW EV $W | |

PW return/yr: A% (≥ / < 13%) · Compounding/yr at flat multiple: B% · Re-rating share of PW return: C%
Implied expectations: spot requires D% growth for E years at r = F%
Base rate: Bull assumes G% real growth; H% of companies this size have done it over five years
Year ten: <one sentence>
R/R: (Bull upside %) ÷ (Bear downside %) = X:1
```

---

## Asymmetry Assessment (Required)

After the table, always answer:
1. **What must be TRUE for the bear case to materialize?** Is that currently supported by data?
2. **Is the bear case already priced in?** (If stock has already fallen 30%, the bear math changes)
3. **What is the specific catalyst that resolves uncertainty?** (next earnings, FDA decision, etc.)

---

## Wiki Examples

| Ticker | Bull | Base | Bear | PW EV | PW return/yr | Asymmetry | Date |
|--------|------|------|------|-------|--------------|-----------|------|
| DKS | $330 (20%) | $215 (50%) | $100 (30%) | $204 | 11.5% (<13%) | 4.9:1 | Sep 2026 |
| PEP | $249 (22%) | $205 (50%) | $119 (28%) | $191 | 11.0% (<13%) | 6.0:1 | Sep 2026 |
| UBER | $330 (20%) | $190 (50%) | $55 (30%) | $178 | 18.6% (≥13%) | 12.2:1 | Sep 2026 |

*Table updated by LLM agent after each full thesis update.*
