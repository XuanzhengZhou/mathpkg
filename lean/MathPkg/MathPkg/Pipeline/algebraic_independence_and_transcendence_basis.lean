import Mathlib

/-!
# Algebraic Independence and Transcendence Basis

A subset `B` of a field extension `K/k` is **algebraically independent** over `k` if the
canonical map from the polynomial ring `k[{X_b}_{b∈B}]` to `k(B)` sending `X_b ↦ b` is injective.
Equivalently, for any distinct `b₁,…,bₙ ∈ B` and any nonzero polynomial `f ∈ k[t₁,…,tₙ]`,
we have `f(b₁,…,bₙ) ≠ 0`.

A subset `B` is a **transcendence basis** for `K` over `k` if it is a maximal algebraically
independent subset — i.e., `B` is algebraically independent and `K` is algebraic over `k(B)`.

Mathlib4 provides both definitions in `Mathlib.RingTheory.AlgebraicIndependent.Defs`:

* `AlgebraicIndependent R x` — the family `x : ι → A` is algebraically independent over `R`,
  meaning that the canonical `aeval` map `MvPolynomial ι R →ₐ[R] A` is injective.

* `IsTranscendenceBasis R x` — the family `x` is a transcendence basis over `R`, defined as
  `AlgebraicIndependent R x ∧` maximality: any algebraically independent superset of `range x`
  must equal `range x`.

## References

* [Stacks: 030D Transcendence](https://stacks.math.columbia.edu/tag/030D)
* [Stacks: 030E Algebraically independent](https://stacks.math.columbia.edu/tag/030E)
-/

open AlgebraicIndependent

/-!
## Convenience abbreviations

These abbreviations point to the canonical Mathlib4 definitions, providing convenient access
with the same names used in the textbook context.
-/

/--
`algebraicIndependent R x` states that the family `x : ι → A` is algebraically independent
over the commutative ring `R`. This means the `aeval` homomorphism from the multivariable
polynomial ring `MvPolynomial ι R` to `A` is injective.

For a field extension `K/k`, a subset `B` is algebraically independent over `k` iff the
subfield `k(B)` is isomorphic to the rational function field `k({X_b}_{b∈B})` via the map
sending `X_b ↦ b`.
-/
abbrev algebraicIndependent {ι R A : Type*} (x : ι → A)
    [CommRing R] [CommRing A] [Algebra R A] : Prop :=
  AlgebraicIndependent R x

/--
`isTranscendenceBasis R x` states that the family `x : ι → A` is a transcendence basis over `R`.

This means:
1. `AlgebraicIndependent R x` — the family is algebraically independent, and
2. Maximality: any algebraically independent superset of `range x` must equal `range x`.

For field extensions `K/k`, this is equivalent to: `B` is algebraically independent over `k`
and `K` is algebraic over `k(B)`.
-/
abbrev isTranscendenceBasis {ι R A : Type*} (x : ι → A)
    [CommRing R] [CommRing A] [Algebra R A] : Prop :=
  IsTranscendenceBasis R x

/-!
## Examples
-/

-- Example 1: The variables X₀, X₁ in ℚ[X₀, X₁] are algebraically independent over ℚ.
example : algebraicIndependent ℚ (fun (i : Fin 2) =>
  (X i : MvPolynomial (Fin 2) ℚ)) :=
  MvPolynomial.algebraicIndependent_X _ _

-- Example 2: The empty family is always algebraically independent.
example : algebraicIndependent ℚ (fun (_ : Empty) => (0 : ℚ)) := by
  rw [algebraicIndependent_empty_iff]
  exact fun a b => by simp

-- Example 3: A singleton {√2} is NOT algebraically independent over ℚ, because
-- it satisfies the polynomial equation (√2)² - 2 = 0.
example : ¬ algebraicIndependent ℚ (fun (_ : Unit) => (Real.sqrt 2 : ℝ)) := by
  intro h
  have hzero := h.eq_zero_of_aeval_eq_zero
    (MvPolynomial.X () ^ 2 - C (2 : ℚ) : MvPolynomial Unit ℚ)
  -- aeval maps X² - 2 to (√2)² - 2 = 0 in ℝ, but X² - 2 ≠ 0 in ℚ[X]
  sorry

-- Example 4: A transcendence basis exists for any faithful algebra.
example [FaithfulSMul ℚ (MvPolynomial (Fin 1) ℚ)] :
    ∃ (s : Set (MvPolynomial (Fin 1) ℚ)), isTranscendenceBasis ℚ ((↑) : s → _) :=
  exists_isTranscendenceBasis ℚ _
