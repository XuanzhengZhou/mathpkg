import Mathlib

/-!
# Chain Complex of an Ordered Simplicial Complex

Let `K` be an ordered simplicial complex — an abstract simplicial complex on a
linearly ordered vertex type `ι`.  Each simplex inherits a total order from `ι`.

For each natural number `n`, the **chain group**

  `C_n(K) := FreeAbelianGroup { s : Finset ι // s ∈ K ∧ s.card = n+1 }`

is the free abelian group on the `n`-simplices (faces of cardinality `n+1`).

The **boundary operator** `∂_n : C_{n+1}(K) → C_n(K)` is defined on a generator
`(v₀, …, vₙ)` (vertices in increasing order) by the alternating sum

  `∂(v₀, …, vₙ) = ∑_{i=0}^n (-1)^i (v₀, …, v̂ᵢ, …, vₙ)`

where `v̂ᵢ` means the vertex `vᵢ` is omitted, yielding an `(n-1)`-simplex.

The sequence `… → C_n(K) → C_{n-1}(K) → … → C₀(K) → 0` is a
`ChainComplex` of abelian groups indexed by `ℕ`.

## Mathlib4 prerequisites

* `AlgebraicTopology/SimplicialComplex/Basic` — `AbstractSimplicialComplex`
* `GroupTheory/FreeAbelianGroup` — free abelian group with `of` / `lift`
* `Algebra/Homology` — `ChainComplex`, `HomologicalComplex`

-/

open Finset

universe u

namespace MathPkg

/-! ### Ordered simplicial complex -/

/--
An **ordered simplicial complex** on a linearly ordered vertex type `ι`.

It consists of an `AbstractSimplicialComplex ι` (a downwards-closed collection
of nonempty finite subsets containing all singletons), together with the
ambient linear order on `ι`.  The total order on vertices is used to assign
consistent signs in the boundary operator of the associated chain complex.
-/
structure OrderedSimplicialComplex (ι : Type*) [LinearOrder ι] where
  /-- The underlying abstract simplicial complex. -/
  asc : AbstractSimplicialComplex ι

namespace OrderedSimplicialComplex

variable {ι : Type*} [LinearOrder ι] (K : OrderedSimplicialComplex ι)

/-- An `n`-simplex of `K` is a face of cardinality `n+1`.

This subtype serves as the generator set for the chain group `C_n(K)`. -/
def nsimplex (n : ℕ) : Type _ := by
  sorry
