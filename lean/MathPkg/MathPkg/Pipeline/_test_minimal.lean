import Mathlib
open scoped Classical
open Module (Basis)

variable (R : Type*) [CommRing R]
variable (E F : Type*) [AddCommGroup E] [Module R E] [AddCommGroup F] [Module R F]
variable (ι : Type*) [Fintype ι] [DecidableEq ι] [Finite ι]
variable (b_E : Basis ι R E) (b_F : Basis ι R F)

theorem test_theorem (A : Matrix ι ι R) :
    IsUnit A ↔ ∃ (f : E ≃ₗ[R] F), LinearMap.toMatrix b_E b_F (f : E →ₗ[R] F) = A := by
  constructor
  · intro hA
    let u := hA.unit
    have hAB : A * ((u⁻¹ : Units (Matrix ι ι R)) : Matrix ι ι R) = 1 := by
      calc
        A * ((u⁻¹ : Units (Matrix ι ι R)) : Matrix ι ι R) = ((u : Matrix ι ι R)) * ((u⁻¹ : Units (Matrix ι ι R)) : Matrix ι ι R) := by rw [hA.unit_spec]
        _ = ((u * u⁻¹ : Units (Matrix ι ι R)) : Matrix ι ι R) := by simp
        _ = ((1 : Units (Matrix ι ι R)) : Matrix ι ι R) := by simpa using congrArg Units.val (u.mul_inv)
        _ = (1 : Matrix ι ι R) := by simp
    have hBA : ((u⁻¹ : Units (Matrix ι ι R)) : Matrix ι ι R) * A = 1 := by
      calc
        ((u⁻¹ : Units (Matrix ι ι R)) : Matrix ι ι R) * A = ((u⁻¹ : Units (Matrix ι ι R)) : Matrix ι ι R) * ((u : Matrix ι ι R)) := by rw [hA.unit_spec]
        _ = ((u⁻¹ * u : Units (Matrix ι ι R)) : Matrix ι ι R) := by simp
        _ = ((1 : Units (Matrix ι ι R)) : Matrix ι ι R) := by simpa using congrArg Units.val (u.inv_mul)
        _ = (1 : Matrix ι ι R) := by simp
    let f := Matrix.toLinOfInv b_E b_F hAB hBA
    refine ⟨f, ?_⟩
    simpa [f, Matrix.toLinOfInv] using LinearMap.toMatrix_toLin b_E b_F A
  · intro ⟨f, hf⟩
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
    let u : Units (Matrix ι ι R) := Units.mk A B hAB hBA
    exact ⟨u, rfl⟩
