import Mathlib

/- properties_of_closed_sets -/

theorem properties_of_closed_sets {X : Type*} [TopologicalSpace X] :
    IsClosed (Set.univ : Set X) ∧ IsClosed (∅ : Set X) ∧
    (∀ (A B : Set X), IsClosed A → IsClosed B → IsClosed (A ∪ B)) ∧
    (∀ {ι : Type*} (A : ι → Set X), (∀ i, IsClosed (A i)) → IsClosed (⋂ i, A i)) := by
  sorry
