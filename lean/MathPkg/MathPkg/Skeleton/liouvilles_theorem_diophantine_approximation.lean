import Mathlib

/- Liouville's Theorem on Diophantine Approximation

If α is an algebraic number of degree d > 1, there exists a constant c(α) > 0 such that
for all rational numbers p/q (q > 0), we have |α - p/q| > c(α) / q^d.
-/

open Polynomial

theorem liouvilles_theorem_diophantine_approximation {α : ℝ} (halg : IsIntegral ℚ α)
    (hdeg : (minpoly ℚ α).natDegree > 1) :
    ∃ c : ℝ, c > 0 ∧ ∀ (p : ℤ) (q : ℤ), q > 0 →
      |α - (p : ℝ) / (q : ℝ)| > c / ((q : ℝ) ^ (minpoly ℚ α).natDegree) := by
  sorry
