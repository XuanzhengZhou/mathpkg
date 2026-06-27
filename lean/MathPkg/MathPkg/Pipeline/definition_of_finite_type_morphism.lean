import Mathlib
import Mathlib.AlgebraicGeometry.Morphisms.FiniteType
import Mathlib.AlgebraicGeometry.Morphisms.QuasiCompact

/-!
# Definition of Finite Type Morphism

A morphism of schemes `f : X ⟶ Y` is **of finite type** if the extensions of local rings
`𝒪_{Y, f(x)} → 𝒪_{X, x}` are finitely generated algebras for all points `x ∈ X`.

In Mathlib4, this is captured by two separate typeclasses:

- `LocallyOfFiniteType f`: the induced map `Γ(Y, U) → Γ(X, V)` is a ring homomorphism of finite
  type for all affine opens `U ⊆ Y` and `V ⊆ f⁻¹(U)`. This is the algebraic core of the
  definition (cf. `AlgebraicGeometry/Morphisms/FiniteType.lean`).

- `QuasiCompact f`: the preimage of every quasi-compact open in `Y` is quasi-compact in `X`
  (cf. `AlgebraicGeometry/Morphisms/QuasiCompact.lean`).

A morphism is **of finite type** if it satisfies both properties simultaneously
([Stacks Project, Tag 01T0](https://stacks.math.columbia.edu/tag/01T0)).

We provide the combined class `IsFiniteType` for convenience.

## Mathlib4 References
- `LocallyOfFiniteType` in `AlgebraicGeometry/Morphisms/FiniteType.lean`
- `QuasiCompact` in `AlgebraicGeometry/Morphisms/QuasiCompact.lean`
- `RingHom.FiniteType` / `Algebra.FiniteType` in `RingTheory/FiniteType.lean`
-/

open AlgebraicGeometry

universe u

/-! ### Combined class for finite type morphisms -/

/-- A morphism of schemes `f : X ⟶ Y` is **of finite type** if it is both
**locally of finite type** and **quasi-compact**.

This class bundles the two properties for convenience; it is equivalent to
`[LocallyOfFiniteType f] [QuasiCompact f]`.

At the level of local rings, for each `x ∈ X`, the induced map
`𝒪_{Y, f(x)} → 𝒪_{X, x}` makes `𝒪_{X, x}` a finitely generated `𝒪_{Y, f(x)}`-algebra,
and the topological preimage condition ensures "finiteness" is not just local but global. -/
class IsFiniteType {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop extends
  LocallyOfFiniteType f, QuasiCompact f

/-! ### Examples -/

section examples

variable {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)

/-- The identity morphism `𝟙 X` is always of finite type.
This follows from the fact that `LocallyOfFiniteType` and `QuasiCompact` are
both multiplicative (contain all identity morphisms). -/
example : IsFiniteType (𝟙 X : X ⟶ X) where
  toLocallyOfFiniteType := inferInstance
  toQuasiCompact := inferInstance

/-- Composition of finite type morphisms is of finite type.
Both `LocallyOfFiniteType` and `QuasiCompact` are stable under composition
(instances `locallyOfFiniteType_comp` and `quasiCompact_comp` in Mathlib4). -/
example [IsFiniteType f] [IsFiniteType g] : IsFiniteType (f ≫ g) where
  toLocallyOfFiniteType := inferInstance
  toQuasiCompact := inferInstance

/-- For affine schemes, a ring homomorphism of finite type `φ : R →+* S` induces a
finite type morphism `Spec S → Spec R`. This connects the ring-theoretic definition
(`RingHom.FiniteType`) to the geometric definition (`LocallyOfFiniteType`).

The combined `IsFiniteType` also requires quasi-compactness, which holds because
`Spec R` and `Spec S` are quasi-compact. -/
example {R S : CommRingCat.{u}} (φ : R ⟶ S) (hφ : φ.hom.FiniteType) :
    LocallyOfFiniteType (Spec.map φ) :=
  HasRingHomProperty.Spec_iff.mpr hφ

/-- At the ring level, `RingHom.FiniteType` means `B` is a finitely generated `A`-algebra.
For a local ring homomorphism `(A, m) → (B, n)` induced by a scheme morphism, this
is exactly the condition that "the extension of local rings is finitely generated." -/
example (A B : Type u) [CommRing A] [CommRing B] [Algebra A B] :
    ((algebraMap A B).FiniteType ↔ Algebra.FiniteType A B) :=
  RingHom.finiteType_algebraMap

end examples
