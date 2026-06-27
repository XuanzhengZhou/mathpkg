import Mathlib

open scoped Classical

/-!
# Completion Relative to a Filtration

Let `A : a₁ ⊇ a₂ ⊇ a₃ ⊇ ⋯` be a descending filtration on a commutative ring `R` (i.e., a sequence
of ideals with `a_{i+1} ≤ a_i` for all `i`).

The **completion** `R̂_A` of `R` relative to `A` is the ring of all infinite sequences

    (x₁ + a₁, x₂ + a₂, …, xᵢ + aᵢ, …)

with `xᵢ ∈ R`, subject to the compatibility condition

    xᵢ + aᵢ = xⱼ + aᵢ   whenever   j ≥ i

(equivalently, `xⱼ` maps to `xᵢ + aᵢ` under the natural projection `R/aⱼ → R/aᵢ`).

`R̂_A` is a subring of `∏ᵢ R/aᵢ`.

## Mathlib4 Context

Mathlib4 provides `AdicCompletion` in `RingTheory/AdicCompletion/Basic.lean` for the `I`-adic
filtration `Iⁿ` (i.e. powers of a single ideal). This file defines the more general notion of a
completion with respect to an arbitrary descending filtration of ideals.

See `RingTheory/Filtration.lean` for `Ideal.Filtration` which additionally requires
`I • N i ≤ N (i + 1)` (the `I`-adic condition). Here we only require nested, decreasing ideals.
-/

universe u

variable {R : Type u} [CommRing R]

/-- A **ring filtration** on a commutative ring `R` is a descending sequence of ideals
`a₁ ⊇ a₂ ⊇ a₃ ⊇ ⋯`, i.e., `a_{i+1} ≤ a_i` for all `i`.

This is more general than `Ideal.Filtration` in Mathlib4 (which requires an `I`-adic condition
`I • N i ≤ N (i + 1)`) — here we only require the ideals to be nested and decreasing.

The indices are 0-indexed for convenience, corresponding to `a₁, a₂, …` in the original text. -/
@[ext]
structure RingFiltration (R : Type u) [CommRing R] where
  /-- The `i`-th ideal in the filtration. Index `0` corresponds to `a₁` in the text. -/
  a : ℕ → Ideal R
  /-- The filtration is descending: `a_{i+1} ≤ a_i`. -/
  mono' : ∀ i, a (i + 1) ≤ a i

namespace RingFiltration

variable (F : RingFiltration R)

/-- The filtration is antitone: `F.a j ≤ F.a i` whenever `i ≤ j`. -/
lemma antitone : Antitone F.a :=
  antitone_nat_of_succ_le F.mono'

/-- The natural transition homomorphism `R / aⱼ → R / aᵢ` induced by the inclusion `aⱼ ≤ aᵢ`
when `i ≤ j`. -/
def transitionMap {i j : ℕ} (hij : i ≤ j) : R ⧸ F.a j →+* R ⧸ F.a i :=
  Ideal.Quotient.factor (F.antitone hij)

/-- The **completion** `R̂_A` of `R` relative to the filtration `F`.

An element of the completion is a compatible family `(fᵢ)ᵢ` with `fᵢ ∈ R / aᵢ` such that
whenever `i ≤ j`, the natural transition map `R / aⱼ → R / aᵢ` sends `fⱼ` to `fᵢ`.

Equivalently, this is the projective limit `lim_{i} R / aᵢ`.

This is a subring of `∏ᵢ R / aᵢ` via the natural inclusion. -/
def Completion : Type u :=
  { f : ∀ n : ℕ, R ⧸ F.a n //
    ∀ ⦃i j : ℕ⦄ (hij : i ≤ j), F.transitionMap hij (f j) = f i }

instance : CoeSort (RingFiltration R) (Type u) :=
  ⟨Completion⟩

namespace Completion

/-- The natural projection from the completion onto the `n`-th component. -/
def eval (n : ℕ) (x : F.Completion) : R ⧸ F.a n :=
  x.val n

/-- The canonical map of `x ∈ R` into the completion, sending `x` to the constant
sequence `(x + a₁, x + a₂, …)`. -/
def of (x : R) : F.Completion :=
  ⟨fun n => Ideal.Quotient.mk (F.a n) x, by
    intro i j hij
    simp [transitionMap, Ideal.Quotient.factor_mk]⟩

end Completion

end RingFiltration

/-- An `I`-adic filtration: `aₙ = Iⁿ` gives a `RingFiltration`. -/
def Ideal.ringFiltration {R : Type u} [CommRing R] (I : Ideal R) : RingFiltration R where
  a n := I ^ n
  mono' n := Ideal.pow_le_pow_right (by omega)

/-- Example: The `I`-adic filtration for `I = (2)` in `ℤ` gives the `2`-adic filtration. -/
example : RingFiltration ℤ :=
  Ideal.ringFiltration (Ideal.span {(2 : ℤ)})

/-- Example: The trivial filtration `aᵢ = ⊥` for all `i`. The completion is `R` itself
(via the diagonal embedding). -/
example (R : Type u) [CommRing R] : RingFiltration R where
  a _ := ⊥
  mono' _ := le_rfl

/-- Example: An element of the `2`-adic completion of `ℤ` given by the constant sequence
`(3 mod 2, 3 mod 4, 3 mod 8, …)`. -/
example : ((Ideal.ringFiltration (Ideal.span {(2 : ℤ)})).Completion : Type) :=
  RingFiltration.Completion.of (Ideal.ringFiltration (Ideal.span {(2 : ℤ)})) 3
