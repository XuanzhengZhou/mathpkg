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
abbrev FormalLaurentSeries (K : Type*) [Field K] : Type _ :=
  LaurentSeries K

/-- Notation `K⸨X⸩` for `FormalLaurentSeries K`, matching Mathlib's `LaurentSeries`. -/
scoped notation:max K "⸨X⸩" => FormalLaurentSeries K

/-- The field of formal Laurent series over `K` inherits Mathlib's `Field` instance
because `LaurentSeries K = HahnSeries ℤ K` is a field when `K` is a field. -/
instance (K : Type*) [Field K] : Field (FormalLaurentSeries K) :=
  inferInstanceAs (Field (LaurentSeries K))

/-- The `n`-th coefficient of a formal Laurent series `f = ∑ a_n X^n`. -/
def coeffL (K : Type*) [Field K] (n : ℤ) (f : FormalLaurentSeries K) : K :=
  f.coeff n

/-- The order of a nonzero formal Laurent series (the smallest `n` with `a_n ≠ 0`). -/
def orderL (K : Type*) [Field K] (f : FormalLaurentSeries K) : ℤ :=
  f.order

end field_of_formal_generalized_power_series_laurent_series

/-! ### Examples -/

section examples

open scoped LaurentSeries

variable (K : Type*) [Field K]

/-- The constant series: `a ∈ K` viewed as the series `a + 0·X + 0·X^2 + …`. -/
example (a : K) : FormalLaurentSeries K :=
  HahnSeries.C a

/-- The variable `X` as a Laurent series (a single term `1·X^1`). -/
example : FormalLaurentSeries K :=
  single (1 : ℤ) (1 : K)

/-- Addition of two Laurent series is termwise. -/
example (f g : FormalLaurentSeries K) (n : ℤ) : (f + g).coeff n = f.coeff n + g.coeff n := by
  simp

/-- Multiplication is convolution: `(f*g)_n = ∑_{i+j=n} f_i * g_j`. -/
example (f g : FormalLaurentSeries K) (n : ℤ) : (f * g).coeff n = ∑ x in f.support, ∑ y in g.support,
    if x + y = n then f.coeff x * g.coeff y else 0 := by
  simp [add_comm]

/-- The formal Laurent series over a field form a field. -/
example [Field K] : Field (FormalLaurentSeries K) := by
  infer_instance

/-- Every nonzero Laurent series has a multiplicative inverse. -/
example (f : FormalLaurentSeries K) (hf : f ≠ 0) : f * f⁻¹ = 1 := by
  apply mul_inv_cancel hf

/-- Power series embed into Laurent series (via `HahnSeries.ofPowerSeries`). -/
example (f : PowerSeries K) : FormalLaurentSeries K :=
  HahnSeries.ofPowerSeries ℤ K f

/-- The constant term of the inverse of `1 - X` (geometric series). -/
example : (HahnSeries.single (0 : ℤ) (1 : K) - HahnSeries.single (1 : ℤ) (1 : K))⁻¹ =
    HahnSeries.single (0 : ℤ) (1 : K) - HahnSeries.single (-1 : ℤ) (1 : K) := by
  sorry -- This is a nontrivial computation; included as a placeholder

/-- The coefficient of `X^{-1}` in a series is its residue. -/
def residue (f : FormalLaurentSeries K) : K :=
  f.coeff (-1)

end examples
