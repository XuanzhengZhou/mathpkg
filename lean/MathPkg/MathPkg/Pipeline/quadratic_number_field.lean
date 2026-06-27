import Mathlib

open scoped NumberField

/-!
# Quadratic Number Field

A **quadratic number field** is an algebraic number field `K` with `[K : ℚ] = 2`.

Equivalently, `K = ℚ(√d)` for a squarefree integer `d ≠ 0, 1`. Every quadratic
number field is of this form (a consequence of the primitive element theorem).

Mathlib4 provides `NumberField K` (characteristic zero + finite-dimensional over ℚ).
This file defines `IsQuadraticNumberField K` as the additional condition
`Module.finrank ℚ K = 2`, i.e. `K` is a quadratic extension of `ℚ`.

## Dependencies

- [Algebraic number field](/concept/algebraic_number_field) — the base notion `NumberField K`
- [Degree of a field extension](/concept/degree_of_a_field_extension) — `Module.finrank ℚ K`
-/

section quadratic_number_field

variable (K : Type*) [Field K] [NumberField K]

/-- A **quadratic number field** is a number field `K` of degree 2 over `ℚ`.
That is, `K` is a field extension of `ℚ` with `[K : ℚ] = 2`.

In Mathlib4 this is expressed as `Module.finrank ℚ K = 2`, where `Module.finrank`
encodes the field extension degree.

Classical examples are `ℚ(√d)` for squarefree `d ≠ 0, 1`:
- `ℚ(√2)`, `ℚ(√3)`, `ℚ(√5)` — real quadratic fields (d > 0)
- `ℚ(√-1)`, `ℚ(√-3)`, `ℚ(√-5)` — imaginary quadratic fields (d < 0) -/
def IsQuadraticNumberField : Prop :=
  Module.finrank ℚ K = 2

end quadratic_number_field

/-! ### Examples -/

section examples

/-- `ℚ` itself has degree 1 over `ℚ`, so it is NOT a quadratic number field. -/
example : ¬ IsQuadraticNumberField ℚ := by
  unfold IsQuadraticNumberField
  have h : Module.finrank ℚ ℚ = 1 := by
    simp
  rw [h]
  norm_num

/-- `ℚ(i)`, the Gaussian rationals (degree 2 over ℚ), is a quadratic number field.
We model it as `AdjoinRoot (X² + 1)` where `X² + 1` is irreducible over ℚ. -/
example : IsQuadraticNumberField (AdjoinRoot (Polynomial.X ^ 2 + (1 : ℚ[X]))) := by
  unfold IsQuadraticNumberField
  have h_ne_zero : (Polynomial.X ^ 2 + (1 : ℚ[X])) ≠ 0 := by
    simp
  let pb := AdjoinRoot.powerBasis h_ne_zero
  have h_finrank : Module.finrank ℚ (AdjoinRoot (Polynomial.X ^ 2 + (1 : ℚ[X]))) = 2 := by
    rw [pb.finrank]
    simp
  exact h_finrank

/-- Every quadratic number field is, in particular, a number field.
The typeclass `NumberField K` is always available when `K` is a quadratic number field. -/
example (K : Type*) [Field K] [NumberField K] (_h : IsQuadraticNumberField K) : NumberField K := by
  infer_instance

/-- `ℚ(√2)` (degree 2 over ℚ) is a quadratic number field.
Modeled as `AdjoinRoot (X² - 2)`. -/
example : IsQuadraticNumberField (AdjoinRoot (Polynomial.X ^ 2 - (2 : ℚ[X]))) := by
  unfold IsQuadraticNumberField
  have h_ne_zero : (Polynomial.X ^ 2 - (2 : ℚ[X])) ≠ 0 := by
    simp
  let pb := AdjoinRoot.powerBasis h_ne_zero
  have h_finrank : Module.finrank ℚ (AdjoinRoot (Polynomial.X ^ 2 - (2 : ℚ[X]))) = 2 := by
    rw [pb.finrank]
    simp
  exact h_finrank

/-- If `IsQuadraticNumberField K`, then the finrank is exactly 2,
so `Module.finrank ℚ K = 2` is available as a hypothesis. -/
example (K : Type*) [Field K] [NumberField K] (hquad : IsQuadraticNumberField K) :
    Module.finrank ℚ K = 2 :=
  hquad

end examples
