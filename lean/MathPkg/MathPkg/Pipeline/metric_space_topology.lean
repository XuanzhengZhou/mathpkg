import Mathlib

open Set
open scoped Topology

/-!
# Metric Space Topology

Let `(X, d)` be a metric space. A subset `U ⊆ X` is **open** (in the metric topology)
if for every `x ∈ U` there exists `δ > 0` such that the open ball
`B(x, δ) = {y ∈ X | d(x, y) < δ}` is contained in `U`.

This defines the **metric space topology** on `X`. Mathlib4 bakes this into the
`MetricSpace` typeclass: `MetricSpace α` extends `PseudoMetricSpace α`,
which extends `UniformSpace α`, which extends `TopologicalSpace α`.
So every metric space automatically carries a topology whose open sets are
characterised by `Metric.isOpen_iff`.

## Main definitions

* `Metric.ball x ε` : the set of points `y` with `dist x y < ε`.
* `Metric.isOpen_iff` : `IsOpen s ↔ ∀ x ∈ s, ∃ ε > 0, Metric.ball x ε ⊆ s`.

## References

* https://en.wikipedia.org/wiki/Metric_space#Open_and_closed_sets,_topology_and_convergence
-/

namespace MathPkg

section metric_space_topology

/-- The metric topology on a metric space `X` is the topology whose open sets are precisely
the subsets `U` such that every point in `U` has an open ball around it
contained in `U`.

This is already the default topology carried by `MetricSpace α`, so we define an
abbreviation that makes the property explicit. -/
abbrev metricTopologyOpens (X : Type*) [MetricSpace X] : Set (Set X) :=
  {U : Set X | IsOpen U}

/-- The characterisation of open sets in the metric topology: `U` is open iff
for every point `x ∈ U` there is a positive radius `ε` whose ball is
contained in `U`. This is `Metric.isOpen_iff` from Mathlib. -/
abbrev isOpen_metric_iff {X : Type*} [MetricSpace X] (U : Set X) : Prop :=
  IsOpen U ↔ ∀ x ∈ U, ∃ ε > (0 : ℝ), Metric.ball x ε ⊆ U

variable {X : Type*} [MetricSpace X]

/-- An example: in ℝ with the usual metric, the interval `(0,1)` is open
because for any `x ∈ (0,1)` we can take `δ = min(x, 1-x)`. -/
example (U : Set ℝ) (hU : U = Set.Ioo (0 : ℝ) 1) : IsOpen U := by
  rcases hU with rfl
  rw [Metric.isOpen_iff]
  intro x ⟨hx0, hx1⟩
  set δ := min x (1 - x) with hδ
  refine ⟨δ, by
    have hx0' : x > 0 := hx0
    have hx1' : x < 1 := hx1
    have hpos : min x (1 - x) > 0 := lt_min_iff.mpr ⟨hx0', by linarith⟩
    exact hpos,
    ?_⟩
  intro y hy
  rw [Metric.mem_ball, Real.dist_eq] at hy
  have hxsub : |y - x| < δ := hy
  have hy0 : (0 : ℝ) < y := by
    have : y > x - δ := sub_lt_sub_right (by simpa using hxsub) _
    linarith [min_le_left x (1 - x)]
  have hy1 : y < 1 := by
    have : y < x + δ := by linarith
    have hδ2 : δ ≤ 1 - x := min_le_right x (1 - x)
    linarith
  exact ⟨hy0, hy1⟩

/-- Another example: the closed ball is closed in the metric topology. -/
example (x : X) (r : ℝ) : IsClosed (Metric.closedBall x r) :=
  Metric.isClosed_closedBall

end metric_space_topology

end MathPkg
