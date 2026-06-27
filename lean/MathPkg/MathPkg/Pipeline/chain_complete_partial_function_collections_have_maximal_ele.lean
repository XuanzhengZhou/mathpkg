import Mathlib

open Set

/-- Partial function extension order: p extends q if p.1 ⊆ q.1 and the functions agree on p.1 -/
def PartialFunc.extends {X Y : Type*} (p q : Σ (A : Set X), ({x // x ∈ A} → Y)) : Prop :=
  ∃ (h : p.1 ⊆ q.1), ∀ (x : X) (hx : x ∈ p.1), p.2 ⟨x, hx⟩ = q.2 ⟨x, h hx⟩

/-- An application of Zorn's Lemma: a nonempty collection of partial functions ordered by
extension in which every chain has an upper bound contains a maximal element. -/
theorem chain_complete_partial_function_collections_have_maximal_ele
    {X Y : Type*}
    (S : Set (Σ (A : Set X), ({x // x ∈ A} → Y)))
    (hS : S.Nonempty)
    (hchain : ∀ (C : Set (Σ (A : Set X), ({x // x ∈ A} → Y))), C ⊆ S → IsChain PartialFunc.extends C →
      ∃ z ∈ S, ∀ a ∈ C, PartialFunc.extends a z) :
    ∃ m ∈ S, ∀ a ∈ S, PartialFunc.extends m a → PartialFunc.extends a m :=
  by
  sorry
