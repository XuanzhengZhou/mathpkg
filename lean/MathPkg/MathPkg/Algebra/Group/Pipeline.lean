import Mathlib

open Subgroup

/-- First Sylow Theorem: there exists a subgroup of order p^k. -/
theorem sylow_first {G : Type*} [Group G] [Finite G] (p : ℕ) [Fact p.Prime] (k : ℕ)
    (h : p ^ k ∣ Nat.card G) : ∃ (H : Subgroup G), Nat.card H = p ^ k :=
  Sylow.exists_subgroup_card_pow_prime p h

/-- Third Sylow Theorem: n_p ≡ 1 (mod p) and n_p ∣ |G|. -/
theorem sylow_third {G : Type*} [Group G] [Finite G] [Finite (Sylow p G)]
    (p : ℕ) [Fact p.Prime] :
    Nat.card (Sylow p G) ∣ Nat.card G ∧
    Nat.card (Sylow p G) ≡ 1 [MOD p] := by
  have h_mod : Nat.card (Sylow p G) ≡ 1 [MOD p] := card_sylow_modEq_one p G
  have h_exists : Nonempty (Sylow p G) := by
    apply Sylow.nonempty
  rcases h_exists with ⟨P⟩
  have h_dvd_index : Nat.card (Sylow p G) ∣ (P : Sylow p G).index := Sylow.card_dvd_index P
  have h_dvd : Nat.card (Sylow p G) ∣ Nat.card G := by
    have h := Subgroup.index_dvd_card (P : Subgroup G)
    exact Nat.dvd_trans h_dvd_index h
  exact ⟨h_dvd, h_mod⟩
