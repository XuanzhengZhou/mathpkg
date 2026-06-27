import Mathlib

open Set

/-- Partial function extension order: p extends q if p.1 ⊆ q.1 and the functions agree on p.1 -/
def PartialFunc.extends {X Y : Type*} (p q : Σ (A : Set X), ({x // x ∈ A} → Y)) : Prop := by
  sorry
