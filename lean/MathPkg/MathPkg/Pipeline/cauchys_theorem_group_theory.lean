import Mathlib

/-!
# Cauchy's Theorem (Group Theory)

If `G` is a finite group and `p` is a prime dividing the order of `G`, then `G` contains
an element of order `p`.

## Mathlib4 Location

The theorem is proved in `Mathlib/GroupTheory/Perm/Cycle/Type.lean` as:

* `exists_prime_orderOf_dvd_card` — the `Fintype` version
* `exists_prime_orderOf_dvd_card'` — the `Finite` version (with `Nat.card`)
* `exists_prime_addOrderOf_dvd_card` — the additive group version

## Proof Strategy (classical)

The proof constructs the set `S = {(a₁, ..., aₚ) ∈ G^p | a₁···aₚ = e}` of size `|G|^{p-1}`,
lets the cyclic group `Cₚ` act on `S` by cyclic shifts, and uses the orbit-stabilizer theorem.
Since `p` divides `|S|` and orbits have size 1 or `p`, the number of fixed points (tuples with
all equal entries) is also divisible by `p`. A fixed point `(a, …, a)` satisfies `a^p = e`,
giving the desired element of order `p`.
-/

open scoped BigOperators

/--
**Cauchy's Theorem (Group Theory).**

For every prime `p` dividing the order of a finite group `G`, there exists an element
of order `p` in `G`.

This is the `Fintype` version using `Fintype.card`. For the `Finite` version using
`Nat.card`, see `exists_prime_orderOf_dvd_card'`.
-/
theorem cauchys_theorem_group_theory {G : Type*} [Group G] [Fintype G] (p : ℕ)
    [Fact p.Prime] (hdvd : p ∣ Fintype.card G) : ∃ x : G, orderOf x = p :=
  exists_prime_orderOf_dvd_card p hdvd

/--
**Cauchy's Theorem** — `Finite` version.

Uses `Nat.card` instead of `Fintype.card`. Useful when only a `Finite` instance
(rather than `Fintype`) is available.
-/
theorem cauchys_theorem_group_theory' {G : Type*} [Group G] [Finite G] (p : ℕ)
    [Fact p.Prime] (hdvd : p ∣ Nat.card G) : ∃ x : G, orderOf x = p :=
  exists_prime_orderOf_dvd_card' p hdvd

/--
**Cauchy's Theorem** — additive version.

For every prime `p` dividing the order of a finite additive group `G`, there exists
an element of additive order `p` in `G`.
-/
theorem cauchys_theorem_additive {G : Type*} [AddGroup G] [Fintype G] (p : ℕ)
    [Fact p.Prime] (hdvd : p ∣ Fintype.card G) : ∃ x : G, addOrderOf x = p :=
  exists_prime_addOrderOf_dvd_card p hdvd

/--
**Example:** In the symmetric group S₃ (order 6), there is an element of order 2
(since 2 | 6) and an element of order 3 (since 3 | 6).
-/
example : ∃ x : Equiv.Perm (Fin 3), orderOf x = 2 := by
  have hcard : Fintype.card (Equiv.Perm (Fin 3)) = 6 := by
    rw [Fintype.card_perm, Fintype.card_fin]
    rfl
  have hdvd : 2 ∣ Fintype.card (Equiv.Perm (Fin 3)) := by
    rw [hcard]
    norm_num
  haveI : Fact (Nat.Prime 2) := ⟨by norm_num⟩
  exact cauchys_theorem_group_theory 2 hdvd

/--
**Example:** In the symmetric group S₃, there is also an element of order 3.
-/
example : ∃ x : Equiv.Perm (Fin 3), orderOf x = 3 := by
  have hcard : Fintype.card (Equiv.Perm (Fin 3)) = 6 := by
    rw [Fintype.card_perm, Fintype.card_fin]
    rfl
  have hdvd : 3 ∣ Fintype.card (Equiv.Perm (Fin 3)) := by
    rw [hcard]
    norm_num
  haveI : Fact (Nat.Prime 3) := ⟨by norm_num⟩
  exact cauchys_theorem_group_theory 3 hdvd

/--
**Example:** In ZMod 7 (additive group of order 7, which is prime), there is an
element of additive order 7.
-/
example : ∃ x : ZMod 7, addOrderOf x = 7 := by
  have hdvd : 7 ∣ Fintype.card (ZMod 7) := by
    simp
  haveI : Fact (Nat.Prime 7) := ⟨by norm_num⟩
  exact cauchys_theorem_additive 7 hdvd

/--
**Example:** In the dihedral group D₅ (order 10), there is an element of order 5
since 5 | 10.
-/
example : ∃ x : DihedralGroup 5, orderOf x = 5 := by
  have hcard : Fintype.card (DihedralGroup 5) = 10 := by
    simp [DihedralGroup.card]
  have hdvd : 5 ∣ Fintype.card (DihedralGroup 5) := by
    rw [hcard]
    norm_num
  haveI : Fact (Nat.Prime 5) := ⟨by norm_num⟩
  exact cauchys_theorem_group_theory 5 hdvd

/--
**Counterexample verification:** In a group of order 4, there is no element of order 3
(since 3 does not divide 4). The theorem gives no guarantee because the premise
`p ∣ Fintype.card G` is not satisfied.
-/
example : ¬ (3 ∣ Fintype.card (ZMod 4)) := by
  have hcard : Fintype.card (ZMod 4) = 4 := by
    rw [ZMod.card]
  rw [hcard]
  norm_num
