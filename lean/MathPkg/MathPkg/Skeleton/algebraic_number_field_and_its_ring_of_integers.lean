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
abbrev AlgebraicNumberField (K : Type*) [Field K] : Prop := by
  sorry
