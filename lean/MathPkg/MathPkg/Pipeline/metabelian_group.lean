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
def IsMetabelian (G : Type*) [Group G] : Prop :=
  derivedSeries G 2 = ⊥

namespace IsMetabelian

variable {G : Type*} [Group G]

/-- Every metabelian group is solvable (with `n = 2` in the derived series). -/
theorem isSolvable (h : IsMetabelian G) : IsSolvable G := by
  rw [IsMetabelian] at h
  exact ⟨⟨2, h⟩⟩

/-- In a metabelian group, the commutator of the commutator subgroup with itself is trivial.
This is the key structural property: `⁅⁅G, G⁆, ⁅G, G⁆⁆ = {1}`. -/
theorem commutator_commutator_eq_bot (h : IsMetabelian G) :
    ⁅commutator G, commutator G⁆ = ⊥ := by
  calc
    ⁅commutator G, commutator G⁆ = ⁅derivedSeries G 1, derivedSeries G 1⁆ := by simp
    _ = derivedSeries G 2 := by simp
    _ = ⊥ := h

/-- Every abelian group is metabelian.
For an abelian group, the commutator subgroup is already trivial (`derivedSeries G 1 = ⊥`),
so the second derived subgroup is also trivial. -/
theorem of_abelian {G : Type*} [CommGroup G] : IsMetabelian G := by
  have hcomm : commutator G = ⊥ := by
    apply le_bot_iff.mp
    exact Abelianization.commutator_subset_ker (MonoidHom.id G)
  rw [IsMetabelian, derivedSeries_succ, derivedSeries_one]
  rw [hcomm]
  simp

/-- The trivial group (where `⊤ = ⊥`) is metabelian. -/
theorem of_subsingleton {G : Type*} [Group G] [Subsingleton G] : IsMetabelian G := by
  rw [IsMetabelian]
  apply le_bot_iff.mp
  calc
    derivedSeries G 2 ≤ derivedSeries G 0 := derivedSeries_antitone G (by omega)
    _ = ⊤ := derivedSeries_zero G
    _ = ⊥ := Subgroup.eq_bot_of_subsingleton _

/-- The property of being metabelian is invariant under group isomorphism. -/
theorem of_mulEquiv {G H : Type*} [Group G] [Group H] (e : G ≃* H) (hG : IsMetabelian G) :
    IsMetabelian H := by
  rw [IsMetabelian] at hG ⊢
  have h_map := map_derivedSeries_eq (f := (e : G →* H)) (hf := e.surjective) 2
  -- h_map : (derivedSeries G 2).map (e : G →* H) = derivedSeries H 2
  rw [hG] at h_map
  have h_map_bot : ((⊥ : Subgroup G).map (e : G →* H)) = (⊥ : Subgroup H) := Subgroup.map_bot _
  rw [h_map_bot] at h_map
  exact h_map.symm

end IsMetabelian

-- Example: Any abelian group is metabelian.
example (G : Type*) [CommGroup G] : IsMetabelian G :=
  IsMetabelian.of_abelian

-- Example: The trivial group is metabelian.
example (G : Type*) [Group G] [Subsingleton G] : IsMetabelian G :=
  IsMetabelian.of_subsingleton

-- Example: If G is metabelian, then it is in particular solvable.
example (G : Type*) [Group G] (h : IsMetabelian G) : IsSolvable G :=
  IsMetabelian.isSolvable h
