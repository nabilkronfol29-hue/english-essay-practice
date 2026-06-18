# Financial Ratio Reference

Keys in brackets match the JSON keys recognized by `scripts/finance_calcs.py ratios`.

## Liquidity (can the company meet short-term obligations?)
| Ratio | Formula | Keys |
|---|---|---|
| Current ratio | current assets / current liabilities | `current_assets`, `current_liabilities` |
| Quick ratio | (current assets − inventory) / current liabilities | `current_assets`, `current_liabilities`, `inventory` |
| Cash ratio | cash / current liabilities | `cash`, `current_liabilities` |

Higher generally means more liquid, but a current ratio that's *very* high can mean the company is sitting on idle assets instead of investing them.

## Leverage / solvency (how much debt, and can it be serviced?)
| Ratio | Formula | Keys |
|---|---|---|
| Debt-to-equity | total debt / total equity | `total_debt`, `total_equity` |
| Debt-to-assets | total debt / total assets | `total_debt`, `total_assets` |
| Interest coverage | EBIT / interest expense | `ebit`, `interest_expense` |

Low interest coverage (under ~2-3x is often flagged as risky) means operating income barely covers interest payments.

## Profitability (how much profit per dollar of sales/assets/equity?)
| Ratio | Formula | Keys |
|---|---|---|
| Gross margin | (revenue − COGS) / revenue | `revenue`, `cogs` |
| Net profit margin | net income / revenue | `net_income`, `revenue` |
| Return on assets (ROA) | net income / total assets | `net_income`, `total_assets` |
| Return on equity (ROE) | net income / total equity | `net_income`, `total_equity` |

## Efficiency (how well are assets being used?)
| Ratio | Formula | Keys |
|---|---|---|
| Asset turnover | revenue / total assets | `revenue`, `total_assets` |
| Inventory turnover | COGS / inventory | `cogs`, `inventory` |

## DuPont identity (decomposing ROE)
```
ROE = Net profit margin × Asset turnover × Equity multiplier
    = (Net income / Revenue) × (Revenue / Total assets) × (Total assets / Total equity)
```
Use this whenever ROE changed and the question is *why* — a margin problem, an efficiency problem, or a leverage problem each call for a different explanation and a different fix.

## Market-value ratios (need share price / market cap — not computed by the script)
| Ratio | Formula | What it signals |
|---|---|---|
| P/E | Price per share / EPS | How much investors pay per dollar of current earnings |
| P/B | Price per share / Book value per share | Premium over accounting net worth |
| EV/EBITDA | Enterprise value / EBITDA | Capital-structure-neutral valuation multiple, common in comps |

## Reading a ratio
A ratio means little in isolation. Always compare it to one of:
- The same company's value last year or last quarter (trend).
- A direct industry peer or industry average (cross-sectional).
- A covenant or policy threshold, if the question specifies one (e.g., a loan covenant requiring current ratio ≥ 1.5x).
