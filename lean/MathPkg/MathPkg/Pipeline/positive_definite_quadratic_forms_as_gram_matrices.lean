import Mathlib

open scoped Classical

/-!
# Positive Definite Quadratic Forms as Gram Matrices

Let `Q` be an `n × n` real matrix representing a positive definite quadratic form.

1. **Gram matrix representation**: If `Q` is positive definite, then `Q` is the
   Gram matrix of some lattice basis, i.e. there exists an invertible matrix
   `B ∈ GL_n(ℝ)` such that `Q = Bᵀ B`.

2. **Uniqueness up to isometry**: The Gram matrix of a lattice basis determines
   the basis uniquely up to orthogonal transformation. In other words, if two
   bases `bᵢ` and `b'ᵢ` have the same Gram matrix, then one can be obtained
   from the other by an orthogonal transformation. In matrix terms, if
   `B₁ᵀ B₁ = B₂ᵀ B₂`, then `B₂ = K B₁` for some orthogonal matrix `K`
   (i.e. `Kᵀ K = 1`).

## Dependencies

- [positive definite quadratic form](/concept/positive_definite_quadratic_form)
- [Gram matrix](/concept/gram_matrix)
- [orthogonal matrix](/concept/orthogonal_matrix)
- [lattice basis](/concept/lattice_basis)
-/

/-- **Positive definite quadratic forms as Gram matrices.**

If `Q` is a positive definite real matrix, then:
1. `Q` can be factored as `Bᵀ B` for some invertible matrix `B`.
2. Any two matrices with the same Gram matrix differ by an orthogonal transformation.
-/
theorem positive_definite_quadratic_forms_as_gram_matrices (n : ℕ) (Q : Matrix (Fin n) (Fin n) ℝ)
    (hQ : Q.PosDef) :
    (∃ (B : Matrix (Fin n) (Fin n) ℝ), IsUnit B ∧ Q = Bᵀ * B) ∧
    (∀ (B₁ B₂ : Matrix (Fin n) (Fin n) ℝ), B₁ᵀ * B₁ = B₂ᵀ * B₂ →
      ∃ (K : Matrix (Fin n) (Fin n) ℝ), Kᵀ * K = 1 ∧ K * Kᵀ = 1 ∧ B₂ = K * B₁) := by
  sorry
