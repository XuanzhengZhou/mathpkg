import Mathlib

/-!
# Extension of Monomial Order to Terms

Given a monomial order `m` on `σ →₀ ℕ` and a commutative semiring `R`,
a **term** is a pair of a monomial (exponent vector `σ →₀ ℕ`) and a
nonzero coefficient in `R`.

The monomial order `m` is extended to terms by comparing only the
monomial parts, ignoring coefficients:
`(u, m) < (v, n)` iff `m ≺[m] n`, and
`(u, m) ≤ (v, n)` iff `m ≼[m] n`.

**This is not a partial order** -- different terms with the same monomial
but different coefficients are not comparable by `<`, and two distinct
terms `(u, a)` and `(v, a)` satisfy both `(u, a) ≤ (v, a)` and
`(v, a) ≤ (u, a)` but are not equal.  It is nevertheless a convenient
notation for working with Gröbner bases.

## Mathlib4 References
- `MonomialOrder`: `Data/Finsupp/MonomialOrder.lean`
- `MvPolynomial`: `Algebra/MvPolynomial/Basic.lean`
-/

open scoped MonomialOrder

universe u v

variable {σ : Type u} {R : Type v} [CommSemiring R]

/-- A *term* is a monomial together with a nonzero coefficient.
This is the basic unit for extending a monomial order to the full polynomial ring:
we compare two terms by comparing their monomial parts, ignoring the coefficients. -/
structure Term (σ : Type u) (R : Type v) [CommSemiring R] where
  /-- The exponent vector (the monomial part). -/
  monomial : σ →₀ ℕ
  /-- The coefficient, required to be nonzero. -/
  coeff : R
  /-- The coefficient is nonzero. -/
  coeff_ne_zero : coeff ≠ 0

namespace Term

variable (m : MonomialOrder σ)

/-- The **strict term order** induced by a monomial order:
`t₁ < t₂` iff the monomial of `t₁` is strictly smaller than the monomial of `t₂`.
This ignores coefficients entirely. -/
def lt (t₁ t₂ : Term σ R) : Prop := by
  sorry
