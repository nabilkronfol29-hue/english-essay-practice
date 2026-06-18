#!/usr/bin/env python3
"""CLI calculators for corporate finance coursework: time value of money,
NPV/IRR/payback, WACC, and financial-statement ratios. Use this for the
arithmetic instead of doing it by hand or in your head -- it keeps
compounding and discounting consistent across a whole problem set.

All amounts are plain magnitudes (no Excel-style sign flipping between
PV and FV) except cash flow series for npv/irr/payback, where the sign
of each entry must reflect its direction (outflow negative, inflow
positive) -- that part of the convention is unavoidable and standard.

Note: when a --cashflows value starts with a negative number, you must
use the `=` form (`--cashflows=-5000,...`) or argparse will mistake the
negative sign for a new flag.

Examples:
    finance_calcs.py fv --rate 0.07 --nper 10 --pv 1000
    finance_calcs.py pv --rate 0.05 --nper 5 --fv 10000
    finance_calcs.py npv --rate 0.1 --cashflows=-5000,1500,1800,2200,2500,2700
    finance_calcs.py irr --cashflows=-5000,1500,1800,2200,2500,2700
    finance_calcs.py payback --cashflows=-5000,1500,1800,2200,2500,2700
    finance_calcs.py wacc --equity 6000 --debt 4000 --cost-equity 0.12 --cost-debt 0.06 --tax-rate 0.25
    finance_calcs.py ratios --json '{"current_assets": 500, "current_liabilities": 250}'
    finance_calcs.py ratios --file statement.json
"""
import argparse
import json
import sys


def fv(rate, nper, pv=0.0, pmt=0.0):
    if rate == 0:
        return pv + pmt * nper
    return pv * (1 + rate) ** nper + pmt * (((1 + rate) ** nper - 1) / rate)


def pv(rate, nper, fv=0.0, pmt=0.0):
    if rate == 0:
        return fv + pmt * nper
    return fv / (1 + rate) ** nper + pmt * ((1 - (1 + rate) ** (-nper)) / rate)


def npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows, guess=0.1, tol=1e-9, max_iter=1000):
    if not any(cf < 0 for cf in cashflows) or not any(cf > 0 for cf in cashflows):
        raise ValueError("IRR needs at least one negative and one positive cash flow.")
    rate = guess
    for _ in range(max_iter):
        npv_val = npv(rate, cashflows)
        d_rate = 1e-6
        derivative = (npv(rate + d_rate, cashflows) - npv_val) / d_rate
        if derivative == 0:
            break
        new_rate = rate - npv_val / derivative
        if abs(new_rate - rate) < tol:
            return new_rate
        rate = new_rate
    raise ValueError("IRR did not converge -- check the cash flow series.")


def payback_period(cashflows):
    cumulative = 0.0
    for t, cf in enumerate(cashflows):
        prev_cumulative = cumulative
        cumulative += cf
        if t > 0 and cumulative >= 0 and prev_cumulative < 0:
            return (t - 1) + (-prev_cumulative / cf)
    return None


def wacc(equity, debt, cost_equity, cost_debt, tax_rate):
    total = equity + debt
    return (equity / total) * cost_equity + (debt / total) * cost_debt * (1 - tax_rate)


# (display name, formula, required statement keys, format: "x" multiple or "pct" percentage)
RATIO_DEFS = [
    ("Current ratio", lambda d: d["current_assets"] / d["current_liabilities"], ["current_assets", "current_liabilities"], "x"),
    ("Quick ratio", lambda d: (d["current_assets"] - d.get("inventory", 0)) / d["current_liabilities"], ["current_assets", "current_liabilities"], "x"),
    ("Cash ratio", lambda d: d["cash"] / d["current_liabilities"], ["cash", "current_liabilities"], "x"),
    ("Debt-to-equity", lambda d: d["total_debt"] / d["total_equity"], ["total_debt", "total_equity"], "x"),
    ("Debt-to-assets", lambda d: d["total_debt"] / d["total_assets"], ["total_debt", "total_assets"], "pct"),
    ("Interest coverage (EBIT/Interest)", lambda d: d["ebit"] / d["interest_expense"], ["ebit", "interest_expense"], "x"),
    ("Gross margin", lambda d: (d["revenue"] - d["cogs"]) / d["revenue"], ["revenue", "cogs"], "pct"),
    ("Net profit margin", lambda d: d["net_income"] / d["revenue"], ["net_income", "revenue"], "pct"),
    ("Return on assets (ROA)", lambda d: d["net_income"] / d["total_assets"], ["net_income", "total_assets"], "pct"),
    ("Return on equity (ROE)", lambda d: d["net_income"] / d["total_equity"], ["net_income", "total_equity"], "pct"),
    ("Asset turnover", lambda d: d["revenue"] / d["total_assets"], ["revenue", "total_assets"], "x"),
    ("Inventory turnover", lambda d: d["cogs"] / d["inventory"], ["cogs", "inventory"], "x"),
]


