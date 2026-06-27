import Mathlib

/-!
# Cosets Partition a Group

Let `H` be a subgroup of a group `G`. The left cosets of `H` form a partition of `G`;
the right cosets of `H` form a partition of `G`.

A family of subsets partitions a set if the subsets cover the set and any two
are either equal or disjoint.
-/

open Set
open scoped Pointwise

/--
**Cosets Partition a Group.**

For a subgroup `H` of a group `G`, the left cosets `g • (H : Set G)` form a partition of `G`:
they cover `G` and any two left cosets are either equal or disjoint.

The symmetric statement holds for right cosets `(H : Set G) * {g}`.
-/
theorem cosets_partition_a_group {G : Type*} [Group G] (H : Subgroup G) :
    (⋃ g : G, g • (H : Set G)) = Set.univ ∧
    ∀ g₁ g₂ : G, Disjoint (g₁ • (H : Set G)) (g₂ • (H : Set G)) ∨
    g₁ • (H : Set G) = g₂ • (H : Set G) := by
  sorry
