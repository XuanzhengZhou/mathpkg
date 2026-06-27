import Mathlib

open CategoryTheory

namespace CategoryTheory.Limits

/-!
# Colimit as a functor

If a category `C` has all colimits of diagrams of index shape `J`, then taking
colimits defines a functor `colim : (J ⥤ C) ⥤ C`. This functor sends:
- a diagram `F : J ⥤ C` to its colimit `colimit F`
- a natural transformation `α : F ⟶ G` to the unique morphism
  `colim.map α : colimit F ⟶ colimit G` induced by the universal property
  (the composite cocone `F(j) ⟶ G(j) ⟶ colimit G`).

In Mathlib4, this functor is defined as `colim` inside the `HasColimitsOfShape`
typeclass. We restate it here as an explicit definition.
-/

section colimit_as_a_functor

  variable {J C : Type*} [Category J] [Category C]

  /-- If `C` has all colimits of shape `J`, then taking colimits defines a functor
  `colim : (J ⥤ C) ⥤ C` from the functor category to `C`.

  - On objects: sends a diagram `F : J ⥤ C` to its colimit `colimit F`.
  - On morphisms: sends a natural transformation `α : F ⟶ G` to the unique
    morphism `colim.map α : colimit F ⟶ colimit G` induced by the composite
    cocone `F(j) → G(j) → colimit G`. -/
  noncomputable def colimitAsAFunctor [HasColimitsOfShape J C] : (J ⥤ C) ⥤ C := by
    sorry
