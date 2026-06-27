import Mathlib

open Set

/- Roth's Theorem -/
theorem roths_theorem {α : ℝ} (hα : IsAlgebraic ℚ α) (hdeg : 2 ≤ Polynomial.natDegree (minpoly ℚ α)) (ε : ℝ) (hε : ε > 0) :
  Set.Finite {r : ℚ | |α - (r : ℝ)| < ((r.den : ℝ) ^ (2 + ε))⁻¹} := by
  sorry
