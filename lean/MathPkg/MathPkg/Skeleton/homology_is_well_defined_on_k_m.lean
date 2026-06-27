import Mathlib

open CategoryTheory HomologicalComplex

/- Homology is well-defined on the homotopy category K(M) -/
theorem homology_is_well_defined_on_K_M {A : Type _} [Category A] [Preadditive A]
    {ι : Type _} {c : ComplexShape ι}
    (X Y : HomologicalComplex A c) (f g : X ⟶ Y) (h : Homotopy f g) (i : ι)
    [X.HasHomology i] [Y.HasHomology i] :
    homologyMap f i = homologyMap g i := by
  sorry
