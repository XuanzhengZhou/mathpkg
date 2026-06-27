/-
  Translation of: Unit Group and Torsion Subgroup
  Source concept ID: unit_group_and_torsion_subgroup

  In a number field K, the set of units in the ring of integers 𝓞 K forms
  a multiplicative group denoted U(K). The torsion subgroup of U(K),
  consisting of the roots of unity in K, is denoted μ(K).

  Mathlib4 already provides:
  - `(𝓞 K)ˣ` : the unit group of the ring of integers of K
  - `NumberField.Units.torsion K` : the torsion subgroup of the unit group
-/

import Mathlib

open scoped NumberField

/--
  `UnitGroup K` is the multiplicative group of units of the ring of integers
  `𝓞 K` of a number field `K`. This is the classical U(K).

  An element `x : 𝓞 K` is a unit iff `|norm ℚ x| = 1` (see `NumberField.isUnit_iff_norm`).

  We introduce the abbreviation `UnitGroup K` for `(𝓞 K)ˣ` to match the
  classical notation U(K) used in algebraic number theory.
-/
abbrev UnitGroup (K : Type*) [Field K] : Type _ := (𝓞 K)ˣ

/--
  `TorsionSubgroup K` is the torsion subgroup of the unit group of a number
  field `K`. It consists of the units of finite order, which are exactly the
  roots of unity lying in `K`. This is the classical μ(K).

  In Mathlib4 this is `NumberField.Units.torsion K`, which is defined as
  `CommGroup.torsion ((𝓞 K)ˣ)`.

  Equivalent characterization: a unit `x : (𝓞 K)ˣ` is in the torsion subgroup
  iff `w x = 1` for all infinite places `w` of `K`
  (see `NumberField.Units.mem_torsion`).
-/
abbrev TorsionSubgroup (K : Type*) [Field K] : Subgroup ((𝓞 K)ˣ) := by
  sorry
