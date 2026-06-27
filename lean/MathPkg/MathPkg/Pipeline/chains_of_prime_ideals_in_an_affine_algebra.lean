import Mathlib

open Ideal

/-!
# Chains of prime ideals in an affine algebra

Let `A` be an affine algebra over a field `K` (i.e., a finitely generated `K`-algebra).
If `P₀ ⊊ P₁ ⊊ ... ⊊ Pₙ` is a maximal chain of prime ideals in `Spec(A)`, then
`n = dim(A/P₀)`.

In particular, if `A` is equidimensional (which is always the case if `A` is an affine domain),
then every maximal chain of prime ideals of `A` has length equal to `dim(A)`.

The proof proceeds by induction on `n`. Replacing `A` by `A/P₀` reduces to the case where
`A` is an affine domain and `P₀ = {0}`. If `n = 0`, then `{0}` is a maximal ideal, so `A`
is a field and `dim(A) = 0 = n`.
-/

/-- **Chains of prime ideals in an affine algebra**
Given a finitely generated algebra `A` over a field `K` and a maximal chain of prime ideals
`P₀ ⊊ P₁ ⊊ ... ⊊ Pₙ` in `Spec(A)` (represented as an `LTSeries` of maximal length),
the length `n` of the chain equals the Krull dimension of `A/P₀`. -/
theorem chains_of_prime_ideals_in_an_affine_algebra
    {K A : Type*} [Field K] [CommRing A] [Algebra K A] [Algebra.FiniteType K A]
    (p : LTSeries (PrimeSpectrum A))
    (hchain_max : ∀ (q : LTSeries (PrimeSpectrum A)), q.length ≤ p.length) :
    (p.length : WithBot ℕ∞) = ringKrullDim (A ⧸ (p 0).asIdeal) := by
  sorry
