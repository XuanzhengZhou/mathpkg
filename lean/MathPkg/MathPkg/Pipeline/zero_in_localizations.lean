import Mathlib

open LocalizedModule

/-- An element m of an R-module M is zero if and only if its image in every localization
    M_m at a maximal ideal m of R is zero. -/
lemma zero_iff_zero_in_all_localizations {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]
    (x : M) : x = 0 ↔ ∀ (I : Ideal R) (hI : I.IsMaximal), (mkLinearMap hI.isPrime.primeCompl) x = 0 := by
  sorry

/-- An R-module M is zero if and only if all its localizations M_m at maximal ideals m of R
    are zero. -/
lemma subsingleton_iff_all_localizations_subsingleton {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M] :
    Subsingleton M ↔ ∀ (I : Ideal R) (hI : I.IsMaximal), Subsingleton (LocalizedModule hI.isPrime.primeCompl M) := by
  sorry
