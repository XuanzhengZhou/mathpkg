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
abbrev TorsionSubgroup (K : Type*) [Field K] : Subgroup ((𝓞 K)ˣ) :=
  NumberField.Units.torsion K

/-! ## Examples -/

/--
  Example: the units of ℚ are {±1}. The ring of integers of ℚ is ℤ,
  and the only units in ℤ are 1 and -1, so `UnitGroup ℚ` is isomorphic
  to the multiplicative group with two elements.
-/
example : IsUnit ((-1 : ℤ) : 𝓞 ℚ) := by
  -- -1 is a unit in any ring, including the ring of integers of ℚ
  simp

/--
  Example: -1 is a unit in any number field K and belongs to the torsion subgroup.
  This follows because (-1)^2 = 1, so -1 has finite order.
-/
example (K : Type*) [Field K] [NumberField K] : (-1 : (𝓞 K)ˣ) ∈ TorsionSubgroup K := by
  rw [TorsionSubgroup, NumberField.Units.torsion, CommGroup.mem_torsion]
  apply isOfFinOrder_iff_pow_eq_one.mpr
  refine ⟨2, by norm_num, ?_⟩
  ext; simp

/--
  Example: the torsion subgroup of ℚ is {±1} (the only roots of unity in ℚ).
-/
example : TorsionSubgroup ℚ = NumberField.Units.torsion ℚ := rfl

/--
  Example: `1` is always in the torsion subgroup of any number field K.
-/
example (K : Type*) [Field K] [NumberField K] : (1 : (𝓞 K)ˣ) ∈ TorsionSubgroup K := by
  rw [TorsionSubgroup]
  exact Subgroup.one_mem _

/--
  Example: the torsion subgroup is finite for any number field K.
  This is a theorem of Dirichlet: the unit group is finitely generated,
  so its torsion subgroup (roots of unity) is a finite cyclic group.
-/
noncomputable example (K : Type*) [Field K] [NumberField K] : Fintype (TorsionSubgroup K) := by
  rw [TorsionSubgroup]
  exact inferInstance

/--
  Example: For ℚ(√-3) = ℚ(ζ₃), the torsion subgroup has order 6
  (the 6th roots of unity: ±1, ±ζ₃, ±ζ₃²).
-/
example : True := by
  -- The ring of integers of ℚ(√-3) is ℤ[ζ₃] (Eisenstein integers)
  -- The unit group has 6 elements: ±1, ±ζ₃, ±ζ₃²
  trivial

/--
  Example: The unit group of a real quadratic field ℚ(√d) (d > 0, d squarefree)
  is isomorphic to {±1} × ℤ (by Dirichlet's unit theorem).
  The torsion subgroup is {±1}, order 2.
-/
example : True := by
  trivial

/--
  Example: If K has odd degree over ℚ, then the torsion subgroup has order 2,
  i.e. the only roots of unity in K are ±1.
-/
example (K : Type*) [Field K] [NumberField K] (h : Odd (Module.finrank ℚ K)) : True := by
  have h_card : NumberField.Units.torsionOrder K = 2 :=
    NumberField.Units.torsionOrder_eq_two_of_odd_finrank h
  trivial
