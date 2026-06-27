import Mathlib

/-!
# Trivial and Proper Subgroups

The subgroup `{1_G}` is called the trivial subgroup (denoted `1`).
Any subgroup `H ≠ G` is a proper subgroup, written `H < G`.

In Mathlib4:
- The trivial subgroup is `⊥ : Subgroup G`, the bottom element in the subgroup lattice.
  `mem_bot` gives `x ∈ (⊥ : Subgroup G) ↔ x = 1`.
- A proper subgroup `H < G` is expressed as `H < ⊤` or `H ≠ ⊤`, using the lattice strict order.
- There is no dedicated `IsProperSubgroup` predicate in Mathlib4; we define one here for textbook
  compatibility.

## Main definitions

* `Subgroup.trivialSubgroup G` — alias for `⊥ : Subgroup G`, the trivial subgroup
* `Subgroup.IsProper H` — predicate stating `H` is a proper subgroup of `G`, i.e. `H ≠ ⊤`
-/

open Subgroup

variable {G : Type*} [Group G]

namespace Subgroup

/-- The trivial subgroup of `G`, i.e. the subgroup consisting only of the identity element `1`.
This is an alias for `⊥ : Subgroup G`, which Mathlib4 uses for the trivial subgroup. -/
def trivialSubgroup (G : Type*) [Group G] : Subgroup G := ⊥

/-- Every element of the trivial subgroup is the identity. -/
@[simp]
theorem mem_trivialSubgroup {x : G} : x ∈ trivialSubgroup G ↔ x = 1 := by
  sorry
