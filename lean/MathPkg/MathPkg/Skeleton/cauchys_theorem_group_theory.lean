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
    [Fact p.Prime] (hdvd : p ∣ Fintype.card G) : ∃ x : G, orderOf x = p := by
  sorry
