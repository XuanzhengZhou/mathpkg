import Mathlib

open scoped Classical

/-!
# Sum of Character Values

For a Dirichlet character χ modulo q:
(i) If χ ≠ χ₀ (the principal character), then the sum of χ(x) over all x ∈ (ℤ/qℤ)ˣ is zero.
(ii) If x ≢ 1 (mod q), then the sum of χ(x) over all Dirichlet characters modulo q is zero.

These are the fundamental orthogonality relations for Dirichlet characters.
-/

section sum_of_character_values

open DirichletCharacter

/-- Orthogonality relations for Dirichlet characters.

(i) If χ is not the principal character, then ∑_{x∈(ℤ/qℤ)ˣ} χ(x) = 0.
(ii) If x ≠ 1 (mod q), then ∑_{χ} χ(x) = 0, where the sum runs over all Dirichlet characters
    modulo q. -/
theorem sum_of_character_values (q : ℕ) (hq : 0 < q) :
    ((∀ (χ : DirichletCharacter ℂ q), χ ≠ 1 → (∑ x : (ZMod q)ˣ, χ x) = 0) ∧
     (∀ (x : (ZMod q)ˣ), x ≠ 1 → (∑ χ : DirichletCharacter ℂ q, χ x) = 0)) := by
  sorry

end sum_of_character_values
