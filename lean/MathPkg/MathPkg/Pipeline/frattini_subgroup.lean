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
def FrattiniSubgroup (G : Type*) [Group G] : Subgroup G :=
  frattini G

namespace FrattiniSubgroup

/-- The Frattini subgroup equals Mathlib4's `frattini G`. -/
theorem eq_frattini : FrattiniSubgroup G = frattini G := rfl

/-- The Frattini subgroup is contained in every maximal subgroup (coatom). -/
theorem le_maximal {K : Subgroup G} (hK : IsCoatom K) : FrattiniSubgroup G ≤ K :=
  frattini_le_coatom hK

/-- The Frattini subgroup is a characteristic subgroup of `G`. -/
theorem characteristic : (FrattiniSubgroup G).Characteristic := by
  rw [eq_frattini]
  exact inferInstance

/--
  Non-generating property: if a subgroup `K` together with the Frattini subgroup
  generates the whole group, then `K` is already the whole group.

  This holds when the subgroup lattice is coatomic (every proper subgroup is
  contained in a maximal subgroup).
-/
theorem nongenerating [IsCoatomic (Subgroup G)] {K : Subgroup G}
    (h : K ⊔ FrattiniSubgroup G = ⊤) : K = ⊤ := by
  rw [eq_frattini] at h
  exact frattini_nongenerating h

/-- In a finite group, the Frattini subgroup is nilpotent. -/
theorem nilpotent [Finite G] : Group.IsNilpotent (FrattiniSubgroup G) := by
  rw [eq_frattini]
  exact frattini_nilpotent

end FrattiniSubgroup

/-
  Examples
-/

/-- The Frattini subgroup is contained in every maximal subgroup (coatom). -/
example {K : Subgroup G} (isMax : IsCoatom K) : FrattiniSubgroup G ≤ K :=
  FrattiniSubgroup.le_maximal isMax

/-- The non-generating property: if `H` together with the Frattini generates the
    whole group, then `H` is the whole group. -/
example [IsCoatomic (Subgroup G)] {H : Subgroup G}
    (hgen : H ⊔ FrattiniSubgroup G = ⊤) : H = ⊤ :=
  FrattiniSubgroup.nongenerating hgen

/-- In a finite group, the Frattini subgroup is nilpotent. -/
example [Finite G] : Group.IsNilpotent (FrattiniSubgroup G) :=
  FrattiniSubgroup.nilpotent

/-- The Frattini subgroup is characteristic, so it is invariant under all automorphisms. -/
example : (FrattiniSubgroup G).Characteristic :=
  FrattiniSubgroup.characteristic

/-- In any finite group, the Frattini subgroup is characteristic. -/
example [Finite G] : (FrattiniSubgroup G).Characteristic :=
  FrattiniSubgroup.characteristic

/-- The Frattini subgroup is always a normal subgroup
    (since it is characteristic, and characteristic subgroups are normal). -/
example : (FrattiniSubgroup G).Normal := by
  have h : (FrattiniSubgroup G).Characteristic := FrattiniSubgroup.characteristic
  exact inferInstance

/-- The Frattini subgroup equals Mathlib4's `frattini G`. -/
example : FrattiniSubgroup G = frattini G :=
  FrattiniSubgroup.eq_frattini
