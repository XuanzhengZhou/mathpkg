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
  constructor
  · rintro ⟨⟨n, hn⟩⟩; exact ⟨n, hn⟩
  · rintro ⟨n, hn⟩; exact ⟨⟨n, hn⟩⟩

end bounded_below_complexes

section homotopy_category_plus

/-! ### K+(C) : The homotopy category of bounded-below complexes -/

variable (C : Type u) [Category.{u} C] [Preadditive C]

/--
**K+(C)** is the full (triangulated) subcategory of the homotopy category
`K(C) = HomotopyCategory C (ComplexShape.up ℤ)` consisting of cochain complexes
that are bounded below.

Mathlib4 defines this as `HomotopyCategory.Plus C`.
-/
abbrev KPlusCategory := HomotopyCategory.Plus C

/-- The inclusion functor `K+(C) ⥤ K(C)`. -/
abbrev KPlusCategory.ι : KPlusCategory C ⥤ HomotopyCategory C (ComplexShape.up ℤ) :=
  HomotopyCategory.Plus.ι C

end homotopy_category_plus

section examples

/-! ### Examples -/

open ComplexShape

/-- A single-object complex concentrated in degree 0 is bounded below. -/
example (A : Ab.{u}) : BoundedBelow Ab ((single Ab (up ℤ) 0).obj A) := by
  refine ⟨⟨0, ?_⟩⟩
  infer_instance

/-- The zero complex is bounded below. -/
example (C : Type u) [Category.{u} C] [HasZeroMorphisms C] [HasZeroObject C] :
    BoundedBelow C (0 : CochainComplex C ℤ) := by
  refine ⟨⟨0, ?_⟩⟩
  -- zero complex is strictly GE 0 since all components are zero
  rw [CochainComplex.isStrictlyGE_iff]
  intro i hi
  exact isZero_zero _

/-- In ℤ-Mod (the category of abelian groups), the cochain complex
`… → 0 → 0 → ℤ → ℤ → 0 → …` (with nonzero terms in degrees 0, 1)
is bounded below, since all terms in degrees < 0 are zero. -/
example : BoundedBelow Ab
    ((single Ab (up ℤ) (0 : ℤ)).obj (AddCommGroupCat.of ℤ)) := by
  refine ⟨⟨0, ?_⟩⟩
  infer_instance

/-- A complex that vanishes in all negative degrees is bounded below
with bound `n = 0`. -/
example (K : CochainComplex Ab ℤ) (h : ∀ (i : ℤ), i < 0 → IsZero (K.X i)) :
    BoundedBelow Ab K := by
  refine ⟨⟨0, ?_⟩⟩
  rw [CochainComplex.isStrictlyGE_iff]
  exact h

/-- If `K` is bounded below with bound `n`, then shifting `K` by `a`
gives a complex bounded below with bound `n - a`. -/
example (K : CochainComplex Ab ℤ) (n a : ℤ) [K.IsStrictlyGE n] :
    ((shiftFunctor (CochainComplex Ab ℤ) a).obj K).IsStrictlyGE (n - a) :=
  K.isStrictlyGE_shift a (n - a) (by ring)

/-- Mathlib4's `HomotopyCategory.Plus` gives a triangulated subcategory
of the homotopy category. This is the canonical implementation of K+(C). -/
example (C : Type u) [Category.{u} C] [Preadditive C] [HasZeroObject C]
    [HasBinaryBiproducts C] :
    HomotopyCategory.Plus C := by
  -- The zero object lives in K+(C)
  have : (HomotopyCategory.plus C).ContainsZero := by infer_instance
  obtain ⟨Z, _, _⟩ := this.exists_zero
  exact Z

end examples
