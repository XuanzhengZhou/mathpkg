import Mathlib

/-!
# Fundamental Discriminant

An integer `D` is called a **fundamental discriminant** if `D` is the discriminant
of a quadratic field `ℚ(√D)`. Equivalently, `D ≠ 1` and either:

1. `D ≡ 1 mod 4` and `D` is squarefree; or
2. `D ≡ 0 mod 4`, `D/4` is squarefree, and `D/4 ≡ 2 or 3 mod 4`.

These conditions ensure that the quadratic field `ℚ(√D)` has its ring of integers
exactly `ℤ[(D+√D)/2]` when `D ≡ 1 mod 4`, and `ℤ[√D]` when `D ≡ 0 mod 4`.

## Examples

- `-4`, `-3`, `5`, `8`, `12` are fundamental discriminants.
- `1`, `-1`, `4`, `9`, `20` are NOT fundamental discriminants.

## References

- Cohen, *A Course in Computational Algebraic Number Theory*, Section 5.2
- Borevich–Shafarevich, *Number Theory*, Chapter 2
-/

/--
An integer `D` is a **fundamental discriminant** if `D ≠ 1` and either:
- `D ≡ 1 (mod 4)` and `D` is squarefree, or
- `D ≡ 0 (mod 4)`, `D/4` is squarefree, and `D/4 ≡ 2 or 3 (mod 4)`.

This characterizes discriminants of quadratic fields.
-/
def isFundamentalDiscriminant (D : ℤ) : Prop := by
  sorry
