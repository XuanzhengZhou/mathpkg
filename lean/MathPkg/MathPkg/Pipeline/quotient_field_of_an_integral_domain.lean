import Mathlib

open scoped Classical

/-!
# Quotient Field of an Integral Domain

The **quotient field** (also called **field of fractions**) `K(R)` of an integral domain `R`
is the localization `R[U⁻¹]` where `U = R \ {0}`, i.e. the set of non-zero elements of `R`.

In Mathlib4, this is formalized as:

```lean
abbrev FractionRing (R : Type*) [CommSemiring R] := Localization (nonZeroDivisors R)
```

See `Mathlib/RingTheory/Localization/FractionRing.lean` for full details. The typeclass
`IsFractionRing R K` (defined as `IsLocalization (nonZeroDivisors R) K`) expresses that
`K` is a field of fractions of `R`.

## Key properties (all in Mathlib4)

- `FractionRing.field` (for integral domains): `FractionRing R` is a field when `R` is an
  integral domain.
- `IsFractionRing.toField`: any `K` with `IsFractionRing R K` for an integral domain `R` is a field.
- `FractionRing.algEquiv`: any two fraction fields of `R` are `R`-algebra isomorphic.
- `Rat.isFractionRing`: `ℚ` is the fraction field of `ℤ`.

## Dependencies

- `localization_of_a_ring` — quotient field is a special case of localization.
-/

section quotient_field_of_an_integral_domain

/-! ### Definition as alias for Mathlib's `FractionRing` -/

variable (R : Type*) [CommRing R] [IsDomain R]

/--
`QuotientField R` is the field of fractions of an integral domain `R`,
defined as the localization at `R \ {0}` (i.e. `nonZeroDivisors R`).

Formally: `QuotientField R := FractionRing R := Localization (nonZeroDivisors R)`.

Elements of `QuotientField R` are fractions `a / b` with `a, b ∈ R` and `b ≠ 0`,
modulo the usual equivalence relation:

  `a / b = c / d`  iff  `a * d = c * b`

This is the standard construction of the quotient field (field of fractions)
of an integral domain.
-/
abbrev QuotientField (R : Type*) [CommRing R] [IsDomain R] : Type _ :=
  FractionRing R

/--
The natural embedding of `R` into its quotient field. Every `r ∈ R` is sent to
the equivalence class of the fraction `r / 1`.
-/
example (r : R) : QuotientField R :=
  algebraMap R (QuotientField R) r

end quotient_field_of_an_integral_domain

/-! ### Examples -/

section examples

/--
**Example**: `ℚ` is the quotient field of `ℤ`. This is a Mathlib4 instance
via `Rat.isFractionRing`.
-/
example : QuotientField ℤ = FractionRing ℤ :=
  rfl

/--
**Example**: The quotient field of a field `K` is `K` itself (up to isomorphism).
Mathlib4 provides `IsFractionRing K K` as an instance for any field `K`.
-/
example (K : Type*) [Field K] : IsFractionRing K K := by
  infer_instance

/--
**Example**: Every element `z` of the quotient field can be written as a fraction
`x / y` with `x, y ∈ R` and `y ≠ 0`. This is the `div_surjective` lemma from Mathlib.
-/
example (z : FractionRing R) : ∃ (x : R) (y : R), y ≠ 0 ∧
    (algebraMap R (FractionRing R) x) / (algebraMap R (FractionRing R) y) = z := by
  have h := IsFractionRing.div_surjective R z
  rcases h with ⟨x, y, hy, hz⟩
  refine ⟨x, y, y.prop, ?_⟩
  -- Convert from `nonZeroDivisors` to `≠ 0`
  have hy_ne_zero : y ≠ 0 := by
    rw [mem_nonZeroDivisors_iff_ne_zero] at hy
    exact hy
  exact ⟨x, y, hy_ne_zero, hz⟩

/--
**Example**: In the quotient field, `algebraMap` is injective for an integral domain.
-/
example (x y : R) (h : (algebraMap R (FractionRing R) x) = algebraMap R (FractionRing R) y) :
    x = y :=
  IsFractionRing.injective R (FractionRing R) h

/--
**Example**: The equality of fractions in the quotient field:
`a/b = c/d` iff `a*d = c*b` (when `b, d ≠ 0`).
-/
example (a b c d : R) (hb : b ≠ 0) (hd : d ≠ 0) :
    ((algebraMap R (FractionRing R) a) / (algebraMap R (FractionRing R) b) =
     (algebraMap R (FractionRing R) c) / (algebraMap R (FractionRing R) d)) ↔
    a * d = c * b := by
  have hb' : algebraMap R (FractionRing R) b ≠ 0 :=
    IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors
      (by
        rw [mem_nonZeroDivisors_iff_ne_zero]
        exact hb)
  have hd' : algebraMap R (FractionRing R) d ≠ 0 :=
    IsFractionRing.to_map_ne_zero_of_mem_nonZeroDivisors
      (by
        rw [mem_nonZeroDivisors_iff_ne_zero]
        exact hd)
  simp [div_eq_div_iff hb' hd']

/--
**Example**: In the quotient field of ℤ, we have `2/3 = 4/6` because `2*6 = 4*3`.
-/
example : ((2 : ℤ) : FractionRing ℤ) / ((3 : ℤ) : FractionRing ℤ) =
           ((4 : ℤ) : FractionRing ℤ) / ((6 : ℤ) : FractionRing ℤ) := by
  norm_num

end examples
