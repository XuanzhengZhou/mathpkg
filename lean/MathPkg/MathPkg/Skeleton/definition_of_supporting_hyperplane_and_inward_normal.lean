import Mathlib

open scoped InnerProductSpace

/-!
# Definition of Supporting Hyperplane and Inward Normal

For a polytope Q ⊂ ℝⁿ (the convex hull of finitely many points) and a nonzero vector ν ∈ ℝⁿ,
let a_Q(ν) = −min_{m∈Q} (m·ν). The equation m·ν = −a_Q(ν) is called a **supporting hyperplane**
of Q, and ν is called an **inward pointing normal**.

Since a polytope is the convex hull of its vertices and a linear functional attains its minimum
at a vertex, we define a_Q in terms of the finite vertex set.

**Reference:** This definition formalizes the notion used in toric geometry and convex geometry,
where supporting hyperplanes describe facets of polytopes.
-/

variable {n : ℕ}

/-- A (convex) polytope in ℝⁿ, represented by a finite set of vertices.
The polytope itself is the convex hull of these vertices. -/
structure Polytope (n : ℕ) where
  /-- The vertex set of the polytope. -/
  vertices : Finset (Fin n → ℝ)
  /-- The vertex set is nonempty. -/
  vertices_nonempty : vertices.Nonempty

namespace Polytope

/-- The polytope as a subset of ℝⁿ, i.e., the convex hull of its vertices. -/
def toSet (P : Polytope n) : Set (Fin n → ℝ) := by
  sorry
