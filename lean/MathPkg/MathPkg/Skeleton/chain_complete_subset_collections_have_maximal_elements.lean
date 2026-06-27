import Mathlib

/- Let X be a set and let S be a nonempty collection of subsets of X, partially ordered by inclusion.
If for every chain T in S the union ∪T is an element of S, then S has a maximal element. -/
theorem chain_complete_subset_collections_have_maximal_elements {α : Type*} (S : Set (Set α))
    (hS : S.Nonempty)
    (hchain : ∀ T ⊆ S, IsChain (· ⊆ ·) T → ⋃₀ T ∈ S) :
    ∃ M ∈ S, ∀ A ∈ S, M ⊆ A → A = M := by
  sorry