def compute_ratios(data):
    results = []
    for name, formula, required, fmt in RATIO_DEFS:
        if not all(k in data for k in required):
            continue
        try:
            value = formula(data)
        except ZeroDivisionError:
            continue
        results.append((name, value, fmt))
    return results


def parse_cashflows(s):
    return [float(x) for x in s.split(",")]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("fv", help="Future value of a present sum and/or payment stream")
    p.add_argument("--rate", type=float, required=True)
    p.add_argument("--nper", type=float, required=True)
    p.add_argument("--pv", type=float, default=0.0)
    p.add_argument("--pmt", type=float, default=0.0)

    p = sub.add_parser("pv", help="Present value of a future sum and/or payment stream")
    p.add_argument("--rate", type=float, required=True)
    p.add_argument("--nper", type=float, required=True)
    p.add_argument("--fv", type=float, default=0.0)
    p.add_argument("--pmt", type=float, default=0.0)

    p = sub.add_parser("npv", help="Net present value of a cash flow series (t=0 first)")
    p.add_argument("--rate", type=float, required=True)
    p.add_argument("--cashflows", type=parse_cashflows, required=True)

    p = sub.add_parser("irr", help="Internal rate of return of a cash flow series (t=0 first)")
    p.add_argument("--cashflows", type=parse_cashflows, required=True)

    p = sub.add_parser("payback", help="Payback period in years for a cash flow series (t=0 first)")
    p.add_argument("--cashflows", type=parse_cashflows, required=True)

    p = sub.add_parser("wacc", help="Weighted average cost of capital")
    p.add_argument("--equity", type=float, required=True)
    p.add_argument("--debt", type=float, required=True)
    p.add_argument("--cost-equity", type=float, required=True)
    p.add_argument("--cost-debt", type=float, required=True)
    p.add_argument("--tax-rate", type=float, required=True)

    p = sub.add_parser("ratios", help="Compute whichever ratios the given statement line items support")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--json", type=str, help="JSON object of statement line items")
    group.add_argument("--file", type=str, help="Path to a JSON file of statement line items")

    args = parser.parse_args()

    if args.command == "fv":
        print(f"FV = {fv(args.rate, args.nper, args.pv, args.pmt):,.2f}")
    elif args.command == "pv":
        print(f"PV = {pv(args.rate, args.nper, args.fv, args.pmt):,.2f}")
    elif args.command == "npv":
        print(f"NPV at {args.rate:.2%} = {npv(args.rate, args.cashflows):,.2f}")
    elif args.command == "irr":
        try:
            result = irr(args.cashflows)
            print(f"IRR = {result:.4%}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "payback":
        result = payback_period(args.cashflows)
        print(f"Payback period = {result:.2f} years" if result is not None else "Payback period: never recovers initial investment within the given series")
    elif args.command == "wacc":
        result = wacc(args.equity, args.debt, args.cost_equity, args.cost_debt, args.tax_rate)
        print(f"WACC = {result:.4%}")
    elif args.command == "ratios":
        if args.file:
            with open(args.file) as f:
                data = json.load(f)
        else:
            data = json.loads(args.json)
        results = compute_ratios(data)
        if not results:
            print("No ratios could be computed -- check that the input keys match the expected names (see SKILL.md / references/ratios.md).")
            return
        for name, value, fmt in results:
            formatted = f"{value:.1%}" if fmt == "pct" else f"{value:.2f}x"
            print(f"{name}: {formatted}")


if __name__ == "__main__":
    main()
