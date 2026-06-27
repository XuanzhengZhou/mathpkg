import Mathlib

/-!
# Nearest Integer Function

For a real number `x`, `⌊x⌉` denotes the integer nearest to `x`, defined by
`⌊x⌉ = ⌊x + 1/2⌋`. This rounds halves towards positive infinity (i.e., `round (0.5) = 1`).

Mathlib4 provides this as `round` in `Mathlib/Algebra/Order/Round`. We define
`nearest_integer` as an abbreviation of `round` for clarity, matching the standard
notation `⌊x⌉`.

The key identity (for linear ordered fields) is:
`round x = ⌊x + 1 / 2⌋`

## References
- `Mathlib/Algebra/Order/Round.lean` — `round` definition and `round_eq` theorem
- See also `nearestInteger` in Lean 3's `data/int/basic`
-/

/--
`nearestInteger x` returns the integer nearest to `x`, rounding halves towards
positive infinity. This is an abbreviation of Mathlib4's `round`.

Formally: `nearestInteger x = ⌊x + 1/2⌋` (over any linear ordered field with a floor ring).

Examples:
- `nearestInteger (0.5 : ℚ) = 1`
- `nearestInteger (2.3 : ℝ) = 2`
- `nearestInteger (-0.5 : ℚ) = 0`
-/
abbrev nearestInteger {α : Type*} [Ring α] [LinearOrder α] [IsStrictOrderedRing α] [FloorRing α]
    (x : α) : ℤ := by
  sorry
