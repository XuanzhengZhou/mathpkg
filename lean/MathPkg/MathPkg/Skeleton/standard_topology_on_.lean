import Mathlib

open Set
open Filter
open Topology

/-!
# Standard topology on ℝ

A nonempty subset `U ⊆ ℝ` is **open** in the standard topology if for every `x ∈ U`
there exists `δ > 0` such that `(x - δ, x + δ) ⊆ U`. Together with `∅`, this defines the
standard topology on ℝ.

In Mathlib4, `TopologicalSpace ℝ` is already defined as the order topology, which
coincides with this epsilon-ball (metric) topology. We provide:
- `standardTopologyReal` : an abbreviation for the existing Mathlib4 instance.
- `IsStandardOpen` : the epsilon-ball characterization of open sets.
- `isStandardOpen_iff_isOpen` : the lemma that `IsStandardOpen U ↔ IsOpen U` in ℝ.
-/

section standard_topology_real

/-! ### The standard topology as the existing Mathlib instance -/

/-- The standard topology on ℝ.
In Mathlib4 this is the order topology, which coincides with the metric topology
induced by `|x - y|`. -/
abbrev standardTopologyReal : TopologicalSpace ℝ := by infer_instance

/-! ### Epsilon-ball characterization of open sets -/

/-- A set `U ⊆ ℝ` is *standard open* if it is empty, or for every `x ∈ U`
there exists `δ > 0` such that the open interval `(x - δ, x + δ)` is contained in `U`.

This is the textbook definition of the standard (Euclidean) topology on ℝ. -/
def IsStandardOpen (U : Set ℝ) : Prop := by
  sorry
