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
abbrev metricTopologyOpens (X : Type*) [MetricSpace X] : Set (Set X) := by
  sorry
