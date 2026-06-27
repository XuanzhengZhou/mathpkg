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
def AlgebraicSet (S : Set (MvPolynomial (Fin n) K)) : Set (Fin n → K) :=
  { x | ∀ p ∈ S, MvPolynomial.eval x p = 0 }

/-- An **algebraic variety** (irreducible algebraic set) is a nonempty algebraic set
that can be expressed as the zero set of a **prime ideal** of polynomials.

Formally, `A ⊆ Kⁿ` is an algebraic variety if `A ≠ ∅` and there exists a prime ideal
`I ⊲ K[X₁, …, Xₙ]` such that `A = {x ∈ Kⁿ | ∀ p ∈ I, p(x) = 0}`.

This captures the classical definition: an algebraic set is a variety exactly when
its vanishing ideal is prime (or, over an algebraically closed field, when it is
irreducible in the Zariski topology). -/
def IsAlgebraicVariety (A : Set (Fin n → K)) : Prop :=
  A.Nonempty ∧ ∃ (I : Ideal (MvPolynomial (Fin n) K)), I.IsPrime ∧
    A = AlgebraicSet (I : Set (MvPolynomial (Fin n) K))

/-! ## Examples -/

/-- The whole affine space `Kⁿ` is an algebraic variety.
It is the zero set of the zero ideal `(0)`, which is prime because
`K[X₁,…,Xₙ]` is an integral domain. -/
example : IsAlgebraicVariety (Set.univ : Set (Fin n → K)) := by
  have h_nonempty : (Set.univ : Set (Fin n → K)).Nonempty :=
    ⟨λ _ => 0, Set.mem_univ _⟩
  have hprime : (⊥ : Ideal (MvPolynomial (Fin n) K)).IsPrime :=
    Ideal.bot_prime
  refine ⟨h_nonempty, ⊥, hprime, ?_⟩
  ext x; simp [AlgebraicSet]

/-- The empty set is NOT an algebraic variety (fails the nonempty condition). -/
example : ¬ IsAlgebraicVariety (∅ : Set (Fin n → K)) := by
  intro h
  rcases h with ⟨hne, _⟩
  exact hne.ne_empty rfl

/-- Using `AlgebraicSet` directly: the hyperplane defined by `X₁ = 0`.
This algebraic set is irreducible when `n ≥ 2`, but we only demonstrate
the construction here. -/
example : AlgebraicSet ({MvPolynomial.X 0} : Set (MvPolynomial (Fin 2) K)) =
    { x : Fin 2 → K | x 0 = 0 } := by
  ext x; simp [AlgebraicSet, MvPolynomial.eval_X]
