import Mathlib

/-!
# Algebraic Variety Definition

An **algebraic set** `A ⊆ Kⁿ` is irreducible, or an **algebraic variety**, if `A ≠ ∅`
and `A` is the zero set of a prime ideal.

In classical algebraic geometry (over an algebraically closed field), the
irreducibility of an algebraic set is equivalent to its vanishing ideal being prime.
This file formalizes the definition using multivariate polynomials over a field.

## Main Definitions
* `AlgebraicSet K n S` -- the common zero locus in `Kⁿ` of a set `S` of polynomials.
* `IsAlgebraicVariety A` -- the predicate that `A` is a nonempty algebraic set
  that is the zero locus of a prime ideal.

## Mathlib4 Cross-References
* `Ideal.IsPrime` -- prime ideal typeclass (`RingTheory/Ideal/Prime.lean`)
* `Ideal.bot_prime` -- the zero ideal is prime in a domain
* `MvPolynomial.eval` -- evaluation of multivariate polynomials
* `IsIrreducible` (in `Topology/Irreducible.lean`) -- topological irreducibility of a set;
  for algebraic sets in the Zariski topology this coincides with the prime-ideal criterion.
-/

open Set

variable {K : Type*} [Field K] {n : ℕ}

/-- An **algebraic set** in `Kⁿ` is the common zero set of a collection of
multivariate polynomials. Given `S : Set (MvPolynomial (Fin n) K)`, the algebraic set
`AlgebraicSet S` consists of all points `x ∈ Kⁿ` such that every `p ∈ S` evaluates
to zero at `x`. -/
def AlgebraicSet (S : Set (MvPolynomial (Fin n) K)) : Set (Fin n → K) := by
  sorry
