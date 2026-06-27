import Mathlib

open scoped Classical

/-!
# Maximal Ideals of the Coordinate Ring

For an algebraic set `A` over an algebraically closed field `K`, define
`m_x = { f ∈ C(A) | f(x) = 0 }` for `x ∈ A`. The map `x ↦ m_x` is a bijection
from `A` onto the set of all maximal ideals of the coordinate ring `C(A)`.

This is a consequence of Hilbert's Nullstellensatz: over an algebraically closed
field, maximal ideals of `K[X₁,…,Xₙ]` correspond to points of `Kⁿ`, and
maximal ideals of `C(A) = K[X_σ] / I(A)` correspond to points of `A`.

## Main definitions

* `evalAtPoint` : The evaluation homomorphism `C(A) → K` at a point `x ∈ A`
* `pointIdeal` : The maximal ideal `m_x = {f ∈ C(A) | f(x) = 0}`
* `pointIdeal_isMaximal` : `pointIdeal` is a maximal ideal of `C(A)`
* `maximal_ideals_of_the_coordinate_ring` : The map `x ↦ pointIdeal x` is a bijection
  from `A` onto the set of all maximal ideals of `C(A)`

## References

* `Mathlib/FieldTheory/IsAlgClosed/Basic.lean` for algebraically closed fields
* `Mathlib/RingTheory/Nullstellensatz.lean` for Hilbert's Nullstellensatz
* `Mathlib/RingTheory/Ideal/Quotient.lean` for quotient ring constructions
-/

section MaximalIdealCorrespondence

variable (K : Type*) [Field K] [IsAlgClosed K] {σ : Type*}

/-- The evaluation ring homomorphism `C(A) → K` at a point `x ∈ A`. For a polynomial
class `[p] ∈ C(A) = K[X_σ]/I(A)`, this sends it to `p(x)`. The quotient is well-defined
because if `p ∈ I(A)`, then `p(x) = 0` for all `x ∈ A`. -/
noncomputable def evalAtPoint (A : Set (σ → K)) (x : A) : coordinateRing K A →+* K := by
  sorry

/-- The ideal `m_x = {f ∈ C(A) | f(x) = 0}` of functions in the coordinate ring
that vanish at the point `x ∈ A`. This is the kernel of the evaluation homomorphism
`evalAtPoint x`. -/
def pointIdeal (A : Set (σ → K)) (x : A) : Ideal (coordinateRing K A) :=
  RingHom.ker (evalAtPoint K A x)

/-- Via Hilbert's Nullstellensatz (over an algebraically closed field `K`),
`m_x` is a **maximal** ideal of the coordinate ring `C(A)`. -/
theorem pointIdeal_isMaximal (A : Set (σ → K)) (x : A) : (pointIdeal K A x).IsMaximal := by
  sorry

end MaximalIdealCorrespondence

/-- **Maximal ideal correspondence for coordinate rings.**

For an algebraic set `A` over an algebraically closed field `K`, the map
`x ↦ m_x = {f ∈ C(A) | f(x) = 0}` is a bijection from `A` onto the set of all
maximal ideals of the coordinate ring `C(A)`.

This establishes the fundamental link between points of an algebraic set and
the algebraic structure of its coordinate ring. -/
theorem maximal_ideals_of_the_coordinate_ring {K : Type*} [Field K] [IsAlgClosed K] {σ : Type*}
    (A : Set (σ → K)) :
    Function.Bijective (fun (x : A) =>
      ⟨pointIdeal K A x, pointIdeal_isMaximal K A x⟩ :
      A → {J : Ideal (coordinateRing K A) // J.IsMaximal}) := by
  sorry
