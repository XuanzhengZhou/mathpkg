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
def SpaceOfSections (B : Type*) (V : B → Type*) : Type _ :=
  ∀ x : B, V x

@[inherit_doc]
notation "Γ(" B ", " V ")" => SpaceOfSections B V

/-- A **classical section** of a bundle `V → B` is a map `s : B → TotalSpace F V`
such that `π ∘ s = id_B`.  We define this as a predicate on functions
`B → TotalSpace F V`. -/
def IsSection (s : B → TotalSpace F V) : Prop :=
  ∀ x : B, (s x).proj = x

/-- Convert a Mathlib4-style dependent section `f : Γ(B, V)` into a classical section
`B → TotalSpace F V` satisfying `IsSection`. -/
def dependentToSection (f : Γ(B, V)) : B → TotalSpace F V :=
  fun x => TotalSpace.mk' F x (f x)

/-- Convert a classical section `s : B → TotalSpace F V` (satisfying `IsSection s`)
into a Mathlib4-style dependent section `Γ(B, V)`. -/
def sectionToDependent (s : B → TotalSpace F V) (h : IsSection V s) : Γ(B, V) :=
  fun x => by
    have hx := h x
    -- `s x` is of type `TotalSpace F V` with `.proj = x`
    simpa [hx] using (s x).snd

/-- The conversion `dependentToSection` indeed produces a section in the classical sense. -/
theorem dependentToSection_isSection (f : Γ(B, V)) : IsSection V (dependentToSection F V f) := by
  intro x
  simp [dependentToSection]

/-- These two conversions are mutual inverses on the dependent side. -/
theorem section_dependent_leftInv (f : Γ(B, V)) :
    sectionToDependent F V (dependentToSection F V f) (dependentToSection_isSection F V f) = f := by
  ext x
  simp [sectionToDependent, dependentToSection]

end basic_definitions

/-! ### The global zero section -/

section zero_section

variable {B F : Type*} (V : B → Type*) [∀ x, Zero (V x)]

/-- The **global zero section** `0 : Γ(B, V)` sends every `x : B` to `0 : V x`. -/
def globalZeroSection : Γ(B, V) :=
  fun _ => 0

/-- As a classical section into `TotalSpace F V`, the zero section is `x ↦ (x, 0)`. -/
def globalZeroSectionTotal : B → TotalSpace F V :=
  fun x => TotalSpace.mk' F x (0 : V x)

/-- The global zero section in the classical sense satisfies `IsSection`. -/
theorem globalZeroSection_isSection : IsSection V (globalZeroSectionTotal F V) := by
  intro x
  simp [globalZeroSectionTotal]

/-- This coincides with Mathlib4's built-in `zeroSection` from `Topology/VectorBundle/Basic`. -/
theorem globalZeroSection_eq_zeroSection : zeroSection F V = globalZeroSectionTotal F V := by
  ext x
  simp [globalZeroSectionTotal, zeroSection]

end zero_section

/-! ### FiberFrame: a collection of sections forming a fiberwise basis -/

section fiber_frame

variable {B 𝕜 : Type*} [CommRing 𝕜]
  (V : B → Type*) [∀ x, AddCommGroup (V x)] [∀ x, Module 𝕜 (V x)]

/-- A **fiber frame** of a vector bundle `V → B` over a set `U ⊆ B` is a finite collection
of sections `sᵢ : Γ(B, V)` (indexed by `ι` with `Fintype ι`) such that for each
`x ∈ U`, the vectors `sᵢ x` form a basis of the fiber `V x`.

We use the Mathlib4 "junk value pattern": each section is defined on all of `B`,
and the basis property is only guaranteed on `baseSet`. Outside `baseSet`, the
value `basisAt x hx` is a valid basis but does not necessarily correspond to
`sections i x`.

