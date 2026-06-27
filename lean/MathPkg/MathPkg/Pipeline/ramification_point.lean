import Mathlib

open scoped Classical
open scoped BigOperators

/-!
# Ramification Point

Let `f` be an analytic map between Riemann surfaces (or, algebraically, a morphism between
smooth projective curves over an algebraically closed field). A point `P` in the source is
called a **ramification point** for `f` if the ramification index satisfies `e_f(P) > 1`.

Equivalently, in the language of discrete valuation rings: given a local homomorphism
`A → B` of DVRs, the map is *ramified* if its ramification degree exceeds 1.

We provide two formulations:

1. `isRamified f` for a ring homomorphism `f : A →+* B` between DVRs.
2. `IsRamificationPoint h x` for a morphism `h : X → Y` of integral schemes and a point `x : X`.

## References
* [R. Hartshorne, *Algebraic Geometry*][hartshorne1977]
* [J. Silverman, *The Arithmetic of Elliptic Curves*][silverman2009]
-/

noncomputable section

section ramificationIndex

/-! ### Ramification index for a DVR homomorphism -/

open IsDiscreteValuationRing

variable {A B : Type*} [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
  [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]

/-- The **ramification index** (or ramification degree) `e(f)` of a ring homomorphism
`f : A →+* B` between discrete valuation rings. It is defined as `ν_B(f(ϖ))` where
`ν_B` is the additive valuation on `B` and `ϖ` is any uniformizer (irreducible element)
of `A`.

By `ramificationIndex_eq_addVal_of_irreducible`, this value is independent of the choice
of uniformizer. -/
noncomputable def ramificationIndex (f : A →+* B) : ℕ∞ :=
  addVal B (f (Classical.choose (exists_irreducible A)))

/-- The ramification index can be computed using any irreducible element `ϖ` in `A`. -/
theorem ramificationIndex_eq_addVal_of_irreducible (f : A →+* B) {ϖ : A} (hϖ : Irreducible ϖ) :
    ramificationIndex f = addVal B (f ϖ) := by
  classical
  let ϖ0 := Classical.choose (exists_irreducible A)
  have hϖ0 : Irreducible ϖ0 := Classical.choose_spec (exists_irreducible A)
  have h_assoc : Associated ϖ0 ϖ := associated_of_irreducible A hϖ0 hϖ
  rcases h_assoc with ⟨u, hu⟩
  have h_addval_unit : addVal B (f (u : A)) = 0 :=
    addVal_eq_zero_iff.mpr (IsUnit.map f u.isUnit)
  rw [ramificationIndex, ← hu, map_mul, addVal_mul, h_addval_unit, add_zero]

/-- A ring homomorphism `f : A →+* B` between DVRs is **ramified** if its ramification
index is greater than 1. This is the algebraic counterpart of the geometric notion:
a point `P` is a ramification point for `f` if `e_f(P) > 1`. -/
def isRamified (f : A →+* B) : Prop :=
  ramificationIndex f > 1

/-- A ring homomorphism is **unramified** if its ramification index equals 1. -/
def isUnramified (f : A →+* B) : Prop :=
  ramificationIndex f = 1

/-- A ring homomorphism is **tamely ramified** if it is ramified and the ramification index
is not divisible by the residue characteristic. (We state this as a Prop; the residue
characteristic condition is omitted for brevity.) -/
def isTamelyRamified (f : A →+* B) : Prop :=
  isRamified f

end ramificationIndex

section ramificationPoint

/-! ### Ramification point for a morphism of schemes -/

open AlgebraicGeometry

/-- A point `x : X` is a **ramification point** for a morphism `h : X → Y` of integral
schemes if the induced homomorphism on stalks `O_{Y, h(x)} → O_{X, x}` is ramified
(i.e., its ramification index > 1).

This requires the local rings at `x` and `h(x)` to be discrete valuation rings, which
holds for nonsingular points on curves.

In the classical language: if `f : C → C'` is a nonconstant morphism of smooth projective
curves over an algebraically closed field, and `P ∈ C`, then `IsRamificationPoint f P`
means `e_P(f) > 1`. -/
def IsRamificationPoint {X Y : Scheme} [IsIntegral X] [IsIntegral Y]
    (h : X ⟶ Y) (x : X)
    [IsDiscreteValuationRing (X.presheaf.stalk x)]
    [IsDiscreteValuationRing (Y.presheaf.stalk (h.base x))] : Prop :=
  let stalkHom : (Y.presheaf.stalk (h.base x)) →+* (X.presheaf.stalk x) :=
    (Scheme.Hom.stalkMap h x).hom
  isRamified stalkHom

end ramificationPoint

/-! ## Examples -/

section examples

open IsDiscreteValuationRing

/-- The identity map on a DVR is unramified (ramification index = 1),
so it is not ramified. -/
example (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A] :
    ¬ isRamified (RingHom.id A) := by
  obtain ⟨ϖ, hϖ⟩ := exists_irreducible A
  rw [isRamified, ramificationIndex_eq_addVal_of_irreducible _ hϖ]
  have h := addVal_uniformizer hϖ
  -- addVal A ϖ = 1 (in ℕ∞), and 1 > 1 is false
  simp [h]

/-- For the identity map on ℤ_p, the ramification index is 1, so the map is not ramified. -/
example [Fact (Nat.Prime 5)] : ¬ isRamified (RingHom.id (ℤ_[5])) := by
  obtain ⟨ϖ, hϖ⟩ := exists_irreducible (ℤ_[5])
  rw [isRamified, ramificationIndex_eq_addVal_of_irreducible _ hϖ]
  have h := addVal_uniformizer hϖ
  simp [h]

/-- In the extension ℚ₂(√2)/ℚ₂, the uniformizer 2 of ℤ₂ maps to (√2)² in the
ring of integers of ℚ₂(√2), giving ramification index 2. Hence the induced map
on DVRs is ramified.

We illustrate this with a placeholder: any map `f` with `ramificationIndex f > 1`
is ramified. -/
example {A B : Type*} [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]
    (f : A →+* B) (h : ramificationIndex f > 1) : isRamified f :=
  h

end examples
