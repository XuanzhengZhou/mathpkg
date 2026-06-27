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
abbrev QuotientField (R : Type*) [CommRing R] [IsDomain R] : Type _ := by
  sorry
