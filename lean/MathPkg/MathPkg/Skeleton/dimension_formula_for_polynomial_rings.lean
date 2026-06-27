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
