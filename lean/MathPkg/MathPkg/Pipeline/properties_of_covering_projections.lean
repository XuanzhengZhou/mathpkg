import Mathlib

open Set

/-!
# Properties of Covering Projections

If `p : Y → X` is a covering map, then the fibers are discrete, `p` is a local
homeomorphism, and the topology on `X` is the quotient topology from `Y`.
-/

/-- Let `p : Y → X` be a covering projection. Then:
(i) For every `x ∈ X`, the fiber `p⁻¹({x})` is a discrete subset of `Y`.
(ii) `p` is a local homeomorphism.
(iii) The topology on `X` is the quotient topology it inherits from `Y` via the map `p`. -/
theorem properties_of_covering_projections {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y]
    (p : Y → X) (hp : IsCoveringMap p) :
    (∀ x : X, DiscreteTopology {y | p y = x}) ∧ IsLocalHomeomorph p ∧ IsQuotientMap p := by
  sorry
