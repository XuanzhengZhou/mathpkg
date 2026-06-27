import Mathlib

/-!
# Metabelian Group

A **metabelian group** is a soluble group whose derived length is at most 2.
Equivalently, the second derived subgroup (the commutator of the commutator subgroup)
is trivial: `⁅⁅G, G⁆, ⁅G, G⁆⁆ = {1}`.

In Mathlib4, the derived series of a group `G` is given by `derivedSeries G n`
(`GroupTheory/Solvable.lean`). The derived length is the smallest `n` such that
`derivedSeries G n = ⊥`. Thus, a group is metabelian precisely when
`derivedSeries G 2 = ⊥`.

## Mathlib4 References
- `derivedSeries`: `Mathlib/GroupTheory/Solvable.lean`
- `IsSolvable`: `Mathlib/GroupTheory/Solvable.lean`
- `commutator`: `Mathlib/GroupTheory/Commutator/Basic.lean`
-/

open scoped commutatorElement

/-- A group `G` is **metabelian** if its second derived subgroup is trivial,
i.e., `derivedSeries G 2 = ⊥`. Equivalently, `⁅⁅G, G⁆, ⁅G, G⁆⁆ = {1}`.

This means the group is solvable with derived length at most 2. -/
def IsMetabelian (G : Type*) [Group G] : Prop := by
  sorry
