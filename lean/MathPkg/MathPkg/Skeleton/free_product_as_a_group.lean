import Mathlib

open Monoid

/- free_product_as_a_group -/
theorem free_product_as_a_group {G : Type*} [Group G] (A B : Subgroup G) (h : A ⊓ B = ⊥) :
    Function.Injective (Coprod.lift (Subgroup.subtype A) (Subgroup.subtype B) : Coprod (↥A) (↥B) →* G) := by
  sorry
