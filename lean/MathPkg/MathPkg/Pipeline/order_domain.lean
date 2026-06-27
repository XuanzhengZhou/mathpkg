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
variable {Γ : Type w} [LinearOrderedAddCommMonoid Γ]

/-- An **order function** on an `F`-algebra `R` is a function `ρ : R → WithBot Γ`
satisfying the five axioms of Definition (1.1) in Cox–Little–O'Shea, Chapter 10.

The value `ρ(f) = ⊥` (i.e. `-∞`) means `f = 0`; otherwise `ρ(f)` is an element of `Γ`
that behaves like a "degree" or "leading exponent" under addition and multiplication. -/
structure OrderFunction (F : Type u) (R : Type v) (Γ : Type w)
    [Field F] [CommRing R] [Algebra F R] [LinearOrderedAddCommMonoid Γ] where
  /-- The underlying function `R → WithBot Γ`. -/
  ρ : R → WithBot Γ
  /-- `ρ(0) = ⊥`. -/
  map_zero' : ρ 0 = ⊥
  /-- If `ρ(f) = ⊥` then `f = 0`. -/
  map_eq_bot (f : R) (h : ρ f = ⊥) : f = 0
  /-- `ρ(λ • f) = ρ(f)` for all non-zero scalars `λ`. -/
  map_smul_eq (λ : F) (f : R) (hλ : λ ≠ 0) : ρ (λ • f) = ρ f
  /-- `ρ(f + g) ≤ max (ρ f) (ρ g)`. -/
  map_add_le_max (f g : R) : ρ (f + g) ≤ max (ρ f) (ρ g)
  /-- If `ρ(f) ≠ ρ(g)`, then `ρ(f + g) = max (ρ f) (ρ g)`. -/
  map_add_eq_max_of_ne (f g : R) (h : ρ f ≠ ρ g) : ρ (f + g) = max (ρ f) (ρ g)
  /-- If `ρ(f) = ρ(g) ≠ ⊥`, then there exists `λ ≠ 0` such that `ρ(f + λ • g) < ρ(f)`. -/
  exists_smul_reduce (f g : R) (h_eq : ρ f = ρ g) (h_ne_bot : ρ f ≠ ⊥) :
    ∃ λ : F, λ ≠ 0 ∧ ρ (f + λ • g) < ρ f
  /-- `ρ(f * g) = ρ(f) + ρ(g)` (additive over multiplication). -/
  map_mul (f g : R) : ρ (f * g) = ρ f + ρ g

/-- An **order domain** is a pair `(R, ρ)` consisting of an `F`-algebra `R`
and an order function `ρ` on `R`.

This bundles the ring and its order function into a single structure,
as introduced in Cox–Little–O'Shea, Chapter 10, §1, Exercise 1(b). -/
structure OrderDomain (F : Type u) (Γ : Type w)
    [Field F] [LinearOrderedAddCommMonoid Γ] where
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
theorem map_eq_bot_iff (f : R) : ρ.ρ f = ⊥ ↔ f = 0 :=
  ⟨ρ.map_eq_bot f, fun h => by simpa [h] using ρ.map_zero'⟩

end OrderFunction

/-
## Example

The polynomial ring `F[x₁, …, xₜ]` with `ρ(f) =` exponent vector of the leading monomial
under a monomial order is an order domain with `Γ = ℕᵗ`.

To keep the example self-contained, we demonstrate the simpler case
`R = F[x]` with `ρ(f) = deg(f)` and `Γ = ℕ`.
-/

section PolynomialExample

open Polynomial

variable (F : Type u) [Field F]

/-- For `F[x]`, the standard degree function (with `deg(0) := ⊥`) is an order function
with value monoid `Γ = ℕ`. -/
def polyOrderFunction : OrderFunction F (Polynomial F) ℕ where
  ρ f := if f = 0 then ⊥ else some (natDegree f)
  map_zero' := by simp
  map_eq_bot f h := by
    by_contra hf
    simp [hf] at h
  map_smul_eq λ f hλ := by
    by_cases hf : f = 0
    · simp [hf]
    · simp [hf, natDegree_mul, natDegree_C_mul, hλ]
  map_add_le_max f g := by
    by_cases hf : f = 0
    · simp [hf]
    by_cases hg : g = 0
    · simp [hg]
    by_cases hsum : f + g = 0
    · simp [hsum]
    simp [hf, hg, hsum, natDegree_add_le]
  map_add_eq_max_of_ne f g h := by
    by_cases hf : f = 0
    · simp [hf] at h; simp [hf]
    by_cases hg : g = 0
    · simp [hg] at h; simp [hg]
    by_cases hsum : f + g = 0
    · simp [hsum]
    simp [hf, hg, hsum]
    apply natDegree_add_eq_left_of_natDegree_lt
    -- when degrees differ, the sum has the larger degree
    sorry
  exists_smul_reduce f g h_eq h_ne_bot := by
    by_cases hf : f = 0
    · simp [hf] at h_eq h_ne_bot
      have hg : g = 0 := by
        simpa [hf] using h_eq.symm ▸ (by
          have := ρ.map_eq_bot (OrderFunction.polyOrderFunction F) g ?_
          sorry)
      sorry
    sorry
  map_mul f g := by
    by_cases hf : f = 0
    · simp [hf]
    by_cases hg : g = 0
    · simp [hg]
    simp [hf, hg, natDegree_mul]

-- The example is left incomplete as a proof-of-concept; the key structural definitions
-- (`OrderFunction` and `OrderDomain`) are the main contribution of this file.

end PolynomialExample

/-
## Example: The polynomial ring `F[x₁, …, xₜ]` as an OrderDomain

For `R = F[x₁, …, xₜ]` with a monomial order `≻`, define
`ρ(f) =` the exponent vector of the leading monomial `LM_≻(f)`,
and `ρ(0) = ⊥`.  Then `(R, ρ)` is an order domain with `Γ = ℕᵗ`.

This is Example (1.2) from Cox–Little–O'Shea, Chapter 10.

Usage:
```lean
example (F : Type) [Field F] : OrderDomain F ℕ :=
  { R := Polynomial F
    ρ := polyOrderFunction F }
```
-/
