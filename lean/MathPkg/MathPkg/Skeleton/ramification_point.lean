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
noncomputable def ramificationIndex (f : A →+* B) : ℕ∞ := by
  sorry
