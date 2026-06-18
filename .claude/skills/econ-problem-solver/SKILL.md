---
name: econ-problem-solver
description: Use this skill for microeconomics and macroeconomics coursework -- problem sets, exam review, or wanting a concept explained well. Covers supply & demand, elasticity, consumer/producer surplus, market structures (perfect competition, monopoly, monopolistic competition, oligopoly, game theory), externalities, GDP/inflation/unemployment, the AD-AS model, IS-LM, fiscal and monetary policy, exchange rates, and comparative advantage/trade. Trigger on course terminology even without the word "economics" -- e.g. "deadweight loss," "marginal cost," "Phillips curve," "opportunity cost," "Nash equilibrium," "money multiplier," "elastic demand," or a request to "draw the graph for..."
---

# Economics Problem Solver

Helps with the actual mechanics of an econ course: working a problem correctly, reading a graph, and understanding *why* the answer is what it is — not just stating it.

## 1. Figure out what's actually being asked

Before solving, identify which of these you're dealing with — it changes the approach:
- **Concept check** ("what's the difference between X and Y") → explain with a concrete example, don't just define.
- **Numeric problem** (solve for equilibrium price, calculate elasticity, find profit-maximizing quantity) → solve step by step, show the algebra.
- **Graph problem** (shift the curve, find new equilibrium, shade the welfare loss) → describe the graph precisely in words/ASCII since you can't draw on paper — see below.
- **"Explain why" / policy question** → walk through the causal chain (e.g., why a price ceiling causes a shortage), don't just assert the conclusion.

If the question is ambiguous about course level (principles vs. intermediate vs. grad), match the tools to what they've clearly already used in the conversation rather than introducing calculus-heavy treatment to someone working with simple supply/demand diagrams, or vice versa.

## 2. Graph-based problems: a reliable sequence

Most micro and macro problems reduce to "something shifts, what happens to equilibrium." Work it in this order so nothing gets skipped:
1. **Identify the axes and the initial curves.** State what's on each axis explicitly (e.g., Price/Quantity, or Real GDP/Price Level).
2. **Identify the shock.** Is it a shift of a curve (change in a determinant other than the variable on the axis) or a movement along a curve (change in the axis variable itself)? This is the single most common source of errors — e.g., a price change moves you *along* the demand curve, it does not shift it.
3. **Determine direction of the shift** and state the economic reason (e.g., "input costs rise → supply curve shifts left because producers are willing to supply less at every price").
4. **Find the new equilibrium** and compare to the old one (price up/down, quantity up/down).
5. **If asked about welfare**, identify consumer surplus, producer surplus, deadweight loss, or government revenue/cost as the relevant area(s), and state whether each increases, decreases, or is created/destroyed.

Render the graph as a labeled ASCII sketch or a clear verbal description (axes, curve labels, shift direction, before/after equilibrium points) when it helps — don't skip straight to the answer for a problem that's fundamentally about reading a diagram.

## 3. Worked-example pattern

Show your work the way a grader wants to see it:
1. Write the relevant formula or condition (e.g., profit-maximizing: MR = MC).
2. Plug in the given numbers.
3. Solve algebraically, one step per line for anything non-trivial.
4. State the answer with correct units (e.g., "$4.50 per unit," not just "4.5").
5. Sanity-check: does the sign/magnitude make sense? (A monopolist's price should exceed marginal cost; elasticity of a necessity should be < 1 in magnitude; unemployment rate should be between 0–100%.) If a check fails, say so and re-examine rather than presenting a number you don't believe.

For the full formula set (elasticities, surplus/DWL, GDP components, money multiplier, Fisher equation, Phillips curve, IS-LM, etc.), see `references/formulas.md` — pull it up rather than relying on memory for the exact form.

## 4. Studying vs. submitting

This skill is for understanding the material, not for producing a final write-up to hand in unchanged. When a problem looks like a specific graded assignment (the user pastes problem-set or exam wording verbatim and wants the finished answer), default to walking through the method with a parallel example or the same numbers but explaining each step, rather than just supplying a final answer with no reasoning shown — that's what actually helps on the exam. If they explicitly say it's for practice/review (not submission), solving it straight through is fine.
