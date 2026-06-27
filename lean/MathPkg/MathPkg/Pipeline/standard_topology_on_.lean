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
def IsStandardOpen (U : Set ℝ) : Prop :=
  U = ∅ ∨ ∀ x ∈ U, ∃ δ > (0 : ℝ), Ioo (x - δ) (x + δ) ⊆ U

/-- In ℝ, `IsStandardOpen U` is equivalent to `IsOpen U`.
This connects the textbook epsilon-ball definition with Mathlib4's topology instance. -/
lemma isStandardOpen_iff_isOpen (U : Set ℝ) : IsStandardOpen U ↔ IsOpen U := by
  constructor
  · intro h
    rcases h with (rfl | h)
    · exact isOpen_empty
    · refine isOpen_iff_forall_mem_open.mpr fun x hx => ?_
      rcases h x hx with ⟨δ, hδ_pos, hδ⟩
      exact ⟨Ioo (x - δ) (x + δ), hδ, isOpen_Ioo, by
        rw [mem_Ioo]
        constructor <;> linarith⟩
  · intro h
    by_cases hne : U.Nonempty
    · refine Or.inr fun x hx => ?_
      rcases Metric.isOpen_iff.mp h x hx with ⟨ε, hε_pos, hε⟩
      refine ⟨ε, hε_pos, ?_⟩
      intro y hy
      rcases hy with ⟨hyl, hyr⟩
      apply hε
      rw [Metric.mem_ball, Real.dist_eq]
      rw [abs_lt]
      constructor <;> linarith
    · exact Or.inl (not_nonempty_iff_eq_empty.mp hne)

end standard_topology_real

/-! ### Examples -/

section examples

/-- The whole space ℝ is standard open. -/
example : IsStandardOpen (Set.univ : Set ℝ) :=
  Or.inr fun x _ => ⟨1, by norm_num, by simp⟩

/-- The open interval `(0, 1)` is standard open. -/
example : IsStandardOpen (Ioo (0 : ℝ) 1) :=
  Or.inr fun x hx => by
    rcases hx with ⟨hx0, hx1⟩
    let δ := min x (1 - x)
    have hδ_pos : δ > 0 := by
      refine lt_min_iff.mpr ⟨hx0, ?_⟩
      linarith
    refine ⟨δ, hδ_pos, fun y hy => ?_⟩
    rcases hy with ⟨hyl, hyr⟩
    have hyl' : 0 < y := by linarith
    have hyr' : y < 1 := by linarith
    exact ⟨hyl', hyr'⟩

/-- The empty set is standard open (by definition). -/
example : IsStandardOpen (∅ : Set ℝ) :=
  Or.inl rfl

/-- A closed interval `[0, 1]` is NOT standard open (nor open in ℝ).
We illustrate this by providing a point `0` on the boundary where no `δ` works. -/
example : ¬ IsStandardOpen (Set.Icc (0 : ℝ) 1) := by
  intro h
  rcases h with (h_empty | h_forall)
  · -- `Icc 0 1` is nonempty (contains 0), so cannot be empty
    have h_nonempty : (Set.Icc (0 : ℝ) 1).Nonempty := ⟨0, left_mem_Icc.mpr (by norm_num)⟩
    exact h_nonempty.ne_empty h_empty.symm
  · -- Consider 0 ∈ [0,1]; no δ > 0 satisfies (0-δ, 0+δ) ⊆ [0,1] since -δ/2 < 0
    rcases h_forall 0 (left_mem_Icc.mpr (by norm_num)) with ⟨δ, hδ_pos, hδ⟩
    have : -(δ/2) ∈ Ioo (0 - δ) (0 + δ) := by
      constructor <;> linarith
    have hmem := hδ this
    rcases hmem with ⟨hlo, hhi⟩
    -- hlo says 0 ≤ -(δ/2) which contradicts hδ_pos
    linarith

/-- The open ray `(a, ∞)` is standard open. -/
example (a : ℝ) : IsStandardOpen (Set.Ioi a) :=
  Or.inr fun x hx => by
    have hx_gt_a : a < x := hx
    let δ := x - a
    have hδ_pos : δ > 0 := by linarith
    refine ⟨δ, hδ_pos, fun y hy => ?_⟩
    rcases hy with ⟨hyl, hyr⟩
    -- y > x - δ = a
    have : a < y := by linarith
    exact this

/-- The standard topology on ℝ is exactly `TopologicalSpace ℝ` from Mathlib4. -/
example : standardTopologyReal = TopologicalSpace ℝ := rfl

end examples
