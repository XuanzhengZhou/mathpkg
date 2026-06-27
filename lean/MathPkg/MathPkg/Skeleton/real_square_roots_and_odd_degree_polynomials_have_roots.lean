import Mathlib

open Polynomial

/- real_square_roots_and_odd_degree_polynomials_have_roots -/
lemma real_square_roots_and_odd_degree_polynomials_have_roots : (∀ (a : ℝ), 0 ≤ a → ∃ (x : ℝ), x ^ 2 = a) ∧ (∀ (f : Polynomial ℝ), Odd (natDegree f) → ∃ (x : ℝ), f.eval x = 0) := by
  sorry
