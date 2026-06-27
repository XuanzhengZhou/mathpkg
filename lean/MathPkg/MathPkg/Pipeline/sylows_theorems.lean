import Mathlib

open scoped Classical

/-!
# Sylow's Theorems

Let G be a finite group of order p^a * m where p is prime and p ∤ m.
Sylow's Theorems are three fundamental results about the structure of finite groups:

1. **Sylow's First Theorem** (Existence): Every p-subgroup is contained in a Sylow p-subgroup.
   In particular, Sylow p-subgroups (subgroups of order p^a) always exist.

2. **Sylow's Second Theorem** (Conjugacy): All Sylow p-subgroups are conjugate.

3. **Sylow's Third Theorem** (Counting): The number n_p of Sylow p-subgroups satisfies
   n_p ≡ 1 mod p and n_p divides the index of a Sylow p-subgroup.

Mathlib4 provides full proofs of all three Sylow theorems in
`Mathlib/GroupTheory/Sylow.lean`, along with many generalizations.

## Main definitions

* `Sylow p G` : The type of Sylow p-subgroups of G (defined as maximal p-subgroups).
* `IsPGroup p H` : The proposition that H is a p-group.

## Main statements

* `IsPGroup.exists_le_sylow` : Sylow's First Theorem (containment).
* `Sylow.nonempty` : Sylow p-subgroups always exist.
* `Sylow.isPretransitive_of_finite` : Sylow's Second Theorem (conjugacy, instance).
* `card_sylow_modEq_one` : Sylow's Third Theorem (n_p ≡ 1 mod p).
-/

section sylows_theorems

open Subgroup

/-!
## Sylow's First Theorem: Existence

Every p-subgroup is contained in a Sylow p-subgroup.
In particular, Sylow p-subgroups always exist.
-/

/-- **Sylow's First Theorem**: Every p-subgroup of G is contained in some Sylow p-subgroup. -/
theorem sylow_first_theorem {p : ℕ} {G : Type*} [Group G] {P : Subgroup G} (hP : IsPGroup p P) :
    ∃ Q : Sylow p G, P ≤ Q :=
  IsPGroup.exists_le_sylow hP

/-- Sylow p-subgroups always exist. `Sylow.nonempty` provides an explicit inhabitant. -/
example (p : ℕ) (G : Type*) [Group G] : Nonempty (Sylow p G) := by
  infer_instance

/-- A stronger form: if p^n divides |G|, there exists a subgroup of order p^n. -/
theorem exists_subgroup_of_prime_power_order (p n : ℕ) (G : Type*) [Group G]
    [Fact p.Prime] [Finite G] (hdvd : p ^ n ∣ Nat.card G) : ∃ K : Subgroup G, Nat.card K = p ^ n :=
  Sylow.exists_subgroup_card_pow_prime p hdvd

/-- A Sylow p-subgroup P satisfies `IsPGroup p P` by definition. -/
example (p : ℕ) (G : Type*) [Group G] (P : Sylow p G) : IsPGroup p (P : Subgroup G) :=
  P.isPGroup'

/-!
## Sylow's Second Theorem: Conjugacy

All Sylow p-subgroups are conjugate under the action of G.
Given P, Q : Sylow p G, there exists g ∈ G such that gPg⁻¹ = Q.
-/

/-- **Sylow's Second Theorem**: If the number of Sylow p-subgroups is finite,
then the conjugation action of G on Sylow p-subgroups is pretransitive.
This means any two Sylow p-subgroups are conjugate. -/
example (p : ℕ) (G : Type*) [Group G] [Fact p.Prime] [Finite (Sylow p G)] :
    MulAction.IsPretransitive G (Sylow p G) := by
  infer_instance

/-- Explicit form: for any two Sylow p-subgroups P, Q, there exists g : G with g • P = Q. -/
theorem sylow_second_theorem {p : ℕ} {G : Type*} [Group G] [Fact p.Prime] [Finite (Sylow p G)]
    (P Q : Sylow p G) : ∃ g : G, g • P = Q :=
  MulAction.exists_smul_eq G P Q

/-- Sylow p-subgroups are pairwise isomorphic (they are conjugate). -/
theorem sylow_are_isomorphic {p : ℕ} {G : Type*} [Group G] [Fact p.Prime] [Finite (Sylow p G)]
    (P Q : Sylow p G) : Nonempty (P ≃* Q) := by
  obtain ⟨g, hg⟩ := sylow_second_theorem P Q
  have h_equiv : P ≃* (g • P : Sylow p G) := P.equivSMul g
  rw [hg] at h_equiv
  exact ⟨h_equiv⟩

/-!
## Sylow's Third Theorem: Counting

The number n_p of Sylow p-subgroups satisfies:
- n_p ≡ 1 (mod p)
- n_p divides the index [G : P] of any Sylow p-subgroup P
- p does not divide n_p
-/

/-- **Sylow's Third Theorem**: n_p ≡ 1 mod p. -/
theorem sylow_third_theorem (p : ℕ) (G : Type*) [Group G] [Fact p.Prime] [Finite (Sylow p G)] :
    Nat.card (Sylow p G) ≡ 1 [MOD p] :=
  card_sylow_modEq_one p G

