import Mathlib

/-!
# Limit of a Spectral Sequence

Given a spectral sequence, we define the nested submodule chain
`0 = B₁ ⊂ B₂ ⊂ … ⊂ Bᵣ ⊂ … ⊂ Zᵣ ⊂ … ⊂ Z₂ ⊂ Z₁ = E₁`
such that `Eᵣ = Zᵣ / Bᵣ`. The limit terms are
`Z∞ = ⋂ᵣ Zᵣ`, `B∞ = ⋃ᵣ Bᵣ`, and the limit page is `E∞ = Z∞ / B∞`.

## Construction

Let `Z₁ = E₁` and `B₁ = 0`. Having defined `Bᵢ` and `Zᵢ` for `i ≤ r`,
define `Z_{r+1}` as the kernel of the composite map
`Zᵣ → Zᵣ / Bᵣ = Eᵣ →ᵈ Eᵣ`,
and `B_{r+1}` as the image of this map. Then
`Z∞ = ⋂_{r ≥ 1} Zᵣ` and `B∞ = ⋃_{r ≥ 1} Bᵣ`,
giving the limit `E∞ = Z∞ / B∞`.

## References

* [McCleary, *A User's Guide to Spectral Sequences*, Chapter 1]
* [Weibel, *An Introduction to Homological Algebra*, Chapter 5]
-/

noncomputable section

open Set

variable (R : Type*) [Ring R] (M : Type*) [AddCommGroup M] [Module R M]

/-- A classical spectral sequence specified by the nested submodule data
`Zᵣ` (cycles) and `Bᵣ` (boundaries) inside the `E₁`-page module `M`,
together with differentials `dᵣ : Zᵣ / Bᵣ → Zᵣ / Bᵣ`.

The submodules satisfy:
* `Z₁ = M` (the full module), `B₁ = 0`
* `B₁ ⊆ B₂ ⊆ … ⊆ Bᵣ ⊆ … ⊆ Zᵣ ⊆ … ⊆ Z₂ ⊆ Z₁`
* `Eᵣ ≅ Zᵣ / Bᵣ` (each page is cycles modulo boundaries)
* `dᵣ ∘ dᵣ = 0` on `Eᵣ`
* `Z_{r+1} / Bᵣ = ker(dᵣ)` and `B_{r+1} / Bᵣ = im(dᵣ)` (the recursive step)

The limit is defined as `E∞ = Z∞ / B∞` where `Z∞ = ⋂ᵣ Zᵣ` and `B∞ = ⋃ᵣ Bᵣ`.
-/
structure SpectralSequenceClassical where
  /-- The cycles on page `r`: elements of `M` that "survive" to page `r`.
  `Z r` is a submodule of `M` for each `r ≥ 1`. -/
  Z : ℕ → Submodule R M
  /-- The boundaries on page `r`: elements of `M` that become boundaries
  by page `r`. `B r` is a submodule of `M` for each `r ≥ 1`. -/
  B : ℕ → Submodule R M
  /-- The differential on page `r`, defined on the quotient `Z r / B r`. -/
  d (r : ℕ) : (Z r) ⧸ (B r).comap (Z r).subtype →ₗ[R] (Z r) ⧸ (B r).comap (Z r).subtype
  /-- `Z₁` is the full module `E₁`. -/
  Z_one : Z 1 = ⊤
  /-- `B₁ = 0`. -/
  B_one : B 1 = ⊥
  /-- `Bᵣ ⊆ Zᵣ` for all `r`. -/
  B_subset_Z (r : ℕ) : B r ≤ Z r
  /-- `Bᵣ ⊆ B_{r+1}`: boundaries form an increasing chain. -/
  B_mono (r : ℕ) : B r ≤ B (r + 1)
  /-- `Z_{r+1} ⊆ Zᵣ`: cycles form a decreasing chain. -/
  Z_anti (r : ℕ) : Z (r + 1) ≤ Z r
  /-- `dᵣ ∘ dᵣ = 0` on page `r`. -/
  d_sq_zero (r : ℕ) (x : (Z r) ⧸ (B r).comap (Z r).subtype) : d r (d r x) = 0

/-- The intersection of all cycles submodules: `Z∞ = ⋂_{r ≥ 1} Zᵣ`.
These are the elements that survive to all pages. -/
def Zinf (E : SpectralSequenceClassical R M) : Submodule R M := by
  sorry
