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
noncomputable def ramificationDegree (f : A →+* B) : ℕ∞ := by
  sorry
