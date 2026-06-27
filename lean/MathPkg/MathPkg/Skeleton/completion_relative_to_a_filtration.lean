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
lemma antitone : Antitone F.a := by
  sorry
