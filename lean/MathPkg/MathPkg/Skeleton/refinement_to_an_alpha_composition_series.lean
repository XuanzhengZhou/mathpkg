import Mathlib

open scoped Classical

/-!
# Refinement to an α-Composition Series

Every α-series (admissible series) in a group G with a set of operators can be refined
to an α-composition series (a maximal α-series with no proper α-refinements).

An α-series is a subnormal series `S : CompositionSeries G` where each term is an
α-subgroup (invariant under the given operators) and each inclusion is α-normal
(i.e., the quotient is operator-simple in the sense of having no proper α-subgroups).

The proof applies Zorn's lemma to the set of all α-series that refine a given α-series,
ordered by refinement (`≤`). Since the union of a chain of α-series is again an α-series,
Zorn's lemma guarantees a maximal element, which is an α-composition series.

In Mathlib4, `CompositionSeries G` represents a finite subnormal series
`⊥ = H₀ ⊲ H₁ ⊲ ⋯ ⊲ Hₙ = ⊤`, and `S ≤ T` means `T` refines `S`.
-/

section refinement_to_an_alpha_composition_series

open Subgroup

/-- An α-series is a composition series where each term is admissible (operator-invariant).

Since the formalization of "operators" depends on context (e.g., a monoid action on `G`),
we define this as a placeholder predicate that can be specialized later. -/
def IsASeries {X : Type u} [Lattice X] [JordanHolderLattice X] (_S : CompositionSeries X) : Prop := by
  sorry
