import Mathlib

/- lemma_c_10_surjectivity_of_ -/
lemma lemma_c_10_surjectivity_of_ {A A' : Type*} [AddCommGroup A] [Module ℝ A]
  [AddCommGroup A'] [Module ℝ A'] (φ : A →ₗ[ℝ] A') (hφ : Function.Injective φ) :
  Function.Surjective (λ (f : A' →ₗ[ℝ] ℝ) => f.comp φ) := by
  sorry
