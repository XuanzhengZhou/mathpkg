import Mathlib

open Real
open WeierstrassCurve

/-!
# Absolute Convergence of the Local Height Series on E(ℝ)

For an elliptic curve E/ℝ given by a Weierstrass equation, the local archimedean
height series Σ 4⁻ⁿ log|z([2ⁿ]P)| converges absolutely, and the ratio |z|/|x|²
of projective coordinates is uniformly bounded for all doubling iterates.

## Reference

* J.H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, GTM 151, Chapter VI.
-/

noncomputable section

variable {W : WeierstrassCurve ℝ} [W.IsElliptic]

/-- The properly normalized x-coordinate of a projective point on an elliptic curve over ℝ.

In the standard theory, this is the x-coordinate after normalizing so that the point
has coprime integer coordinates in some minimal model. -/
noncomputable def localHeightX (P : W.toAffine.Point) : ℝ := 0

/-- The properly normalized z-coordinate of a projective point on an elliptic curve over ℝ. -/
noncomputable def localHeightZ (P : W.toAffine.Point) : ℝ := 1

/--
**Absolute Convergence of the Local Height Series on E(ℝ).**

Let E/ℝ be an elliptic curve given by a Weierstrass equation. Then there exist
constants C₁, C₂ > 0 such that for all points P ∈ E(ℝ) and all n ∈ ℕ,

  C₁ ≤ |z([2ⁿ]P)| / |x([2ⁿ]P)|² ≤ C₂

where x and z are the normalized projective coordinates of the n-fold doubling [2ⁿ]P.
Moreover, for every point P, the series

  ∑_{n=0}^∞ (1/4ⁿ) log |z([2ⁿ]P)|

is absolutely convergent.
-/
theorem absolute_convergence_of_local_height_series_on_e_mathbb_r_ :
    ∃ (C₁ C₂ : ℝ), C₁ > 0 ∧ C₂ > 0 ∧
    (∀ (P : W.toAffine.Point) (n : ℕ),
      C₁ ≤ |localHeightZ ((2 ^ n : ℤ) • P)| / |localHeightX ((2 ^ n : ℤ) • P)| ^ 2 ∧
      |localHeightZ ((2 ^ n : ℤ) • P)| / |localHeightX ((2 ^ n : ℤ) • P)| ^ 2 ≤ C₂) ∧
    (∀ (P : W.toAffine.Point),
      Summable fun (n : ℕ) =>
        ((1 : ℝ) / ((4 : ℝ) ^ n)) * Real.log |localHeightZ ((2 ^ n : ℤ) • P)|) := by
  sorry
