import Mathlib

/-!
# Order Domain

A pair `(R, ρ)` is an **order domain** if `ρ` is an **order function** on the `F`-algebra `R`.

An order function `ρ : R → WithBot Γ` (where `Γ` is a linearly ordered additive commutative monoid)
satisfies axioms analogous to a degree function on a polynomial ring, as defined in
Cox–Little–O'Shea, *Using Algebraic Geometry* (GTM 185), Chapter 10, Definition (1.1):

1. `ρ(f) = ⊥` if and only if `f = 0`
2. `ρ(λ • f) = ρ(f)` for all non-zero scalars `λ : F`
3. `ρ(f + g) ≤ max (ρ f) (ρ g)`, with equality when `ρ(f) ≠ ρ(g)`
4. If `ρ(f) = ρ(g) ≠ ⊥`, then there exists a non-zero scalar `λ` such that `ρ(f + λ • g) < ρ(f)`
5. `ρ(f * g) = ρ(f) + ρ(g)` (the order function is additive over products)

In the chapter, `F` is typically a finite field `F_q` and `Γ` is a submonoid of `ℤᵣ_{≥0}`.

## Main definitions

* `OrderFunction F R Γ` — the type of order functions on an `F`-algebra `R` with values in `WithBot Γ`
* `OrderDomain F R Γ` — a pair `(R, ρ)` where `ρ` is an order function on `R`
-/

universe u v w

variable {F : Type u} [Field F]
variable {R : Type v} [CommRing R] [Algebra F R]
variable {Γ : Type w} [AddCommMonoid Γ] [LinearOrder Γ] [IsOrderedAddMonoid Γ]

/-- An **order function** on an `F`-algebra `R` is a function `ρ : R → WithBot Γ`
satisfying the five axioms of Definition (1.1) in Cox–Little–O'Shea, Chapter 10.

The value `ρ(f) = ⊥` (i.e. `-∞`) means `f = 0`; otherwise `ρ(f)` is an element of `Γ`
that behaves like a "degree" or "leading exponent" under addition and multiplication. -/
structure OrderFunction (F : Type u) (R : Type v) (Γ : Type w)
    [Field F] [CommRing R] [Algebra F R] [AddCommMonoid Γ] [LinearOrder Γ] [IsOrderedAddMonoid Γ] where
  /-- The underlying function `R → WithBot Γ`. -/
  ρ : R → WithBot Γ
  /-- `ρ(0) = ⊥`. -/
  map_zero' : ρ 0 = ⊥
  /-- If `ρ(f) = ⊥` then `f = 0`. -/
  map_eq_bot (f : R) (h : ρ f = ⊥) : f = 0
  /-- `ρ(c • f) = ρ(f)` for all non-zero scalars `c`. -/
  map_smul_eq (c : F) (f : R) (hc : c ≠ 0) : ρ (c • f) = ρ f
  /-- `ρ(f + g) ≤ max (ρ f) (ρ g)`. -/
  map_add_le_max (f g : R) : ρ (f + g) ≤ max (ρ f) (ρ g)
  /-- If `ρ(f) ≠ ρ(g)`, then `ρ(f + g) = max (ρ f) (ρ g)`. -/
  map_add_eq_max_of_ne (f g : R) (h : ρ f ≠ ρ g) : ρ (f + g) = max (ρ f) (ρ g)
  /-- If `ρ(f) = ρ(g) ≠ ⊥`, then there exists `c ≠ 0` such that `ρ(f + c • g) < ρ(f)`. -/
  exists_smul_reduce (f g : R) (h_eq : ρ f = ρ g) (h_ne_bot : ρ f ≠ ⊥) :
    ∃ c : F, c ≠ 0 ∧ ρ (f + c • g) < ρ f
  /-- `ρ(f * g) = ρ(f) + ρ(g)` (additive over multiplication). -/
  map_mul (f g : R) : ρ (f * g) = ρ f + ρ g

/-- An **order domain** is a pair `(R, ρ)` consisting of an `F`-algebra `R`
and an order function `ρ` on `R`.

This bundles the ring and its order function into a single structure,
as introduced in Cox–Little–O'Shea, Chapter 10, §1, Exercise 1(b). -/
structure OrderDomain (F : Type u) (Γ : Type w)
    [Field F] [AddCommMonoid Γ] [LinearOrder Γ] [IsOrderedAddMonoid Γ] where
  /-- The underlying `F`-algebra. -/
  R : Type v
  /-- The `F`-algebra structure on `R`. -/
  [str : CommRing R]
  /-- The `F`-algebra instance. -/
  [alg : Algebra F R]
  /-- The order function on `R`. -/
  ρ : OrderFunction F R Γ

attribute [instance] OrderDomain.str OrderDomain.alg

namespace OrderFunction

variable (ρ : OrderFunction F R Γ)

/-- `ρ(f) = ⊥` if and only if `f = 0`. -/
theorem map_eq_bot_iff (f : R) : ρ.ρ f = ⊥ ↔ f = 0 := by
  sorry
