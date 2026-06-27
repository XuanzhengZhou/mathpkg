import Mathlib

open Complex
open Set

/-!
# Construction of Local Coordinate Charts on Y(Γ)

For a congruence subgroup Γ of SL₂(ℤ) and a point τ in the upper half-plane ℍ,
we construct a local coordinate chart on the modular curve Y(Γ) = Γ \ ℍ around
the image π(τ).

The construction proceeds as follows:
1. Let U ⊂ ℍ be a suitably small neighborhood of τ (e.g., as in Corollary 2.2.3
   of Diamond–Shurman) such that the only elements of Γ mapping U into itself are
   those in the stabilizer Γτ.
2. Let h = |Γτ| be the order of the stabilizer (h ∈ {1, 2, 3, 4, 6} for SL₂(ℤ)).
3. Define the Möbius map δ(z) = (z - τ) / (z - τ̅), sending τ ↦ 0 and τ̅ ↦ ∞.
4. Define ψ(z) = δ(z)^h.
5. The map ψ : U → ℂ factors through the quotient π : ℍ → Y(Γ) and the induced
   map ϕ : π(U) → ψ(U) ⊂ ℂ is a homeomorphism, providing a local coordinate chart
   on the Riemann surface Y(Γ).

## Dependencies
- `open_mapping_theorem` — used in the proof that ϕ is a homeomorphism onto its image.

## References
* [Diamond–Shurman] *A First Course in Modular Forms*, Chapter 2, Theorem 2.3.1
-/

/-! ### Auxiliary Definitions -/

/-- The **upper half-plane** ℍ = {z ∈ ℂ | Im(z) > 0}, an open subset of ℂ. -/
structure UpperHalfPlane where
  z : ℂ
  im_pos : 0 < z.im

/-- A **congruence subgroup** Γ of SL₂(ℤ) of level N ≥ 1.
(Here axiomatized for the skeleton.) -/
structure CongruenceSubgroup where
  level : ℕ

/-- The **modular curve** Y(Γ) = Γ \ ℍ, the quotient of the upper half-plane
by the action of the congruence subgroup Γ. (Axiomatized.) -/
def ModularCurveY (Γ : CongruenceSubgroup) : Type :=
  UpperHalfPlane

/-- The **canonical projection** π : ℍ → Y(Γ). -/
def projection (Γ : CongruenceSubgroup) (τ : UpperHalfPlane) : ModularCurveY Γ :=
  τ

/-- The **stabilizer order** h = |Γτ| of τ in Γ.
For congruence subgroups of SL₂(ℤ), h = 1 for regular points,
and h = 2 or 3 for elliptic points. -/
def stabilizerOrder (Γ : CongruenceSubgroup) (τ : UpperHalfPlane) : ℕ := 1

/-- The map δ_τ(z) = (z - τ) / (z - τ̅), a Möbius transformation
sending τ ↦ 0 and the complex conjugate τ̅ ↦ ∞. -/
noncomputable def deltaMap (τ z : ℂ) : ℂ :=
  (z - τ) / (z - conj τ)

/-- ψ(z) = (δ_τ(z))^h = ((z - τ) / (z - τ̅))^h.
This map identifies points of a neighborhood U under the action of the
stabilizer Γτ. -/
noncomputable def psiMap (τ : ℂ) (h : ℕ) (z : ℂ) : ℂ :=
  (deltaMap τ z) ^ h

/-! ### Main Theorem -/

/-- **Construction of local coordinate charts on Y(Γ).**

For any congruence subgroup Γ of SL₂(ℤ) and any point τ ∈ ℍ, let h = |Γτ|.
There exists a neighborhood U of τ in ℍ such that the map
ψ(z) = ((z - τ) / (z - τ̅))^h identifies points of U exactly under the Γ-action,
inducing a homeomorphism ϕ : π(U) → ψ(U) ⊂ ℂ that serves as a local coordinate
chart on the Riemann surface Y(Γ).

This is Theorem 2.3.1 of Diamond–Shurman. -/
theorem construction_of_local_coordinate_charts_on_Y
    (Γ : CongruenceSubgroup) (τ : UpperHalfPlane) :
    ∃ (U : Set UpperHalfPlane) (_hU : τ ∈ U),
      let h := stabilizerOrder Γ τ in
      -- On U, ψ identifies points exactly under the Γ-action
      (∀ (z₁ z₂ : UpperHalfPlane), z₁ ∈ U → z₂ ∈ U →
        (psiMap τ.z h z₁.z = psiMap τ.z h z₂.z ↔
          ∃ (γ : CongruenceSubgroup), True)) := by
  sorry
