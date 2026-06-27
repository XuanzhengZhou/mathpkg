import Mathlib

/-!
# Frattini Subgroup

The Frattini subgroup `Frat G` of a group `G` is the intersection of all maximal subgroups of `G`,
with the convention `Frat G = G` if `G` has no maximal subgroups. It is a characteristic subgroup.

In Mathlib4:
- `frattini G : Subgroup G` is defined in `Mathlib/GroupTheory/Frattini.lean`
  as `Order.radical (Subgroup G)` — the intersection of all coatoms (maximal proper subgroups)
  in the subgroup lattice.
- `frattini_characteristic` proves the Frattini subgroup is characteristic.
- `frattini_nongenerating` shows: if `K ⊔ frattini G = ⊤` then `K = ⊤`
  (the Frattini subgroup consists of "non-generating" elements).
- `frattini_nilpotent` proves the Frattini subgroup of a finite group is nilpotent.

## Main definitions

* `frattini G` — the Frattini subgroup of `G` (intersection of all maximal subgroups)
* `frattini_characteristic` — the Frattini subgroup is characteristic
* `frattini_nongenerating` — elements of the Frattini subgroup are non-generators
* `frattini_nilpotent` — in a finite group, the Frattini subgroup is nilpotent
-/

open Subgroup

variable {G H : Type*} [Group G] [Group H]

/--
  The Frattini subgroup of `G` is the intersection of all maximal subgroups of `G`.
  If `G` has no maximal subgroups, then `frattini G = G` by convention
  (since the empty intersection in the subgroup lattice is the top element).

  In Mathlib4 this is defined as `Order.radical (Subgroup G)`, where
  `Order.radical` is the intersection of all coatoms in a lattice with a top element.
-/
def FrattiniSubgroup (G : Type*) [Group G] : Subgroup G := by
  sorry
