import Mathlib

open scoped LaurentSeries

/-!
# Field of Formal Generalized Power Series (Laurent Series)

For a field `K`, `K((X))` is the set of formal sums

    ∑_{n=n₀}^∞ a_n X^n

with `n₀ ∈ ℤ` and `a_n ∈ K`. Addition is termwise and multiplication is convolution.
The set `K((X))` is a field with these operations.

## Mathlib4 Implementation

Mathlib4 defines `LaurentSeries R` as an abbreviation for `HahnSeries ℤ R`, with
notation `R⸨X⸩`.  Since `K⸨X⸩` is the fraction field of `K⟦X⟧` (power series),
the typeclass `Field (K⸨X⸩)` is available whenever `K` is a field.

See `Mathlib/RingTheory/LaurentSeries.lean` and
`Mathlib/RingTheory/HahnSeries/Summable.lean` (`instField`).
-/

section field_of_formal_generalized_power_series_laurent_series

/-! ### The definition (alias for Mathlib's `LaurentSeries`) -/

/-- `FormalLaurentSeries K` is the field of formal Laurent series over `K`.

Formally, an element is a sum `∑_{n ∈ ℤ} a_n X^n` where only finitely many
negative-index coefficients are non-zero.  Addition is termwise,
multiplication is the Cauchy (convolution) product.

This is an alias for `Mathlib.RingTheory.LaurentSeries.LaurentSeries K`,
which is itself an abbreviation for `HahnSeries ℤ K`. -/
abbrev FormalLaurentSeries (K : Type*) [Field K] : Type _ := by
  sorry
