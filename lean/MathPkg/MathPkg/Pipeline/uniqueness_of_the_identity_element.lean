import Mathlib

/- Uniqueness of the identity element -/
theorem uniqueness_of_the_identity_element {α : Type _} (op : α → α → α) (e₁ e₂ : α)
    (h₁ : ∀ x, op e₁ x = x) (h₂ : ∀ x, op x e₂ = x) : e₁ = e₂ := by
  sorry
