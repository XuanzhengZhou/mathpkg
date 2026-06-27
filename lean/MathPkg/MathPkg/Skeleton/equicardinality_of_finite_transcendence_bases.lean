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
    (hx : IsTranscendenceBasis K x) (hy : IsTranscendenceBasis K y) : #ι = #ι' := by
  sorry
