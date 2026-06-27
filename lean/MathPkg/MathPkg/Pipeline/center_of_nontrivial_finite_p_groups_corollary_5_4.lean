import Mathlib

open scoped Classical

/-!
# Center of Nontrivial Finite p-Groups (Corollary 5.4)

The center C(G) of a nontrivial finite p-group G contains more than one element.

This is a fundamental result in finite group theory. The proof relies on the class equation:
|G| = |C(G)| + Σ [G : C_G(xᵢ)], where the sum is over conjugacy class representatives
outside the center. Since G is a p-group, each index [G : C_G(xᵢ)] is divisible by p,
hence p divides |C(G)|, forcing |C(G)| ≥ p ≥ 2.

Mathlib4 provides this as `IsPGroup.center_nontrivial` and `IsPGroup.bot_lt_center`,
proven in `Mathlib/GroupTheory/PGroup.lean` via the class equation and fixed-point
theorem for p-group actions.
-/

section center_of_nontrivial_finite_p_groups_corollary_5_4

open Subgroup

/-- **Corollary 5.4**: The center of a nontrivial finite p-group G contains more than one element.

Formally: if G is a nontrivial finite group and `IsPGroup p G` for a prime p, then the center
`Subgroup.center G` is nontrivial (i.e., contains a non-identity element).

This is a direct application of `IsPGroup.center_nontrivial` from Mathlib. -/
theorem center_of_nontrivial_finite_p_groups_corollary_5_4 (p : ℕ) (G : Type*) [Group G]
    [Fact p.Prime] [Nontrivial G] [Finite G] (hG : IsPGroup p G) :
    Nontrivial (center G) :=
  hG.center_nontrivial

/-- Equivalent formulation: the center is strictly larger than the trivial subgroup ⊥.

Since ⊥ has exactly one element (the identity), `⊥ < center G` means the center must contain
at least one non-identity element. -/
theorem bot_lt_center_of_nontrivial_pgroup (p : ℕ) (G : Type*) [Group G]
    [Fact p.Prime] [Nontrivial G] [Finite G] (hG : IsPGroup p G) :
    ⊥ < center G :=
  hG.bot_lt_center

/-- Example: `ZMod 2` as an additive group is a 2-group of order 2.
Its center is the whole group, hence nontrivial.

We use `Multiplicative (ZMod 2)` to get a multiplicative group,
then apply the corollary. -/
example : Nontrivial (Subgroup.center (Multiplicative (ZMod 2))) := by
  haveI : Fact (Nat.Prime 2) := ⟨by decide⟩
  haveI : Nontrivial (Multiplicative (ZMod 2)) := Multiplicative.instNontrivial
  have hpg : IsPGroup 2 (Multiplicative (ZMod 2)) := by
    refine IsPGroup.of_card (n := 1) ?_
    simp [Nat.card_eq_fintype_card]
  exact center_of_nontrivial_finite_p_groups_corollary_5_4 2 (Multiplicative (ZMod 2)) hpg

end center_of_nontrivial_finite_p_groups_corollary_5_4
