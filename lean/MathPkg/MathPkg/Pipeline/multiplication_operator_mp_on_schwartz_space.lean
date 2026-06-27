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
  refine ⟨?_, ?_⟩
  · -- ContDiff ℝ ∞ (coordFun j): linear functions are smooth
    exact contDiff_id.proj j
  · -- ∀ N, ∃ k C, ∀ x, ‖iteratedFDeriv ℝ N (coordFun j) x‖ ≤ C * (1 + ‖x‖) ^ k
    intro N
    refine ⟨1, ‖(1 : (Fin n → ℝ) →L[ℝ] ℝ)‖, fun x ↦ ?_⟩
    -- For N = 0: |xⱼ| ≤ ‖x‖ ≤ 1 + ‖x‖
    -- For N = 1: the derivative is a constant projection, norm bounded by ‖projⱼ‖
    -- For N ≥ 2: derivative is zero
    by_cases hN0 : N = 0
    · subst hN0
      simp [coordFun]
      calc
        ‖x j‖ ≤ ‖x‖ := Pi.norm_le_norm' x j
        _ ≤ 1 * (1 + ‖x‖) ^ (1 : ℕ) := by
          simp; nlinarith [norm_nonneg x]
    · by_cases hN1 : N = 1
      · subst hN1
        -- First derivative: iteratedFDeriv 1 of coordFun is constant = the projection
        simp [coordFun, iteratedFDeriv_succ_apply_right, iteratedFDeriv_zero_apply,
          fderiv_proj]
      · -- For N ≥ 2, the iterated derivative is zero (linear function)
        have hN2 : 2 ≤ N := by omega
        have hzero : iteratedFDeriv ℝ N (coordFun j) = 0 := by
          apply iteratedFDeriv_eq_zero_of_contDiffOn
          · exact contDiff_id.proj j
          · exact le_of_lt (by omega)
        simp [hzero]

/-- The multiplication operator `Mⱼ` on Schwartz space: multiplication by the `j`-th coordinate.

`(Mⱼ f)(x) = xⱼ · f(x)`.

This is a continuous linear endomorphism of `𝓢(Fin n → ℝ, F)`. -/
def coordMulOperatorCLM (j : Fin n) : 𝓢(Fin n → ℝ, F) →L[ℝ] 𝓢(Fin n → ℝ, F) :=
  smulLeftCLM F (coordFun j) (coordFun_hasTemperateGrowth j)

/-- The multiplication operator `Mⱼ` on Schwartz space (unbundled version).

`(Mⱼ f)(x) = xⱼ · f(x)`. -/
def coordMulOperator (j : Fin n) (f : 𝓢(Fin n → ℝ, F)) : 𝓢(Fin n → ℝ, F) :=
  coordMulOperatorCLM j f

/-- The multi-index multiplication operator `M^P` on Schwartz space.

For a multi-index `P : Fin n → ℕ`, define
`M^P f(x) = (∏ⱼ xⱼ^{Pⱼ}) · f(x)`.

This is the composition `M₀^{P₀} ∘ … ∘ M_{n-1}^{P_{n-1}}` of the single-variable
multiplication operators, each applied `Pⱼ` times.

This is a continuous linear endomorphism of `𝓢(Fin n → ℝ, F)`. -/
def coordMulMultiIndexCLM (P : Fin n → ℕ) : 𝓢(Fin n → ℝ, F) →L[ℝ] 𝓢(Fin n → ℝ, F) :=
  -- We apply Mⱼ Pⱼ times for each coordinate j, and compose them all
  -- Since smulLeftCLM for coordinate functions commute, the order doesn't matter.
  (Finset.univ : Finset (Fin n)).val.toList.prod
    (fun j ↦ coordMulOperatorCLM j ^ P j)

/-- The multi-index multiplication operator `M^P` on Schwartz space (unbundled version).

`M^P f(x) = (∏ⱼ xⱼ^{Pⱼ}) · f(x)`. -/
def coordMulMultiIndex (P : Fin n → ℕ) (f : 𝓢(Fin n → ℝ, F)) : 𝓢(Fin n → ℝ, F) :=
  coordMulMultiIndexCLM P f

end SchwartzMap

variable (n : ℕ) (F : Type v) [NormedAddCommGroup F] [NormedSpace ℝ F]

/-- Notation `M[P]` for the multi-index multiplication operator on Schwartz space. -/
scoped notation "M[" P "]" => SchwartzMap.coordMulMultiIndex P

/-- Notation `Mⱼ` for the single-variable multiplication operator on Schwartz space. -/
scoped notation "M[" j "]_coeff" => SchwartzMap.coordMulOperator j

/-- Example: For n=2, M₁ is multiplication by x₁ (the first coordinate).

`(M₁ f)(x₁, x₂) = x₁ · f(x₁, x₂)` -/
example {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F] (f : 𝓢(Fin 2 → ℝ, F)) (x : Fin 2 → ℝ) :
    (SchwartzMap.coordMulOperator 0 f) x = x 0 • f x := by
  simp [SchwartzMap.coordMulOperator, SchwartzMap.coordMulOperatorCLM,
    SchwartzMap.coordFun, smulLeftCLM_apply_apply]

/-- Example: For n=2 and P = (2, 1), M^P f(x₁, x₂) = x₁² · x₂ · f(x₁, x₂) -/
example {F : Type v} [NormedAddCommGroup F] [NormedSpace ℝ F] (f : 𝓢(Fin 2 → ℝ, F)) (x : Fin 2 → ℝ) :
    let P : Fin 2 → ℕ := fun i ↦ match i with | 0 => 2 | 1 => 1
    (SchwartzMap.coordMulMultiIndex P f) x = (x 0 ^ 2) * (x 1) • f x := by
  intro P
  sorry
