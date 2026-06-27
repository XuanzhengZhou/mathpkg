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
variable (b_E : Basis ι R E) (b_F : Basis ι R F)

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
  constructor
  · -- Forward direction: If A is a unit in the matrix ring, show it's the matrix of an isomorphism
    intro hA
    let u := hA.unit
    have huA : (u : Matrix ι ι R) = A := hA.unit_spec
    let B : Matrix ι ι R := (u⁻¹ : Units (Matrix ι ι R)) |>.val
    have hAB : A * B = 1 := by
      calc
        A * B = ((u : Matrix ι ι R)) * ((u⁻¹ : Units (Matrix ι ι R)) |>.val) := by rfl
        _ = ((u * u⁻¹ : Units (Matrix ι ι R)) |>.val) := by simp
        _ = ((1 : Units (Matrix ι ι R)) |>.val) := by rw [u.mul_inv]
        _ = (1 : Matrix ι ι R) := by simp
    have hBA : B * A = 1 := by
      calc
        B * A = ((u⁻¹ : Units (Matrix ι ι R)) |>.val) * ((u : Matrix ι ι R)) := by rfl
        _ = ((u⁻¹ * u : Units (Matrix ι ι R)) |>.val) := by simp
        _ = ((1 : Units (Matrix ι ι R)) |>.val) := by rw [u.inv_mul]
        _ = (1 : Matrix ι ι R) := by simp
    -- Construct the linear equivalence using toLinOfInv
    let f := Matrix.toLinOfInv b_E b_F hAB hBA
    refine ⟨f, ?_⟩
    -- The matrix of f should be A
    simpa [f, Matrix.toLinOfInv] using (LinearMap.toMatrix_toLin b_E b_F A)
  · -- Reverse direction: If A is the matrix of an isomorphism f, show A is a unit
    intro ⟨f, hf⟩
    -- f.symm is the inverse isomorphism. Its matrix B should satisfy A * B = 1 and B * A = 1
    let B := LinearMap.toMatrix b_F b_E (f.symm : F →ₗ[R] E)
    have hAB : A * B = 1 := by
      calc
        A * B = LinearMap.toMatrix b_E b_F (f : E →ₗ[R] F) *
                LinearMap.toMatrix b_F b_E (f.symm : F →ₗ[R] E) := by rw [hf]
        _ = LinearMap.toMatrix b_E b_E ((f : E →ₗ[R] F).comp (f.symm : F →ₗ[R] E)) := by
          rw [LinearMap.toMatrix_comp b_E b_F b_E]
        _ = LinearMap.toMatrix b_E b_E (LinearMap.id : E →ₗ[R] E) := by
          have hcomp : ((f : E →ₗ[R] F).comp (f.symm : F →ₗ[R] E)) = LinearMap.id := by
            ext x; simp
          rw [hcomp]
        _ = 1 := by simp
    have hBA : B * A = 1 := by
      calc
        B * A = LinearMap.toMatrix b_F b_E (f.symm : F →ₗ[R] E) *
                LinearMap.toMatrix b_E b_F (f : E →ₗ[R] F) := by rw [hf]
        _ = LinearMap.toMatrix b_F b_F ((f.symm : F →ₗ[R] E).comp (f : E →ₗ[R] F)) := by
          rw [LinearMap.toMatrix_comp b_F b_E b_F]
        _ = LinearMap.toMatrix b_F b_F (LinearMap.id : F →ₗ[R] F) := by
          have hcomp : ((f.symm : F →ₗ[R] E).comp (f : E →ₗ[R] F)) = LinearMap.id := by
            ext x; simp
          rw [hcomp]
        _ = 1 := by simp
    -- A has a two-sided inverse B, so A is a unit
    let u : Units (Matrix ι ι R) := Units.mk A B hAB hBA
    exact ⟨u, rfl⟩

