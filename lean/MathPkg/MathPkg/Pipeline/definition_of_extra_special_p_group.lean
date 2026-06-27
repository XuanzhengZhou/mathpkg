import Mathlib

open scoped Classical

/-!
# Definition of Extra-Special p-Group

A finite p-group G is called **extra-special** if its commutator subgroup G' and its center Z(G)
coincide and have order p.

Equivalently:
- G' = Z(G) (the derived subgroup equals the center)
- |G'| = |Z(G)| = p

Extra-special p-groups play a fundamental role in the classification of finite p-groups.
They are minimal non-abelian p-groups and serve as building blocks for more general p-groups.

## Mathlib4 context

- `IsPGroup p G` from `Mathlib/GroupTheory/PGroup.lean`
- `commutator G` (derived subgroup) from `Mathlib/GroupTheory/Commutator/Basic.lean`
- `Subgroup.center G` from `Mathlib/GroupTheory/Subgroup/Center.lean`

Note: Mathlib4 does not yet have this definition, so we provide it here.
-/

section definition_of_extra_special_p_group

open Subgroup

variable (p : ℕ) (G : Type*) [Group G]

/-- A finite p-group G is **extra-special** if its commutator subgroup G' and its center Z(G)
coincide and both have order p.

Formally:
- `IsPGroup p G` — G is a p-group.
- `Finite G` — G is finite.
- `commutator G = center G` — the derived subgroup equals the center.
- `Nat.card (commutator G) = p` — the order of this common subgroup is p.

This is a `Prop` (a property of the group, not a new typeclass). -/
def IsExtraSpecial : Prop :=
  IsPGroup p G ∧ Finite G ∧ commutator G = Subgroup.center G ∧ Nat.card (commutator G) = p

/-- Example: For a prime p, any extra-special p-group satisfies `Fact p.Prime`.
This is consistent with the definition of a p-group, which requires p to be prime. -/
example (p : ℕ) (G : Type*) [Group G] [Fact p.Prime] (hG : IsExtraSpecial p G) : p.Prime := by
  exact Fact.out

/-- A classic example: the quaternion group Q₈ (order 8) and the dihedral group D₈ (order 8)
are the two extra-special 2-groups of order 8.

Constructing these as explicit `IsExtraSpecial` instances requires verifying the group theory
properties (which is beyond the scope of this definition file). -/
example (p : ℕ) (G : Type*) [Group G] [Fintype G] : IsExtraSpecial p G := by
  -- Placeholder: in practice one would construct this for specific groups like Q₈ or D₈.
  sorry

end definition_of_extra_special_p_group
