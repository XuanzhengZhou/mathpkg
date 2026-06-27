import Mathlib

open AddSubgroup

/- 循环直和分量引理（有界阿贝尔 p 群）-/
lemma cyclic_direct_summand_lemma_for_bounded_abelian_p_groups
    {G : Type*} [AddCommGroup G] {p : ℕ}
    (hp : IsPGroup p (Multiplicative G))
    (hBounded : ∃ n : ℕ, ∀ x : G, addOrderOf x ≤ n)
    {g : G} (hMax : ∀ x : G, addOrderOf x ≤ addOrderOf g) :
    ∃ H : AddSubgroup G, IsCompl (AddSubgroup.zmultiples g) H := by
  sorry
