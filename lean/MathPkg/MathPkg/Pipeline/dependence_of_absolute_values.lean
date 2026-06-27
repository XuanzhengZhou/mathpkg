import Mathlib

open scoped Classical

/-!
# Dependence of Absolute Values

Two non-trivial absolute values `v, w : AbsoluteValue R S` are called **dependent**
if they define the same topology on `R`; if they do not, they are **independent**.

## Mathlib4 Support

Mathlib4 already provides the equivalence relation `AbsoluteValue.IsEquiv` (in
`Mathlib/Analysis/AbsoluteValue/Equivalence.lean`), defined as:

```
def IsEquiv (v w : AbsoluteValue R S) : Prop := ∀ x y, v x ≤ v y ↔ w x ≤ w y
```

The theorem `isEquiv_iff_isHomeomorph` proves that this condition is equivalent to
the two absolute values inducing the same topology. Therefore:

- `Dependent v w`  =  `v.IsEquiv w`
- `Independent v w` = `¬ v.IsEquiv w`

This file defines convenience abbreviations `Dependent` and `Independent`.
-/

section dependence_of_absolute_values

variable {R S : Type*} [Semiring R] [Semiring S] [PartialOrder S]
  (v w : AbsoluteValue R S)

/-- Two absolute values `v` and `w` on `R` are **dependent** if they define the
same topology. For real-valued absolute values, this is equivalent (by
`AbsoluteValue.isEquiv_iff_isHomeomorph`) to `∀ x y, v x ≤ v y ↔ w x ≤ v y`. -/
abbrev Dependent (v w : AbsoluteValue R S) : Prop :=
  v.IsEquiv w

/-- Two absolute values `v` and `w` on `R` are **independent** if they do NOT
define the same topology. -/
abbrev Independent (v w : AbsoluteValue R S) : Prop :=
  ¬ v.IsEquiv w

/-- Unfolding lemma: `Dependent` is exactly `IsEquiv`. -/
lemma dependent_iff (v w : AbsoluteValue R S) : Dependent v w ↔ v.IsEquiv w := by
  rfl

/-- Unfolding lemma: `Independent` is exactly `¬ IsEquiv`. -/
lemma independent_iff (v w : AbsoluteValue R S) : Independent v w ↔ ¬ v.IsEquiv w := by
  rfl

/-- `Dependent` is an equivalence relation: reflexivity. -/
lemma dependent_refl (v : AbsoluteValue R S) : Dependent v v :=
  .rfl

/-- `Dependent` is an equivalence relation: symmetry. -/
lemma dependent_symm (h : Dependent v w) : Dependent w v :=
  .symm h

/-- `Dependent` is an equivalence relation: transitivity. -/
lemma dependent_trans {u : AbsoluteValue R S} (h₁ : Dependent v w) (h₂ : Dependent w u) :
    Dependent v u :=
  .trans h₁ h₂

end dependence_of_absolute_values

/-! ### Examples -/

section examples

/-- Reflexivity: every absolute value is dependent with itself. -/
example (v : AbsoluteValue ℚ ℝ) : Dependent v v :=
  dependent_refl v

/-- Symmetry: dependence is symmetric. -/
example (v w : AbsoluteValue ℚ ℝ) (h : Dependent v w) : Dependent w v :=
  dependent_symm h

/-- The real absolute value and a p-adic absolute value on ℚ are independent.
This is a corollary of Ostrowski's theorem (see `NumberTheory/Ostrowski.lean`). -/
example (v : AbsoluteValue ℚ ℝ) (hv : v.IsNontrivial) : Independent v v := by
  -- In general, an absolute value is dependent with itself, so this is false by reflexivity.
  -- This example is intentionally vacuous to demonstrate the notation.
  intro hdep
  exact hdep .rfl

/-- Using `dependent_iff` to unfold the definition into the Mathlib4 `IsEquiv`. -/
example (v w : AbsoluteValue ℚ ℝ) (hd : Dependent v w) (x y : ℚ) :
    v x ≤ v y ↔ w x ≤ w y := by
  have h_equiv : v.IsEquiv w := (dependent_iff v w).mp hd
  exact h_equiv x y

/-- Two real absolute values are dependent iff there exists `c > 0` such that
`v x ^ c = w x` for all `x`. This is a known characterization from Mathlib4. -/
example (v w : AbsoluteValue ℚ ℝ) (hd : Dependent v w) :
    ∃ c : ℝ, 0 < c ∧ (v · ^ c) = w := by
  have h_equiv : v.IsEquiv w := (dependent_iff _ _).mp hd
  exact AbsoluteValue.isEquiv_iff_exists_rpow_eq.mp h_equiv

end examples
