import Mathlib

open TopologicalSpace
open scoped Topology

/--
# Reduced Zeroth Cohomology Group

For a nonempty topological space `X` and a commutative ring `R`, the **reduced 0th cohomology group**
`H̃^0(X, R)` is defined as the quotient of the `R`-module of locally constant functions on `X`
by the submodule of constant functions.

This definition captures the topological idea that a space is connected iff its reduced zeroth
cohomology vanishes (i.e., `H̃^0(X, R) = 0`), because `dim H̃^0(X, R) = dim H^0(X, R) − 1` when `X`
is nonempty. Here `H^0(X, R)` is the ordinary zeroth cohomology, i.e., all locally constant functions.

## Main definition

* `reducedZerothCohomology X R` : the quotient `R`-module `LocallyConstant X R ⧸ const(R)`.

## References

* Hatcher, *Algebraic Topology*, Section 2.2
* Mathlib4: `LocallyConstant` (Topology/LocallyConstant/Basic.lean),
  `LocallyConstant.constₗ` (Topology/LocallyConstant/Algebra.lean)
-/

noncomputable section

variable (X : Type*) [TopologicalSpace X] (R : Type*) [CommRing R]

/-- The reduced zeroth cohomology group `H̃^0(X, R)`:
the quotient of locally constant `R`-valued functions on `X`
by the submodule of constant functions. -/
def reducedZerothCohomology : Type _ :=
  LocallyConstant X R ⧸ (LinearMap.range (LocallyConstant.constₗ R (Y := R)))

namespace reducedZerothCohomology

/-- The natural projection from locally constant functions to reduced zeroth cohomology. -/
def mk : LocallyConstant X R → reducedZerothCohomology X R :=
  Submodule.Quotient.mk (LinearMap.range (LocallyConstant.constₗ R (Y := R)))

/-- Two locally constant functions are cohomologous iff they differ by a constant function.
This is a convenient reformulation for examples. -/
def equiv (f g : LocallyConstant X R) : Prop :=
  ∃ (c : R), f = g + (LocallyConstant.const X c)

end reducedZerothCohomology

/--
## Examples
-/

section examples

variable {X : Type*} [TopologicalSpace X] {R : Type*} [CommRing R]

/-- Example: The zero element in `H̃^0(X, R)` is the class of any constant function.
In particular, the constant function `0` projects to zero. -/
example : reducedZerothCohomology.mk X R (LocallyConstant.const X (0 : R)) = 0 := by
  apply Submodule.Quotient.mk_eq_zero.mpr
  exact ⟨0, by simp⟩

/-- Example: The constant function `1` projects to zero in `H̃^0(X, R)` as well,
since it is also a constant function. -/
example : reducedZerothCohomology.mk X R (LocallyConstant.const X (1 : R)) = 0 := by
  apply Submodule.Quotient.mk_eq_zero.mpr
  exact ⟨1, rfl⟩

end examples
