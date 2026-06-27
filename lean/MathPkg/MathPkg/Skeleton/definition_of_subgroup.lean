import Mathlib

open Subgroup

/--
An Ω-group is a group `G` together with a monoid `Ω` acting by endomorphisms.
In Mathlib4, this is captured by `MulDistribMulAction Ω G`, which ensures:
  `ω • (g₁ * g₂) = (ω • g₁) * (ω • g₂)` and `ω • 1 = 1` for all `ω : Ω`, `g₁ g₂ : G`.

We introduce this as a type alias for convenience.
-/
def OmegaGroupAlias (Ω G : Type*) [Monoid Ω] [Group G] [MulDistribMulAction Ω G] : Type _ := G

namespace OmegaGroupAlias

variable (Ω G : Type*) [Monoid Ω] [Group G] [MulDistribMulAction Ω G]

/-- An Ω-subgroup of an Ω-group `G` is a subgroup `H` that is Ω-admissible,
  i.e., `ω • h ∈ H` for every `h ∈ H` and `ω ∈ Ω`. -/
def IsOmegaSubgroup (H : Subgroup G) : Prop := by
  sorry
