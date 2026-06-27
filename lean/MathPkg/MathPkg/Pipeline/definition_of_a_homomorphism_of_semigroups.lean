import Mathlib

/-!
# Definition of a Homomorphism of Semigroups

Let `G` and `H` be semigroups. A function `f : G → H` that preserves the semigroup
operation (i.e., `f (a * b) = f a * f b` for all `a, b ∈ G`) is called a
**semigroup homomorphism**.

Mathlib4 already provides `MulHom` (notation `G →ₙ* H`) for exactly this purpose.
We define `SemigroupHom` as a type alias to make the terminology explicit.
-/

/-- A semigroup homomorphism from `G` to `H` is a map preserving multiplication.
This is exactly `MulHom G H` (notation `G →ₙ* H`).
Using `abbrev` ensures the `FunLike` and `MulHomClass` instances are available. -/
abbrev SemigroupHom (G H : Type*) [Semigroup G] [Semigroup H] := G →ₙ* H

namespace SemigroupHom

variable {G H : Type*} [Semigroup G] [Semigroup H]

/-- A semigroup homomorphism preserves the operation: `f (a * b) = f a * f b`. -/
theorem map_mul (f : SemigroupHom G H) (a b : G) : f (a * b) = f a * f b :=
  MulHom.map_mul f a b

end SemigroupHom

/-! ## Examples -/

/-- Example: the natural inclusion `ℕ → ℤ` (both under multiplication) is a
semigroup homomorphism. -/
example : SemigroupHom ℕ ℤ where
  toFun := fun n => (n : ℤ)
  map_mul' := by
    intro a b
    simp

/-- Example: on a commutative semigroup, the squaring map `x ↦ x * x` is a
semigroup homomorphism. -/
example [CommSemigroup G] : SemigroupHom G G where
  toFun := fun x => x * x
  map_mul' := by
    intro a b
    simp [mul_comm, mul_left_comm]

/-- Example: the constant map to the identity is a semigroup homomorphism
when the target has a one (a monoid).  Here we show a simpler example:
the projection `ℕ × ℕ → ℕ` on the first coordinate. -/
example : SemigroupHom (ℕ × ℕ) ℕ where
  toFun := Prod.fst
  map_mul' := by
    intro a b
    rfl
