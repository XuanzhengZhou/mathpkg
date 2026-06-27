import Mathlib

open LocalizedModule

/- An element m of an R-module M is zero if and only if its image in every localization
    M_m at a maximal ideal m of R is zero. -/
lemma zero_iff_zero_in_all_localizations {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]
    (x : M) : x = 0 ↔ ∀ (I : Ideal R) [I.IsMaximal], (mkLinearMap (I.primeCompl) M) x = 0 := by
  sorry
