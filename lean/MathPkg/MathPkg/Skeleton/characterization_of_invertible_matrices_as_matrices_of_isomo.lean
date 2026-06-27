import Mathlib

open scoped Classical

/-!
# Characterization of Invertible Matrices as Matrices of Isomorphisms

Let R be a ring with identity and E, F free left R-modules with ordered bases V, V′ respectively
such that |V| = n = |V′|. For A ∈ Mat_n R, A is invertible if and only if A is the matrix
of an isomorphism f: E → F relative to V and V′. In this case A⁻¹ is the matrix of f⁻¹
relative to V′ and V.

Mathlib4 provides `Matrix.toLinOfInv` for the forward direction (invertible matrix ⇒ isomorphism)
and `LinearMap.toMatrix_comp` for the reverse direction (isomorphism matrix ⇒ invertible).
-/

section characterization_of_invertible_matrices_as_matrices_of_isomorphisms

variable (R : Type*) [CommRing R]
variable (E F : Type*) [AddCommGroup E] [Module R E] [AddCommGroup F] [Module R F]
variable (ι : Type*) [Fintype ι] [DecidableEq ι]
variable (b_E : Module.Basis ι R E) (b_F : Module.Basis ι R F)

/-- **Characterization of Invertible Matrices**: A square matrix A (of size |ι| × |ι|) over a
commutative ring R is invertible (i.e., a unit in the matrix ring) if and only if A is the matrix
of an isomorphism f: E → F relative to the bases b_E and b_F.

Formally: `IsUnit A ↔ ∃ (f : E ≃ₗ[R] F), LinearMap.toMatrix b_E b_F (f : E →ₗ[R] F) = A`.

The forward direction uses `Matrix.toLinOfInv` to construct the isomorphism from the
two-sided inverse of A. The reverse direction uses `LinearMap.toMatrix_comp` to show that
A * (matrix of f⁻¹) = 1 and (matrix of f⁻¹) * A = 1, hence A is a unit. -/
theorem characterization_of_invertible_matrices_as_matrices_of_isomorphisms
    (A : Matrix ι ι R) :
    IsUnit A ↔ ∃ (f : E ≃ₗ[R] F), LinearMap.toMatrix b_E b_F (f : E →ₗ[R] F) = A := by
  sorry
