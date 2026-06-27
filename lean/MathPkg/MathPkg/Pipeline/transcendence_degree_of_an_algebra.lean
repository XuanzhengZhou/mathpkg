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
abbrev transcendenceDegree : Cardinal.{v} := Algebra.trdeg K A

end transcendence_degree

/-! ### Properties and Examples -/

section examples

/--
Example: The transcendence degree of a purely algebraic extension is zero.
If every element of `A` is algebraic over `K`, then `trdeg_K(A) = 0`.
-/
example (K A : Type*) [CommRing K] [CommRing A] [Algebra K A]
    [Algebra.IsAlgebraic K A] : Algebra.trdeg K A = 0 :=
  trdeg_eq_zero

/--
Example: The transcendence degree of `K[X]` (polynomial ring in one variable)
over a domain `K` is 1.
-/
example (K : Type*) [CommRing K] [IsDomain K] [Nontrivial K] :
    Algebra.trdeg K (Polynomial K) = 1 :=
  Polynomial.trdeg_of_isDomain (R := K)

/--
Example: The transcendence degree of `K[X₁, …, Xₙ]` (multivariate polynomial ring
over a domain `K`) is `#ι` (the cardinality of the set of indeterminates),
appropriately universe-lifted.
-/
example (K : Type u) [CommRing K] [IsDomain K] [Nontrivial K] (ι : Type v) :
    Algebra.trdeg K (MvPolynomial ι K) = lift.{v} #ι :=
  MvPolynomial.trdeg_of_isDomain (S := K) (ι := ι)

/--
Example: The transcendence degree is monotone with respect to injective
algebra homomorphisms. If `f : A →ₐ[K] B` is injective, then
`trdeg_K(A) ≤ trdeg_K(B)`.
-/
example (K A B : Type v) [CommRing K] [CommRing A] [CommRing B]
    [Algebra K A] [Algebra K B] (f : A →ₐ[K] B) (hf : Injective f) :
    Algebra.trdeg K A ≤ Algebra.trdeg K B :=
  trdeg_le_of_injective f hf

/--
Example: An algebraically independent set of size `κ` witnesses that
the transcendence degree is at least `κ`.
-/
example (K A : Type v) [CommRing K] [CommRing A] [Algebra K A] [Nontrivial K]
    {ι : Type v} {x : ι → A} (hx : AlgebraicIndependent K x) :
    #ι ≤ Algebra.trdeg K A :=
  hx.cardinalMk_le_trdeg

/--
Example: For a finitely generated extension, the transcendence degree is less
than `ℵ₀` (the cardinality of `ℕ`), i.e., it is finite.
-/
example (K S : Type*) [CommRing K] [CommRing S] [IsDomain K] [IsDomain S]
    [Algebra K S] [FiniteType K S] :
    Algebra.trdeg K S < ℵ₀ :=
  trdeg_lt_aleph0 K S

/--
Example: The transcendence degree of the zero ring `ℤ/1ℤ` (the ring with one element)
over itself is 0, since there are no nonempty algebraically independent subsets.
-/
example : Algebra.trdeg (ZMod 1) (ZMod 1) = 0 := by
  have : Subsingleton (ZMod 1) := by infer_instance
  have h : ¬ Injective (algebraMap (ZMod 1) (ZMod 1)) := by
    -- In the zero ring, the algebraMap cannot be injective
    -- (unless we consider it trivially, but ZMod 1 has only 0=1)
    intro hinj
    apply zero_ne_one (ZMod 1)
    exact hinj (by simp)
  exact trdeg_eq_zero_of_not_injective (R := ZMod 1) (A := ZMod 1) h

end examples
