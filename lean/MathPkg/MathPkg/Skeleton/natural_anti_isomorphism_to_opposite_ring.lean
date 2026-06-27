import Mathlib

open MulOpposite

/-!
# Natural Anti-isomorphism to Opposite Ring

The identity map on the underlying set, r ↦ r, is an anti-isomorphism from
a ring R to its opposite ring Rᵒᵖ.

In Mathlib4, the map is `MulOpposite.op` (and its inverse is `MulOpposite.unop`).
This map is:
- **Bijective**: `MulOpposite.opEquiv` gives the canonical bijection between R and Rᵐᵒᵖ
- **Additive**: `op (a + b) = op a + op b` (rfl)
- **Anti-multiplicative**: `op (a * b) = op b * op a` (rfl, this is the definition of multiplication in Rᵐᵒᵖ)

For commutative rings, this anti-isomorphism is actually an ordinary ring isomorphism
(`MulOpposite.opMulEquiv`). For non-commutative rings, it is a genuine anti-isomorphism.
-/

/-! ### 1. Definition of Ring Anti-isomorphism

We define a `RingAntiEquiv` as a bijective map between rings that preserves addition
and reverses multiplication. -/

/-- A `RingAntiEquiv R S` is a bijective map `R → S` that preserves addition
and reverses multiplication: `φ(a + b) = φ a + φ b` and `φ(a * b) = φ b * φ a`.

This is the appropriate notion of "anti-isomorphism" between (possibly non-commutative) rings.
-/
structure RingAntiEquiv (R S : Type*) [Add R] [Mul R] [Add S] [Mul S] extends R ≃ S where
  map_add' : ∀ x y, toEquiv (x + y) = toEquiv x + toEquiv y
  map_mul' : ∀ x y, toEquiv (x * y) = toEquiv y * toEquiv x

/-- Notation for `RingAntiEquiv`. -/
infixl:25 " ≃ₐ+* " => RingAntiEquiv

namespace RingAntiEquiv

variable {R S T : Type*} [Add R] [Mul R] [Add S] [Mul S] [Add T] [Mul T]

instance : CoeFun (R ≃ₐ+* S) fun _ => R → S := by
  sorry
