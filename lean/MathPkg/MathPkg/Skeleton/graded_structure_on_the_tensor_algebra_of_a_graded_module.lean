import Mathlib

/-!
# Graded structure on the tensor algebra of a graded module

If R is a graded ring concentrated in degree 0 and M = ⊕ M_i is a ℤ-graded R-module,
then T_R(M) is ℤ-graded with i-th graded component
    ⊕_{k≥0} ⊕_{d₁+⋯+dₖ=i} M_{d₁} ⊗_R ⋯ ⊗_R M_{dₖ}.

This file defines the homogeneous submodule for each degree `i : ℤ`.
-/

open scoped DirectSum

variable (R : Type*) [CommRing R]

/-- Given a ℤ-graded R-module presented as a family `M : ℤ → Type*` of R-modules,
the tensor algebra `T_R(⨁ j, M j)` inherits a ℤ-grading.

For each degree `i : ℤ`, the homogeneous component `gradedComponent R M i` is the
R-submodule spanned by pure tensors of the form `ι(m₁) * ⋯ * ι(mₖ)` where each
`mₚ ∈ M_{dₚ}` and `∑ dₚ = i`.

Equivalently, this is the submodule of elements of "total internal degree" `i`. -/
noncomputable def gradedComponent
    (M : ℤ → Type*) [∀ j, AddCommGroup (M j)] [∀ j, Module R (M j)]
    (i : ℤ) : Submodule R (TensorAlgebra R (⨁ j, M j)) := by
  sorry
