import Mathlib

/-!
# Ω-Direct Factor and Indecomposability

Let G be a group with operator domain Ω. An Ω-subgroup H is called an Ω-direct factor of G
if there exists an Ω-subgroup K such that G = H × K; K is an Ω-direct complement of H.
If G has no proper nontrivial Ω-direct factors, G is Ω-indecomposable
(or indecomposable if Ω = ∅).

## Main definitions

* `OmegaGroup G Ω` — a group G equipped with an action of Ω via group endomorphisms
* `IsOmegaSubgroup G Ω H` — a subgroup H closed under the operators in Ω
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
def IsOmegaSubgroup (Ω : Type*) [OmegaGroup G Ω] (H : Subgroup G) : Prop :=
  ∀ (ω : Ω) {h : G}, h ∈ H → OmegaGroup.act ω h ∈ H

/-- The trivial subgroup is always an Ω-subgroup. -/
theorem isOmegaSubgroup_bot (Ω : Type*) [OmegaGroup G Ω] : IsOmegaSubgroup Ω (⊥ : Subgroup G) := by
  intro ω h hh
  simpa using congrArg (OmegaGroup.act ω) (Subgroup.mem_bot.mp hh)

/-- The full group is always an Ω-subgroup. -/
theorem isOmegaSubgroup_top (Ω : Type*) [OmegaGroup G Ω] : IsOmegaSubgroup Ω (⊤ : Subgroup G) := by
  intro ω h _
  exact Subgroup.mem_top _

/-- H is an Ω-direct factor of G if H is an Ω-subgroup and there exists an Ω-subgroup K
such that G is the internal direct product of H and K (via `IsComplement'`). -/
def IsOmegaDirectFactor (Ω : Type*) [OmegaGroup G Ω] (H : Subgroup G) : Prop :=
  IsOmegaSubgroup Ω H ∧ ∃ (K : Subgroup G), IsOmegaSubgroup Ω K ∧ IsComplement' H K

/-- K is an Ω-direct complement of H if K is an Ω-subgroup and H, K are complementary in G. -/
def IsOmegaDirectComplement (Ω : Type*) [OmegaGroup G Ω] (K H : Subgroup G) : Prop :=
  IsOmegaSubgroup Ω K ∧ IsComplement' H K

/-- The trivial subgroup ⊥ is always an Ω-direct factor (with complement ⊤). -/
theorem isOmegaDirectFactor_bot (Ω : Type*) [OmegaGroup G Ω] :
    IsOmegaDirectFactor Ω (⊥ : Subgroup G) := by
  refine ⟨isOmegaSubgroup_bot Ω, ⊤, isOmegaSubgroup_top Ω, ?_⟩
  exact isComplement'_bot_top

/-- The full group ⊤ is always an Ω-direct factor (with complement ⊥). -/
theorem isOmegaDirectFactor_top (Ω : Type*) [OmegaGroup G Ω] :
    IsOmegaDirectFactor Ω (⊤ : Subgroup G) := by
  refine ⟨isOmegaSubgroup_top Ω, ⊥, isOmegaSubgroup_bot Ω, ?_⟩
  exact isComplement'_top_bot

/-- G is Ω-indecomposable if G is nontrivial and has no proper nontrivial Ω-direct factors.
Equivalently: every Ω-direct factor is either ⊥ or ⊤. -/
def IsOmegaIndecomposable (G : Type*) [Group G] (Ω : Type*) [OmegaGroup G Ω] : Prop :=
  Nontrivial G ∧ ∀ (H : Subgroup G), IsOmegaDirectFactor Ω H → H = ⊥ ∨ H = ⊤

end Defs

section OmegaEmpty

