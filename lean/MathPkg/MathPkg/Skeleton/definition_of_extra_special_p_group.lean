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
def IsExtraSpecial : Prop := by
  sorry
