import Mathlib

/-!
# Supporting Hyperplane of a Polytope

A supporting hyperplane H of a convex polytope P ⊂ ℝⁿ is a hyperplane such that
P is entirely contained in one of the closed half-spaces determined by H and
H ∩ P is non-empty.

We represent a hyperplane as `{x | l x = a}` where `l` is a nonzero continuous linear
functional (`StrongDual ℝ E`) and `a` is a real number. The closed half-space
containing the polytope is `{x | l x ≥ a}` (or equivalently `{x | a ≤ l x}`).

## Main definition

* `IsSupportingHyperplane l a P` -- asserts that the hyperplane `H = {x | l x = a}`
  supports the set `P`. Formally, every point `x ∈ P` lies in the closed half-space
  `{x | a ≤ l x}`, and the hyperplane touches `P`, i.e., `H ∩ P ≠ ∅`.

This definition generalizes the classical notion of a supporting hyperplane of a
convex polytope in ℝⁿ and can be instantiated for any set in a real normed vector space.

## References

* [Barry Simon, *Convexity*][simon2011], Chapter 8
-/

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/--
A supporting hyperplane of a set `P` in a real normed vector space `E`,
represented by a continuous linear functional `l : StrongDual ℝ E` and a threshold `a : ℝ`.

The hyperplane is `H = {x : E | l x = a}`. The definition states:

1. `P` is contained in the closed half-space determined by `H`: `∀ x ∈ P, a ≤ l x`.
   (Equivalently, all points of `P` lie on the same side of `H`.)
2. The hyperplane touches `P`: `∃ x ∈ P, l x = a`. (i.e., `H ∩ P ≠ ∅`.)

This matches the classical geometric intuition: the hyperplane `H` bounds `P` from
"below" and makes contact with `P` at least at one point. Negating `l` gives the
upper-supporting variant `∀ x ∈ P, l x ≤ a`.
-/
def IsSupportingHyperplane (l : StrongDual ℝ E) (a : ℝ) (P : Set E) : Prop := by
  sorry
