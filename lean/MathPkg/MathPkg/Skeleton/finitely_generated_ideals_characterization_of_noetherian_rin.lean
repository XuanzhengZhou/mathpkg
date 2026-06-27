import Mathlib

/- A commutative ring R is Noetherian if and only if every ideal of R is finitely generated. -/
theorem finitely_generated_ideals_characterization_of_noetherian_ring (R : Type*) [CommRing R] :
    IsNoetherianRing R ↔ ∀ (I : Ideal R), I.FG := by
  sorry
