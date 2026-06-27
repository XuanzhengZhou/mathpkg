import Mathlib

open CategoryTheory
open CategoryTheory.Limits

/- hom_functor_preserves_limits -/

/-- A cone `c` over a diagram `F` in a category `C` is a limit cone if and only if
    for every object `X` in `Cᵒᵖ`, the image of `c` under the covariant hom-functor
    `coyoneda.obj X` is a limit cone in `Type v`.
    This is the statement that representable functors jointly reflect limits. -/
noncomputable def hom_functor_preserves_limits {C : Type u} [Category.{v} C] {J : Type w} [Category.{t} J]
    {F : J ⥤ C} (c : Cone F) :
    IsLimit c ≃ ∀ (X : Cᵒᵖ), IsLimit ((coyoneda.obj X).mapCone c) := by
  sorry
