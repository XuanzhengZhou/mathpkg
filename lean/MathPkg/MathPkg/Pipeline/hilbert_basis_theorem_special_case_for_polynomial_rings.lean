import Mathlib

/- The ring k[x1, ..., xn] is Noetherian -/
theorem hilbert_basis_theorem_special_case_for_polynomial_rings (k : Type*) [Field k] (n : ℕ) :
    IsNoetherianRing (MvPolynomial (Fin n) k) :=
by
  sorry
