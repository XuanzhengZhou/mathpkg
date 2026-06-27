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
abbrev Dependent (v w : AbsoluteValue R S) : Prop := by
  sorry
