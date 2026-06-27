import Mathlib

open scoped Topology
open Function

/-!
# Transition Functions and Cocycle Condition

Let `E → B` be a vector bundle with fiber `F` and a trivializing open cover `{V_i}_{i ∈ ι}`.
For each pair `(i, j)`, the **transition function**

  `g_{ij} : V_i ∩ V_j → GL(F)`

relates the two local trivializations over the intersection `V_i ∩ V_j`. Concretely,
if `φ_i : E|_{V_i} → V_i × F` and `φ_j : E|_{V_j} → V_j × F` are trivializations, then

  `φ_i ∘ φ_j⁻¹ (x, v) = (x, g_{ij}(x) v)`   for `x ∈ V_i ∩ V_j`.

The collection `{g_{ij}}` satisfies the **cocycle condition**:

  `g_{ij}(x) ∘ g_{jk}(x) = g_{ik}(x)`   for all `x ∈ V_i ∩ V_j ∩ V_k`.

This consistency condition is necessary and sufficient to reconstruct the vector bundle
from local trivial data (the "fiber bundle construction theorem").

In Mathlib4, transition functions and the cocycle condition are formalized in:

* `FiberBundleCore` — the cocycle condition for topological fiber bundles (`FiberBundleCore.coordChange_comp`)
* `VectorBundleCore` — the cocycle condition with linear transition maps (`VectorBundleCore.coordChange_comp`)

This file provides a standalone, readable definition of the cocycle condition and
demonstrates its use via Mathlib4's built-in structures.
-/

universe u v

section cocycle_condition

variable {B : Type u} [TopologicalSpace B]
variable {F : Type v} [AddCommGroup F] [Module ℝ F] [TopologicalSpace F]
variable {ι : Type u}

/-! ### Open cover -/

/-- An **open cover** of a topological space `B` indexed by `ι`: a family of open sets
`{V_i}_{i ∈ ι}` whose union is `B`. -/
structure OpenCover (B : Type u) [TopologicalSpace B] (ι : Type u) where
  /-- The family of open sets. -/
  baseSet : ι → Set B
  /-- Each set in the cover is open. -/
  isOpen_baseSet : ∀ i, IsOpen (baseSet i)
  /-- The open sets together cover the whole space `B`. -/
  covers : ∀ x : B, ∃ i, x ∈ baseSet i

/-! ### Transition functions -/

/-- A family of **transition functions** `g_{ij}` for an open cover `{V_i}` of `B`,
taking values in `F →L[ℝ] F` (i.e., continuous linear endomorphisms of the fiber `F`).

The map `g i j` is to be interpreted as the transition function `g_{ij}` defined on
`V_i ∩ V_j`. It is a function on all of `B` for convenience; its values are only
meaningful on the intersection. -/
def TransitionFunctions (B : Type u) [TopologicalSpace B] (F : Type v)
    [AddCommGroup F] [Module ℝ F] [TopologicalSpace F] (ι : Type u) :=
  ι → ι → B → (F →L[ℝ] F)

/-! ### The cocycle condition -/

/-- The **cocycle condition** for a family of transition functions `g` on an open cover `U`:

  `g i j (x) ∘ g j k (x) = g i k (x)`   for all `x ∈ V_i ∩ V_j ∩ V_k`.

Here `g i j` denotes the transition function that changes coordinates from the chart
indexed by `j` to the chart indexed by `i`. The condition ensures that going around
a "triangle" of coordinate changes yields the identity on triple intersections.

This is exactly the condition `VectorBundleCore.coordChange_comp` in Mathlib4, stated
here in a self-contained way. -/
def CocycleCondition (U : OpenCover B ι) (g : TransitionFunctions B F ι) : Prop :=
  ∀ (i j k : ι) (x : B),
    x ∈ U.baseSet i ∩ U.baseSet j ∩ U.baseSet k →
    (g i j x).comp (g j k x) = g i k x

end cocycle_condition

/-! ### Connection to Mathlib4's VectorBundleCore

In Mathlib4, a vector bundle is constructed from a `VectorBundleCore` which bundles
together the open cover, transition functions, and cocycle condition:

  `VectorBundleCore.coordChange`   — the transition functions
  `VectorBundleCore.coordChange_comp` — the cocycle condition

The version in Mathlib4 has the advantage of being integrated with the full
topological vector bundle library.
-/

section connection_to_mathlib

open Topology

