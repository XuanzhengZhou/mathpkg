import Mathlib

/-!
# Identity Value of Order Function

For an order function `ρ` on an `F`-algebra `R`:
- `ρ(1) = 0`
- `ρ(f) = 0` if and only if `f` is a nonzero constant in `F`
-/

lemma identity_value_of_order_function {F : Type u} [Field F] {R : Type v} [CommRing R] [Algebra F R]
    {Γ₀ : Type w} [LinearOrderedAddCommMonoidWithTop Γ₀] (v : AddValuation R Γ₀) :
    v 1 = (0 : Γ₀) ∧ (∀ (f : R), v f = (0 : Γ₀) ↔ ∃ (c : F), c ≠ 0 ∧ (algebraMap F R) c = f) := by
  sorry
