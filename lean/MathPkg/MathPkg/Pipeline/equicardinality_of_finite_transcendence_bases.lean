import Mathlib

open Cardinal
open scoped Classical

/-!
# Equicardinality of Finite Transcendence Bases

Let `F` be an extension field of `K`. If `S` is a finite transcendence base of `F`
over `K`, then every transcendence base of `F` over `K` has the same number of
elements as `S`.

This theorem is proved in Mathlib4 as `IsTranscendenceBasis.cardinalMk_eq`.
We provide a specialized version that gives cardinal equalities for finite bases.
-/

universe u v w

section equicardinality

variable {K : Type v} {F : Type w} [CommRing K] [CommRing F] [Algebra K F]
  [Nontrivial K] [IsDomain F]

/--
  Any two transcendence bases of a domain have the same cardinality
  when their index types live in the same universe.

  This is `IsTranscendenceBasis.cardinalMk_eq` from Mathlib.
-/
theorem equicardinality_of_transcendence_bases
    {ι ι' : Type u} {x : ι → F} {y : ι' → F}
    (hx : IsTranscendenceBasis K x) (hy : IsTranscendenceBasis K y) : #ι = #ι' :=
  hx.cardinalMk_eq hy

/--
  If one transcendence basis has a `Fintype` index type, then any other
  transcendence basis has cardinality equal to `Fintype.card ι`.
-/
theorem equicardinality_of_finite_transcendence_bases
    {ι ι' : Type u} {x : ι → F} {y : ι' → F}
    [Fintype ι] (hx : IsTranscendenceBasis K x) (hy : IsTranscendenceBasis K y) :
    #ι' = (Fintype.card ι : Cardinal) := by
  have h_card : #ι = #ι' := hx.cardinalMk_eq hy
  have h_fin : #ι = (Fintype.card ι : Cardinal) := mk_fintype ι
  rw [← h_fin, h_card]

/--
  The transcendence degree equals the cardinality of any transcendence basis.
  The index type must be in the same universe as `F`.
-/
theorem trdeg_eq_card_of_transcendence_basis
    {ι : Type w} {x : ι → F} (hx : IsTranscendenceBasis K x) :
    #ι = Algebra.trdeg K F :=
  hx.cardinalMk_eq_trdeg

/--
  If there exists a finite transcendence basis, then the transcendence degree
  is finite (less than `ℵ₀`).
-/
theorem trdeg_finite_of_finite_transcendence_basis
    {ι : Type w} {x : ι → F} [Fintype ι] (hx : IsTranscendenceBasis K x) :
    Algebra.trdeg K F < ℵ₀ := by
  rw [← hx.cardinalMk_eq_trdeg, mk_fintype ι]
  exact Cardinal.natCast_lt_aleph0

/--
  General version of transcendence degree equality, using `lift` to handle
  arbitrary universe for the index type.
-/
theorem trdeg_eq_lift_card_of_transcendence_basis
    {ι : Type u} {x : ι → F} (hx : IsTranscendenceBasis K x) :
    lift.{w} #ι = lift.{u} (Algebra.trdeg K F) :=
  hx.lift_cardinalMk_eq_trdeg

end equicardinality

/-! ## Examples -/

/--
  Example: The transcendence degree of an algebraic extension is zero.
-/
example {K F : Type*} [CommRing K] [CommRing F] [Algebra K F] [Algebra.IsAlgebraic K F] :
    Algebra.trdeg K F = 0 :=
  trdeg_eq_zero

/--
  Example: The transcendence degree of `K[X]` over `K` is 1.
-/
example {K : Type*} [CommRing K] [IsDomain K] :
    Algebra.trdeg K (Polynomial K) = 1 :=
  Polynomial.trdeg_of_isDomain

/--
  Example: The transcendence degree of `K[X₁, …, Xₙ]` over `K` is `#ι`
  (lifted to the appropriate universe).
  This is `MvPolynomial.trdeg_of_isDomain`.
-/
example {K : Type v} [CommRing K] [IsDomain K] (ι : Type u) :
    Algebra.trdeg K (MvPolynomial ι K) = lift.{v} #ι :=
  MvPolynomial.trdeg_of_isDomain
