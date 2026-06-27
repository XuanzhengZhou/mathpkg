import Mathlib

/-!
# Partial Differential Operator D^P on Schwartz Space

Let `𝓢(ℝⁿ, F)` denote the Schwartz space of rapidly decreasing smooth functions on `ℝⁿ`
(where `ℝⁿ` is modeled as `Fin n → ℝ`).

For a multi-index `P = (p₁, …, pₙ)` of non-negative integers (`P : Fin n → ℕ`), the partial
differential operator `D^P` is defined as

  `D^P = ∂^{|P|} / (∂x₁^{p₁} ⋯ ∂xₙ^{pₙ})`

where `|P| = p₁ + … + pₙ`. In other words, `D^P` differentiates `p₁` times with respect to
`x₁`, `p₂` times with respect to `x₂`, etc.

The operator `D^P` maps the Schwartz space `𝓢(Fin n → ℝ, F)` continuously into itself.

## Mathlib4 background

Mathlib4 uses Fréchet derivatives and directional (line) derivatives instead of partial
derivatives. The Schwartz space `𝓢(E, F)` has a `LineDeriv E 𝓢(E, F) 𝓢(E, F)` instance,
so `∂_{v} f` (the directional derivative along `v`) maps Schwartz functions to Schwartz
functions. The iterated version `∂^{m}` (with `m : Fin k → E`) is also available as a
continuous linear map via `LineDeriv.iteratedLineDerivOpCLM`.

We model the partial derivative `∂/∂xⱼ` as the directional derivative along the `j`-th
standard basis vector `eⱼ`, and then define `D^P` as the iterated composition of these
operators.

## Main definitions

* `basisVec` : the `j`-th standard basis vector in `Fin n → ℝ`
* `dpOperatorCLM` : `D^P` as a continuous linear endomorphism of Schwartz space
* `dpOperator` : `D^P` as an unbundled function on Schwartz space
-/

open scoped SchwartzMap

noncomputable section

universe v

variable {n : ℕ} {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F]

namespace SchwartzMap

/-- The `j`-th standard basis vector in `Fin n → ℝ`:
`(eⱼ)ᵢ = 1` if `i = j`, and `0` otherwise. -/
def basisVec (j : Fin n) : Fin n → ℝ := by
  sorry
