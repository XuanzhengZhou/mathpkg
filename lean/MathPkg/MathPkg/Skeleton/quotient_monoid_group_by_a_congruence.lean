import Mathlib

open Con

/-!
# Quotient Monoid/Group by a Congruence

Let R be an equivalence relation on a monoid G such that a₁ ~ a₂ and b₁ ~ b₂ imply
a₁·b₁ ~ a₂·b₂ for all a_i, b_i ∈ G. Then G/R with operation [a]·[b] = [a·b] is a monoid.
If G is a group, G/R is a group; if G is abelian, G/R is abelian.

Mathlib4 provides this via `Con` (congruence relation) and `Con.Quotient`.
All the results below are existing instances in Mathlib4.
-/

/-- Part 1: The quotient of a monoid by a congruence relation is a monoid.
The identity is the class of the identity element [e],
and multiplication is defined by [a]·[b] = [a·b]. -/
example {M : Type*} [Monoid M] (c : Con M) : Monoid c.Quotient := by
  sorry
