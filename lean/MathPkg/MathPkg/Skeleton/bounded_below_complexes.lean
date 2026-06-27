import Mathlib

/-!
# Bounded-below complexes and K+(M)

**K+(M)** is the full subcategory of the homotopy category K(M) consisting of
bounded-below complexes, i.e., chain complexes `F` such that `F_i = 0` for `i`
sufficiently small.

Mathlib4 provides this as `HomotopyCategory.Plus C` (for cochain complexes
graded by ℤ). The bounded-below property for a complex is `CochainComplex.plus C`,
which is equivalent to `∃ n : ℤ, K.IsStrictlyGE n`, meaning all components
of `K` in degrees `< n` are zero.

## Main definitions in Mathlib4

* `CochainComplex.plus C` : `ObjectProperty (CochainComplex C ℤ)` --
  the property of being bounded below
* `CochainComplex.Plus C` : the full subcategory of bounded-below cochain complexes
* `HomotopyCategory.plus C` : the shifted property on `HomotopyCategory C (.up ℤ)`
* `HomotopyCategory.Plus C` : **K+(C)**, the homotopy category of bounded-below
  cochain complexes (a triangulated subcategory of `K(C)`)

## References

* `Mathlib/Algebra/Homology/CochainComplexPlus.lean`
* `Mathlib/Algebra/Homology/HomotopyCategory/Plus.lean`
-/

open CategoryTheory
open CategoryTheory.Limits
open HomologicalComplex

universe u

section bounded_below_complexes

/-! ### The bounded-below property for cochain complexes -/

/--
`BoundedBelow` is a typeclass capturing the property that a cochain complex
`K : CochainComplex C ℤ` is bounded below, i.e., `K_i = 0` for all `i`
sufficiently small.

This is equivalent to Mathlib4's `CochainComplex.plus C K`.
-/
class BoundedBelow (C : Type u) [Category.{u} C] [HasZeroMorphisms C]
    (K : CochainComplex C ℤ) : Prop where
  /-- There exists an integer `n` such that `K.IsStrictlyGE n` --
  all components of `K` in degrees `< n` are zero. -/
  exists_n : ∃ (n : ℤ), K.IsStrictlyGE n

/-- `BoundedBelow` coincides with Mathlib4's `CochainComplex.plus`. -/
theorem boundedBelow_iff_plus (C : Type u) [Category.{u} C] [HasZeroMorphisms C]
    (K : CochainComplex C ℤ) :
    BoundedBelow C K ↔ CochainComplex.plus C K := by
  sorry
