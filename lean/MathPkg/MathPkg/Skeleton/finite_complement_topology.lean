import Mathlib

/-!
# Finite Complement Topology (Cofinite Topology)

On a set `X`, the **finite complement topology** (also called the **cofinite topology**)
is defined by declaring a proper subset of `X` closed if it is finite. Equivalently,
a nonempty subset is open if its complement is finite.

## Mathlib4 Cross-References

* `TopologicalSpace.cofinite` — the cofinite topological space structure on any type, defined
  in `Mathlib/Topology/Constructions.lean`.
* `CofiniteTopology X` — the type synonym `WithTopology X .cofinite`.
* `isOpen_iff` / `isClosed_iff` — characterizations of open and closed sets in the cofinite
  topology, in `CofiniteTopology` namespace.

## Basic Properties

* `isClosed_iff` : a set is closed iff it is the whole space or finite.
* `isOpen_iff` : a set is open iff it is empty or has finite complement.
* The topology is T₁ (points are closed) and compact.
* Every infinite subset is dense.
-/

/-- The **finite complement (cofinite) topology** on a type `X`.
A set is open if it is empty or its complement is finite. -/
def finite_complement_topology (X : Type*) : TopologicalSpace X := by
  sorry
