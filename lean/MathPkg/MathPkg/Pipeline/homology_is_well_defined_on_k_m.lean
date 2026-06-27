import Mathlib

open CategoryTheory

/- Homology is well-defined on the homotopy category K(M) -/
theorem homology_is_well_defined_on_K_M {A : Type _} [Category A] [Abelian A]
    {ι : Type _} {c : ComplexShape ι} [DecidableEq ι]
    (X Y : HomologicalComplex A c) (f g : X ⟶ Y) (h : Homotopy f g) (i : ι) :
    (homologyFunctor A c i).map f = (homologyFunctor A c i).map g := by
  sorry
