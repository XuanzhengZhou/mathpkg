import Mathlib

open Set

/-!
# Definition of a Lattice Polytope

A **lattice polytope** is a set of the form `Conv(A)`, where `A ⊂ ℤⁿ` is finite.
These are convex hulls of sets of points with integer coordinates.

In Mathlib4, `convexHull ℝ s` (from `Mathlib/Analysis/Convex/Hull.lean`) gives the convex hull
of a subset `s` of an `ℝ`-module.  We define a lattice polytope as the convex hull over `ℝ`
of the image of a finite subset of `ℤⁿ` under the natural embedding `ℤⁿ → ℝⁿ`.
-/

/-- The natural componentwise embedding of `ℤⁿ` into `ℝⁿ`. -/
def toRealVec {n : ℕ} (a : Fin n → ℤ) : Fin n → ℝ := by
  sorry
