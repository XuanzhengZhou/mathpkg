import Mathlib

/-!
# Factor Theorem

Let `R` be a commutative ring, `r ∈ R`, and `A ∈ R[X]`. Then `A` is a multiple of
`X - r` if and only if `A(r) = 0`.
-/

open Polynomial

/--
**Factor Theorem.** For a commutative ring `R`, an element `r : R`, and a polynomial
`p : Polynomial R`, the polynomial `X - C r` divides `p` if and only if evaluating
`p` at `r` yields zero.
-/
theorem factor_theorem {R : Type*} [CommRing R] (r : R) (p : Polynomial R) :
    (X - C r) ∣ p ↔ eval r p = 0 := by
  sorry
