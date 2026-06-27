/-
Copyright (c) 2024 MathPkg contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib

/-! # Adapted Monomial Order

A monomial order on `k[z₁,…,zₘ, w₁,…,wₙ]` is said to be **adapted** to a given linear function
`ℓ` if, for any two monomial exponents `a, b : σ →₀ ℕ`, the condition `ℓ a < ℓ b` implies
`a ≺[m] b`.  In other words, the monomial order *refines* the preorder induced by `ℓ`.

This definition is tailored for integer programming problems, where one first compares
monomials by a linear objective function `ℓ`, and breaks ties using the underlying monomial order.

## Main definition

* `MonomialOrder.IsAdapted ℓ` : a predicate stating that a monomial order `m` is adapted to a
  linear function `ℓ : (σ →₀ ℕ) → M` where `M` is a linearly ordered additive commutative monoid.

## References

* [Cox, Little and O'Shea, *Ideals, varieties, and algorithms*][coxlittleoshea1997]
* [Thomas, *Integer Programming and Gröbner Bases*]
-/

open scoped MonomialOrder

namespace MonomialOrder

variable {σ : Type*} (m : MonomialOrder σ)

/-- A monomial order `m` is **adapted** to a linear function `ℓ : (σ →₀ ℕ) → M`
(where `M` is a linearly ordered additive commutative monoid) if `ℓ a < ℓ b`
implies `a ≺[m] b`.  This means the monomial order refines the order given by `ℓ`.

In the context of integer programming, `ℓ` is typically a linear objective function
(an `AddMonoidHom`), and the adapted monomial order lets one solve optimisation problems
via Gröbner basis techniques. -/
def IsAdapted {M : Type*} [LinearOrder M] [AddCommMonoid M] [IsOrderedAddMonoid M]
    (ℓ : (σ →₀ ℕ) → M) : Prop := by
  sorry
