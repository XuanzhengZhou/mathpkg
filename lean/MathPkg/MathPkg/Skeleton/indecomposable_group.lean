import Mathlib

/-!
# Indecomposable Group

A group G is indecomposable when G ≠ 1 and G = A ⊕ B implies A = 1 or B = 1.

We formalize this for additive commutative groups, using `IsCompl` to capture the internal
direct sum decomposition: `IsCompl A B` means `Disjoint A B` and `Codisjoint A B`.

## Main definition

* `IsIndecomposable G` : An additive commutative group `G` is indecomposable if it is nontrivial
  and whenever it is the internal direct sum of two subgroups, one of them must be trivial.
-/

open AddSubgroup

variable {G : Type*} [AddCommGroup G]

/-- An additive commutative group `G` is indecomposable if it is nontrivial and
cannot be written as the internal direct sum of two nontrivial subgroups.

Formally: whenever `A, B` are additive subgroups of `G` with `IsCompl A B`
(i.e., `Disjoint A B` and `Codisjoint A B`), then one of `A` or `B` must be `⊥`. -/
def IsIndecomposable (G : Type*) [AddCommGroup G] : Prop := by
  sorry
