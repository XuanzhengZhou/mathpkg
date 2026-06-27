import Mathlib

open Metric
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
def IsVectorFieldOnSphere (V : sphere (0 : E) r → E) : Prop := by
  sorry
