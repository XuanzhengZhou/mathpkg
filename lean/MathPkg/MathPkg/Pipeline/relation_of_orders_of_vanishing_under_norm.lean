import Mathlib

open Finset

/--
  Relation of Orders of Vanishing Under the Norm Map

  Let h : X → Y be a morphism of algebraic curves, with function fields
  F' = C(X) and F = C(Y). For a place y ∈ Y, the valuation of the norm
  of f ∈ F'^{×} equals the sum of valuations over the fiber h⁻¹(y):

    ν_y(norm_h f) = Σ_{x ∈ h⁻¹(y)} ν_x(f)

  This is a fundamental formula in algebraic number theory and the theory
  of algebraic function fields.
-/
lemma relation_of_orders_of_vanishing_under_norm
    {X Y : Type} [Fintype X] [Fintype Y] [DecidableEq X] [DecidableEq Y]
    (h : X → Y)
    (F' F : Type) [Field F'] [Field F] [Algebra F F'] [FiniteDimensional F F']
    (ν_F' : X → F' → ℤ) (ν_F : Y → F → ℤ)
    (norm_h : F' → F) (y : Y) (f : F') (hf : f ≠ 0) :
    ν_F y (norm_h f) = ((univ : Finset X).filter (λ x => h x = y)).sum (λ x => ν_F' x f) := by
  sorry
