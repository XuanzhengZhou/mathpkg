import Mathlib

open scoped Classical

/-!
# Syzygy Module

For a set of polynomials (or more generally, elements) f₁, ..., f_t in a commutative ring R,
the **syzygy module** Syz(f₁, ..., f_t) is the set of all (h₁, ..., h_t) ∈ R^t such that
h₁f₁ + ... + h_t f_t = 0.

In more abstract terms: given a commutative ring `R` and a family `f : ι → R`, the syzygy
module is the kernel of the `R`-linear map `(ι →₀ R) →ₗ[R] R` that sends a finitely supported
function `h : ι →₀ R` to `∑ᵢ hᵢ • fᵢ`. This is exactly `LinearMap.ker (Finsupp.linearCombination R f)`.

## Mathlib4 correspondence

Mathlib4 already provides all the ingredients:
- `Finsupp.linearCombination R f` is the `R`-linear map `(ι →₀ R) →ₗ[R] R` sending a
  finitely-supported function to the linear combination of the `f i`.
- `LinearMap.ker` gives the submodule of relations (syzygies).
- The syzygy module is a submodule of the free `R`-module `(ι →₀ R)`.

This file:
1. Defines `Syz R f` as a `Submodule R (ι →₀ R)`.
2. Proves the membership condition: `h ∈ Syz R f ↔ (Finsupp.linearCombination R f) h = 0`.
3. Provides examples.
-/

section syzygy_module

variable {ι R : Type*} [CommRing R] (f : ι → R)

/-- The **syzygy module** of a family `f : ι → R` of elements in a commutative ring `R`.
It is the submodule of `(ι →₀ R)` consisting of all finitely-supported functions
`h : ι →₀ R` such that `∑ᵢ hᵢ • fᵢ = 0`. -/
noncomputable def Syz (f : ι → R) : Submodule R (ι →₀ R) :=
  LinearMap.ker (Finsupp.linearCombination R f)

/-- Membership in the syzygy module: `h ∈ Syz R f` iff the linear combination vanishes. -/
theorem mem_Syz_iff (h : ι →₀ R) : h ∈ Syz f ↔ (Finsupp.linearCombination R f) h = 0 := by
  rfl

/-- Membership in the syzygy module expanded using sums:
`h ∈ Syz R f` iff `∑ᵢ hᵢ • fᵢ = 0`. -/
theorem mem_Syz_iff_sum (h : ι →₀ R) : h ∈ Syz f ↔ h.sum (fun i a => a • f i) = 0 := by
  rw [mem_Syz_iff, Finsupp.linearCombination_apply]

/-- The syzygy module as the kernel of the linear combination map (unfolding the definition). -/
theorem Syz_eq_ker_linearCombination : Syz f = LinearMap.ker (Finsupp.linearCombination R f) :=
  rfl

/-- If `f i = 0` for all i, then the syzygy module is the whole free module. -/
theorem Syz_zero : Syz (0 : ι → R) = ⊤ := by
  ext h
  simp [mem_Syz_iff]

/-- If the family `f` is linearly independent over `R`, then `Syz f = ⊥`.
(This is essentially the definition of linear independence.) -/
theorem Syz_eq_bot_of_linearIndependent (h_indep : LinearIndependent R f) : Syz f = ⊥ := by
  rw [Syz_eq_ker_linearCombination, ← linearIndependent_iff_ker]
  exact h_indep

end syzygy_module

/-! ### Examples -/

section examples

/-- Example: For f₁ = 1 in ℤ, the syzygy h₁·1 = 0 implies h₁ = 0, so Syz(1) = {0}. -/
example : Syz (fun (_ : Unit) => (1 : ℤ)) = ⊥ := by
  apply Syz_eq_bot_of_linearIndependent
  rw [linearIndependent_unique_iff]
  norm_num

/-- Example: For f₁ = 2, f₂ = 4 in ℤ, we have the syzygy (2, -1) since 2·2 + (-1)·4 = 0. -/
example : (Finsupp.single (0 : Fin 2) (2 : ℤ) + Finsupp.single (1 : Fin 2) (-1 : ℤ)) ∈
    Syz (fun (i : Fin 2) => [(2 : ℤ), (4 : ℤ)][i.val]) := by
  rw [mem_Syz_iff_sum]
  rw [Finsupp.sum_add_index' (by intro i; simp) (by intro i a b; simp [add_mul])]
  rw [Finsupp.sum_single_index (by simp), Finsupp.sum_single_index (by simp)]
  norm_num

/-- Example: The trivial syzygy (0, …, 0) is always in Syz(f). -/
example {ι R : Type*} [CommRing R] (f : ι → R) : (0 : ι →₀ R) ∈ Syz f := by
  rw [mem_Syz_iff]
  simp

end examples
