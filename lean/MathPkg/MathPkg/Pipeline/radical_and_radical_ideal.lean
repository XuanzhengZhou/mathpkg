import Mathlib

/-!
# Radical and Radical Ideal

Let `I` be an ideal in a commutative semiring `R`. Mathlib4 defines:

* `Ideal.radical I`: the set of all `r : R` such that `r ^ n ∈ I` for some `n ≥ 1`.
  This is `√I` in standard notation.
* `Ideal.IsRadical I`: the proposition that `I` is a **radical ideal**, i.e. `I.radical ≤ I`,
  which is equivalent to `I.radical = I`.

## Mathlib4 location

These definitions are in `Mathlib/RingTheory/Ideal/Operations.lean`, section `MulAndRadical`.
They require `[CommSemiring R]`.

## Sources

* [Atiyah-Macdonald, Chapter 1, Exercise 1.13]
-/

open Ideal

/-- The radical of an ideal: `√I = {r | r ^ n ∈ I for some n ≥ 1}`. -/
-- Already defined in Mathlib as `Ideal.radical`; see also `Ideal.IsRadical` for radical ideals.
example (R : Type) [CommSemiring R] (I : Ideal R) (r : R) : Prop :=
  r ∈ I.radical

/-- `I` is a radical ideal if `√I = I`, i.e. `I.radical ≤ I`. -/
-- Already defined in Mathlib as `Ideal.IsRadical`.
example (R : Type) [CommSemiring R] (I : Ideal R) : Prop :=
  I.IsRadical

/-- Being radical is equivalent to equality with the radical. -/
example (R : Type) [CommSemiring R] (I : Ideal R) : I.IsRadical ↔ I.radical = I :=
  (Ideal.radical_eq_iff).symm

/-- The zero ideal is radical in an integral domain (prime elements have no nilpotency). -/
example (R : Type) [CommSemiring R] (I : Ideal R) : (I.radical).IsRadical :=
  Ideal.radical_isRadical I
