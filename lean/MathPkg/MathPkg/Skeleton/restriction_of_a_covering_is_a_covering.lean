import Mathlib

open Set

/-!
# Restriction of a Covering Is a Covering

If `p : Y → X` is a covering map and `X'` is any subspace of `X`, then the restriction
`p' : p⁻¹(X') → X'` is also a covering map.

## Main Statement

* `restriction_of_a_covering_is_a_covering`: the restriction of a covering map to a subspace
  of the base is again a covering map.
-/

/-- The restriction of a covering map `p : Y → X` to a subspace `X' ⊆ X` is again a covering map.
The restricted map is defined on `p⁻¹(X')` (with the subspace topology from `Y`) and maps into
`X'` (with the subspace topology from `X`) by sending `y` to `p y`. -/
theorem restriction_of_a_covering_is_a_covering {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y]
    (p : Y → X) (hp : IsCoveringMap p) (X' : Set X) :
    IsCoveringMap (fun (y : (p ⁻¹' X')) => (⟨p y.val, y.property⟩ : X')) := by
  sorry
