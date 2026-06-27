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
abbrev IsNonarchimedeanAbsoluteValue (v : AbsoluteValue R S) : Prop :=
  IsNonarchimedean (v : R → S)

/-- Unfolding lemma: `IsNonarchimedeanAbsoluteValue` expands exactly to
`IsNonarchimedean` applied to the underlying function of the absolute value. -/
lemma isNonarchimedeanAbsoluteValue_iff (v : AbsoluteValue R S) :
    IsNonarchimedeanAbsoluteValue v ↔ IsNonarchimedean (v : R → S) := by
  rfl

/-- The strong triangle inequality written with `max` instead of `⊔`.
In a linear order, `sup` and `max` agree. -/
lemma add_le_max (v : AbsoluteValue R S) [hna : IsNonarchimedeanAbsoluteValue v] (x y : R) :
    v (x + y) ≤ max (v x) (v y) := by
  have h := hna x y
  -- In a LinearOrder, `⊔` coincides with `max`
  simpa [sup_eq_max] using h

end non_archimedean_absolute_value_valuation

/-! ### Examples -/

section examples

/-- The defining property: `v (x + y) ≤ v x ⊔ v y`. -/
example (v : AbsoluteValue ℚ ℝ) (hna : IsNonarchimedeanAbsoluteValue v) (x y : ℚ) :
    v (x + y) ≤ v x ⊔ v y :=
  hna x y

/-- The strong triangle inequality implies the usual triangle inequality,
since `v x ⊔ v y ≤ v x + v y` for nonnegative values. -/
example (v : AbsoluteValue ℚ ℝ) (hna : IsNonarchimedeanAbsoluteValue v) (x y : ℚ) :
    v (x + y) ≤ v x + v y := by
  have h := hna x y
  have hsup : v x ⊔ v y ≤ v x + v y :=
    sup_le (le_add_of_nonneg_right (AbsoluteValue.nonneg _ _))
      (le_add_of_nonneg_left (AbsoluteValue.nonneg _ _))
  exact le_trans h hsup

/-- For integers, the absolute value satisfies `|n|_v ≤ 1`
when the absolute value is non-archimedean and `|1|_v = 1`. -/
example (v : AbsoluteValue ℤ ℝ) (hna : IsNonarchimedeanAbsoluteValue v) (n : ℤ) :
    v n ≤ 1 := by
  have h_na : IsNonarchimedean (v : ℤ → ℝ) := hna
  exact IsNonarchimedean.apply_intCast_le_one h_na

/-- The equality case: if `v x < v y`, then `v (x + y) = v y`. -/
example (v : AbsoluteValue ℚ ℝ) (hna : IsNonarchimedeanAbsoluteValue v) (x y : ℚ)
    (hlt : v x < v y) : v (x + y) = v y := by
  have h_na : IsNonarchimedean (v : ℚ → ℝ) := hna
  exact IsNonarchimedean.add_eq_right_of_lt h_na hlt

/-- Non-archimedean absolute values satisfy `|x - y|_v ≤ max(|x|_v, |y|_v)`. -/
example (v : AbsoluteValue ℚ ℝ) (hna : IsNonarchimedeanAbsoluteValue v) (x y : ℚ) :
    v (x - y) ≤ max (v x) (v y) := by
  have h := hna x (-y)
  simpa [sub_eq_add_neg, map_neg_eq_map, sup_eq_max] using h

end examples
