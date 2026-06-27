import Mathlib

open scoped Classical

/-!
# Definition of Contraction and Lies Over

If `S` is an extension ring of `R` and `I` is an ideal of `S`, then `I ∩ R` is an ideal of `R`
called the **contraction** of `I` to `R`, and `I` is said to **lie over** `J = I ∩ R`.
If `Q` is a prime ideal in `S`, then `Q ∩ R` is a prime ideal of `R`.

In Mathlib4, this is formalized in `Mathlib/RingTheory/Ideal/Over.lean`:
- **Contraction**: `Ideal.under A P := Ideal.comap (algebraMap A B) P`
- **Lies Over**: `Ideal.LiesOver` is a typeclass with field `over : p = P.under A`
- **Prime contraction**: The instance `IsPrime.under` proves that `P.under A` is prime.
- **primesOver**: The set of all prime ideals lying over a given ideal.

## Sub-concepts

- **Going-up / Going-down**: Properties of ring extensions concerning chains of prime ideals
  lying over each other.
- **Incomparability**: Two prime ideals lying over the same prime ideal are incomparable.
-/

noncomputable section

/-! ### 1. Contraction of an ideal to a subring -/

section contraction

variable (R S : Type*) [CommSemiring R] [Semiring S] [Algebra R S]

/-- The contraction of an ideal `I` of `S` to `R` is `I ∩ R`, realized as `Ideal.under R I`. -/
example (I : Ideal S) : I.under R = Ideal.comap (algebraMap R S) I := by
  sorry
