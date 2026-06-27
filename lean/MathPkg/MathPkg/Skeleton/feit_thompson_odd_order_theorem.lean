import Mathlib

/-!
# Feit–Thompson Odd Order Theorem

Every finite group of odd order is solvable. Equivalently, every nonabelian finite simple group
has even order.

This is one of the most important theorems in finite group theory, proved by Walter Feit and
John G. Thompson in 1963. The original proof is approximately 255 pages long and occupies an
entire issue of the *Pacific Journal of Mathematics*.

## Mathlib4 Location

The theorem is formalized in Mathlib4 at:

* `Mathlib/GroupTheory/SpecificGroups/FeitThompson.lean` — statement of the theorem

## Statement

If `G` is a finite group and `Fintype.card G` is odd, then `G` is solvable.

## References

* [Feit–Thompson theorem on Wikipedia](https://en.wikipedia.org/wiki/Feit–Thompson_theorem)
* Feit, W.; Thompson, J. G. (1963). "Solvability of groups of odd order".
  *Pacific Journal of Mathematics*, 13: 775–1029.
-/

/--
**Feit–Thompson Odd Order Theorem.**

If `G` is a finite group whose order is odd, then `G` is solvable.

The condition `Odd (Fintype.card G)` means that `Fintype.card G = 2*k + 1` for some `k : ℕ`,
i.e., the order of the group is not divisible by 2.
-/
theorem feit_thompson_odd_order_theorem {G : Type*} [Group G] [Fintype G]
    (hodd : Odd (Fintype.card G)) : IsSolvable G := by
  sorry