/-- For Ω = Empty, the operator condition is vacuous: every subgroup is an Ω-subgroup.
Thus Ω-indecomposability for Ω = Empty reduces to: G is nontrivial and every subgroup
that has a complementary subgroup is ⊥ or ⊤. -/
theorem isOmegaIndecomposable_empty_iff (G : Type*) [Group G] :
    IsOmegaIndecomposable G Empty ↔ Nontrivial G ∧
      ∀ (H : Subgroup G), (∃ (K : Subgroup G), IsComplement' H K) → H = ⊥ ∨ H = ⊤ := by
  constructor
  · rintro ⟨hn, h⟩
    refine ⟨hn, ?_⟩
    intro H ⟨K, hCompl⟩
    have hΩH : IsOmegaSubgroup Empty H := by
      intro ω; exact Empty.elim ω
    have hΩK : IsOmegaSubgroup Empty K := by
      intro ω; exact Empty.elim ω
    have hDirect : IsOmegaDirectFactor Empty H := ⟨hΩH, K, hΩK, hCompl⟩
    exact h H hDirect
  · rintro ⟨hn, h⟩
    refine ⟨hn, ?_⟩
    intro H ⟨hΩH, K, hΩK, hCompl⟩
    exact h H ⟨K, hCompl⟩

end OmegaEmpty

section PrimeOrder

/-- In a group of prime order, every proper subgroup is trivial (by Lagrange's theorem).
Therefore the group is Ω-indecomposable for any operator domain Ω. -/
theorem isOmegaIndecomposable_of_prime_order {G : Type*} [Group G] [Fintype G]
    (hp : Nat.Prime (Fintype.card G)) (Ω : Type*) [OmegaGroup G Ω] :
    IsOmegaIndecomposable G Ω := by
  have h_nontriv : Nontrivial G := by
    have h_one_lt : 1 < Fintype.card G := Nat.Prime.one_lt hp
    exact (Fintype.one_lt_card_iff_nontrivial.mp h_one_lt)
  refine ⟨h_nontriv, ?_⟩
  intro H ⟨hΩH, K, hΩK, hCompl⟩
  classical
    -- From IsComplement'.card_mul, we have Nat.card H * Nat.card K = Nat.card G
    have h_card_mul : Nat.card H * Nat.card K = Nat.card G := hCompl.card_mul
    -- For finite groups, Nat.card = Fintype.card
    have h_fin_card_mul : Fintype.card H * Fintype.card K = Fintype.card G := by
      simpa [Nat.card_eq_fintype_card] using h_card_mul
    -- By Lagrange, the order of H divides the group order
    have h_card_H_div : Nat.card H ∣ Nat.card G := Subgroup.card_subgroup_dvd_card H
    have h_card_H_div' : Fintype.card H ∣ Fintype.card G := by
      simpa [Nat.card_eq_fintype_card] using h_card_H_div
    -- Since |G| is prime, any divisor is 1 or |G|
    have h_fin_card : Fintype.card H = 1 ∨ Fintype.card H = Fintype.card G :=
      hp.eq_one_or_self_of_dvd (Fintype.card H) h_card_H_div'
    rcases h_fin_card with hcard | hcard
    · -- card H = 1 → H = ⊥
      left
      have h_nat_card : Nat.card H = 1 := by
        simpa [Nat.card_eq_fintype_card] using hcard
      exact Subgroup.eq_bot_of_card_eq H h_nat_card
    · -- card H = card G → H = ⊤
      right
      have h_nat_card : Nat.card H = Nat.card G := by
        simpa [Nat.card_eq_fintype_card] using hcard
      exact Subgroup.eq_top_of_card_eq H h_nat_card

/-- The multiplicative group of Z/pZ is Ω-indecomposable (for any Ω).
`Multiplicative (ZMod p)` is a multiplicative group of prime order p. -/
theorem isOmegaIndecomposable_multiplicative_ZMod {p : ℕ} [Fact p.Prime] (Ω : Type*)
    [OmegaGroup (Multiplicative (ZMod p)) Ω] :
    IsOmegaIndecomposable (Multiplicative (ZMod p)) Ω := by
  have hp : Nat.Prime (Fintype.card (Multiplicative (ZMod p))) := by
    have hcard : Fintype.card (Multiplicative (ZMod p)) = p := by
      simp [ZMod.card, Fintype.card_multiplicative]
    rw [hcard]
    exact Fact.out (p := Nat.Prime p)
  exact isOmegaIndecomposable_of_prime_order hp Ω

end PrimeOrder

/-!
## Examples
-/

section Examples

/-- Example: The trivial group is NOT Ω-indecomposable because it is not nontrivial.
ZMod 1 has only one element, so `Multiplicative (ZMod 1)` has only one element. -/
example (Ω : Type*) [OmegaGroup (Multiplicative (ZMod 1)) Ω] :
    ¬ IsOmegaIndecomposable (Multiplicative (ZMod 1)) Ω := by
  intro h
  rcases h with ⟨hn, _⟩
  -- ZMod 1 is a subsingleton, so Multiplicative (ZMod 1) is trivially not nontrivial
  have : ¬ Nontrivial (Multiplicative (ZMod 1)) := not_nontrivial _
  exact this hn

/-- Example: Symmetric group S3 (6 elements).
The extreme cases: ⊥ and ⊤ are always Ω-direct factors. -/
example (Ω : Type*) [OmegaGroup (Equiv.Perm (Fin 3)) Ω] :
    IsOmegaDirectFactor Ω (⊥ : Subgroup (Equiv.Perm (Fin 3))) :=
  isOmegaDirectFactor_bot Ω

example (Ω : Type*) [OmegaGroup (Equiv.Perm (Fin 3)) Ω] :
    IsOmegaDirectFactor Ω (⊤ : Subgroup (Equiv.Perm (Fin 3))) :=
  isOmegaDirectFactor_top Ω

/-- Fact instance: 5 is prime (needed for ZMod 5 examples). -/
instance : Fact (Nat.Prime 5) := ⟨Nat.prime_five⟩

/-- Example: Multiplicative Z/2Z is Ω-indecomposable (for Ω = Empty). -/
example : IsOmegaIndecomposable (Multiplicative (ZMod 2)) Empty :=
  isOmegaIndecomposable_multiplicative_ZMod Empty

/-- Example: Multiplicative Z/5Z is Ω-indecomposable (for Ω = Empty). -/
example : IsOmegaIndecomposable (Multiplicative (ZMod 5)) Empty :=
  isOmegaIndecomposable_multiplicative_ZMod Empty

/-- Example: For Ω = ∅, the indecomposability condition reduces to the ordinary one:
a nontrivial group where no proper nontrivial subgroup has a complementary subgroup. -/
example (G : Type*) [Group G] : (IsOmegaIndecomposable G Empty) ↔
    (Nontrivial G ∧ ∀ (H : Subgroup G), (∃ (K : Subgroup G), IsComplement' H K) → H = ⊥ ∨ H = ⊤) :=
  isOmegaIndecomposable_empty_iff G

/-- Example: An Ω-group with a nontrivial operator.
Let Ω = Unit with the self-map φ(g) = g. (identity operator).
Multiplicative Z/5Z with the identity operator is Ω-indecomposable. -/
instance : OmegaGroup (Multiplicative (ZMod 5)) Unit where
  act _ := MonoidHom.id (Multiplicative (ZMod 5))

/-- With the identity operator, Multiplicative Z/5Z is still Ω-indecomposable. -/
example : IsOmegaIndecomposable (Multiplicative (ZMod 5)) Unit :=
  isOmegaIndecomposable_multiplicative_ZMod Unit

/-- Example: Ω-subgroups are closed under intersection. -/
example (G : Type*) [Group G] (Ω : Type*) [OmegaGroup G Ω]
    (H K : Subgroup G) (hH : IsOmegaSubgroup Ω H) (hK : IsOmegaSubgroup Ω K) :
    IsOmegaSubgroup Ω (H ⊓ K) := by
  intro ω h ⟨hhH, hhK⟩
  exact ⟨hH ω hhH, hK ω hhK⟩

end Examples
