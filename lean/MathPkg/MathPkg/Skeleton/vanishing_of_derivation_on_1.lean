import Mathlib

/-!
# Vanishing of Derivation on 1

For any derivation `d : S → M`, `d(1) = 0`.

This follows from the Leibniz rule:
`d(1) = d(1·1) = 1·d(1) + 1·d(1) = d(1) + d(1)`, hence `d(1) = 0`.

Note: Mathlib already provides `Derivation.map_one_eq_zero` for this fact.
We restate it here for completeness with the concept in the dependency graph.
-/

open Algebra

/-- For any derivation `d : Derivation R S M` from an `R`-algebra `S` to an `S`-module `M`,
`d(1) = 0`. -/
theorem vanishing_of_derivation_on_1 {R S M : Type*}
    [CommSemiring R] [CommSemiring S] [AddCommMonoid M]
    [Algebra R S] [Module S M] [Module R M]
    (d : Derivation R S M) : d 1 = 0 := by
  sorry
