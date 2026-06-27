import Mathlib

open Finset

/--
Given an elliptic curve E : y² = x³ - Ax - B with integer coefficients A, B
and a prime number p, define

  f_p(A, B, p) = -∑_{x=0}^{p-1} ((x³ - Ax - B)/p)

where ((x³ - Ax - B)/p) is the Legendre symbol (as defined by `legendreSym p` in Mathlib4).

This quantity equals the trace of Frobenius a_p = p + 1 - #E(F_p) for the elliptic curve E
over the finite field F_p, i.e., the deviation of the number of F_p-rational points
from p + 1. The Hasse bound implies |f_p| ≤ 2√p.

## References

* J.H. Silverman, *The Arithmetic of Elliptic Curves*, GTM 106, Chapter V.
-/
def f_p (A B : ℤ) (p : ℕ) [Fact p.Prime] : ℤ :=
  -Finset.sum (range p) fun x : ℕ =>
    legendreSym p (((x : ℤ) ^ 3) - A * (x : ℤ) - B)

/--
Example: For the elliptic curve E : y² = x³ - x (so A = 1, B = 0) over F₅,
compute f₅.

  x   | x³ - x (mod 5) | Legendre symbol
  0   | 0              |  0
  1   | 0              |  0
  2   | 6 ≡ 1          |  1
  3   | 24 ≡ 4         |  1
  4   | 60 ≡ 0         |  0

Sum = 2, therefore f₅ = -2.
-/
example : f_p 1 0 5 = -2 := by
  native_decide
