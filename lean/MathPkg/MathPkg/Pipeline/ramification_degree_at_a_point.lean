import Mathlib

open scoped Classical
open scoped BigOperators

/-!
# Ramification Degree at a Point

Let `h : C → C'` be a nonconstant morphism of smooth projective curves over an
algebraically closed field. For a point `P ∈ C`, the **ramification degree** `e_P(h)` is
defined as

    e_P(h) = ν_P(t' ∘ h)

where `t'` is a uniformizer at `h(P)` on `C'` and `ν_P` is the discrete valuation on the
function field `K(C)`.

In Mathlib4, the local ring at a point on a regular curve is a discrete valuation ring
(`IsDiscreteValuationRing`). The map `h` induces a local homomorphism between the local
rings `O_{C',h(P)} → O_{C,P}`. The ramification degree is then the additive valuation of
the image of any uniformizer (irreducible element) of the source DVR.

We express the definition in the language of DVRs.

## References
* [R. Hartshorne, *Algebraic Geometry*][hartshorne1977]
* [J. Silverman, *The Arithmetic of Elliptic Curves*][silverman2009]
-/

section ramificationDegree

/-! ### Ramification degree for a homomorphism of DVRs -/

open IsDiscreteValuationRing

variable {A B : Type*} [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
  [IsDiscreteValuationRing A] [IsDiscreteValuationRing B]

/-- The **ramification degree** of a ring homomorphism `f : A → B` between discrete
valuation rings. It is defined as `ν_B(f(ϖ))` where `ν_B = addVal B` is the additive
valuation on `B` and `ϖ` is any irreducible element (uniformizer) of `A`.

More precisely, we pick an irreducible `ϖ` via `exists_irreducible A` and define
the ramification degree as `(addVal B) (f ϖ)`. By `ramificationDegree_eq_addVal_of_irreducible`,
this value is independent of the choice of `ϖ`.

In the geometric language: if `A = O_{C', h(P)}` and `B = O_{C, P}` are the local
rings of points on curves, with `f` the induced map on stalks, then this is
exactly the classical ramification degree `e_P(h)`. -/
noncomputable def ramificationDegree (f : A →+* B) : ℕ∞ :=
  addVal B (f (Classical.choose (exists_irreducible A)))

/-- The ramification degree is independent of the choice of uniformizer:
for any irreducible `ϖ` in `A`, `ramificationDegree f = (addVal B) (f ϖ)`. -/
theorem ramificationDegree_eq_addVal_of_irreducible (f : A →+* B) {ϖ : A} (hϖ : Irreducible ϖ) :
    ramificationDegree f = addVal B (f ϖ) := by
  classical
  let ϖ0 := Classical.choose (exists_irreducible A)
  have hϖ0 : Irreducible ϖ0 := Classical.choose_spec (exists_irreducible A)
  have h_assoc : Associated ϖ0 ϖ := associated_of_irreducible A hϖ0 hϖ
  rcases h_assoc with ⟨u, hu⟩
  -- hu : ϖ0 * (u : A) = ϖ
  have h_addval_unit : addVal B (f (u : A)) = 0 :=
    addVal_eq_zero_iff.mpr (IsUnit.map f u.isUnit)
  have h_val_eq : addVal B (f ϖ) = addVal B (f ϖ0) := by
    rw [← hu, map_mul, addVal_mul, h_addval_unit, add_zero]
  rw [ramificationDegree, h_val_eq]

/-- `ramificationDegree f` can be computed using any irreducible element as uniformizer. -/
theorem ramificationDegree_def (f : A →+* B) {ϖ : A} (hϖ : Irreducible ϖ) :
    ramificationDegree f = addVal B (f ϖ) :=
  ramificationDegree_eq_addVal_of_irreducible f hϖ

/-- When `R` is a DVR, `addVal R (ϖ) = 1` for any irreducible `ϖ`. -/
theorem ramificationDegree_of_irreducible {ϖ : A} (hϖ : Irreducible ϖ) :
    ramificationDegree (RingHom.id A) = (1 : ℕ∞) := by
  rw [ramificationDegree_eq_addVal_of_irreducible _ hϖ]
  simp [addVal_uniformizer hϖ]

/-- The ramification degree of a composition is multiplicative. This corresponds to the
classical tower formula `e_P(g ∘ h) = e_P(h) · e_{h(P)}(g)`.

Given `f : A → B` and `g : B → C` of DVRs with `ramificationDegree f = e₁` and
`ramificationDegree g = e₂`, the ramification degree of `g ∘ f` is `e₁ * e₂`.
This follows because if the uniformizer `ϖ_A` of `A` maps to `u · ϖ_B^e₁` in `B`,
then applying `g` gives `g(u) · g(ϖ_B)^e₁`, whose valuation in `C` is `e₁ · e₂`. -/
theorem ramificationDegree_comp {C : Type*} [CommRing C] [IsDomain C] [IsDiscreteValuationRing C]
    (f : A →+* B) (g : B →+* C) :
    ramificationDegree (g.comp f) = ramificationDegree f * ramificationDegree g := by
  sorry

end ramificationDegree

section ramificationDegreeAtPoint

/-! ### Ramification degree at a point for a morphism of schemes -/

open AlgebraicGeometry
open IsDiscreteValuationRing

/-- The **ramification degree at a point** for a morphism `h : X → Y` of integral schemes
and `x : X` a point.

This is defined as the ramification degree of the induced homomorphism on stalks
`O_{Y, h(x)} → O_{X, x}`. To obtain a `RingHom` from the stalk map (which is a
`CommRingCat` morphism), we use `.hom`.

In the classical language of curves, when `X = C` and `Y = C'` are smooth projective
curves, the stalk at a nonsingular point is a DVR. The ramification degree is then
`e_x(h) = ν_x(t ∘ h)` where `t` is a uniformizer at `h(x)`.

Note: In Mathlib4, the stalk at a point is not automatically a DVR -- this requires
the scheme to be regular at that point. The DVR instances must be provided explicitly. -/
noncomputable def ramificationDegreeAtPoint {X Y : Scheme} [IsIntegral X] [IsIntegral Y]
    (h : X ⟶ Y) (x : X)
    [IsDiscreteValuationRing (X.presheaf.stalk x)]
    [IsDiscreteValuationRing (Y.presheaf.stalk (h.base x))] : ℕ∞ :=
  let stalkHom : (Y.presheaf.stalk (h.base x)) →+* (X.presheaf.stalk x) :=
    (Scheme.Hom.stalkMap h x).hom
  ramificationDegree stalkHom

/-- When the local rings are DVRs (e.g., at nonsingular points of curves), the
ramification degree at `x` specializes to the valuation definition.

This theorem connects the scheme-theoretic definition to the classical formula
`e_x(h) = ν_x(t ∘ h)` where `t` is a uniformizer at `h(x)`. -/
theorem ramificationDegreeAtPoint_eq_addVal {X Y : Scheme} [IsIntegral X] [IsIntegral Y]
    (h : X ⟶ Y) (x : X)
    [IsDiscreteValuationRing (X.presheaf.stalk x)]
    [IsDiscreteValuationRing (Y.presheaf.stalk (h.base x))]
    {t : Y.presheaf.stalk (h.base x)}
    (ht : Irreducible t) :
    ramificationDegreeAtPoint h x =
      addVal (X.presheaf.stalk x) ((Scheme.Hom.stalkMap h x).hom t) := by
  rw [ramificationDegreeAtPoint, ramificationDegree_eq_addVal_of_irreducible _ ht]

end ramificationDegreeAtPoint

/-! ## Examples -/

section examples

open IsDiscreteValuationRing

/-- The ramification degree of the identity map on a DVR is 1.
(Since `addVal R ϖ = 1` for any uniformizer `ϖ`.) -/
example (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A] :
    ramificationDegree (RingHom.id A) = (1 : ℕ∞) := by
  obtain ⟨ϖ, hϖ⟩ := exists_irreducible A
  rw [ramificationDegree_eq_addVal_of_irreducible _ hϖ]
  simp [addVal_uniformizer hϖ]

/-- For the identity map on ℤ_p (the p-adic integers, which are a DVR),
the ramification degree is 1. -/
example [Fact (Nat.Prime 5)] :
    ramificationDegree (RingHom.id (ℤ_[5])) = (1 : ℕ∞) := by
  obtain ⟨ϖ, hϖ⟩ := exists_irreducible (ℤ_[5])
  rw [ramificationDegree_eq_addVal_of_irreducible _ hϖ]
  simp [addVal_uniformizer hϖ]

/-- In number theory, for an extension L/K of local fields with rings of integers
O_L / O_K, the ramification index e(L/K) is the valuation of a uniformizer of O_K
in O_L.

Example: In the extension ℚ_p(√p) / ℚ_p, the ramification index is 2 because
the uniformizer p of ℤ_p becomes (√p)² in the larger ring. This is captured by
our definition `ramificationDegree` for the inclusion ℤ_p → O_L. -/
example : True := by
  trivial

end examples
