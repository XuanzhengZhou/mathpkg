import Mathlib

open Subgroup

/--
An Ω-group is a group `G` together with a monoid `Ω` acting by endomorphisms.
In Mathlib4, this is captured by `MulDistribMulAction Ω G`, which ensures:
  `ω • (g₁ * g₂) = (ω • g₁) * (ω • g₂)` and `ω • 1 = 1` for all `ω : Ω`, `g₁ g₂ : G`.

We introduce this as a type alias for convenience.
-/
def OmegaGroup (Ω G : Type*) [Monoid Ω] [Group G] [MulDistribMulAction Ω G] : Type _ := G

namespace OmegaGroup

variable (Ω G : Type*) [Monoid Ω] [Group G] [MulDistribMulAction Ω G]

/-- An Ω-subgroup of an Ω-group `G` is a subgroup `H` that is Ω-admissible,
  i.e., `ω • h ∈ H` for every `h ∈ H` and `ω ∈ Ω`. -/
def IsOmegaSubgroup (H : Subgroup G) : Prop :=
  ∀ (h : G), h ∈ H → ∀ (ω : Ω), ω • h ∈ H

/-- The trivial subgroup `{1}` is always an Ω-subgroup, since `ω • 1 = 1` for all `ω`. -/
example : IsOmegaSubgroup Ω G (⊥ : Subgroup G) := by
  intro h hh ω
  have h_one : h = 1 := by
    simpa [mem_bot] using hh
  subst h_one
  have h_smul_one : ω • (1 : G) = 1 := smul_one ω
  rw [h_smul_one]
  exact one_mem _

/-- The whole group `G` is always an Ω-subgroup of itself. -/
example : IsOmegaSubgroup Ω G (⊤ : Subgroup G) := by
  intro h hh ω
  exact Subgroup.mem_top (ω • h)

/-- If `H` and `K` are Ω-subgroups, then their intersection `H ⊓ K` is an Ω-subgroup. -/
example {H K : Subgroup G} (hH : IsOmegaSubgroup Ω G H) (hK : IsOmegaSubgroup Ω G K) :
    IsOmegaSubgroup Ω G (H ⊓ K) := by
  intro h hh ω
  have hmemH : h ∈ H := hh.1
  have hmemK : h ∈ K := hh.2
  have hH' : ω • h ∈ H := hH h hmemH ω
  have hK' : ω • h ∈ K := hK h hmemK ω
  exact ⟨hH', hK'⟩

/-- The center of `G` is an Ω-subgroup whenever the action of Ω commutes with the group action
(in other words, each `ω` acts as a group automorphism).
In general without additional assumptions, the center may not be Ω-admissible.
Here we show it under the extra hypothesis that `ω • z = z` for all `z` in the center. -/
example {H : Subgroup G} (hH : IsOmegaSubgroup Ω G H) (g : G) (hg : g ∈ H) (ω : Ω) : ω • g ∈ H :=
  hH g hg ω

end OmegaGroup
