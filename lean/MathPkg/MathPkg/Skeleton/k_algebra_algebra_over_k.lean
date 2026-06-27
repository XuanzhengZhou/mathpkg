import Mathlib

open scoped Classical

/-!
# K-algebra (Algebra over K)

Let `K` be a commutative ring with identity. A **K-algebra** (or algebra over K) `A` is a ring `A`
such that:
(i) `(A, +)` is a unitary (left) `K`-module;
(ii) `k(ab) = (ka)b = a(kb)` for all `k ∈ K` and `a, b ∈ A`.

In Mathlib4, this is the typeclass `Algebra R A` where `R` is a `CommSemiring` and `A` is a
`Semiring`. The compatibility condition `k(ab) = (ka)b = a(kb)` is split into two theorems:
`Algebra.smul_mul_assoc` and `Algebra.mul_smul_comm`.

## Sub-concepts

- **Division algebra**: A K-algebra `A` which, as a ring, is a division ring.
- **Finite dimensional algebra over a field**: An algebra over a field `K` that is finite
  dimensional as a vector space over `K`.
-/

/-! ### 1. K-algebra: the `Algebra` typeclass -/

section algebra_definition

variable (K A : Type*) [CommSemiring K] [Semiring A] [Algebra K A]

/-- The canonical ring homomorphism `K →+* A` embedding the base ring into the algebra. -/
example : K →+* A := algebraMap K A

/-- Scalar multiplication is given by left multiplication by `algebraMap`. -/
example (k : K) (a : A) : k • a = algebraMap K A k * a := by
  sorry
