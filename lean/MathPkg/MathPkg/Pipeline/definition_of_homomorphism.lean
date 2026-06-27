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
    [MulDistribMulAction Ω G] [MulDistribMulAction Ω H] :=
  G →*[Ω] H

namespace OmegaHom

variable {Ω G H : Type*} [Monoid Ω] [Monoid G] [Monoid H]
  [MulDistribMulAction Ω G] [MulDistribMulAction Ω H]

/-- An Ω-homomorphism preserves the operation: `f (g * h) = f g * f h`. -/
theorem map_mul (f : OmegaHom Ω G H) (g h : G) : f (g * h) = f g * f h :=
  f.map_mul' g h

/-- An Ω-homomorphism preserves the identity: `f 1 = 1`. -/
theorem map_one (f : OmegaHom Ω G H) : f 1 = 1 :=
  f.map_one'

/-- An Ω-homomorphism commutes with the Ω-action: `f (ω • g) = ω • f g`. -/
theorem map_smul (f : OmegaHom Ω G H) (ω : Ω) (g : G) : f (ω • g) = ω • f g :=
  f.map_smul' ω g

end OmegaHom

/-! ## Examples -/

/-- Example: the identity homomorphism is an Ω-homomorphism
for any Ω-group `G`. -/
example (Ω G : Type*) [Monoid Ω] [Monoid G] [MulDistribMulAction Ω G] : OmegaHom Ω G G where
  toFun := id
  map_one' := rfl
  map_mul' := fun _ _ => rfl
  map_smul' := fun _ _ => rfl

/-- Example: the identity map is a `ConjAct G`-homomorphism.
`ConjAct G` acts on `G` by conjugation (`g • h := g * h * g⁻¹`),
and the identity trivially commutes with this action. -/
example (G : Type*) [Group G] : OmegaHom (ConjAct G) G G where
  toFun := id
  map_one' := rfl
  map_mul' := fun _ _ => rfl
  map_smul' := fun _ _ => rfl
