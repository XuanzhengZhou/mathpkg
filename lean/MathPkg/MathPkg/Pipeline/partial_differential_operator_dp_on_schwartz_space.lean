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
def basisVec (j : Fin n) : Fin n → ℝ :=
  Pi.single j 1

/-- The partial differential operator `D^P` on Schwartz space as a continuous linear map.

For a multi-index `P : Fin n → ℕ`, the operator `D^P` differentiates `P j` times with
respect to `xⱼ` for each coordinate `j`. Since all directional derivative operators
commute on smooth functions, the order of composition does not matter.

This is defined as the composition over all coordinates `j` of `(∂_{eⱼ})^(P j)`, where
`∂_{eⱼ}` is the directional derivative along the `j`-th standard basis vector and
`(·)^k` denotes the `k`-fold iteration (functional power) of the operator.

The `Monoid` instance for `ContinuousLinearMap` endomorphisms uses composition `∘` as
multiplication, so `Finset.prod` over all `j` composes the iterated derivative operators. -/
def dpOperatorCLM (P : Fin n → ℕ) : 𝓢(Fin n → ℝ, F) →L[ℝ] 𝓢(Fin n → ℝ, F) :=
  (Finset.univ : Finset (Fin n)).prod
    (fun j => (LineDeriv.lineDerivOpCLM ℝ 𝓢(Fin n → ℝ, F) (basisVec j)) ^ P j)

/-- The partial differential operator `D^P` on Schwartz space (unbundled version).

`D^P f` differentiates `f` according to the multi-index `P`. -/
def dpOperator (P : Fin n → ℕ) (f : 𝓢(Fin n → ℝ, F)) : 𝓢(Fin n → ℝ, F) :=
  dpOperatorCLM P f

end SchwartzMap

variable (n : ℕ) (F : Type v) [NormedAddCommGroup F] [NormedSpace ℝ F]

/-- Notation `D[P]` for the multi-index partial differential operator on Schwartz space. -/
scoped notation "D[" P "]" => SchwartzMap.dpOperator P

/-- Example: For n=2, `D^{(1,0)} = ∂/∂x₁`.
Applying it to a Schwartz function `f` gives the directional derivative along `e₀`. -/
example {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F] (f : 𝓢(Fin 2 → ℝ, F)) :
    let P : Fin 2 → ℕ := fun i => match i with | 0 => 1 | 1 => 0
    SchwartzMap.dpOperator P f = (LineDeriv.lineDerivOpCLM ℝ 𝓢(Fin 2 → ℝ, F)
      (SchwartzMap.basisVec 0)) f := by
  intro P
  simp [SchwartzMap.dpOperator, SchwartzMap.dpOperatorCLM, SchwartzMap.basisVec]

/-- Example: For n=2 and P = (2, 1), D^P = ∂³/(∂x₁² ∂x₂).
This is the composition `∂_{e₀} ∘ ∂_{e₀} ∘ ∂_{e₁}`. -/
example {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F] (f : 𝓢(Fin 2 → ℝ, F)) :
    let P : Fin 2 → ℕ := fun i => match i with | 0 => 2 | 1 => 1
    SchwartzMap.dpOperator P f =
      (LineDeriv.lineDerivOpCLM ℝ 𝓢(Fin 2 → ℝ, F) (SchwartzMap.basisVec 0)) (
      (LineDeriv.lineDerivOpCLM ℝ 𝓢(Fin 2 → ℝ, F) (SchwartzMap.basisVec 0)) (
      (LineDeriv.lineDerivOpCLM ℝ 𝓢(Fin 2 → ℝ, F) (SchwartzMap.basisVec 1)) f)) := by
  intro P
  simp [SchwartzMap.dpOperator, SchwartzMap.dpOperatorCLM, SchwartzMap.basisVec]

/-- Example: For P = (0, …, 0), D^P is the identity operator (no differentiation). -/
example {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F] (f : 𝓢(Fin 3 → ℝ, F)) :
    let P : Fin 3 → ℕ := fun _ => 0
    SchwartzMap.dpOperator P f = f := by
  intro P
  simp [SchwartzMap.dpOperator, SchwartzMap.dpOperatorCLM]
