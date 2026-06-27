import Mathlib

/-!
# Powers with Integer Exponents

Let `G` be a group and `a ∈ G`. For an integer `n : ℤ`, the power `a ^ n` is defined as:

- If `n ≥ 0` (i.e., `n : ℕ`): `a ^ n` is the product of `n` copies of `a`, with
  `a ^ 0 = 1` and `a ^ 1 = a`.
- If `n < 0` with `n = -m` (where `m > 0`): `a ^ n = (a ^ m)⁻¹`.

In particular, `a ^ (-1 : ℤ)` equals the group inverse `a⁻¹`.

## Mathlib4 References

Mathlib4 defines integer powers via `DivInvMonoid.zpow` (in
`Algebra/Group/Defs.lean`). The notation `a ^ (n : ℤ)` is available through the
`Pow G ℤ` instance `DivInvMonoid.toZPow`.

Key lemmas (in `Algebra/Group/Defs.lean`):
- `zpow_zero`    : `a ^ (0 : ℤ) = 1`
- `zpow_one`     : `a ^ (1 : ℤ) = a`
- `zpow_negSucc` : `a ^ (Int.negSucc n) = (a ^ (n+1))⁻¹`
- `zpow_neg_one` : `x ^ (-1 : ℤ) = x⁻¹`
- `zpow_natCast` : `a ^ (n : ℤ) = a ^ n` for `n : ℕ`
- `zpow_ofNat`   : `a ^ (OfNat.ofNat n : ℤ) = a ^ n`
- `zpow_add`     : `a ^ (m + n : ℤ) = a ^ m * a ^ n` (for commuting `a`)
-/

open scoped Int

/-- `integerPower G a n` is the same as `a ^ (n : ℤ)`, i.e. the integer exponent
power of `a` in a group `G`. This `abbrev` exists for documentation purposes;
in practice one uses the `a ^ (n : ℤ)` notation directly. -/
abbrev integerPower {G : Type*} [DivInvMonoid G] (a : G) (n : ℤ) : G := a ^ n

/-- `integerPower` is notationally identical to the built-in `^` operator
with an `ℤ` exponent in any `DivInvMonoid`. -/
example {G : Type*} [DivInvMonoid G] (a : G) (n : ℤ) : integerPower G a n = a ^ n := rfl

-- Example 1: zero exponent
example {G : Type*} [Group G] (a : G) : a ^ (0 : ℤ) = 1 := by
  simp

-- Example 2: one exponent
example {G : Type*} [Group G] (a : G) : a ^ (1 : ℤ) = a := by
  simp

-- Example 3: negative one gives the inverse
example {G : Type*} [Group G] (a : G) : a ^ (-1 : ℤ) = a⁻¹ := by
  simp

-- Example 4: a positive integer n yields n-fold product
example {G : Type*} [Group G] (a : G) : a ^ (3 : ℤ) = a * a * a := by
  simp

-- Example 5: negative exponent via the inverse of a positive power
example {G : Type*} [Group G] (a : G) : a ^ (-2 : ℤ) = (a * a)⁻¹ := by
  simp

-- Example 6: additivity of exponents (for commuting elements)
example {G : Type*} [CommGroup G] (a : G) (m n : ℤ) : a ^ (m + n : ℤ) = a ^ m * a ^ n := by
  simp [zpow_add a m n]

-- Example 7: relation between natural and integer exponent
example {G : Type*} [Group G] (a : G) (n : ℕ) : a ^ (n : ℤ) = a ^ n := by
  simp
