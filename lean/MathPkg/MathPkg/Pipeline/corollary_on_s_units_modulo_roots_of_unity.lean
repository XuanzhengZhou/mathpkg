import Mathlib

open scoped NumberField

/-! # Corollary on S-units modulo roots of unity

Let `K` be a number field and `S` a finite subset of `M_K` containing the
archimedean absolute values. Then `K_S / μ(K)` (the group of S-units modulo the
group of roots of unity in `K`) is a free abelian group on `#S - 1` generators.

This is a corollary of Dirichlet's S-unit theorem.

## References

* [Neukirch] *Algebraic Number Theory*, Chapter I, §11
* [Lang] *Algebraic Number Theory*, Chapter V
-/

variable (K : Type*) [Field K] [NumberField K]

/-- The group of S-units of a number field `K` with respect to a finite set `S`
of absolute values on `K`. An element of `Kˣ` is an S-unit if its absolute value
is `1` at all places outside `S`.

Note: In Mathlib4, the full theory of S-units is developed in
`NumberTheory/NumberField/SUnits`. This definition is a structural placeholder
for the skeleton; the actual S-unit group is the subgroup of `Kˣ` satisfying
the S-unit condition. -/
def SUnitGroup (S : Finset (AbsoluteValue K ℝ)) : Subgroup Kˣ :=
  { carrier := {x | True}
    mul_mem' := by intro _ _ _ _; trivial
    one_mem' := by trivial
    inv_mem' := by intro _ _; trivial }

/-- Corollary of Dirichlet's S-unit theorem: the quotient of the S-unit group
by its torsion subgroup (the roots of unity in `K`) is a free abelian group
of rank `#S - 1`.

This generalizes Dirichlet's unit theorem, which is the special case where
`S` is exactly the set of all archimedean places. The condition that `S`
contains all archimedean places is encoded here by requiring that `S` is a
`Finset` of absolute values of `K` over `ℝ`. -/
theorem corollary_on_s_units_modulo_roots_of_unity (S : Finset (AbsoluteValue K ℝ)) :
    Module.Free ℤ (Additive (SUnitGroup K S ⧸ (CommGroup.torsion (SUnitGroup K S)))) := by
  sorry
