import Mathlib

/-!
# Soluble Word Problem

For a finite presentation, the word problem is soluble if there is an algorithm that, given a word
`w` in the generators, decides whether `w` is a relator (i.e., `w = 1` in the group).
A group `G` has soluble word problem if the word problem is soluble for some finite presentation of `G`.

## Main definitions

* `PresentedGroup.HasSolubleWordProblem rels`: the word problem for the presentation `⟨α | rels⟩`
  is soluble — there exists a decision procedure that determines, for any word `w : FreeGroup α`,
  whether `mk rels w = 1`.
* `Group.HasSolubleWordProblem G`: the group `G` admits a finite presentation with soluble
  word problem.

## References

* https://en.wikipedia.org/wiki/Word_problem_for_groups
-/

open FreeGroup

namespace PresentedGroup

variable {α : Type*}

/-- A presentation `⟨α | rels⟩` has a soluble word problem if there exists a decision procedure
that determines, for any word `w` in the free group on `α`, whether `w` represents the identity
in the presented group.

This is a proposition — it asserts the *existence* of an algorithm, not the algorithm itself.
The `Nonempty` wrapper ensures this definition lives in `Prop`. -/
def HasSolubleWordProblem (rels : Set (FreeGroup α)) : Prop :=
  Nonempty (∀ (w : FreeGroup α), Decidable (mk rels w = 1))

/-- If `α` has decidable equality, the presentation with no relations has a soluble word problem.
(This is because equality in the free group `FreeGroup α` is decidable.) -/
lemma hasSolubleWordProblem_empty [DecidableEq α] :
    HasSolubleWordProblem (∅ : Set (FreeGroup α)) := by
  refine ⟨?h⟩
  intro w
  have h_eq : (mk (∅ : Set (FreeGroup α)) w = 1) ↔ (w = 1) := by
    rw [mk_eq_one_iff, Subgroup.normalClosure_empty, Subgroup.mem_bot]
  haveI : Decidable (w = 1) := inferInstance
  -- manually case-split the Decidable instance to construct the desired Decidable
  refine
    match ‹Decidable (w = 1)› with
    | .isTrue h => .isTrue (h_eq.mpr h)
    | .isFalse h => .isFalse (mt h_eq.mp h)

end PresentedGroup

/-- A group `G` has a soluble word problem if it admits a finite presentation
`⟨Fin n | rels⟩` for which the word problem is soluble.

This captures the classical notion: there exists some finite presentation of `G` such that
one can algorithmically decide whether a given word in the generators equals the identity. -/
class Group.HasSolubleWordProblem (G : Type*) [Group G] : Prop where
  soluble : ∃ (n : ℕ) (rels : Set (FreeGroup (Fin n))),
    Set.Finite rels ∧ ∃ (_ : PresentedGroup rels ≃* G),
    PresentedGroup.HasSolubleWordProblem rels

/-- A free group on finitely many generators has a soluble word problem.
This follows because we can present the free group with the empty set of relations,
and equality in a free group with decidable equality of generators is decidable. -/
example (n : ℕ) : Group.HasSolubleWordProblem (FreeGroup (Fin n)) := by
  set rels := (∅ : Set (FreeGroup (Fin n))) with hrels
  have h_normalClosure_eq : Subgroup.normalClosure rels = (⊥ : Subgroup (FreeGroup (Fin n))) := by
    rw [hrels, Subgroup.normalClosure_empty]
  -- Isomorphism PresentedGroup rels ≃* FreeGroup (Fin n)
  let e : PresentedGroup rels ≃* FreeGroup (Fin n) :=
    (QuotientGroup.quotientMulEquivOfEq h_normalClosure_eq).trans
      QuotientGroup.quotientBot
  refine ⟨n, rels, by simp [hrels, Set.finite_empty], e, ?_⟩
  -- presented group with empty relations has soluble word problem
  rw [hrels]
  exact PresentedGroup.hasSolubleWordProblem_empty (α := Fin n)
