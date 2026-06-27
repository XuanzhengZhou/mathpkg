import Mathlib.NumberTheory.LegendreSymbol.JacobiSymbol

/-!
# Jacobi Symbol Definition

Let `b` be a positive odd integer with prime factorization `b = p₁ p₂ ... pₘ`,
where the `pᵢ` are (not necessarily distinct) primes. The **Jacobi symbol** `(a/b)` is defined as
the product of the Legendre symbols:

    (a/b) = (a/p₁) · (a/p₂) · ... · (a/pₘ)

where `(a/pᵢ)` is the Legendre symbol.

In Mathlib4, the Jacobi symbol is defined as `jacobiSym a b` for `a : ℤ` and `b : ℕ`,
using the prime factorization of `b` via `Nat.factors`:

    jacobiSym a b = ∏_{p ∈ primeFactorsList b} legendreSym p a

The localized notation `J(a | b)` is available in the `NumberTheorySymbols` scope.
-/

open NumberTheorySymbols

/-- The Jacobi symbol, as already defined in Mathlib4. -/
abbrev JacobiSymbol := jacobiSym

example (a : ℤ) (b : ℕ) : ℤ :=
  J(a | b)

/-- Example: For any integer `a`, the Jacobi symbol `J(a | 1)` is `1`. -/
example (a : ℤ) : J(a | 1) = 1 := by
  simp [JacobiSymbol]

/-- Example: The Jacobi symbol is multiplicative in the second argument
for nonzero `b₁`, `b₂`. -/
example (a : ℤ) (b₁ b₂ : ℕ) [NeZero b₁] [NeZero b₂] : J(a | b₁ * b₂) = J(a | b₁) * J(a | b₂) := by
  exact jacobiSym.mul_right a b₁ b₂
