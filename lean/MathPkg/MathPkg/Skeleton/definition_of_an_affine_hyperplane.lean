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
-/
def affineHyperplane (ν : E) (a : ℝ) (hν : ν ≠ 0) : AffineSubspace ℝ E := by
  sorry
