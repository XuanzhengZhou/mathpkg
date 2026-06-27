import Mathlib

open Set Filter MeasureTheory

/- Differentiation under the integral sign -/
theorem differentiation_under_integral_sign {α : Type*} [MeasurableSpace α]
    {μ : Measure α} {f : ℝ → α → ℝ} {f' : ℝ → α → ℝ} {t₀ : ℝ} {g : α → ℝ}
    (hf : ∀ᵐ x ∂μ, HasDerivAt (λ t => f t x) (f' t₀ x) t₀)
    (h_bound : ∀ᵐ x ∂μ, ∀ t, ‖f' t x‖ ≤ g x)
    (hg : Integrable g μ) :
    HasDerivAt (λ t => ∫ x, f t x ∂μ) (∫ x, f' t₀ x ∂μ) t₀ := by
  sorry
