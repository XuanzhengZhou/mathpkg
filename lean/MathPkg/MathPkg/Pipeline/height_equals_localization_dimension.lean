import Mathlib

/- Height of a prime ideal equals the dimension of its localization -/
theorem height_equals_localization_dimension {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime] :
    Ideal.height p = ringKrullDim (Localization.AtPrime p) := by
  sorry
