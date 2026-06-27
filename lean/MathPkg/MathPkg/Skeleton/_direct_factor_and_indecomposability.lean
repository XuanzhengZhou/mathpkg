import Mathlib

/-!
# Ω-Direct Factor and Indecomposability

Let G be a group with operator domain Ω. An Ω-subgroup H is called an Ω-direct factor of G
if there exists an Ω-subgroup K such that G = H × K; K is an Ω-direct complement of H.
If G has no proper nontrivial Ω-direct factors, G is Ω-indecomposable
(or indecomposable if Ω = ∅).

## Main definitions

* `OmegaGroup G Ω` — a group G equipped with an action of Ω via group endomorphisms
* `_direct_factor_and_indecomposability_IsOmegaSubgroup G Ω H` — a subgroup H closed under the operators in Ω
* `IsOmegaDirectFactor G Ω H` — H is an Ω-subgroup that is an Ω-direct factor of G
* `IsOmegaDirectComplement G Ω K H` — K is an Ω-direct complement of H
* `IsOmegaIndecomposable G Ω` — G has no proper nontrivial Ω-direct factors
-/

open Subgroup

/-- An Ω-group is a group `G` equipped with an action of the operator domain `Ω` via
group endomorphisms. Each `ω : Ω` acts as a `Monoid.End G` (i.e., a multiplicative homomorphism). -/
class OmegaGroup (G : Type*) [Group G] (Ω : Type*) where
  act : Ω → Monoid.End G

namespace OmegaGroup

/-- The empty operator domain: every group is vacuously an Ω-group for Ω = Empty. -/
instance empty (G : Type*) [Group G] : OmegaGroup G Empty where
  act ω := Empty.elim ω

end OmegaGroup

section Defs

variable {G : Type*} [Group G]

/-- An Ω-subgroup is a subgroup of `G` that is closed under all operators in `Ω`. -/
def _direct_factor_and_indecomposability_IsOmegaSubgroup (Ω : Type*) [OmegaGroup G Ω] (H : Subgroup G) : Prop := by
  sorry
