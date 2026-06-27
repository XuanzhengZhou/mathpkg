import Mathlib

open FreeGroup

/-!
# Higman Embedding Theorem

A finitely generated group `G` can be embedded in a finitely presented group if and only if
`G` is recursively presented.

## Statement

Let `G` be a finitely generated group. Then `G` embeds into a finitely presented group
if and only if `G` admits a presentation with finitely many generators and a recursively
enumerable set of relations (i.e., `G` is recursively presented).

## References

* Graham Higman, "Subgroups of finitely presented groups", Proc. Royal Soc. London, 1961
* https://en.wikipedia.org/wiki/Higman%27s_embedding_theorem

## Dependencies

* recursive functions — for the definition of `RecursivelyEnumerable`
* free groups — `FreeGroup`, `PresentedGroup`

## Formalization Notes

* **Finitely presented**: the group can be presented as `⟨Fin n | rels⟩` with `rels` finite.
* **Recursively presented**: the group can be presented as `⟨Fin n | rels⟩` with `rels`
  being a recursively enumerable set — either empty, or the range of a computable function
  from `ℕ` to `FreeGroup (Fin n)`.
* **Embedding**: there exists an injective group homomorphism `f : G →* H`.
-/

/-- A set `s : Set α` is **recursively enumerable** if it is either empty or the range of a
computable function `f : ℕ → α`. This captures the classical notion of an r.e. set:
the function `f` enumerates the elements of `s` (possibly with repetitions). -/
def RecursivelyEnumerable {α : Type*} [Primcodable α] (s : Set α) : Prop :=
  s = ∅ ∨ ∃ (f : ℕ → α), Computable f ∧ Set.range f = s

/-- **Higman Embedding Theorem**: A finitely generated group `G` embeds into a finitely
presented group if and only if `G` is recursively presented.

Formally:
* The forward direction: if `G` embeds into a finitely presented group `H`, then `G`
  itself is recursively presented.
* The reverse direction: if `G` is recursively presented, then there exists a finitely
  presented group `H` and an injective homomorphism `G →* H`. -/
theorem higman_embedding_theorem (G : Type*) [Group G] [Group.FG G] :
    ((∃ (H : Type*) [Group H],
      (∃ (n : ℕ) (rels : Set (FreeGroup (Fin n))), Set.Finite rels ∧
        Nonempty (H ≃* PresentedGroup rels)) ∧
      ∃ (f : G →* H), Function.Injective f) ↔
     (∃ (n : ℕ) (rels : Set (FreeGroup (Fin n))),
      RecursivelyEnumerable rels ∧
      Nonempty (G ≃* PresentedGroup rels))) := by
  sorry
