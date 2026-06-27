import Mathlib

open scoped Classical

/-!
# Non-Archimedean Absolute Value (Valuation)

An absolute value `|·|_v : R → S` satisfies the **strong triangle inequality**
`|x + y|_v ≤ max(|x|_v, |y|_v)` for all `x, y`. Such an absolute value is called
**non-archimedean**, or a **valuation**.

This is AV 4 in the standard axioms for absolute values:
- AV 1: `|x|_v ≥ 0`, with equality iff `x = 0`
- AV 2: `|xy|_v = |x|_v |y|_v`
- AV 3: `|x + y|_v ≤ |x|_v + |y|_v` (triangle inequality)
- AV 4: `|x + y|_v ≤ max(|x|_v, |y|_v)` (strong triangle inequality, this file)

Mathlib4 already provides:
- `AbsoluteValue R S` bundling AV 1-3
- `IsNonarchimedean f` as the predicate `∀ a b, f (a + b) ≤ f a ⊔ f b`

This file defines the abbreviation `IsNonarchimedeanAbsoluteValue v` combining both.
-/

section non_archimedean_absolute_value_valuation

variable {R S : Type*} [Semiring R] [Semiring S] [LinearOrder S]

/-- A **non-archimedean absolute value** (also called a **valuation**) is an absolute value
`v : R → S` satisfying the strong triangle inequality:

`v (x + y) ≤ v x ⊔ v y` for all `x, y : R`.

In a linearly ordered codomain `S` (e.g. `ℝ`), `v x ⊔ v y` is the same as `max (v x) (v y)`. -/
abbrev IsNonarchimedeanAbsoluteValue (v : AbsoluteValue R S) : Prop := by
  sorry
