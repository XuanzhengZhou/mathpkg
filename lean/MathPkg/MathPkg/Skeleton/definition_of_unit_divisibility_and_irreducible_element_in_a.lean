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
  sorry
