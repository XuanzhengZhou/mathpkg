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
abbrev MixedVarianceFunctor (C : Type u₁) [Category.{v₁} C]
    (D : Type u₂) [Category.{v₂} D]
    (E : Type u₃) [Category.{v₃} E] :=
  (Cᵒᵖ × D) ⥤ E

namespace MixedVarianceFunctor

variable {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]
  {E : Type u₃} [Category.{v₃} E] (T : MixedVarianceFunctor C D E)

/-- The image of an object `(C, D)` under a mixed-variance functor `T`,
written `T(C, D)`. -/
abbrev obj' (c : C) (d : D) : E := T.obj (Opposite.op c, d)

/-- The image of a pair of morphisms `f : C → C'` and `g : D → D'` under a mixed-variance
functor `T`, producing a morphism `T(C', D) ⟶ T(C, D')`. Note the contravariance
in the first variable: the direction of `f` is reversed. -/
def map' {c c' : C} (f : c ⟶ c') {d d' : D} (g : d ⟶ d') : T.obj' c' d ⟶ T.obj' c d' :=
  T.map (f.op, g)

/-- The identity law: `T(1_C, 1_D) = 1_{T(C, D)}`. -/
theorem map_id_mixed (c : C) (d : D) : T.map' (𝟙 c) (𝟙 d) = 𝟙 (T.obj' c d) := by
  dsimp [map', obj']
  calc
    T.map ((𝟙 c).op, 𝟙 d) = T.map (𝟙 (Opposite.op c), 𝟙 d) := by simp
    _ = T.map (𝟙 (Opposite.op c, d)) := rfl
    _ = 𝟙 (T.obj (Opposite.op c, d)) := T.map_id _

/-- The composition law for a mixed-variance functor:
`T(f' ∘ f, g' ∘ g) = T(f', g) ∘ T(f, g')`.

Note that `T(f', g)` is applied first (to `T(C'', D), D → T(C', D')`), then `T(f, g')`
(to `T(C', D') → T(C, D'')`). This matches the order `T(f, g') ∘ T(f', g)`. -/
theorem map_comp_mixed {c c' c'' : C} (f : c ⟶ c') (f' : c' ⟶ c'')
    {d d' d'' : D} (g : d ⟶ d') (g' : d' ⟶ d'') :
    T.map' (f ≫ f') (g ≫ g') = T.map' f' g ≫ T.map' f g' := by
  unfold map'
  let φ : (Opposite.op c'', d) ⟶ (Opposite.op c', d') := (f'.op, g)
  let ψ : (Opposite.op c', d') ⟶ (Opposite.op c, d'') := (f.op, g')
  have h := T.map_comp φ ψ
  simpa [op_comp] using h

end MixedVarianceFunctor

/-! ## Examples -/

/-- Example: the constant mixed-variance functor sending every pair `(C, D)` to a fixed
object `X` in `E`, and every pair of morphisms to the identity on `X`. -/
example (C D E : Type*) [Category C] [Category D] [Category E] (X : E) :
    MixedVarianceFunctor C D E where
  obj := fun _ => X
  map := fun _ => 𝟙 X
  map_id _ := rfl
  map_comp _ _ := by simp

/-- Example: a mixed-variance functor `Cᵒᵖ × D ⥤ D` defined by projecting onto the
second factor, ignoring the contravariant `C` argument. -/
example (C D : Type*) [Category C] [Category D] : MixedVarianceFunctor C D D where
  obj := fun ⟨_, d⟩ => d
  map := fun ⟨_, g⟩ => g
  map_id _ := rfl
  map_comp _ _ := rfl
