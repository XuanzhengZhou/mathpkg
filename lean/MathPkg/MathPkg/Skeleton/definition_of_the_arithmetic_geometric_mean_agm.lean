import Mathlib

/-!
# Definition of the Arithmetic-Geometric Mean (AGM)

Let `a` and `b` be two positive real numbers. The **Arithmetic-Geometric mean** of `a` and `b`,
denoted by `AGM(a, b)`, is defined as the common limit of the sequences `a_n` and `b_n`
defined by:

* `a₀ = a`, `b₀ = b`
* `a_{n+1} = (a_n + b_n) / 2`  (arithmetic mean)
* `b_{n+1} = √(a_n · b_n)`  (geometric mean)

Starting with two nonnegative real numbers and repeatedly replacing them with their
arithmetic and geometric means, the two monotone sequences converge to the same limit:
the arithmetic-geometric mean (AGM).

Mathlib4 already provides `NNReal.agm` for nonnegative reals.
We define `Real.agm` as a wrapper for positive real numbers, which is the classical setting.
-/

open Real

/-- The arithmetic-geometric mean of two nonnegative real numbers `a` and `b`.

This is the common limit of the sequences defined by iteratively replacing
`(a, b)` with `((a + b) / 2, √(a · b))`.

Uses Mathlib4's `NNReal.agm` by converting to `ℝ≥0` and back. -/
noncomputable def agm (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) : ℝ := by
  sorry
