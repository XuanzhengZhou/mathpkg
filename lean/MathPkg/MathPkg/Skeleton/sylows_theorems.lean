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
    ∃ Q : Sylow p G, P ≤ Q := by
  sorry
