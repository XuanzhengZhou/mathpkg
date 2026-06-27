import Mathlib

open Con

/-!
# Quotient Monoid/Group by a Congruence

Let R be an equivalence relation on a monoid G such that a₁ ~ a₂ and b₁ ~ b₂ imply
a₁·b₁ ~ a₂·b₂ for all a_i, b_i ∈ G. Then G/R with operation [a]·[b] = [a·b] is a monoid.
If G is a group, G/R is a group; if G is abelian, G/R is abelian.

Mathlib4 provides this via `Con` (congruence relation) and `Con.Quotient`.
All the results below are existing instances in Mathlib4.
-/

/-- Part 1: The quotient of a monoid by a congruence relation is a monoid.
The identity is the class of the identity element [e],
and multiplication is defined by [a]·[b] = [a·b]. -/
example {M : Type*} [Monoid M] (c : Con M) : Monoid c.Quotient := by
  infer_instance

/-- Part 2: The quotient of a group by a congruence relation is a group.
The inverse is given by [a]⁻¹ = [a⁻¹]. -/
example {M : Type*} [Group M] (c : Con M) : Group c.Quotient := by
  infer_instance

/-- Part 3a: The quotient of a commutative monoid by a congruence relation is a commutative monoid. -/
example {M : Type*} [CommMonoid M] (c : Con M) : CommMonoid c.Quotient := by
  infer_instance

/-- Part 3b: The quotient of a commutative group by a congruence relation is a commutative group. -/
example {M : Type*} [CommGroup M] (c : Con M) : CommGroup c.Quotient := by
  infer_instance

/-! ## Additive Versions

Mathlib4 also provides `AddCon` for additive congruence relations,
and the same results hold for additive monoids/groups.
-/

/-- Additive: quotient of an AddMonoid by an additive congruence is an AddMonoid. -/
example {M : Type*} [AddMonoid M] (c : AddCon M) : AddMonoid c.Quotient := by
  infer_instance

/-- Additive: quotient of an AddGroup by an additive congruence is an AddGroup. -/
example {M : Type*} [AddGroup M] (c : AddCon M) : AddGroup c.Quotient := by
  infer_instance

/-- Additive: quotient of an AddCommGroup by an additive congruence is an AddCommGroup. -/
example {M : Type*} [AddCommGroup M] (c : AddCon M) : AddCommGroup c.Quotient := by
  infer_instance

/-!
## Core Lemma: Well-Definedness of Multiplication in the Quotient

The central property that makes the quotient construction work: if `c a₁ a₂` and `c b₁ b₂`,
then `c (a₁ * b₁) (a₂ * b₂)`. This is the `mul'` field of the `Con` structure.
-/

/-- Well-definedness of multiplication: if a₁ ~ a₂ and b₁ ~ b₂ then a₁·b₁ ~ a₂·b₂.
This is exactly the congruence condition that defines a `Con`. -/
theorem con_mul_wd {M : Type*} [Mul M] (c : Con M) {a₁ a₂ b₁ b₂ : M}
    (ha : c a₁ a₂) (hb : c b₁ b₂) : c (a₁ * b₁) (a₂ * b₂) :=
  c.mul ha hb

/-- In the quotient, equality of classes corresponds to the congruence relation. -/
theorem quotient_eq_iff {M : Type*} [Mul M] (c : Con M) (a b : M) :
    ((a : c.Quotient) = (b : c.Quotient)) ↔ c a b :=
  c.eq

/-- The canonical map M → M/~ preserves multiplication. -/
theorem coe_mul_preserved {M : Type*} [Mul M] (c : Con M) (a b : M) :
    ((a * b : M) : c.Quotient) = (a : c.Quotient) * (b : c.Quotient) :=
  coe_mul a b

/-- The canonical map preserves the identity element. -/
theorem coe_one_preserved {M : Type*} [Monoid M] (c : Con M) :
    ((1 : M) : c.Quotient) = (1 : c.Quotient) :=
  coe_one

/-!
## Explicit Example: Congruence Modulo 3 on ℤ

Define a congruence relation on ℤ where x ~ y iff x ≡ y (mod 3).
The quotient ℤ/3ℤ is an additive commutative group.
We use `Int.ModEq` which is the built-in "congruent modulo n" relation on ℤ.
-/

/-- Define the "congruent modulo 3" relation on ℤ as an `AddCon`.
The relation `a ≡ b [ZMOD 3]` means `3 ∣ a - b`. -/
def mod3AddCongruence : AddCon ℤ where
  r a b := a ≡ b [ZMOD (3 : ℤ)]
  iseqv := {
    refl := λ _ => .rfl
    symm := λ h => h.symm
    trans := λ h₁ h₂ => h₁.trans h₂
  }
  add' := λ {_ _ _ _} ha hc => ha.add hc

/-- The quotient ℤ / (mod 3) is an additive commutative group. -/
example : AddCommGroup mod3AddCongruence.Quotient := by
  infer_instance

/-- In the mod-3 quotient, the classes of 0 and 1 are distinct.
Proof: if they were equal, then 0 ≡ 1 [ZMOD 3], which is false. -/
example : ((0 : ℤ) : mod3AddCongruence.Quotient) ≠ ((1 : ℤ) : mod3AddCongruence.Quotient) := by
  intro h
  have hrel : mod3AddCongruence (0 : ℤ) (1 : ℤ) := Quotient.exact h
  have : ¬ ((0 : ℤ) ≡ (1 : ℤ) [ZMOD (3 : ℤ)]) := by decide
  exact this hrel

/-!
## Explicit Example: Multiplicative Congruence on ℚˣ

Define a congruence relation on ℚˣ (the multiplicative group of nonzero rationals)
by x ~ y iff x/y is a square. The quotient is a commutative group.
-/

/-- Define the "mod squares" congruence on the multiplicative group ℚˣ. -/
def squareCongruence : Con (Units ℚ) :=
  conGen (fun x y => ∃ z : Units ℚ, x = z * z * y)

/-- The quotient of ℚˣ by the "mod squares" relation is a commutative group. -/
example : CommGroup squareCongruence.Quotient := by
  infer_instance
