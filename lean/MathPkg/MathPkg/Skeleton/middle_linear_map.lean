import Mathlib

/-- A middle linear map (also called R-balanced map) from `A × B` to `C`.
`A` is a right R-module, `B` is a left R-module, and `C` is an additive abelian group.
For a commutative ring `R`, this is the structure underlying the universal property
of the tensor product `A ⊗[R] B`.

The conditions are:
1. `f(a₁ + a₂, b) = f(a₁, b) + f(a₂, b)` — additive in first argument
2. `f(a, b₁ + b₂) = f(a, b₁) + f(a, b₂)` — additive in second argument
3. `f(r·a, b) = f(a, r·b)` — balanced / middle linear

In Mathlib4, the tensor product is defined using exactly this balanced condition
(see `TensorProduct.liftAddHom` and its `hf` parameter).
-/
structure MiddleLinearMap (R : Type*) [CommSemiring R]
    (A : Type*) [AddCommMonoid A] [Module R A]
    (B : Type*) [AddCommMonoid B] [Module R B]
    (C : Type*) [AddCommGroup C] where
  /-- The underlying function `A → B → C`. -/
  toFun : A → B → C
  /-- Additivity in the first argument: `f(a₁ + a₂, b) = f(a₁, b) + f(a₂, b)`. -/
  map_add_left (a₁ a₂ : A) (b : B) : toFun (a₁ + a₂) b = toFun a₁ b + toFun a₂ b
  /-- Additivity in the second argument: `f(a, b₁ + b₂) = f(a, b₁) + f(a, b₂)`. -/
  map_add_right (a : A) (b₁ b₂ : B) : toFun a (b₁ + b₂) = toFun a b₁ + toFun a b₂
  /-- Middle linearity / balanced condition: `f(r·a, b) = f(a, r·b)`. -/
  map_smul_balanced (r : R) (a : A) (b : B) : toFun (r • a) b = toFun a (r • b)

namespace MiddleLinearMap

variable {R : Type*} [CommSemiring R]
  {A : Type*} [AddCommMonoid A] [Module R A]
  {B : Type*} [AddCommMonoid B] [Module R B]
  {C D : Type*} [AddCommGroup C] [AddCommGroup D]

instance : FunLike (MiddleLinearMap R A B C) A (B → C) where
  coe f := f.toFun
  coe_injective f g h := by
    sorry
