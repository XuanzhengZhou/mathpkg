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
def f_p (A B : ℤ) (p : ℕ) [Fact p.Prime] : ℤ := by
  sorry
