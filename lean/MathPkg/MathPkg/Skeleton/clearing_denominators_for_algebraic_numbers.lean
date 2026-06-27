import Mathlib

/- Clearing denominators for algebraic numbers -/
lemma clearing_denominators_for_algebraic_numbers {K : Type*} [Field K] [NumberField K] (β : K) :
    ∃ (b : ℤ), b ≠ 0 ∧ IsIntegral ℤ ((b : K) • β) := by
  sorry
