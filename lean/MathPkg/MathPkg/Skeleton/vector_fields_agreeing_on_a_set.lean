import Mathlib

open Set

/--
Two vector fields `V` and `W` on a type `X` (taking values in some codomain `Y`)
**agree on a set** `A` if `V(p) = W(p)` for all `p ∈ A`.

This is equivalent to `Set.EqOn V W A` from Mathlib4, which already captures the
same notion for any two functions. We introduce this as an abbrev for readability
in contexts where the "vector field" terminology is preferred.

Note: In the context of smooth manifolds, a vector field is typically a section
of the tangent bundle, i.e., `V : Π (x : M), TangentSpace I x`. The definition
here generalizes to any two functions with the same codomain.
-/
abbrev VectorField.AgreeOn {X Y : Type*} (V W : X → Y) (A : Set X) : Prop := by
  sorry
