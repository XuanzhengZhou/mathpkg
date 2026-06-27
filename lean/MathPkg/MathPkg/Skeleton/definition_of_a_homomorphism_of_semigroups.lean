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
theorem map_mul (f : SemigroupHom G H) (a b : G) : f (a * b) = f a * f b := by
  sorry
