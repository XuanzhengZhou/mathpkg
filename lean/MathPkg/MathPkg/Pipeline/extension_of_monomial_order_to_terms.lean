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
def lt (t₁ t₂ : Term σ R) : Prop :=
  t₁.monomial ≺[m] t₂.monomial

/-- The **non-strict term order** induced by a monomial order:
`t₁ ≤ t₂` iff the monomial of `t₁` is smaller than or equal to the monomial of `t₂`.
This ignores coefficients entirely. -/
def le (t₁ t₂ : Term σ R) : Prop :=
  t₁.monomial ≼[m] t₂.monomial

/-- Notation `t₁ ≺ₜ[m] t₂` for the strict term order. -/
scoped notation:50 t₁:50 " ≺ₜ[" m:25 "] " t₂:50 => Term.lt m t₁ t₂

/-- Notation `t₁ ≼ₜ[m] t₂` for the non-strict term order. -/
scoped notation:50 t₁:50 " ≼ₜ[" m:25 "] " t₂:50 => Term.le m t₁ t₂

end Term

-- ============================================================
-- Examples
-- ============================================================

open Term
open scoped MonomialOrder

section Examples

-- Use the lexicographic monomial order on `Fin 2 →₀ ℕ`.
variable [WellFoundedGT (Fin 2)]

/-- A term with monomial X₀² and coefficient 3. -/
def term1 : Term (Fin 2) ℚ where
  monomial := Finsupp.single 0 2
  coeff := 3
  coeff_ne_zero := by norm_num

/-- A term with monomial X₀¹ X₁¹ and coefficient (-1). -/
def term2 : Term (Fin 2) ℚ where
  monomial := Finsupp.single 0 1 + Finsupp.single 1 1
  coeff := -1
  coeff_ne_zero := by norm_num

/-- In the lex order, X₀² > X₀X₁, so term2 < term1. -/
example : term2 ≺ₜ[MonomialOrder.lex] term1 := by
  unfold term1 term2 lt
  -- `single 0 2 > single 0 1 + single 1 1` in lex order
  simp [MonomialOrder.lex_lt_iff, Finsupp.Lex.lt_iff]
  refine ⟨0, ?_⟩
  simp

/-- Two different terms with the same monomial are both ≤ each other in the term order,
illustrating that the term order is not antisymmetric (not a partial order). -/
example : (Term.mk (Finsupp.single 0 1) (2 : ℚ) (by norm_num) ≼ₜ[MonomialOrder.lex]
           Term.mk (Finsupp.single 0 1) (5 : ℚ) (by norm_num)) := by
  unfold le
  simp

/-- The reverse direction also holds with the same monomial but different coefficient:
both `t₁ ≤ t₂` and `t₂ ≤ t₁` even though `t₁ ≠ t₂`. -/
example : (Term.mk (Finsupp.single 0 1) (5 : ℚ) (by norm_num) ≼ₜ[MonomialOrder.lex]
           Term.mk (Finsupp.single 0 1) (2 : ℚ) (by norm_num)) := by
  unfold le
  simp

end Examples
