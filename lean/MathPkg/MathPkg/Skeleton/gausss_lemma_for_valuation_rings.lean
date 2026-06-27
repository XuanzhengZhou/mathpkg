import Mathlib

open Polynomial

/- Gauss's Lemma for Valuation Rings -/

lemma gausss_lemma_for_valuation_rings {R : Type*} [CommRing R] [IsDomain R] [ValuationRing R]
    {f g : Polynomial R} (hf : IsPrimitive f) (hg : IsPrimitive g) : IsPrimitive (f * g) := by
  sorry
