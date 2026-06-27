import Mathlib

/-!
# Section, Frame, and Space of Sections of a Vector Bundle

Let `π : E → V` be a vector bundle with total space `E`, base `V`, and fibers `π⁻¹(v)`.
In Mathlib4's dependent-type framework, a vector bundle is given by a family `V : B → Type*`
where `V x` is the fiber over `x : B`.  The total space is `Bundle.TotalSpace F V`.

## Main definitions

1. A **section** over `V` is a map `s : V → E` such that `π ∘ s = id_V`.
   In Mathlib4, a section is a dependent function `(x : V) → V x`, which automatically
   satisfies the projection condition.  We define `IsSection` as a predicate on maps
   into the total space, and provide conversions between the two representations.

2. The **space of all sections** is denoted `SpaceOfSections B V` (abbreviated `Γ`).
   It is an additive commutative group and a module over the base field.

3. A **frame** is a collection of sections `s₁, …, sₙ` that form a basis of each fiber
   over a set `U ⊆ B`.  Mathlib4 provides the more refined predicate `IsLocalFrameOn` in
   `Geometry/Manifold/VectorBundle/LocalFrame.lean` for smooth vector bundles over manifolds.
   Here we define the purely algebraic core: a `FiberFrame` structure.

4. The **zero section** exists globally: it maps every `x ∈ V` to the zero element of `V x`.
   Mathlib4's `zeroSection` in `Topology/VectorBundle/Basic.lean` provides this.

## References

* <https://en.wikipedia.org/wiki/Section_(fiber_bundle)>
* <https://en.wikipedia.org/wiki/Frame_(linear_algebra)>
* Mathlib4: `Mathlib/Geometry/Manifold/VectorBundle/ContMDiffSection.lean`
* Mathlib4: `Mathlib/Geometry/Manifold/VectorBundle/LocalFrame.lean`
* Mathlib4: `Mathlib/Topology/VectorBundle/Basic.lean` (zero section)
-/

open Bundle

section basic_definitions

variable {B F : Type*} (V : B → Type*)

/-- The **space of all sections** `SpaceOfSections B V` is the type of all dependent functions
from the base `B` to the fibers `V x`.  In Mathlib4, this is the natural representation
of sections and is used throughout the vector bundle library (e.g. `ContMDiffSection`).

We provide the notation `Γ(B, V)` for `Π x : B, V x`. -/
@[reducible]
def SpaceOfSections (B : Type*) (V : B → Type*) : Type _ := by
  sorry