/-- p does not divide n_p. -/
theorem not_dvd_card_sylow' (p : ℕ) (G : Type*) [Group G] [Fact p.Prime] [Finite (Sylow p G)] :
    ¬ p ∣ Nat.card (Sylow p G) :=
  not_dvd_card_sylow p G

/-- n_p divides the index of any Sylow p-subgroup P. -/
theorem card_sylow_dvd_index {p : ℕ} {G : Type*} [Group G] [Fact p.Prime] [Finite (Sylow p G)]
    (P : Sylow p G) : Nat.card (Sylow p G) ∣ P.index :=
  Sylow.card_dvd_index P

/-- n_p equals the index [G : N_G(P)] of the normalizer of P. -/
theorem card_sylow_eq_index_normalizer {p : ℕ} {G : Type*} [Group G] [Fact p.Prime]
    [Finite (Sylow p G)] (P : Sylow p G) : Nat.card (Sylow p G) = (normalizer (P : Set G)).index :=
  Sylow.card_eq_index_normalizer P

/-!
## Sylow subgroups are Hall subgroups

A Hall subgroup is a subgroup whose order is coprime to its index.
Sylow p-subgroups are Hall subgroups with respect to the prime p.
-/

/-- A Sylow p-subgroup is a Hall subgroup: its order is coprime to its index. -/
theorem sylow_is_hall {p : ℕ} {G : Type*} [Group G] [Finite G] [Fact p.Prime] (P : Sylow p G) :
    (Nat.card P).Coprime P.index :=
  Sylow.card_coprime_index P

/-- The order of a Sylow subgroup divides the order of G. -/
theorem sylow_card_dvd_card {p : ℕ} {G : Type*} [Group G] [Finite G] (P : Sylow p G) :
    Nat.card P ∣ Nat.card G :=
  P.1.card_subgroup_dvd_card

/-- For a finite group, the order of a Sylow p-subgroup is p^a where
a = v_p(|G|) is the p-adic valuation of the group order. -/
theorem card_eq_multiplicity' {p : ℕ} {G : Type*} [Group G] [Finite G] [Fact p.Prime]
    (P : Sylow p G) : Nat.card P = p ^ (Nat.card G).factorization p :=
  Sylow.card_eq_multiplicity P

/-!
## Sylow uniqueness and normality

A Sylow p-subgroup is normal iff it is the unique Sylow p-subgroup.
-/

/-- If a Sylow p-subgroup is normal, then it is the unique Sylow p-subgroup. -/
theorem normal_implies_unique_sylow {p : ℕ} {G : Type*} [Group G] [Fact p.Prime]
    [Finite (Sylow p G)] (P : Sylow p G) (hP : P.Normal) : ∀ Q : Sylow p G, Q = P := by
  haveI : Unique (Sylow p G) := Sylow.unique_of_normal P hP
  intro Q
  exact Subsingleton.elim Q P

/-- If all Sylow p-subgroups are equal (subsingleton), then any Sylow p-subgroup is normal. -/
theorem subsingleton_implies_normal_sylow {p : ℕ} {G : Type*} [Group G]
    [Subsingleton (Sylow p G)] (P : Sylow p G) : P.Normal :=
  Sylow.normal_of_subsingleton P

/-- A Sylow p-subgroup is normal iff it is the unique Sylow p-subgroup. -/
theorem sylow_normal_iff_unique {p : ℕ} {G : Type*} [Group G] [Fact p.Prime]
    [Finite (Sylow p G)] (P : Sylow p G) : P.Normal ↔ ∀ Q : Sylow p G, Q = P := by
  constructor
  · exact normal_implies_unique_sylow P
  · intro h
    have : Subsingleton (Sylow p G) := by
      refine ⟨fun Q R => ?_⟩
      rw [h Q, h R]
    exact subsingleton_implies_normal_sylow P

/-!
## Connection to the class equation

Sylow's Theorems are intimately related to group actions and the class equation.
The proof of Sylow's First Theorem uses the action of G on subsets of size p^a;
the proof of the Second Theorem uses a fixed-point argument on the action of a
p-subgroup on the quotient by a Sylow p-subgroup; the proof of the Third Theorem
refines the fixed-point count.

See `Mathlib/GroupTheory/Sylow.lean` for the complete proof details.
-/

/-!
## Frattini's Argument

An important application of Sylow's Second Theorem.
If N ◁ G and P ∈ Syl_p(N), then G = N_G(P) · N.
-/

/-- **Frattini's Argument**: If N is a normal subgroup of G and P is a Sylow p-subgroup of N,
then G = N_G(P) · N (equivalently, N_G(P) · N generates G). -/
theorem frattini_argument {p : ℕ} {G : Type*} [Group G] [Fact p.Prime] {N : Subgroup G} [N.Normal]
    [Finite (Sylow p N)] (P : Sylow p N) : normalizer (P.map N.subtype) ⊔ N = ⊤ :=
  Sylow.normalizer_sup_eq_top P

/-- **Frattini's Argument** (alternative form): If N ◁ G and P ∈ Syl_p(G) with P ≤ N,
then G = N_G(P) · N. -/
theorem frattini_argument' {p : ℕ} {G : Type*} [Group G] [Fact p.Prime] {N : Subgroup G} [N.Normal]
    [Finite (Sylow p N)] (P : Sylow p G) (hP : P ≤ N) : normalizer P ⊔ N = ⊤ :=
  Sylow.normalizer_sup_eq_top' P hP

end sylows_theorems
