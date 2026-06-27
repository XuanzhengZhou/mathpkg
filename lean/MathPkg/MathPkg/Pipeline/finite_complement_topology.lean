import Mathlib

/-!
# Finite Complement Topology (Cofinite Topology)

Let `X` be a set. The **finite complement topology** (also called the **cofinite
topology**) on `X` is the topology whose closed sets are `X` itself and all finite
subsets of `X`.

Equivalently, a subset `U ⊆ X` is **open** if it is empty or its complement `X \ U`
is finite.

## Main definition

Mathlib4 provides `CofiniteTopology X` as a type synonym for `X` equipped with the
cofinite topology. The definition lives in `Mathlib.Topology.Constructions`.

- `TopologicalSpace.cofinite` constructs the topological space structure directly.
- `CofiniteTopology X` is `WithTopology X .cofinite`, a type synonym.

## Basic properties

- `isOpen_iff` : a set is open iff it is empty or has finite complement.
- `isClosed_iff` : a set is closed iff it is the whole space or finite.
- The topology is T₁ (points are closed) and compact.
- Every infinite subset is dense.
-/

open Set

/-- The cofinite (finite complement) topology on a type `X` via the Mathlib4 definition.
Use `CofiniteTopology X` to get a type synonym for `X` equipped with the cofinite topology. -/
abbrev finiteComplementTopology (X : Type*) := CofiniteTopology X

/-- Example: In the cofinite topology on `ℕ`, the set `{0, 1, 2}` is closed because it is finite. -/
example : IsClosed ({(0 : ℕ), 1, 2} : Set (CofiniteTopology ℕ)) := by
  rw [CofiniteTopology.isClosed_iff]
  right
  simp

/-- Example: The set of all natural numbers greater than 10 is open in the cofinite topology
on `ℕ` because its complement `{0, 1, …, 10}` is finite. -/
example : IsOpen ({n : ℕ | n > 10} : Set (CofiniteTopology ℕ)) := by
  rw [CofiniteTopology.isOpen_iff']
  right
  have : {x : ℕ | x ≤ 10}.Finite := by
    apply Set.finite_le_nat 10
  simpa [Set.compl_setOf, not_lt] using this
