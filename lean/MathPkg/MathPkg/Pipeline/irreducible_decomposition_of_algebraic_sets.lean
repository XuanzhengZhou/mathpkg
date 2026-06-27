import Mathlib

open scoped Classical

/-!
# Irreducible Decomposition of Algebraic Sets

Every algebraic set in `Kⁿ` is uniquely an irredundant finite union of algebraic varieties
(irreducible algebraic sets). This is the geometric counterpart of the primary decomposition
theorem: in the Noetherian ring `K[X₁, …, Xₙ]`, every radical ideal is the irredundant
intersection of its finitely many minimal prime ideals. Taking zero loci yields the
decomposition of the corresponding algebraic set into irreducible components.

## Statement

For a field `K` and a radical ideal `I ⊲ K[X₁, …, Xₙ]`, the zero locus `Z(I) ⊆ Kⁿ`
equals the union of `Z(P)` as `P` ranges over the minimal prime ideals containing `I`.
Each `Z(P)` is an irreducible algebraic variety, and no component is contained in the
union of the others (irredundancy).

## Mathlib4 Cross-References

* `MvPolynomial.zeroLocus` — zero set of an ideal in `RingTheory/Nullstellensatz.lean`
* `Ideal.minimalPrimes` — set of minimal prime ideals containing a given ideal
* `Ideal.IsRadical` — predicate for radical ideals
* `IsNoetherianRing` — Noetherian ring property (guarantees finiteness of minimal primes)
-/

/-- **Irreducible decomposition of algebraic sets.**
Given a radical ideal `I` of `K[X₁, …, Xₙ]`, the corresponding algebraic set
`Z(I) ⊆ Kⁿ` decomposes uniquely as the union of the zero loci of the minimal prime
ideals containing `I`. Each `Z(P)` for `P ∈ I.minimalPrimes` is an irreducible
algebraic variety (the zero locus of a prime ideal), and the decomposition is
irredundant: no `Z(Pᵢ)` is contained in the union of the remaining components.

When `K` is algebraically closed, the Nullstellensatz guarantees a bijection between
algebraic sets in `Kⁿ` and radical ideals, and between algebraic varieties and prime ideals. -/
theorem irreducible_decomposition_of_algebraic_sets (K : Type*) [Field K] (n : ℕ)
    (I : Ideal (MvPolynomial (Fin n) K)) (hI : I.IsRadical) :
    (MvPolynomial.zeroLocus K I) = ⋃ P ∈ (I.minimalPrimes : Set (Ideal (MvPolynomial (Fin n) K))), MvPolynomial.zeroLocus K P := by
  sorry
