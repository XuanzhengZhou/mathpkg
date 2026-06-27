import Mathlib

/-!
# Definition of Uniformizer at a Point

Fix a point `p` in `Spec(R)` with a discrete valuation `ord_p`. A **uniformizer** `u ∈ R` for
`p` is an element with `ord_p(u) = 1`.

In a discrete valuation ring (DVR), there is a unique non-zero prime ideal — the maximal ideal
`m`. The valuation is the `m`-adic valuation. A uniformizer is an element that generates `m`.

## Mathlib4 Correspondence

Mathlib4's `IsDiscreteValuationRing` deliberately does **not** define a `Uniformizer` predicate,
stating: "We do not hence define `Uniformizer` at all, because we can use `Irreducible` instead"
(see `RingTheory/DiscreteValuationRing/Basic.lean`).

Two equivalent ways to capture "uniformizer" in Mathlib4:

1. **Irreducible element** (DVR context): `Irreducible u` — in a DVR, u is irreducible iff
   `maximalIdeal R = Ideal.span {u}`.
2. **Valuation uniformizer** (valuation-theoretic): `v.IsUniformizer u` where `v` is a rank-one
   discrete valuation — this means `v u` is the generator of the value group.

The DVR's additive valuation satisfies `addVal R u = 1` for any uniformizer `u`.
-/

open IsDiscreteValuationRing
open scoped WithZero

variable {R : Type*} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]

/--
A **uniformizer** (also called a *uniformizing parameter*) for a discrete valuation ring `R`
is an irreducible element `u : R`.

In a DVR, irreducibility is equivalent to generating the maximal ideal:
  `Irreducible u ↔ maximalIdeal R = Ideal.span {u}`
and also equivalent to `addVal R u = 1`.

This definition captures the classical notion: for a point `p` in `Spec(R)` whose local ring
is a DVR with discrete valuation `ord_p`, an element `u` is a uniformizer if `ord_p(u) = 1`.
-/
def Uniformizer (u : R) : Prop := by
  sorry

/--
An alternative, valuation-theoretic definition using Mathlib4's `Valuation.IsUniformizer`,
which works for any rank-one discrete valuation (not just DVRs).

If `v` is a rank-one discrete valuation on `R`, then `v.IsUniformizer u` means that
`v u` generates the value group of `v` and `v u < 1`.
-/
example (v : Valuation R ℤᵐ⁰) [Valuation.IsRankOneDiscrete v] (u : R) : Prop := by
  sorry