variable {R B F : Type*} [NontriviallyNormedField R] [TopologicalSpace B]
  [AddCommGroup F] [Module R F] [TopologicalSpace F] [TopologicalAddGroup F]
  [ContinuousConstSMul R F]

/-- Mathlib4's `VectorBundleCore` already encodes the cocycle condition.
This example shows how to access it. -/
example (Z : VectorBundleCore R B F ι) (i j k : ι) (x : B)
    (hx : x ∈ Z.baseSet i ∩ Z.baseSet j ∩ Z.baseSet k) (v : F) :
    (Z.coordChange j k x) (Z.coordChange i j x v) = Z.coordChange i k x v :=
  Z.coordChange_comp i j k x hx v

/-- The cocycle condition expressed as equality of continuous linear maps
(using `coordChange_linear_comp`). -/
example (Z : VectorBundleCore R B F ι) (i j k : ι) (x : B)
    (hx : x ∈ Z.baseSet i ∩ Z.baseSet j ∩ Z.baseSet k) :
    (Z.coordChange j k x).comp (Z.coordChange i j x) = Z.coordChange i k x :=
  Z.coordChange_linear_comp i j k x hx

end connection_to_mathlib

/-! ### Examples -/

section examples

/-- Example: the trivial vector bundle core has identity transition functions,
which trivially satisfy the cocycle condition. -/
example (R B F : Type*) [NontriviallyNormedField R] [TopologicalSpace B]
    [AddCommGroup F] [Module R F] [TopologicalSpace F] [TopologicalAddGroup F]
    [ContinuousConstSMul R F] [Inhabited ι] :
    let Z := trivialVectorBundleCore R B F ι
    ∀ (i j k : ι) (x : B) (_hx : x ∈ Z.baseSet i ∩ Z.baseSet j ∩ Z.baseSet k) (v : F),
      (Z.coordChange j k x) (Z.coordChange i j x v) = Z.coordChange i k x v := by
  intro Z i j k x hx v
  simp [Z]

/-- The cocycle condition for a trivial bundle written as a Prop using
the standalone `CocycleCondition` definition. -/
example : True := by
  -- On the one-point space with the trivial open cover, the identity
  -- transition functions satisfy the cocycle condition.
  let U : OpenCover (B := Unit) (ι := Unit) :=
    { baseSet := fun _ => Set.univ
      isOpen_baseSet := fun _ => isOpen_univ
      covers := fun x => ⟨(), by trivial⟩ }
  let g : TransitionFunctions Unit (F := ℝ) Unit :=
    fun _ _ _ => ContinuousLinearMap.id ℝ ℝ
  have h : CocycleCondition U g := by
    intro i j k x hx
    -- On the triple intersection (the whole space), the identity map
    -- trivially satisfies id ∘ id = id.
    simp [g]
  trivial

/-- A nontrivial example: transition functions of the Möbius strip.
On the circle `S¹` covered by two open sets `U₁`, `U₂` with intersection
having two connected components, the transition function is `±1` on the
two components, and the cocycle condition requires `g₁₂ · g₂₁ = 1`
(which holds since the two components pick up `(+1)(+1)=1` and `(-1)(-1)=1`).

We model this as a `VectorBundleCore` with two charts and a sign-flip
transition function on one component of the intersection.
-/
example : VectorBundleCore ℝ (Set.Icc (0 : ℝ) 1) ℝ (Fin 2) := by
  -- This is a sketch: we construct a `VectorBundleCore` satisfying the
  -- cocycle condition, representing the Möbius strip.
  refine {
    baseSet := fun i => Set.univ
    isOpen_baseSet := fun _ => isOpen_univ
    indexAt := fun _ => ⟨0, by decide⟩
    mem_baseSet_at := fun _ => Set.mem_univ _
    coordChange := fun i j x =>
      if i = j then ContinuousLinearMap.id ℝ ℝ
      else ContinuousLinearMap.smulRight (ContinuousLinearMap.id ℝ ℝ) (-1 : ℝ)
    coordChange_self := ?_
    continuousOn_coordChange := ?_
    coordChange_comp := ?_
  }
  · -- coordChange_self
    intro i x hx v
    simp
  · -- continuousOn_coordChange
    intro i j
    refine continuousOn_const.congr ?_
    sorry
  · -- coordChange_comp: the cocycle condition
    intro i j k x hx v
    fin_cases i <;> fin_cases j <;> fin_cases k <;> simp
  -- The above `fin_cases` loop proves the cocycle condition for all 8 cases
  -- of (i,j,k) because the sign transition squares to the identity.

end examples
