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
    cases f; cases g; congr

@[simp]
theorem toFun_eq_coe (f : MiddleLinearMap R A B C) : f.toFun = f := rfl

@[ext]
theorem ext {f g : MiddleLinearMap R A B C} (h : ∀ a b, f a b = g a b) : f = g :=
  DFunLike.coe_injective (funext fun a => funext fun b => h a b)

@[simp]
theorem coe_mk (f : A → B → C) (h1 h2 h3) : (⟨f, h1, h2, h3⟩ : MiddleLinearMap R A B C) = f := rfl

/-- `f 0 b = 0`. Derived from additivity. -/
@[simp]
theorem map_zero_left (f : MiddleLinearMap R A B C) (b : B) : f 0 b = 0 := by
  have h := f.map_add_left 0 0 b
  rw [zero_add] at h
  have h2 : (f 0 b) + (f 0 b) = (f 0 b) + 0 := by
    calc
      (f 0 b) + (f 0 b) = f 0 b := Eq.symm h
      _ = (f 0 b) + 0 := by simp
  exact add_left_cancel h2

/-- `f a 0 = 0`. Derived from additivity. -/
@[simp]
theorem map_zero_right (f : MiddleLinearMap R A B C) (a : A) : f a 0 = 0 := by
  have h := f.map_add_right a 0 0
  rw [zero_add] at h
  have h2 : (f a 0) + (f a 0) = (f a 0) + 0 := by
    calc
      (f a 0) + (f a 0) = f a 0 := Eq.symm h
      _ = (f a 0) + 0 := by simp
  exact add_left_cancel h2

/-- The additive monoid hom induced by the first argument. -/
def toAddMonoidHom₁ (f : MiddleLinearMap R A B C) (b : B) : A →+ C where
  toFun a := f a b
  map_zero' := map_zero_left f b
  map_add' x y := f.map_add_left x y b

/-- The additive monoid hom induced by the second argument. -/
def toAddMonoidHom₂ (f : MiddleLinearMap R A B C) (a : A) : B →+ C where
  toFun b := f a b
  map_zero' := map_zero_right f a
  map_add' x y := f.map_add_right a x y

instance : Zero (MiddleLinearMap R A B C) where
  zero :=
    { toFun := fun _ _ => 0
      map_add_left := fun _ _ _ => by simp
      map_add_right := fun _ _ _ => by simp
      map_smul_balanced := fun _ _ _ => by simp }

@[simp]
theorem zero_apply (a : A) (b : B) : (0 : MiddleLinearMap R A B C) a b = 0 := rfl

instance : Add (MiddleLinearMap R A B C) where
  add f g :=
    { toFun := fun a b => f a b + g a b
      map_add_left := fun a₁ a₂ b => by
        have hf : f (a₁ + a₂) b = f a₁ b + f a₂ b := f.map_add_left a₁ a₂ b
        have hg : g (a₁ + a₂) b = g a₁ b + g a₂ b := g.map_add_left a₁ a₂ b
        rw [hf, hg]
        abel
      map_add_right := fun a b₁ b₂ => by
        have hf : f a (b₁ + b₂) = f a b₁ + f a b₂ := f.map_add_right a b₁ b₂
        have hg : g a (b₁ + b₂) = g a b₁ + g a b₂ := g.map_add_right a b₁ b₂
        rw [hf, hg]
        abel
      map_smul_balanced := fun r a b => by
        have hf : f (r • a) b = f a (r • b) := f.map_smul_balanced r a b
        have hg : g (r • a) b = g a (r • b) := g.map_smul_balanced r a b
        rw [hf, hg] }

@[simp]
theorem add_apply (f g : MiddleLinearMap R A B C) (a : A) (b : B) : (f + g) a b = f a b + g a b := rfl

instance : AddCommMonoid (MiddleLinearMap R A B C) where
  add := (· + ·)
  zero := 0
  add_assoc f g h := by
    ext a b; simp [add_apply]; abel
  zero_add f := by
    ext a b; simp [add_apply, zero_apply]
  add_zero f := by
    ext a b; simp [add_apply, zero_apply]
  add_comm f g := by
    ext a b; simp [add_apply]; abel
  nsmul := nsmulRec

/-- A middle linear map composed on the target with an additive group homomorphism
is again a middle linear map. -/
def compAddMonoidHom (f : MiddleLinearMap R A B C) (g : C →+ D) : MiddleLinearMap R A B D where
  toFun a b := g (f a b)
  map_add_left a₁ a₂ b := by
    simpa [AddMonoidHom.map_add] using congrArg g (f.map_add_left a₁ a₂ b)
  map_add_right a b₁ b₂ := by
    simpa [AddMonoidHom.map_add] using congrArg g (f.map_add_right a b₁ b₂)
  map_smul_balanced r a b := by
    simpa using congrArg g (f.map_smul_balanced r a b)

end MiddleLinearMap

-- Example 1: The multiplication map ℤ × ℤ → ℤ is middle ℤ-linear.
example : MiddleLinearMap ℤ ℤ ℤ ℤ where
  toFun a b := a * b
  map_add_left a₁ a₂ b := by ring
  map_add_right a b₁ b₂ := by ring
  map_smul_balanced r a b := by
    simp_rw [smul_eq_mul]
    ring

-- Example 2: The dot product ℝⁿ × ℝⁿ → ℝ is middle ℝ-linear.
example (n : ℕ) : MiddleLinearMap ℝ (Fin n → ℝ) (Fin n → ℝ) ℝ where
  toFun a b := ∑ i : Fin n, a i * b i
  map_add_left a₁ a₂ b := by
    simp_rw [Pi.add_apply, add_mul, Finset.sum_add_distrib]
  map_add_right a b₁ b₂ := by
    simp_rw [Pi.add_apply, mul_add, Finset.sum_add_distrib]
  map_smul_balanced r a b := by
    simp_rw [Pi.smul_apply, smul_eq_mul]
    simp_rw [mul_assoc, mul_comm r, ← mul_assoc]

-- Example 3: The zero map is middle linear.
example : MiddleLinearMap ℤ ℤ ℤ ℤ := 0

-- Example 4: We can add two middle linear maps.
example (f g : MiddleLinearMap ℤ ℤ ℤ ℤ) : MiddleLinearMap ℤ ℤ ℤ ℤ := f + g

-- Example 5: From a raw function satisfying the axioms, we can build a middle linear map.
example (f : ℤ → ℤ → ℤ) (haddl : ∀ a₁ a₂ b, f (a₁ + a₂) b = f a₁ b + f a₂ b)
    (haddr : ∀ a b₁ b₂, f a (b₁ + b₂) = f a b₁ + f a b₂)
    (hs : ∀ r a b, f (r * a) b = f a (r * b)) : MiddleLinearMap ℤ ℤ ℤ ℤ where
  toFun := f
  map_add_left := haddl
  map_add_right := haddr
  map_smul_balanced r a b := by
    simpa [smul_eq_mul] using hs r a b
