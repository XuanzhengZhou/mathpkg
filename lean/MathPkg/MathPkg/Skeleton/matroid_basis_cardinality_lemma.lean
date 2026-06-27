import Mathlib

/- Matroid Basis Cardinality Lemma -/
lemma matroid_basis_cardinality_lemma {α : Type*} (M : Matroid α) (B₁ B₂ : Set α)
    (hB₁ : M.IsBase B₁) (hB₂ : M.IsBase B₂) : B₁.encard = B₂.encard := by
  sorry
