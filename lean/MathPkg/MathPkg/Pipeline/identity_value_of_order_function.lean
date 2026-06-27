import Mathlib

/-!
# Identity Value of Order Function

For an order function `ρ` on an `F`-algebra `R`:
- `ρ(1) = 0`
- `ρ(f) = 0` if and only if `f` is a nonzero constant in `F`
-/

lemma identity_value_of_order_function {F : Type u} [Field F] {R : Type v} [CommRing R] [Algebra F R]
    {Γ : Type w} [LinearOrderedAddCommMonoid Γ] (ρf : OrderFunction F R Γ) :
    ρf.ρ 1 = (0 : WithBot Γ) ∧ (∀ (f : R), ρf.ρ f = (0 : WithBot Γ) ↔ ∃ (λ : F), λ ≠ 0 ∧ (algebraMap F R) λ = f) := by
  sorry
