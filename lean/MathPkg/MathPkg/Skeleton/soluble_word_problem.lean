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
def HasSolubleWordProblem (rels : Set (FreeGroup α)) : Prop := by
  sorry
