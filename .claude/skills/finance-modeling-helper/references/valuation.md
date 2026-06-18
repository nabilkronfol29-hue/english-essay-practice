# Valuation Reference

## Discounted Cash Flow (DCF)

1. **Project free cash flow (FCF)** for an explicit forecast period (typically 5-10 years):
   `FCF = EBIT × (1 − tax rate) + Depreciation & Amortization − CapEx − Δ Net Working Capital`
   This is unlevered free cash flow to the firm (FCFF) — it excludes interest, which is why it gets discounted at WACC rather than cost of equity.

2. **Compute the terminal value** at the end of the forecast period using one of:
   - **Perpetuity growth**: `TV = FCF_final × (1+g) / (WACC − g)` — g should be a long-run sustainable rate (roughly GDP growth, not the company's recent high growth).
   - **Exit multiple**: `TV = Final-year EBITDA × peer EV/EBITDA multiple` — anchors the terminal value to how the market actually prices similar mature companies instead of a perpetuity formula.

3. **Discount everything to present value** at WACC: each forecast-year FCF and the terminal value, each discounted by `(1+WACC)^t` for its respective year t.

4. **Sum the discounted cash flows and discounted terminal value** → Enterprise Value.

5. **Bridge to equity value**: `Equity value = Enterprise value − total debt + cash`. Divide by diluted shares outstanding for value per share.

6. **Sensitize.** DCF answers are dominated by WACC and the terminal growth/exit multiple assumption — always show how the per-share value changes across a small grid of WACC and terminal-value assumptions (e.g., ±1pp on each) rather than presenting one point estimate as if it were precise.

### Common DCF mistakes
- Discounting FCFF (unlevered) at cost of equity instead of WACC, or discounting FCFE (levered, after interest) at WACC instead of cost of equity — the cash flow definition and discount rate must match.
- Terminal value assumption silently doing 70-80%+ of the work in the valuation without flagging it.
- Using a terminal growth rate above the long-run GDP/inflation growth rate (implies the company eventually becomes larger than the entire economy).
- Forgetting to subtract net debt when bridging from enterprise value to equity value.

## Comparable Companies ("Comps")

1. **Select a peer set** — companies in the same industry with similar size, growth, and margin profile. A peer set with very different growth or risk doesn't transfer cleanly.
2. **Compute trading multiples** for each peer: EV/EBITDA, EV/Revenue, P/E are the most common. Use forward (next-twelve-months) estimates when available — they're less distorted by one-off items than trailing figures.
3. **Apply the peer median (or a defensible range) multiple to the target company's own metric** (e.g., target EBITDA × peer median EV/EBITDA) to back out an implied enterprise value, then bridge to equity value/share the same way as in DCF.
4. **Cross-check against DCF.** If comps and DCF disagree substantially, that's informative — it usually means the market is pricing in growth/risk assumptions that differ from what went into the DCF, which is worth calling out explicitly rather than picking whichever number is more convenient.

### Common comps mistakes
- Mixing trailing and forward multiples across peers.
- Including a peer that's an outlier (recent M&A target, distressed, very different capital structure) without adjusting or excluding it.
- Treating equity value multiples (P/E) and enterprise value multiples (EV/EBITDA) as interchangeable — P/E is sensitive to capital structure (debt load) in a way EV/EBITDA is not.

## Capital budgeting decision rule
Accept a project if NPV > 0 at the appropriate discount rate (WACC for an average-risk project, adjusted for project-specific risk otherwise). IRR is a useful cross-check but can give multiple or misleading answers when cash flows change sign more than once, or when comparing mutually exclusive projects of different scale — NPV is the more reliable rule when the two disagree.
