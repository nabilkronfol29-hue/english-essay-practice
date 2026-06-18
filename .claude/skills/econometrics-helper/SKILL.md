---
name: econometrics-helper
description: Use this skill for econometrics and applied statistics coursework -- interpreting regression output (coefficients, standard errors, t-stats, p-values, R-squared, F-stat), hypothesis testing, OLS assumptions and violations (heteroskedasticity, autocorrelation, multicollinearity, endogeneity/omitted variable bias), and choosing between OLS, fixed effects, logit/probit, and instrumental variables (2SLS). Trigger when the user pastes regression output, a Stata/R/Python results table, asks "is this coefficient significant," shares a dataset, or is confused about an econometrics concept -- even without the word "econometrics."
---

# Econometrics Helper

Helps with the statistics layer of an economics or finance course: reading regression output correctly, choosing the right model, and diagnosing/explaining what can go wrong with OLS.

## 1. Identify the actual ask

- **Interpret existing output** (a table pasted from Stata/R/Python output) → walk through it systematically, see step 2.
- **Choose the right method** for a research question → see the model-selection table in step 4.
- **Diagnose or explain a violation** (heteroskedasticity, endogeneity, etc.) → see `references/violations.md`.
- **Run an analysis on data they have** → write and run Python (pandas/statsmodels), explain the code and the output, don't just hand back a final paragraph with no visible reasoning if this is for a graded assignment.

## 2. How to read a regression table

Walk through a results table in this order, the way it's actually graded:
1. **Coefficient**: the estimated effect of a one-unit change in the regressor on the dependent variable, holding other included variables fixed. State the units explicitly.
2. **Standard error**: the precision of that estimate — smaller is more precise.
3. **t-statistic** = coefficient / standard error. Compare to ~1.96 (two-tailed, 5% level, large sample) as a rule of thumb, or to the exact critical value for the degrees of freedom if it's a small sample.
4. **p-value**: probability of observing a coefficient this extreme if the true effect were zero. Significant at 5% if p < 0.05 (or check against whatever significance level the course/output specifies).
5. **Confidence interval**: range of plausible values for the true coefficient; if it excludes zero, that's consistent with significance at the corresponding level.
6. **R² / adjusted R²**: share of variation in the dependent variable explained by the model. Adjusted R² penalizes adding regressors that don't help — prefer it when comparing models with different numbers of variables.
7. **F-statistic**: tests whether the regressors *jointly* explain variation in the dependent variable (i.e., whether the whole model is better than no model).

Then translate the statistical result into a plain-English sentence that states the relationship, its direction, its magnitude with units, and whether it's statistically significant — e.g., "a one-year increase in education is associated with a $1,240 increase in annual earnings, holding experience and region fixed, significant at the 1% level." Use "is associated with," not "causes," unless the research design (randomized experiment, valid instrument, credible quasi-experimental setup) actually supports a causal claim.

## 3. Hypothesis testing framework

For any test: (1) state H0 and H1 precisely, (2) identify the test statistic and its distribution under H0, (3) compute or read off the p-value, (4) apply the decision rule against the stated significance level, (5) state the conclusion in terms of the original question, not just "reject/fail to reject H0."

## 4. Choosing a model

| Setup | Typical choice |
|---|---|
| Continuous outcome, cross-sectional data | OLS |
| Binary outcome (0/1) | Logit or probit, not OLS (OLS can predict outside [0,1] and has heteroskedastic errors by construction) |
| Panel data (same units over time), worried about unobserved unit-level confounders | Fixed effects (within estimator) |
| Endogenous regressor (correlated with the error term — omitted variable, reverse causality, measurement error) | Instrumental variables / 2SLS, if a credible instrument exists |
| Time series with trend/seasonality/autocorrelation | AR/ARIMA, or check stationarity before running OLS on levels |

If asked to actually fit one of these in Python, use `statsmodels` (`smf.ols`, `sm.Logit`, `linearmodels.PanelOLS` for fixed effects, `linearmodels.IV2SLS` for instrumental variables) and show the code alongside the output.

## 5. Diagnosing violations

See `references/violations.md` for the full table of OLS assumptions, how each violation shows up, how to detect it, and the standard fix (e.g., robust/clustered standard errors for heteroskedasticity, a Hausman test or instrument for endogeneity).

## 6. Studying vs. submitting

For a question that reads like a specific homework problem (the user pastes the exact dataset/output and assignment wording and wants the final write-up), default to explaining the method and walking through the reasoning rather than producing a polished paragraph meant to be submitted verbatim — that's what actually helps when the exam asks them to do it themselves. If they say it's for review or they've already turned it in, a direct answer is fine.