Note: Mathlib4 provides the more general predicate `IsLocalFrameOn` in
`Geometry/Manifold/VectorBundle/LocalFrame.lean` for smooth vector bundles
over manifolds. This `FiberFrame` structure captures the algebraic core:
a fiberwise basis, without smoothness assumptions. -/
structure FiberFrame (ι : Type*) [Fintype ι] where
  /-- The sections that form the frame. -/
  sections : ι → Γ(B, V)
  /-- The set `U ⊆ B` on which this is a frame. -/
  baseSet : Set B
  /-- For each `x ∈ baseSet`, the family `sections i x` is a basis of the fiber `V x`. -/
  basisAt (x : B) (hx : x ∈ baseSet) : Basis ι 𝕜 (V x)
  /-- The basis vectors agree with the sections on `baseSet`. -/
  basis_eq_sections (x : B) (hx : x ∈ baseSet) (i : ι) : basisAt x hx i = sections i x

/-- For a `FiberFrame` on `U`, every element `v : V x` (with `x ∈ U`) can be written
as a linear combination of the frame sections. -/
theorem FiberFrame.repr_eq (f : FiberFrame V ι) {x : B} (hx : x ∈ f.baseSet) (v : V x) :
    v = ∑ i, (f.basisAt x hx).repr v i • f.sections i x := by
  calc
    v = (f.basisAt x hx).repr v |>.sum fun i c => c • (f.basisAt x hx) i := by
      simpa using (f.basisAt x hx).repr_sum_self v
    _ = ∑ i, (f.basisAt x hx).repr v i • f.sections i x := by
      refine Finset.sum_congr rfl fun i _ => ?_
      simp [f.basis_eq_sections x hx i]

end fiber_frame

/-! ### Examples -/

section examples

variable {B 𝕜 : Type*} [Field 𝕜] (V : B → Type*) [∀ x, AddCommGroup (V x)] [∀ x, Module 𝕜 (V x)]

/-- Example: the zero section belongs to the space of all sections. -/
example : Γ(B, V) :=
  fun _ => 0

/-- Example: for the trivial bundle `B × 𝕜`, a section is just a function `B → 𝕜`. -/
example : Γ(B, fun (_ : B) => 𝕜) = (B → 𝕜) := by
  rfl

/-- Example: adding two sections gives a section. -/
example (s t : Γ(B, V)) : Γ(B, V) :=
  fun x => s x + t x

/-- Example: scaling a section by a scalar field `B → 𝕜` gives a section. -/
example (φ : B → 𝕜) (s : Γ(B, V)) : Γ(B, V) :=
  fun x => φ x • s x

/-- Example: the space of sections of a trivial line bundle `B × 𝕜` has the structure
of a `𝕜`-module. -/
example : Module 𝕜 (Γ(B, fun (_ : B) => 𝕜)) := by
  infer_instance

/-- Example: Mathlib4 already has `zeroSection` defined in `Topology/VectorBundle/Basic.lean`,
which is the global zero section as a map into the total space. -/
example (F : Type*) [Zero F] (V' : B → Type*) [∀ x, Zero (V' x)] : B → TotalSpace F V' :=
  zeroSection F V'

/-- Example: The dependent section `fun x : B => (0 : V x)` corresponds
to the zero section in the total space. -/
example (F : Type*) [Zero F] (V' : B → Type*) [∀ x, Zero (V' x)] (x : B) :
    (zeroSection F V' x).snd = (0 : V' x) := by
  simp [zeroSection]

/-- Example: For the trivial line bundle over a 1-point space, a fiber frame consists
of a nonzero section. -/
example : FiberFrame (fun (_ : Unit) => 𝕜) (Fin 1) where
  sections := fun _ _ => (1 : 𝕜)
  baseSet := Set.univ
  basisAt := fun x hx =>
    Basis.mk (fun _ _ => (1 : 𝕜))
      (by
        have : Fintype.card (Fin 1) = 1 := by decide
        refine linearIndependent_fin_cons.2 ?_
        · exact linearIndependent_empty.2
        · intro f; simpa using f)
      (by
        intro v
        refine ⟨fun _ => v, ?_⟩
        simp)
  basis_eq_sections := by intro x hx i; simp

/-- Example: The space of sections `Γ(B, V)` is an `AddCommGroup` (when each fiber is). -/
example : AddCommGroup (Γ(B, V)) := by
  infer_instance

/-- Example: A section in the classical sense satisfies `IsSection`. -/
example (s : B → TotalSpace ℝ V) (h : ∀ x, (s x).proj = x) : IsSection V s :=
  h

end examples
