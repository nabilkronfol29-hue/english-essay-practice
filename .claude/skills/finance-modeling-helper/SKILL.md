---
name: finance-modeling-helper
description: Use this skill for corporate finance and accounting coursework or case studies -- reading financial statements (income statement, balance sheet, cash flow statement), ratio analysis (liquidity, profitability, leverage, efficiency, DuPont), time value of money, NPV/IRR/payback/WACC, capital budgeting decisions, and company valuation (DCF, comparable companies). Trigger on terms like "balance sheet," "EBITDA," "DCF," "WACC," "NPV," "IRR," "comps," "cost of capital," "cap budgeting," or when the user pastes financial-statement numbers and asks to analyze, value, or compare them.
---

# Finance Modeling Helper

Helps with corporate finance and accounting coursework: analyzing statements, running the standard capital-budgeting and valuation math, and explaining what the numbers mean.

## 1. Clarify the actual question

Before computing anything, pin down what decision is being made: "is this project worth doing," "is this company healthy," "what's this company worth," "which financing option is cheaper." The right tool follows from the question — don't run every calculation available just because the inputs are present.

## 2. Do the arithmetic with the bundled script, not by hand

`scripts/finance_calcs.py` covers time value of money, NPV/IRR/payback, WACC, and ratio analysis. Run it for any of these rather than computing in your head or re-deriving the formula inline — it's easy to flip a sign or miscount a period by hand, and the script keeps compounding/discounting conventions consistent across an entire problem set.

```
python3 scripts/finance_calcs.py fv --rate 0.07 --nper 10 --pv 1000
python3 scripts/finance_calcs.py pv --rate 0.05 --nper 5 --fv 10000
python3 scripts/finance_calcs.py npv --rate=0.1 --cashflows=-5000,1500,1800,2200,2500,2700
python3 scripts/finance_calcs.py irr --cashflows=-5000,1500,1800,2200,2500,2700
python3 scripts/finance_calcs.py payback --cashflows=-5000,1500,1800,2200,2500,2700
python3 scripts/finance_calcs.py wacc --equity 6000 --debt 4000 --cost-equity 0.12 --cost-debt 0.06 --tax-rate 0.25
python3 scripts/finance_calcs.py ratios --json '{"current_assets": 500, "current_liabilities": 250, "total_debt": 300, "total_equity": 700, ...}'
```

Notes:
- `fv`/`pv` use plain magnitudes (no Excel-style sign flipping) — if you put $1,000 in today, you get a positive future value out.
- `npv`/`irr`/`payback` take a `--cashflows` series where t=0 is first and signs matter (outflow negative, inflow positive). If the first value is negative, use the `=` form (`--cashflows=-5000,...`) since a bare `-5000` after a space gets misread as a flag by argparse.
- `ratios` accepts a JSON object of statement line items and silently skips any ratio it doesn't have inputs for — pass whatever you have, see `references/ratios.md` for the full set of recognized keys and what each ratio measures.

After running it, explain the result in plain language and state any assumption that mattered (discount rate, terminal growth rate, tax rate) — the number alone doesn't answer the question.

## 3. Reading financial statements

Tie the three statements together rather than treating them as independent: net income flows from the income statement into retained earnings on the balance sheet and into the top of the cash flow statement; the change in cash on the balance sheet should match the cash flow statement's ending balance. When given raw statements, a common-size analysis (every line as a % of revenue for the income statement, as a % of total assets for the balance sheet) is usually the fastest way to spot what's unusual before running ratios.

## 4. Ratio analysis

See `references/ratios.md` for the full catalog (liquidity, leverage, profitability, efficiency, market-value ratios) with formulas and what each one is actually measuring. Always interpret a ratio relative to something — the company's own trend over time, or an industry peer — a ratio in isolation ("current ratio is 2.0x") doesn't tell you if that's good. The DuPont identity (`ROE = Net margin × Asset turnover × Equity multiplier`) is worth reaching for whenever ROE itself is the question, since it shows *why* ROE moved (margin, efficiency, or leverage).

## 5. Valuation (DCF and comps)

See `references/valuation.md` for the step-by-step DCF process (projecting FCF, terminal value, discounting, bridging to equity value per share) and the comparable-companies approach, plus the most common mistakes (mismatching WACC with the wrong cash flow definition, terminal value silently dominating the whole valuation, comparing multiples across companies with very different growth/risk profiles).

Whenever a valuation or NPV answer depends heavily on an assumption (discount rate, growth rate, exit multiple), show how the answer changes if that input moves by a percentage point or two — a single-point estimate without a sensitivity check is usually a red flag in a real analysis and in grading rubrics alike.

## 6. Scope

This is a study/coursework tool for getting the mechanics and concepts right, not professional investment, tax, or accounting advice. If a case study's numbers look internally inconsistent (e.g., negative equity with no explanation, a balance sheet that doesn't balance), point that out rather than silently computing ratios on top of it.
