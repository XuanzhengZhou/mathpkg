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
def IsQuadraticNumberField : Prop := by
  sorry
