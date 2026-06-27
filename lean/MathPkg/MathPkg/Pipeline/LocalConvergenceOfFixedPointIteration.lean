import Mathlib

/- Local convergence of fixed-point iteration -/
theorem local_convergence_of_fixed_point_iteration (g : ℝ → ℝ) (z : ℝ) (hz : g z = z)
    (g' : ℝ) (hderiv : HasDerivAt g g' z) (hg' : |g'| < 1) :
    ∃ (δ : ℝ), δ > 0 ∧ ∀ (z₀ : ℝ), |z₀ - z| < δ →
      Filter.Tendsto (λ n : ℕ => g^[n] z₀) Filter.atTop (𝓝 z) :=
  by
  sorry
