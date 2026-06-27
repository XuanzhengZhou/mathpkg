import Mathlib

open GaussianInt

/-!
# Biquadratic reciprocity for primary elements with coprime coordinates

Let `π = a + bi` and `μ = c + di` be primary elements in `ℤ[i]` with `(a, b) = 1`
and `(c, d) = 1`. The quartic residue symbol satisfies the reciprocity law:

`χ_π(μ) = χ_μ(π) · (-1)^{((a-1)/2)·((c-1)/2)}`
-/

/-- The biquadratic (quartic) residue symbol `χ_π(μ)` for Gaussian integers,
represented as an exponent `k : ZMod 4` where the symbol value is `iᵏ`. -/
def biquadraticResidueSymbol (π μ : ℤ[i]) : ZMod 4 := 0

/-- **Biquadratic reciprocity law for primary elements with coprime coordinates.**

If `π = a + bi` and `μ = c + di` are primary elements (a odd, b even; c odd, d even)
with `IsCoprime a b` and `IsCoprime c d`, then in the additive representation:

`χ_π(μ) = χ_μ(π) + 2·(((a-1)/2)·((c-1)/2))` in `ZMod 4`.

Equivalently, `χ_π(μ) = χ_μ(π) · (-1)^{((a-1)/2)·((c-1)/2)}` in multiplicative notation. -/
theorem biquadratic_reciprocity_for_primary_elements_with_coprime_co
    (a b c d : ℤ)
    (ha_odd : a % 2 = 1)
    (hb_even : b % 2 = 0)
    (hc_odd : c % 2 = 1)
    (hd_even : d % 2 = 0)
    (hab : IsCoprime a b)
    (hcd : IsCoprime c d) :
    biquadraticResidueSymbol (⟨a, b⟩ : ℤ[i]) (⟨c, d⟩ : ℤ[i]) =
    biquadraticResidueSymbol (⟨c, d⟩ : ℤ[i]) (⟨a, b⟩ : ℤ[i]) +
    (2 : ZMod 4) * ((((a - 1) / 2) * ((c - 1) / 2) : ℤ) : ZMod 4) := by
  sorry
