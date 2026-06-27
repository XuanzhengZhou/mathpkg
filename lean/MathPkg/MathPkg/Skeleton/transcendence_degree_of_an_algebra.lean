import Mathlib

open Cardinal
open Function
open Algebra
open scoped Classical

/-!
# Transcendence Degree of an Algebra

Let `A` be an algebra over a field `K`. The **transcendence degree** of `A` over `K`,
denoted `trdeg_K(A)`, is defined as

    trdeg_K(A) := sup { |T| | T ⊆ A, T algebraically independent over K }

where the supremum ranges over the cardinalities of all algebraically independent
subsets of `A` over `K`.

In the edge case where `A = {0}` is the zero ring, there are no nonempty algebraically
independent subsets, so `trdeg_K({0}) = 0`.

More generally, Mathlib4 defines `Algebra.trdeg R A` for any commutative algebra `A`
over a commutative ring `R`, taking values in `Cardinal`.

## Mathlib4 References

- `Algebra.trdeg` is defined in `Mathlib/RingTheory/AlgebraicIndependent/Basic.lean`
- It is the supremum over all `AlgebraicIndepOn R id s` of `Cardinal.mk s`
- `AlgebraicIndependent` uses `MvPolynomial.aeval` to test algebraic relations
-/

universe u v w

section transcendence_degree

variable (K : Type u) (A : Type v) [Field K] [CommRing A] [Algebra K A]

/--
The transcendence degree of a commutative `K`-algebra `A` (where `K` is a field)
is the maximal cardinality of a `K`-algebraically independent subset of `A`.

This is `Algebra.trdeg K A` from Mathlib4. For fields it coincides with
the textbook definition.
-/
noncomputable abbrev transcendenceDegree : Cardinal.{v} := Algebra.trdeg K A

end transcendence_degree

/-! ### Properties and Examples -/

section examples

/--
Example: The transcendence degree of a purely algebraic extension is zero.
If every element of `A` is algebraic over `K`, then `trdeg_K(A) = 0`.
-/
example (K A : Type*) [CommRing K] [CommRing A] [Algebra K A]
    [Algebra.IsAlgebraic K A] : Algebra.trdeg K A = 0 := by
  sorry
