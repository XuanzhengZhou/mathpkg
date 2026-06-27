import Mathlib

/-!
# Definition of Ω-homomorphism

Let `G` and `H` be Ω-groups (groups equipped with a `MulDistribMulAction Ω G`
and `MulDistribMulAction Ω H` respectively).
An **Ω-homomorphism** is a homomorphism `α : G →* H` such that
`α (ω • g) = ω • α g` for all `g ∈ G` and `ω ∈ Ω`.

Mathlib4 already provides `MulDistribMulActionHom` (notation `G →*[Ω] H`)
for exactly this purpose.  We define `OmegaHom` as a type alias to make the
terminology explicit.
-/

/-- An Ω-homomorphism between Ω-groups `G` and `H` is a monoid homomorphism
that commutes with the Ω-action.  This is exactly
`MulDistribMulActionHom (MonoidHom.id Ω) G H` (notation `G →*[Ω] H`).
Using `abbrev` ensures the `FunLike` and `MulDistribMulActionHomClass` instances
are available. -/
abbrev OmegaHom (Ω G H : Type*) [Monoid Ω] [Monoid G] [Monoid H]
    [MulDistribMulAction Ω G] [MulDistribMulAction Ω H] : Type _ := by
  sorry
