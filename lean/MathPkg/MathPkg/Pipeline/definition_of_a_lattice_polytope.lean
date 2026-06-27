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
def toRealVec {n : ℕ} (a : Fin n → ℤ) : Fin n → ℝ :=
  fun i => (a i : ℝ)

/-- A subset `P ⊆ ℝⁿ` is a **lattice polytope** if it is the convex hull (over `ℝ`)
of a finite set of points in `ℤⁿ`. -/
def IsLatticePolytope {n : ℕ} (P : Set (Fin n → ℝ)) : Prop :=
  ∃ (A : Finset (Fin n → ℤ)), P = convexHull ℝ (toRealVec '' (A : Set (Fin n → ℤ)))

/-! ## Examples -/

/-- A single lattice point is a (degenerate) lattice polytope. -/
example {n : ℕ} (p : Fin n → ℤ) : IsLatticePolytope {toRealVec p} := by
  refine ⟨{p}, ?_⟩
  have h : (toRealVec '' ({p} : Set (Fin n → ℤ))) = {toRealVec p} := by
    ext x; simp [toRealVec]
  simp [h, convexHull_singleton]

/-- The line segment between two lattice points is a lattice polytope. -/
example {n : ℕ} (p q : Fin n → ℤ) : IsLatticePolytope (convexHull ℝ {toRealVec p, toRealVec q}) := by
  refine ⟨{p, q}, ?_⟩
  have h : (toRealVec '' ({p, q} : Set (Fin n → ℤ))) = {toRealVec p, toRealVec q} := by
    ext x; simp [toRealVec]
  simp [h]
