import Mathlib

open scoped Classical

/-!
# Definition: Lying over and going up

For an integral extension `R ⊆ S`:

- A prime ideal `Q ∈ Spec(S)` is said to **lie over** a prime ideal `P ∈ Spec(R)` if
  `R ∩ Q = P` (i.e., the contraction of `Q` to `R` is `P`).

- If additionally an ideal `I ⊆ S` is contained in `Q`, we say that we are **going up**
  from `I` (to `Q`, which lies over `P`).

In Mathlib4:

- **Lying Over**: `Ideal.LiesOver` (in `Mathlib/RingTheory/Ideal/Over.lean`) is a typeclass
  with field `over : p = P.under A`, i.e., `p` is the contraction of `P` from `S` to `R`.
  Here `P.under R := Ideal.comap (algebraMap R S) P`.

- **Going Up**: The theorem `exists_ideal_over_prime_of_isIntegral` (in
  `Mathlib/RingTheory/Ideal/GoingUp.lean`) states that for an integral extension `R ⊆ S`,
  given a prime `P` of `R` and an ideal `I` of `S` whose contraction is contained in `P`,
  there exists a prime `Q ≥ I` of `S` lying over `P`.

- **primesOver**: The set `Ideal.primesOver p S` collects all prime ideals of `S` that lie
  over a given prime ideal `p` of `R`.

We define an explicit predicate `GoingUpFrom` to capture the "going up from I" notion.
-/

noncomputable section

/-! ### 1. Lying Over (already in Mathlib4) -/

section lying_over

variable (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S]

/--
`P` lies over `p` if `p` is the contraction of `P` to `R`, i.e. `p = P.under R`.

This is the Mathlib4 typeclass `Ideal.LiesOver`.
-/
example (p : Ideal R) (P : Ideal S) [P.LiesOver p] : p = P.under R := by
  sorry
