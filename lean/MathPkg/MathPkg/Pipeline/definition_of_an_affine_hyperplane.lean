import Mathlib

open scoped InnerProductSpace

/-!
# Definition of an Affine Hyperplane

An affine hyperplane in ℝⁿ is defined by an equation of the form `m·ν = −a`, where `ν` is a
nonzero vector in ℝⁿ and `a` is a real number.

In Mathlib4, this concept is represented using `AffineSubspace ℝ E` where `E` is a real inner
product space (so that the dot product `⟪x, ν⟫` is defined). The hyperplane consists of all
points `x` satisfying `⟪x, ν⟫ = -a`.
-/

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- An affine hyperplane in a real inner product space `E`, specified by a nonzero normal
vector `ν : E` and a real constant `a`. The hyperplane is the set `{x | inner ℝ x ν = -a}`.

This is an `AffineSubspace ℝ E` because for any `p₁, p₂, p₃` on the hyperplane and any `c : ℝ`:
`⟪c • (p₁ -ᵥ p₂) +ᵥ p₃, ν⟫ = c·(-a) - c·(-a) + (-a) = -a`. -/
def affineHyperplane (ν : E) (a : ℝ) (hν : ν ≠ 0) : AffineSubspace ℝ E where
  carrier := {x | inner ℝ x ν = -a}
  smul_vsub_vadd_mem c p₁ p₂ p₃ hp₁ hp₂ hp₃ := by
    simp only [Set.mem_setOf_eq] at hp₁ hp₂ hp₃ ⊢
    rw [vadd_eq_add, vsub_eq_sub]
    -- In a normed add comm group with InnerProductSpace, vadd is + and vsub is -
    simp only [map_add, map_sub, LinearMap.map_smul, RingHom.id_apply]
    calc
      inner ℝ (c • (p₁ - p₂) + p₃) ν
          = inner ℝ (c • (p₁ - p₂)) ν + inner ℝ p₃ ν := by rw [add_inner]
      _ = c * inner ℝ (p₁ - p₂) ν + inner ℝ p₃ ν := by rw [inner_smul_right, inner_smul_right]
      _ = c * (inner ℝ p₁ ν - inner ℝ p₂ ν) + inner ℝ p₃ ν := by rw [inner_sub_right]
      _ = c * ((-a) - (-a)) + (-a) := by rw [hp₁, hp₂, hp₃]
      _ = c * 0 + (-a) := by ring
      _ = -a := by ring

/-- The predicate `IsAffineHyperplane` asserts that an `AffineSubspace ℝ E` is an affine
hyperplane, meaning it can be written as `{x | inner ℝ x ν = r}` for some nonzero `ν : E`
and some `r : ℝ`. -/
def IsAffineHyperplane (s : AffineSubspace ℝ E) : Prop :=
  ∃ (ν : E) (r : ℝ), ν ≠ 0 ∧ (s : Set E) = {x | inner ℝ x ν = r}

/-- Example: the hyperplane `{x : ℝ² | x·(1,0) = -3}`, i.e., the vertical line `x₁ = -3`. -/
example : IsAffineHyperplane (affineHyperplane ((1 : ℝ), (0 : ℝ)) (3 : ℝ) (by norm_num)) := by
  refine ⟨(1, 0), -3, by norm_num, ?_⟩
  ext x
  simp [affineHyperplane, inner]
  ring

/-- Example: the `affineHyperplane` constructed from a nonzero vector is always an
`IsAffineHyperplane`. -/
example (ν : E) (a : ℝ) (hν : ν ≠ 0) : IsAffineHyperplane (affineHyperplane ν a hν) := by
  refine ⟨ν, -a, hν, ?_⟩
  rfl
