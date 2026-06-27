import Mathlib

open scoped Classical
open CategoryTheory
open CategoryTheory.Limits

/-!
# Coequalizer as a colimit

The **coequalizer** of a pair of parallel morphisms `ψ, ψ' : C₁ ⟶ C₂` in a category `C`
is the colimit of the diagram `parallelPair ψ ψ' : WalkingParallelPair ⥤ C`.

This diagram consists of two objects (`C₁` and `C₂`), their identity morphisms,
and the two morphisms `ψ` and `ψ'`.

Mathlib4 defines `coequalizer f g` as `colimit (parallelPair f g)` — this is the standard
definition of a coequalizer as a special case of a colimit.

The universal property: for any object `W` and morphism `k : C₂ ⟶ W` such that
`ψ ≫ k = ψ' ≫ k`, there exists a unique morphism `coequalizer ψ ψ' ⟶ W` making the
diagram commute.
-/

section coequalizer_as_a_colimit

variable {C : Type u} [Category.{v} C]

/-- The coequalizer of two parallel morphisms `f, g : X ⟶ Y` is defined as
the colimit of the diagram `parallelPair f g`. This is the standard Mathlib4 definition.

We re-state it here with explicit docstring to show that the coequalizer **is**
the colimit, not a distinct construction. -/
def coequalizerAsColimit (X Y : C) (f g : X ⟶ Y) [HasColimit (parallelPair f g)] : C := by
  sorry
