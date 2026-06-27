import Mathlib

open scoped InnerProductSpace Topology

/-!
# Vector Field on a Sphere

A vector field `V` on a sphere `S` assigns to each point `P ∈ S` a vector `V(P)` in the tangent
space `T_p S`, with the mapping `P ↦ V(P)` being continuous.

For the standard sphere `S² = {(x, y, z) | x² + y² + z² = 1}` in `ℝ³`, the tangent space at a
point `p = (x, y, z)` is the plane of vectors orthogonal to `p`:
```
T_p S² = {(a, b, c) : ℝ³ | a·x + b·y + c·z = 0}
```

In this file we define vector fields on the sphere `sphere (0 : E) r` in a real inner product
space `E`. The tangent condition is expressed via the inner product: a vector `v` is tangent at
`p` iff `⟪p, v⟫ = 0`.

## Mathlib4 context

- `Metric.sphere (0 : E) r` — the sphere of radius `r` centered at `0` in a metric space
- `Geometry/Manifold/Instances/Sphere` — the sphere as a smooth manifold with tangent bundle
- `TangentSpace I x` — the tangent space at point `x` on a manifold
- For the manifold sphere, a vector field is a section `Π (x : sphere (0 : E) 1), TangentSpace I x`

This definition provides a predicate `IsVectorFieldOnSphere` that a continuous map from the
sphere to the ambient space constitutes a vector field on the sphere.
-/

section vector_field_on_a_sphere

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
variable {r : ℝ}

/-- A **vector field on the sphere** `sphere (0 : E) r` is a continuous map
`V : sphere (0 : E) r → E` such that for each point `p` on the sphere,
the vector `V p` is tangent to the sphere at `p`.

Tangency means that `V p` is orthogonal to the position vector `p`, i.e.,
`inner ℝ (p : E) (V p) = 0`.

This is a `Prop` predicate, not a new type. -/
def IsVectorFieldOnSphere (V : sphere (0 : E) r → E) : Prop :=
  Continuous V ∧ ∀ p : sphere (0 : E) r, inner ℝ (p : E) (V p) = 0

/-- **Azimuthal vector field on `S²`**: for `p = (x, y, z)`, define `V(p) = (-y, x, 0)`.

This is tangent because `x·(-y) + y·x + z·0 = 0`. -/
def azimuthalVectorField : sphere (0 : EuclideanSpace ℝ (Fin 3)) 1 → EuclideanSpace ℝ (Fin 3) :=
  fun p =>
    let x := (p : EuclideanSpace ℝ (Fin 3)) 0
    let y := (p : EuclideanSpace ℝ (Fin 3)) 1
    fun i => match i with
    | 0 => -y
    | 1 => x
    | 2 => 0

/-- Verification that `azimuthalVectorField` satisfies the tangency condition:
`inner p (V p) = 0` for all `p` on the sphere. -/
example : ∀ p : sphere (0 : EuclideanSpace ℝ (Fin 3)) 1,
    inner ℝ (p : EuclideanSpace ℝ (Fin 3)) (azimuthalVectorField p) = 0 := by
  intro p
  simp [azimuthalVectorField, inner, dotProduct]
  ring

/-- **Example**: the zero vector field is trivially a vector field on any sphere. -/
example (V : sphere (0 : E) r → E) (hV : ∀ p, V p = 0) : IsVectorFieldOnSphere V := by
  constructor
  · exact continuous_const
  · intro p
    simp [hV p]

/-- **Example**: on the unit circle `S¹ ⊂ ℝ²`, the vector field
`V(x, y) = (-y, x)` is tangent because `x·(-y) + y·x = 0`.

This is the velocity field of uniform counterclockwise rotation. -/
def rotationVectorFieldOnCircle : sphere (0 : EuclideanSpace ℝ (Fin 2)) 1 → EuclideanSpace ℝ (Fin 2) :=
  fun p =>
    let x := (p : EuclideanSpace ℝ (Fin 2)) 0
    let y := (p : EuclideanSpace ℝ (Fin 2)) 1
    fun i => match i with
    | 0 => -y
    | 1 => x

example : ∀ p : sphere (0 : EuclideanSpace ℝ (Fin 2)) 1,
    inner ℝ (p : EuclideanSpace ℝ (Fin 2)) (rotationVectorFieldOnCircle p) = 0 := by
  intro p
  simp [rotationVectorFieldOnCircle, inner, dotProduct]
  ring

end vector_field_on_a_sphere
