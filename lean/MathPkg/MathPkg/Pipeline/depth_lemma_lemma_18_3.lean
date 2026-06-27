import Mathlib

/- depth lemma 18.3: depth((I, y), M) ≤ depth(I, M) + 1 -/
lemma depth_lemma_lemma_18_3 (R : Type _) [CommRing R] [LocalRing R]
    (M : Type _) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (y : R) (hy : y ∈ LocalRing.maximalIdeal R) :
    depth (I ⊔ Ideal.span {y}) M ≤ depth I M + (1 : ℕ∞) := by
  sorry
