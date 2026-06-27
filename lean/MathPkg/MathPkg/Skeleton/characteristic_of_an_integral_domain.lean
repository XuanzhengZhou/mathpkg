import Mathlib

/- characteristic of an integral domain -/
theorem characteristic_of_an_integral_domain (R : Type*) [CommRing R] [IsDomain R] (p : ℕ) [CharP R p] :
    p = 0 ∨ Nat.Prime p := by
  sorry
