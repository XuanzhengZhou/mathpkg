import Mathlib

/-!
# Reduced Zeroth Cohomology Group

For a nonempty topological space `X` and a commutative ring `R`, the reduced 0th cohomology group
is defined as the quotient of the `R`-module of locally constant functions on `X`
by the submodule of constant functions. This definition captures the topological idea that a space
is connected iff its reduced zeroth cohomology vanishes.

## Main definition

* `reducedZerothCohomology X R` : the quotient `R`-module `LocallyConstant X R / const(R)`.

## References

* Hatcher, *Algebraic Topology*, Section 2.2
* Mathlib4: `LocallyConstant` (Topology/LocallyConstant/Basic.lean),
  `LocallyConstant.constₗ` (Topology/LocallyConstant/Algebra.lean)
-/

variable (X : Type*) [TopologicalSpace X] (R : Type*) [CommRing R]

/-- The reduced zeroth cohomology group: the quotient of locally constant `R`-valued functions
on `X` by the submodule of constant functions. -/
noncomputable def reducedZerothCohomology :
    LocallyConstant X R ⧸ (LinearMap.range (LocallyConstant.constₗ R (Y := R))) := by
  sorry
