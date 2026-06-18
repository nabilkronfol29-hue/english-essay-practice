# OLS Assumptions and Violations

| Assumption | What violation looks like | How to detect it | Consequence | Standard fix |
|---|---|---|---|---|
| Linearity in parameters | True relationship is curved/non-linear in the variables | Residual-vs-fitted plot shows a pattern, not a random scatter | Biased, misleading coefficients | Add polynomial/log terms, or a non-linear model |
| Zero conditional mean (exogeneity) | Regressor correlated with the error term — omitted variable, reverse causality, measurement error | Hard to test directly; reason from the research design; Hausman test if an instrument is available | Biased and inconsistent coefficients (the central threat to causal interpretation) | Add the omitted control if observable, use instrumental variables / 2SLS, or use a quasi-experimental design (diff-in-diff, RDD) |
| No perfect multicollinearity / limited multicollinearity | Two or more regressors highly correlated with each other | Variance Inflation Factor (VIF); rule of thumb flag around VIF > 10 | Inflated standard errors, unstable/imprecise coefficient estimates (not biased, just noisy) | Drop or combine redundant regressors, collect more data, or accept the imprecision if the variables are theoretically necessary |
| Homoskedasticity (constant error variance) | Spread of residuals changes systematically with fitted values or a regressor | Breusch-Pagan or White test; residual-vs-fitted plot fans out | Standard errors are wrong (often understated), so t-stats/p-values are unreliable even though coefficients stay unbiased | Use heteroskedasticity-robust standard errors (White/HC standard errors) |
| No autocorrelation (independent errors) | Residuals correlated across observations — common in time series | Durbin-Watson statistic, residual autocorrelation plot | Standard errors wrong, often overstated significance | Newey-West (HAC) standard errors, or model the dynamics explicitly (e.g., add lags) |
| Normality of errors | Residuals strongly skewed or heavy-tailed | Q-Q plot, Shapiro-Wilk/Jarque-Bera test | Only matters for small-sample inference (large-sample inference relies on the CLT and is robust to this) | More data, or bootstrap/robust inference methods for small samples |

## Quick triage
- If the standard errors look untrustworthy but coefficients seem reasonable → heteroskedasticity or autocorrelation, fix with robust/clustered/HAC standard errors, not a different model.
- If the coefficient itself seems implausible (wrong sign, implausible magnitude) → suspect omitted variable bias or reverse causality (endogeneity) — this needs a design fix (IV, panel/FE, better controls), not just a different standard-error formula.
- If standard errors are huge and nothing is significant despite a sensible model → check for multicollinearity before concluding there's no effect.
