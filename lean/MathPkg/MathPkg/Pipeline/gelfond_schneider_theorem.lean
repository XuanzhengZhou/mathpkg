import Mathlib

/- Gelfond-Schneider Theorem -/
theorem gelfond_schneider {α β : ℂ} (hα : IsAlgebraic ℚ α) (hβ : IsAlgebraic ℚ β)
    (hα0 : α ≠ 0) (hα1 : α ≠ 1) (hβ_irrational : ∀ q : ℚ, (q : ℂ) ≠ β) :
    ¬ IsAlgebraic ℚ (α ^ β) := by
  sorry
