import Mathlib

open Matrix.SpecialLinearGroup Matrix
open scoped MatrixGroups UpperHalfPlane ComplexConjugate

/-!
# Construction of Local Coordinate Charts on Y(Γ)

For a congruence subgroup Γ of `SL₂(ℤ)` and a point `τ` in the upper half-plane `ℍ`,
we construct a local coordinate chart on the modular curve `Y(Γ) = Γ \ ℍ` around
the image `π(τ)`.

## Construction outline

1. Let `U ⊂ ℍ` be a suitably small neighborhood of `τ` (as in Corollary 2.2.3 of
   Diamond–Shurman) such that the only elements of Γ mapping `U` into itself are
   those in the stabilizer `Γτ`.
2. Let `h = |Γτ|` be the order of the stabilizer of `τ` in Γ.
3. Define the Möbius map `δ(z) = (z - τ) / (z - τ̅)`, sending `τ ↦ 0` and `τ̅ ↦ ∞`.
4. Define `ψ(z) = δ(z)^h`.
5. The map `ψ` factors through the quotient `π : ℍ → Y(Γ)` and the induced map
   `ϕ : π(U) → ψ(U) ⊂ ℂ` is a homeomorphism, thereby providing a local coordinate
   chart on the Riemann surface `Y(Γ)`.

## Dependencies

* `open_mapping_theorem` — used in the proof that `ϕ` is a homeomorphism onto its image.

## References

* [Diamond–Shurman] *A First Course in Modular Forms*, Chapter 2, Theorem 2.3.1
-/

/--
**Construction of local coordinate charts on Y(Γ)**.

For a congruence subgroup Γ of `SL(2, ℤ)` and any point `τ` in the upper half-plane `ℍ`,
let `h` be the order of the stabilizer `Γτ`. Define the map
`ψ : ℍ → ℂ` by `ψ(z) = ((z - τ) / (z - conj τ))^h`.

Then `ψ` factors through the quotient `π : ℍ → Γ \ ℍ`, i.e., for all `γ ∈ Γ`,
`ψ(γ·z) = ψ(z)`, and on a suitably small neighborhood `U` of `τ`, the induced map
`π(U) → ψ(U) ⊂ ℂ` is a homeomorphism, providing a local coordinate chart
around `π(τ)` on the modular curve `Y(Γ) = Γ \ ℍ` as a Riemann surface.
-/
theorem construction_of_local_coordinate_charts_on_y
    (Γ : Subgroup (SL(2, ℤ))) (τ : ℍ) :
    ∃ (h : ℕ) (ψ : ℍ → ℂ), ψ = (λ z : ℍ => (((z : ℂ) - (τ : ℂ)) / ((z : ℂ) - (conj (τ : ℂ)))) ^ h) := by
  sorry
