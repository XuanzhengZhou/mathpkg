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
example (k : K) (a : A) : k • a = algebraMap K A k * a :=
  Algebra.smul_def k a

/-- The image of `K` lies in the center of `A`. -/
example (k : K) (a : A) : algebraMap K A k * a = a * algebraMap K A k :=
  Algebra.commutes k a

/-- Condition (ii) part 1: `k • (a * b) = (k • a) * b` -/
example (k : K) (a b : A) : k • (a * b) = (k • a) * b :=
  (Algebra.smul_mul_assoc k a b).symm

/-- Condition (ii) part 2: `(k • a) * b = a * (k • b)` -/
example (k : K) (a b : A) : (k • a) * b = a * (k • b) := by
  calc
    (k • a) * b = k • (a * b) := Algebra.smul_mul_assoc k a b
    _ = a * (k • b) := (Algebra.mul_smul_comm k a b).symm

/-- The full compatibility condition: `k • (a * b) = a * (k • b)` -/
example (k : K) (a b : A) : k • (a * b) = a * (k • b) :=
  (Algebra.mul_smul_comm k a b).symm

/-- The textbook condition chained: `k(ab) = (ka)b = a(kb)` -/
example (k : K) (a b : A) : k • (a * b) = (k • a) * b ∧ (k • a) * b = a * (k • b) := by
  constructor
  · exact (Algebra.smul_mul_assoc k a b).symm
  · calc
    (k • a) * b = k • (a * b) := Algebra.smul_mul_assoc k a b
    _ = a * (k • b) := (Algebra.mul_smul_comm k a b).symm

end algebra_definition

/-! ### 2. Division algebra -/

section division_algebra

/-- A **division algebra** over `K` is a K-algebra whose underlying ring is a division ring. -/
def IsDivisionAlgebra (K A : Type*) [CommRing K] [Ring A] [Algebra K A] : Prop :=
  IsDomain A ∧ ∀ a : A, a ≠ 0 → IsUnit a

/-- Example: The real numbers form a division algebra over the rational numbers. -/
example : IsDivisionAlgebra ℚ ℝ := by
  refine ⟨by infer_instance, fun a ha => ?_⟩
  exact IsUnit.mk0 a ha

/-- Example: The complex numbers form a division algebra over the real numbers. -/
example : IsDivisionAlgebra ℝ ℂ := by
  refine ⟨by infer_instance, fun a ha => ?_⟩
  exact IsUnit.mk0 a ha

/-- A simpler characterization when `A` is already a division ring: -/
example (K A : Type*) [CommRing K] [DivisionRing A] [Algebra K A] : IsDivisionAlgebra K A := by
  refine ⟨by infer_instance, fun a ha => ?_⟩
  exact IsUnit.mk0 a ha

end division_algebra

/-! ### 3. Finite dimensional algebra over a field -/

section finite_dimensional_algebra

/-- A **finite dimensional algebra** over a field `K` is a K-algebra `A` that is finite
dimensional as a vector space over `K`. -/
def IsFiniteDimensionalAlgebra (K A : Type*) [Field K] [Ring A] [Algebra K A] : Prop :=
  FiniteDimensional K A

/-- Example: ℂ is a 2-dimensional ℝ-algebra. -/
example : FiniteDimensional ℝ ℂ := by
  infer_instance

/-- Example: Every finite field extension is a finite dimensional algebra. -/
example (K A : Type*) [Field K] [Field A] [Algebra K A] [FiniteDimensional K A] :
    IsFiniteDimensionalAlgebra K A :=
  ‹_›

/-- The `finrank` of a finite dimensional algebra over `K` is a natural number. -/
example (K A : Type*) [Field K] [Ring A] [Algebra K A] [FiniteDimensional K A] :
    Module.finrank K A = Module.finrank K A := rfl

/-- Complex numbers have finrank 2 over ℝ. -/
example : Module.finrank ℝ ℂ = 2 :=
  Complex.finrank_real_complex

end finite_dimensional_algebra

/-! ### 4. Standard examples of K-algebras -/

section examples

/-- Every commutative ring is an algebra over itself. -/
example (R : Type*) [CommRing R] : Algebra R R := by
  infer_instance

/-- Polynomial ring `K[X]` is a K-algebra. -/
noncomputable example (K : Type*) [CommRing K] : Algebra K (Polynomial K) := by
  infer_instance

/-- Matrix ring `Mₙ(K)` is a K-algebra. -/
example (K : Type*) [CommRing K] (n : ℕ) : Algebra K (Matrix (Fin n) (Fin n) K) := by
  infer_instance

/-- The zero ring is trivially a K-algebra. -/
example (K : Type*) [CommRing K] : Algebra K (Unit) := by
  infer_instance

/-- Product of two K-algebras is a K-algebra. -/
example (K A B : Type*) [CommRing K] [Ring A] [Algebra K A] [Ring B] [Algebra K B] :
    Algebra K (A × B) := by
  infer_instance

end examples

/-! ### 5. Constructing algebras from a ring homomorphism -/

section construct_algebra

/-- Construct an `Algebra R A` from a ring homomorphism `R →+* A` whose image lies in the center. -/
example (R A : Type*) [CommSemiring R] [Semiring A] (f : R →+* A)
    (h : ∀ r x, f r * x = x * f r) : Algebra R A :=
  RingHom.toAlgebra' f h

/-- If `A` is commutative, any ring homomorphism `R →+* A` gives an algebra structure. -/
example (R A : Type*) [CommSemiring R] [CommSemiring A] (f : R →+* A) : Algebra R A :=
  RingHom.toAlgebra f

end construct_algebra
