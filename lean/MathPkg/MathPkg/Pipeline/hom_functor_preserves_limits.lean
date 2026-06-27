import Mathlib

open CategoryTheory
open CategoryTheory.Limits

/- hom_functor_preserves_limits -/

/-- A cone `c` over a diagram `D` in a category `C` is a limit cone if and only if
    for every object `A` in `C`, the image of `c` under the covariant hom-functor
    `Hom_C(A, −)` (i.e., `coyoneda.obj (Opposite.op A)`) is a limit cone in `Type v`.
    This is the statement that representable functors jointly reflect limits. -/
theorem hom_functor_preserves_limits {C : Type u} [Category.{v} C] {J : Type w} [Category.{t} J]
    (D : J ⥤ C) (c : Cone D) :
    IsLimit c ↔ ∀ (A : C), IsLimit ((coyoneda.obj (Opposite.op A)).mapCone c) := by
  sorry
