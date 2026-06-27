import Mathlib

/-!
# Multiplication Operator M^P on Schwartz Space

Let `S(ℝⁿ)` denote the Schwartz space of rapidly decreasing smooth functions on `ℝⁿ`.

For `j = 1,…,n`, the operator `Mⱼ` is multiplication by the `j`-th variable:
`(Mⱼ f)(x) = xⱼ · f(x)`.

For a multi-index `P = (p₁, …, pₙ)` where each `pᵢ ∈ ℕ`, the operator `M^P` is defined by
`M^P f(x) = x₁^{p₁} · … · xₙ^{pₙ} · f(x)`.

Both `Mⱼ` and `M^P` map the Schwartz space `𝓢(ℝⁿ, F)` continuously into itself.

We use `Fin n → ℝ` to model `ℝⁿ`, and `𝓢(Fin n → ℝ, F)` for the Schwartz space.

## Main definitions

* `coordMulOperatorCLM` : the operator `Mⱼ` as a continuous linear map on Schwartz space
* `coordMulMultiIndexCLM` : the operator `M^P` as a continuous linear map on Schwartz space
* `coordMulOperator` : the operator `Mⱼ` as a function on Schwartz space (without bundling continuity)
* `coordMulMultiIndex` : the operator `M^P` as a function on Schwartz space (without bundling continuity)

## Implementation notes

Mathlib4 already provides `SchwartzMap.smulLeftCLM` which multiplies a Schwartz function by any
scalar-valued function of temperate growth. The coordinate projection `x ↦ xⱼ` is a polynomial
and hence has temperate growth. We use this to define our operators.
-/

open scoped SchwartzMap

noncomputable section

universe v

variable {n : ℕ} {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F]

namespace SchwartzMap

/-- The `j`-th coordinate function `x ↦ xⱼ` from `Fin n → ℝ` to `ℝ`.

This function has temperate growth (it is a polynomial, hence smooth with all derivatives
polynomially bounded), so it can be used with `smulLeftCLM` to multiply Schwartz functions. -/
def coordFun (j : Fin n) : (Fin n → ℝ) → ℝ := fun x ↦ x j

/-- The `j`-th coordinate function has temperate growth.

This is a fundamental fact: linear functions are smooth and their derivatives are bounded. -/
@[fun_prop]
lemma coordFun_hasTemperateGrowth (j : Fin n) : (coordFun j).HasTemperateGrowth := by
  sorry
