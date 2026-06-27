import Mathlib

/-!
# Family as Morphism

A family of varieties parametrized by a base `B` is given by a morphism `φ : X → B`.
The members of the family are the fibers `φ⁻¹(b)` for points `b ∈ B`, which vary as
`b` moves in the base.

In Mathlib4 this perspective is captured by `AlgebraicGeometry.Scheme.Over B` —
a scheme `X` equipped with a structure morphism `X ↘ B : X ⟶ B`.
This definition asserts that any morphism `X ⟶ B` determines a family over `B`.
-/

open AlgebraicGeometry

universe u

/-- Given a morphism `φ : X ⟶ B` of schemes, view `(X, φ)` as a family over `B`
(i.e., an object in the slice category `Over B`). -/
def family_as_morphism {X B : Scheme.{u}} (φ : X ⟶ B) : CategoryTheory.Over B := by
  sorry
