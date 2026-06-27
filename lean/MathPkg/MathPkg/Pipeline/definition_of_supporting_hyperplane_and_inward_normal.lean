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
def toSet (P : Polytope n) : Set (Fin n → ℝ) :=
  convexHull ℝ (P.vertices : Set (Fin n → ℝ))

/-- a_Q(ν) = −min_{m∈Q} (m·ν), where the minimum is taken over the finite vertex set.
Since a linear functional attains its minimum over a polytope at a vertex, this is equivalent
to min_{m∈Q} (m·ν).

Marked `noncomputable` because `Finset.min'` on `ℝ` depends on `Real.decidableEq`,
which is noncomputable. -/
noncomputable def aQ (P : Polytope n) (ν : Fin n → ℝ) (hν : ν ≠ 0) : ℝ :=
  let values := P.vertices.image (λ m => inner ℝ m ν)
  let hne : values.Nonempty := P.vertices_nonempty.image (λ m => inner ℝ m ν)
  -(values.min' hne)

/-- The supporting hyperplane of Q defined by the inward normal ν:
`{x | inner ℝ x ν = -a_Q(ν)}` = `{x | inner ℝ x ν = min_{m∈Q} (m·ν)}`.

This is an affine subspace of codimension 1 that touches Q and has Q entirely on one side
(the side towards which ν points). -/
def supportingHyperplane (P : Polytope n) (ν : Fin n → ℝ) (hν : ν ≠ 0) :
    AffineSubspace ℝ (Fin n → ℝ) where
  carrier := {x | inner ℝ x ν = -(aQ P ν hν)}
  smul_vsub_vadd_mem c p₁ p₂ p₃ hp₁ hp₂ hp₃ := by
    simp only [Set.mem_setOf_eq] at hp₁ hp₂ hp₃ ⊢
    rw [vadd_eq_add, vsub_eq_sub]
    simp only [map_add, map_sub, LinearMap.map_smul, RingHom.id_apply]
    calc
      inner ℝ (c • (p₁ - p₂) + p₃) ν
          = inner ℝ (c • (p₁ - p₂)) ν + inner ℝ p₃ ν := by rw [add_inner]
      _ = c * inner ℝ (p₁ - p₂) ν + inner ℝ p₃ ν := by
        simp [inner_smul_right]
      _ = c * (inner ℝ p₁ ν - inner ℝ p₂ ν) + inner ℝ p₃ ν := by rw [inner_sub_right]
      _ = c * ((-(aQ P ν hν)) - (-(aQ P ν hν))) + (-(aQ P ν hν)) := by rw [hp₁, hp₂, hp₃]
      _ = c * 0 + (-(aQ P ν hν)) := by ring
      _ = -(aQ P ν hν) := by ring

/-- A vector ν is an **inward pointing normal** for a polytope Q if ν ≠ 0.
By convention, ν determines a supporting hyperplane `x·ν = -a_Q(ν)` and points towards
the interior of Q from that hyperplane. -/
def IsInwardNormal (P : Polytope n) (ν : Fin n → ℝ) : Prop :=
  ν ≠ 0

end Polytope

/-! ## Examples -/

open Polytope

/-- A degenerate polytope consisting of a single point `p` in ℝⁿ. -/
def pointPolytope {n : ℕ} (p : Fin n → ℝ) : Polytope n where
  vertices := {p}
  vertices_nonempty := by simp

/-- For a single-point polytope `{p}` and any nonzero ν, we have a_Q(ν) = -(p·ν). -/
example {n : ℕ} (p ν : Fin n → ℝ) (hν : ν ≠ 0) : aQ (pointPolytope p) ν hν = -(inner ℝ p ν) := by
  unfold aQ pointPolytope
  simp

/-- ν = (1, 0) is nonzero in ℝ², hence it is an inward pointing normal for any polytope. -/
example : IsInwardNormal (pointPolytope (λ (_ : Fin 2) => (0 : ℝ)))
    (λ i => if i = 0 then (1 : ℝ) else (0 : ℝ)) := by
  intro h
  have := congr_fun h 0
  simp at this

/-- A line segment polytope between two points p and q in ℝⁿ. -/
def segmentPolytope {n : ℕ} (p q : Fin n → ℝ) : Polytope n where
  vertices := {p, q}
  vertices_nonempty := by simp

/-- For a segment polytope, the supporting hyperplane with normal ν is a valid affine subspace. -/
example {n : ℕ} (p q ν : Fin n → ℝ) (hν : ν ≠ 0) :
    (supportingHyperplane (segmentPolytope p q) ν hν : Set (Fin n → ℝ)) =
    {x | inner ℝ x ν = -(aQ (segmentPolytope p q) ν hν)} := by
  rfl

/-- The zero vector is on the supporting hyperplane exactly when a_Q(ν) = 0,
i.e., when min_{m∈Q} (m·ν) = 0. -/
example {n : ℕ} (p q ν : Fin n → ℝ) (hν : ν ≠ 0) :
    ((0 : Fin n → ℝ) ∈ (supportingHyperplane (segmentPolytope p q) ν hν : Set (Fin n → ℝ))) ↔
    inner ℝ (0 : Fin n → ℝ) ν = -(aQ (segmentPolytope p q) ν hν) := by
  rfl
