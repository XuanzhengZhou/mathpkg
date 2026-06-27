import Mathlib

/-!
# Powers with Integer Exponents

For `a ∈ G`: if `n ≥ 0`, `a^n` is the product of `n` copies of `a` (`a^0 = 1`, `a^1 = a`);
if `n < 0` with `n = -m` (`m ≥ 0`), then `a^n = (a^m)⁻¹`. In particular, `a⁻¹` is the inverse.
-/

def integerPower {G : Type*} [DivInvMonoid G] (a : G) (n : ℤ) : G := by
  sorry
