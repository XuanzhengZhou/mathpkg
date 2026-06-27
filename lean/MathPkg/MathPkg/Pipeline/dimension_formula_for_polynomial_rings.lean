import Mathlib

/-! # Dimension Formula for Polynomial Rings

Let `R` be a commutative ring and `R[x]` the polynomial ring in one variable.

-/
open Polynomial
open MvPolynomial

/-- **(a)** If `k` is a field, then the Krull dimension of `k[x₁,…,xᵣ]` is `r`. -/
theorem ringKrullDim_mvPolynomial_field (k : Type u) [Field k] (r : ℕ) :
    ringKrullDim (MvPolynomial (Fin r) k) = (r : ℕ∞) := by
  sorry

/-- **(b)** For any Noetherian commutative ring `R`, `dim R[x] = 1 + dim R`. -/
theorem ringKrullDim_polynomial (R : Type u) [CommRing R] [IsNoetherianRing R] :
    ringKrullDim (Polynomial R) = ringKrullDim R + 1 := by
  sorry

/-- **(c)** If `P` is a prime ideal of a Noetherian ring `R`, there exists a prime ideal `Q` of
`R[x]` lying over `P` such that `dim (R[x]_Q) = 1 + dim (R_P)`. -/
theorem exists_prime_liesOver_and_ringKrullDim_localization_eq_add_one
    (R : Type u) [CommRing R] [IsNoetherianRing R] (P : Ideal R) [P.IsPrime] :
    ∃ (Q : Ideal (Polynomial R)) (_ : Q.IsPrime) (_ : Q.LiesOver P),
      ringKrullDim (Localization.AtPrime Q) = ringKrullDim (Localization.AtPrime P) + 1 := by
  sorry
