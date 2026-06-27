import Mathlib

/-!
# Conjugacy Classes and Centralizers

The conjugation action `g ↦ (x ↦ g⁻¹xg)` partitions a group `G` into orbits called
**conjugacy classes**. The stabilizer of `x` under this action is the **centralizer**
`C_G(x) = {g ∈ G | gx = xg}`. By the orbit-stabilizer theorem, the size of the
conjugacy class of `x` equals the index `|G : C_G(x)|`.

## Mathlib4 Locations

* `ConjClasses G` — the quotient type of conjugacy classes (`Algebra/Group/Conj.lean`)
* `IsConj a b` — the conjugacy relation
* `ConjAct G` — conjugation action of `G` on itself (`GroupTheory/GroupAction/ConjAct.lean`)
* `Subgroup.centralizer s` — centralizer of a subset (`GroupTheory/Subgroup/Centralizer.lean`)
* `Set.centralizer s` — centralizer as a set (`Algebra/Group/Center.lean`)
* `MulAction.orbit` / `MulAction.stabilizer` — orbit and stabilizer of a group action
* `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` — orbit-stabilizer theorem for finite groups
-/

open scoped BigOperators

/--
The **conjugacy class** of an element `g : G` is the set of all elements conjugate to `g`:
`{h * g * h⁻¹ | h ∈ G}`.

In Mathlib4 this is expressed as either `ConjClasses.mk g` (as a quotient type) or
as `orbit (ConjAct G) g` (as a set via the conjugation action).
-/
def conjugacyClass (G : Type*) [Group G] (g : G) : ConjClasses G := by
  sorry
