/-
  Translation of: Algebraic Number Field and its Ring of Integers
  Source concept ID: algebraic_number_field_and_its_ring_of_integers

  An algebraic number field is a subfield F of the complex numbers with
  [F : ℚ] finite. The ring of algebraic integers in F is D = F ∩ Ω,
  where Ω is the set of all algebraic integers.

  Mathlib4 already provides this as:
  - `NumberField K` : a field K with CharZero K and FiniteDimensional ℚ K
  - `NumberField.RingOfIntegers K` : integralClosure ℤ K, notation 𝓞 K
-/

import Mathlib

/--
  `NumberField K` is a field of characteristic zero that is finite-dimensional
  over ℚ. This captures the classical notion: a subfield F ⊆ ℂ with [F : ℚ] < ∞.

  In Mathlib4 this is:
  ```
  class NumberField (K : Type*) [Field K] : Prop where
    [to_charZero : CharZero K]
    [to_finiteDimensional : FiniteDimensional ℚ K]
  ```
  Because any finite extension of ℚ embeds into ℂ, the two formulations are equivalent.
-/
abbrev AlgebraicNumberField (K : Type*) [Field K] : Prop :=
  NumberField K

/--
  The ring of integers `𝓞 K` of an algebraic number field `K` is
  `integralClosure ℤ K`, i.e. the set of elements of `K` that are integral
  over ℤ (roots of monic polynomials with integer coefficients).

  Notation `𝓞 K` is available after `open scoped NumberField`.

  Classically, for a subfield F ⊆ ℂ : the ring of integers is F ∩ Ω,
  where Ω = {z ∈ ℂ | z is an algebraic integer}.
-/
abbrev AlgebraicRingOfIntegers (K : Type*) [Field K] : Type _ :=
  NumberField.RingOfIntegers K

/--
  Example: ℚ is the simplest number field; its ring of integers is ℤ.
-/
example : NumberField ℚ := by
  exact inferInstance

/--
  Example: the ring of integers of ℚ is isomorphic to ℤ.
-/
example : NumberField.RingOfIntegers ℚ ≃+* ℤ :=
  Rat.ringOfIntegersEquiv

/--
  Example: every number field K has an algebra structure
  `Algebra (𝓞 K) K` (ring of integers embeds into the field).
-/
example (K : Type*) [Field K] [NumberField K] : Algebra (NumberField.RingOfIntegers K) K := by
  exact inferInstance

/--
  Example: the ring of integers of a number field is a Dedekind domain.
-/
example (K : Type*) [Field K] [NumberField K] : IsDedekindDomain (NumberField.RingOfIntegers K) := by
  exact inferInstance
