import Mathlib

open scoped unitInterval

/- Unique Path Lifting -/

theorem unique_path_lifting {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y]
    (p : Y → X) (hp : IsCoveringMap p) (x₀ : X) (y₀ : Y) (hp₀ : p y₀ = x₀)
    (f : I → X) (hf₀ : f 0 = x₀) (hf : Continuous f) :
    ∃! F : I → Y, F 0 = y₀ ∧ Continuous F ∧ p ∘ F = f := by
  sorry
