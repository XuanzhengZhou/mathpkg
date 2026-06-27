import Mathlib

open CategoryTheory
open CategoryTheory.Limits

/- uniqueness_of_products_up_to_isomorphism - If A and B are both products of the same family {A_i}, then A and B are isomorphic. -/
def uniqueness_of_products_up_to_isomorphism {C : Type u} [Category.{v} C] {ι : Type w} (F : Discrete ι ⥤ C) (cA cB : Cone F) (hA : IsLimit cA) (hB : IsLimit cB) : cA.pt ≅ cB.pt := by
  sorry
