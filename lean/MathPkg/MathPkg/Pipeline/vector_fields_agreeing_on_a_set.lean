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
abbrev VectorField.AgreeOn {X Y : Type*} (V W : X → Y) (A : Set X) : Prop :=
  Set.EqOn V W A

namespace VectorField.AgreeOn

variable {X Y : Type*} {V W : X → Y} {A : Set X}

/-- Reflexivity: every vector field agrees with itself on any set. -/
example (V : X → Y) (A : Set X) : VectorField.AgreeOn V V A :=
  Set.eqOn_refl V A

/-- Symmetry: if V agrees with W on A, then W agrees with V on A. -/
example (h : VectorField.AgreeOn V W A) : VectorField.AgreeOn W V A :=
  h.symm

/-- Transitivity: if V agrees with W and W agrees with U on A, then V agrees with U on A. -/
example (hVW : VectorField.AgreeOn V W A) (hWU : VectorField.AgreeOn W U A) :
    VectorField.AgreeOn V U A :=
  hVW.trans hWU

/-- If two vector fields agree on A, they are equal at each point of A. -/
example (h : VectorField.AgreeOn V W A) (x : X) (hx : x ∈ A) : V x = W x :=
  h hx

/-- The empty set: any two vector fields agree on the empty set. -/
example (V W : X → Y) : VectorField.AgreeOn V W ∅ :=
  Set.eqOn_empty V W

end VectorField.AgreeOn
