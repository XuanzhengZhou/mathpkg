import Mathlib

open IsLocalRing

/- depth lemma 18.3: depth((I, y), M) ≤ depth(I, M) + 1 -/

noncomputable def depthHelper {R : Type _} [CommRing R] (I : Ideal R) (M : Type _) [AddCommGroup M] [Module R M] : WithTop ℕ := by
  sorry

lemma depth_lemma_lemma_18_3 (R : Type _) [CommRing R] [IsLocalRing R]
    (M : Type _) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (y : R) (hy : y ∈ maximalIdeal R) :
    depthHelper (I ⊔ Ideal.span {y}) M ≤ depthHelper I M + (1 : WithTop ℕ) := by
  sorry