/-- **Inverse Corollary**: If A is invertible with inverse A⁻¹, then A⁻¹ is the matrix of
f⁻¹ relative to the transposed bases. -/
theorem inverse_is_matrix_of_inverse_isomorphism
    (A : Matrix ι ι R) (hA : IsUnit A) :
    (hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val = LinearMap.toMatrix b_F b_E
      ((Matrix.toLinOfInv b_E b_F
        (by
          -- A * A⁻¹ = 1
          have h := hA.unit.mul_inv
          have hval_mul : ((hA.unit * hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) =
                         ((hA.unit : Matrix ι ι R)) * ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) := by
            simp
          have hval_one : ((1 : Units (Matrix ι ι R)) |>.val) = (1 : Matrix ι ι R) := by simp
          calc
            A * ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) =
              ((hA.unit : Matrix ι ι R)) * ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) := by
              rw [hA.unit_spec]
            _ = ((hA.unit * hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) := by simp
            _ = ((1 : Units (Matrix ι ι R)) |>.val) := by rw [hA.unit.mul_inv]
            _ = 1 := by simp)
        (by
          -- A⁻¹ * A = 1
          calc
            ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) * A =
              ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) * ((hA.unit : Matrix ι ι R)) := by
              rw [hA.unit_spec]
            _ = ((hA.unit⁻¹ * hA.unit : Units (Matrix ι ι R)) |>.val) := by simp
            _ = ((1 : Units (Matrix ι ι R)) |>.val) := by rw [hA.unit.inv_mul]
            _ = 1 := by simp)).symm :
        F →ₗ[R] E) := by
  have hAB : A * ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) = 1 := by
    calc
      A * ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) =
        ((hA.unit : Matrix ι ι R)) * ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) := by
        rw [hA.unit_spec]
      _ = ((hA.unit * hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) := by simp
      _ = ((1 : Units (Matrix ι ι R)) |>.val) := by rw [hA.unit.mul_inv]
      _ = 1 := by simp
  have hBA : ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) * A = 1 := by
    calc
      ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) * A =
        ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) * ((hA.unit : Matrix ι ι R)) := by
        rw [hA.unit_spec]
      _ = ((hA.unit⁻¹ * hA.unit : Units (Matrix ι ι R)) |>.val) := by simp
      _ = ((1 : Units (Matrix ι ι R)) |>.val) := by rw [hA.unit.inv_mul]
      _ = 1 := by simp
  let f := Matrix.toLinOfInv b_E b_F hAB hBA
  have hf_symm_matrix : LinearMap.toMatrix b_F b_E (f.symm : F →ₗ[R] E) =
      ((hA.unit⁻¹ : Units (Matrix ι ι R)) |>.val) := by
    dsimp [f, Matrix.toLinOfInv]
    simp
  exact hf_symm_matrix.symm

/-- **Example**: The identity matrix I_n is the matrix of the identity isomorphism id_E. -/
example : LinearMap.toMatrix b_E b_E (LinearMap.id : E →ₗ[R] E) = (1 : Matrix ι ι R) := by
  simp

/-- **Example**: For the free R-module R^n with the standard basis, an invertible matrix
gives an automorphism. This is a special case of the main theorem where E = F = R^n. -/
example (A : Matrix (Fin 3) (Fin 3) R) (hA : IsUnit A) :
    ∃ (f : (Fin 3 → R) ≃ₗ[R] (Fin 3 → R)),
      LinearMap.toMatrix (Pi.basisFun R (Fin 3)) (Pi.basisFun R (Fin 3))
        (f : (Fin 3 → R) →ₗ[R] (Fin 3 → R)) = A :=
  ((characterization_of_invertible_matrices_as_matrices_of_isomorphisms
    R (Fin 3 → R) (Fin 3 → R) (Fin 3) (Pi.basisFun R (Fin 3)) (Pi.basisFun R (Fin 3)) A).mp hA)

end characterization_of_invertible_matrices_as_matrices_of_isomorphisms
