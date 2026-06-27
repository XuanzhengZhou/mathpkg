import Mathlib

/-!
# Functor of Several Variables (Mixed Variance)

A functor `T` of two variables, contravariant in the first and covariant in the second,
from categories `C` and `D` to `E`. This assigns:
- an object `T(C, D)` in `E` for each `C ∈ C`, `D ∈ D`
- for each `f : C → C'` in `C` and `g : D → D'` in `D`, a morphism
  `T(f, g) : T(C', D) → T(C, D')`

satisfying `T(1_C, 1_D) = 1_{T(C, D)}` and `T(f' ∘ f, g' ∘ g) = T(f, g') ∘ T(f', g)`.

In Mathlib4, this is represented as an ordinary functor `Cᵒᵖ × D ⥤ E`, where the
contravariance in the first variable is handled by the opposite category construction.
-/

open CategoryTheory

universe u v w u₁ v₁ u₂ v₂ u₃ v₃

/-- A **functor of two variables, contravariant in the first, covariant in the second**
from `C` and `D` to `E`. This is exactly a functor `Cᵒᵖ × D ⥤ E`. -/
def MixedVarianceFunctor (C : Type u₁) [Category.{v₁} C]
    (D : Type u₂) [Category.{v₂} D]
    (E : Type u₃) [Category.{v₃} E] : Type (max u₁ v₁ u₂ v₂ u₃ v₃) := by
  sorry
