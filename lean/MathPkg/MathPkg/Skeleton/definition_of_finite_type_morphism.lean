import Mathlib

/-!
# Definition of Finite Type Morphism

A morphism of schemes `f : X ⟶ Y` is **of finite type** if the extensions of local rings
`𝒪_{Y, f(x)} → 𝒪_{X, x}` are finitely generated algebras for all points `x ∈ X`.

In Mathlib4, this corresponds to the conjunction of two properties already defined:
`LocallyOfFiniteType f` (from `AlgebraicGeometry/Morphisms/FiniteType.lean`) and
`QuasiCompact f` (from `AlgebraicGeometry/Morphisms/QuasiCompact.lean`).

## Mathlib4 References
- `LocallyOfFiniteType` in `AlgebraicGeometry/Morphisms/FiniteType.lean`
- `QuasiCompact` in `AlgebraicGeometry/Morphisms/QuasiCompact.lean`
-/

open AlgebraicGeometry

universe u

/-- A morphism `f : X → Y` of schemes is **of finite type** if it is locally of finite type
and quasi-compact. This bundles the two properties into a single predicate for convenience. -/
def IsFiniteType {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop := by
  sorry
