import Mathlib

open scoped Classical
open scoped BigOperators

/-!
# Zero Set of Polynomials

Let `K` be a field and `K` its algebraic closure (or any field extension).
For a set `S ⊆ K[X₁, ..., Xₙ]`, the **zero set** is

    Z(S) = { x ∈ Kⁿ | f(x) = 0 for all f ∈ S }.

Mathlib4 already defines this concept as `MvPolynomial.zeroLocus` in
`Mathlib/RingTheory/Nullstellensatz.lean`.  This file re-exports that definition
and adds convenience wrappers that accept an arbitrary set `S` of polynomials
(rather than requiring an ideal).
-/

section zero_set_of_polynomials

open MvPolynomial

variable {k K : Type*} [Field k] [Field K] [Algebra k K]
variable {σ : Type*}

/-- The zero set of a set of polynomials `S ⊆ K[X₁, ..., Xₙ]`:
`Z(S) = { x ∈ Kⁿ | f(x) = 0 for all f ∈ S }`.

This is defined as the zero locus of the ideal spanned by `S`,
using `MvPolynomial.zeroLocus` from `RingTheory/Nullstellensatz`.
-/
def zeroSet (S : Set (MvPolynomial σ k)) : Set (σ → K) := by
  sorry

end zero_set_of_polynomials
