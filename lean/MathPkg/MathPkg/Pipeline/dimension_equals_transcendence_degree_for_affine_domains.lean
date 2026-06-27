import Mathlib

open scoped Classical

/-!
# Dimension equals transcendence degree for affine domains

If R is an affine domain over a field k, then the Krull dimension of R equals the
transcendence degree of its field of fractions over k.

An **affine domain** is a finitely generated k-algebra that is also an integral domain.
The theorem states `dim R = tr.deg_k R`, connecting the geometric notion of dimension
to the field-theoretic notion of transcendence degree.

In Mathlib4:
* `ringKrullDim R` is the Krull dimension of R, a value in `WithBot ℕ∞`.
* `trdeg k (FractionRing R)` is the transcendence degree, a `Cardinal`.
  For an affine domain, it is finite (< ℵ₀) by `trdeg_lt_aleph0`.
* `Algebra.FiniteType k R` expresses that R is a finitely generated k-algebra.

This is a classical result in commutative algebra: for an affine k-algebra that is
an integral domain, the geometric dimension (length of longest chain of prime ideals)
coincides with the transcendence degree of its function field over k.

## Dependencies

* `noether_normalization` — Noether normalization lemma

## References

* [Matsumura, *Commutative Algebra*, Theorem 5.6][matsumura1980commutative]
* [Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry*, §13][eisenbud1995commutative]
-/

section dimension_equals_transcendence_degree

open scoped KrullDimension

/-- If R is an affine domain over a field k, then the Krull dimension of R equals
the transcendence degree of `FractionRing R` over k.

Both sides are finite natural numbers for an affine domain. We express the equality by
converting the transcendence degree (a `Cardinal`) to `ℕ∞` via `Cardinal.toNat`. -/
theorem dimension_equals_transcendence_degree_for_affine_domains
    (k : Type*) [Field k] (R : Type*) [CommRing R] [Algebra k R] [IsDomain R] [Algebra.FiniteType k R] :
    ringKrullDim R = (Cardinal.toNat (trdeg k (FractionRing R)) : ℕ∞) := by
  sorry

end dimension_equals_transcendence_degree
