import Mathlib

/-!
# Definition of unit, divisibility, and irreducible element in an integral domain

Let `R` be an integral domain (i.e., `R` is a `CommRing` with `IsDomain R`).

1. An element `u : R` is a **unit** if it has a multiplicative inverse in `R`.
   In Mathlib4, this is the predicate `IsUnit u`.

2. For `a b : R` with `b ≠ 0`, we say that **`b` divides `a`** (written `b ∣ a`)
   if there exists `q : R` such that `a = b * q`.  In an integral domain, such
   a `q` is unique (since there are no zero divisors) and is denoted `a / b`.
   In Mathlib4, divisibility is the notation `b ∣ a` from `Dvd.dvd`.

3. An element `p : R` is called **irreducible** if `p` is neither zero nor a unit,
   and whenever `q ∣ p`, then either `q` is a unit or `p / q` is a unit.
   In Mathlib4, this is the `Irreducible p` structure (defined for any `Monoid`).

## Mathlib4 coverage

All three concepts are already available in Mathlib4:
- `IsUnit`        → `Algebra/Group/Units/Defs`
- `∣` (Dvd.dvd)  → `Algebra/Divisibility` / `Algebra/GroupPower`
- `Irreducible`   → `Algebra/Group/Irreducible/Defs`

This module provides convenient namespace aliases and illustrative examples
in ℤ (the prototypical integral domain).
-/

namespace IntegralDomain

variable (R : Type*) [CommRing R] [IsDomain R]

/-- An element `u` in an integral domain `R` is a **unit** if it has a
multiplicative inverse in `R`.  This is exactly `IsUnit u` from Mathlib4. -/
abbrev Unit (u : R) : Prop := IsUnit u

/-- For `a b : R` with `b ≠ 0`, we say that **`b` divides `a`** (written `b ∣ a`)
if there exists `q : R` such that `a = b * q`.  This is exactly the Mathlib4
`Dvd.dvd` notation. -/
abbrev Divides (b a : R) : Prop := b ∣ a

/-- An element `p` in an integral domain `R` is **irreducible** if it is non-zero,
non-unit, and whenever `q ∣ p` then either `q` or `p / q` is a unit.
Equivalent to Mathlib4 `Irreducible p`. -/
abbrev Irred (p : R) : Prop := Irreducible p

end IntegralDomain

/-! ## Examples in ℤ

ℤ is an integral domain (`IsDomain ℤ`).  We illustrate the three definitions
using ℤ as the ambient ring.
-/

/-- In ℤ the only units are `1` and `-1`.  Both are `IsUnit`. -/
example : IsUnit ((1 : ℤ) : ℤ) := isUnit_one

example : IsUnit ((-1 : ℤ) : ℤ) := isUnit_one.neg

/-- `2` divides `6` in ℤ because `6 = 2 * 3`. -/
example : (2 : ℤ) ∣ (6 : ℤ) := ⟨3, by ring⟩

/-- `2` is irreducible in ℤ. In a `DecompositionMonoid` such as ℤ,
a prime element is irreducible. Since `2` is prime in ℤ, it is irreducible. -/
example : Irreducible (2 : ℤ) := by
  rw [irreducible_iff_prime]
  exact Int.prime_two

/-- Units in an integral domain always divide zero (trivially, since 0 = u * 0). -/
example (u : ℤ) (_hu : IsUnit u) : u ∣ (0 : ℤ) :=
  dvd_zero u

/-- In an integral domain, if `b ≠ 0` and `b ∣ a`, the quotient `a / b`
is uniquely determined: if `a = b * q₁` and `a = b * q₂`, then `q₁ = q₂`. -/
example (a b q₁ q₂ : ℤ) (hb : b ≠ 0) (h₁ : a = b * q₁) (h₂ : a = b * q₂) : q₁ = q₂ := by
  have : b * q₁ = b * q₂ := by
    rw [← h₁, h₂]
  -- In ℤ (an integral domain), `b ≠ 0` allows cancellation
  exact mul_left_cancel₀ hb this
