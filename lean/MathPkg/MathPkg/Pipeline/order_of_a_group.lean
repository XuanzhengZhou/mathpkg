import Mathlib

/-!
# Order of a Group

The order of a group is the cardinality of its underlying set G, denoted |G|.

In Mathlib4, the cardinality of a type is accessed via:
- `Nat.card G` — the cardinality of `G` as a natural number (0 for infinite groups)
- `Fintype.card G` — for types with a `Fintype` instance

For finite groups, `Nat.card G = Fintype.card G`, with the equation given by `Nat.card_eq_fintype_card`.
-/

/-- The order of a group is the cardinality of its underlying set.
For a finite group `G`, `order G` equals `Fintype.card G`.
For an infinite group, `order G = 0` (since `Nat.card` returns 0 for infinite types). -/
noncomputable def order (G : Type*) : ℕ := Nat.card G

/-- Notation for the order of a group: `|G|` denotes the cardinality of `G`. -/
local notation "|" G "|" => order G

/--
The order of a finite group equals its `Fintype.card`.
This is the key connection between the abstract notion of order and
the computable cardinality for finite groups.
-/
theorem order_eq_fintype_card (G : Type*) [Group G] [Fintype G] : order G = Fintype.card G :=
  Nat.card_eq_fintype_card (α := G)

/--
For a finite group, the order can be computed via `Fintype.card`.
For example, the order of the cyclic group `ZMod n` (as an additive group) is `n`.
-/
example (n : ℕ) [NeZero n] : Fintype.card (ZMod n) = n := by
  simp

/--
The order of the trivial group (with one element) is 1.
-/
example : order (Equiv.Perm (Fin 1)) = 1 := by
  rw [order_eq_fintype_card, Fintype.card_perm, Fintype.card_fin]
  rfl

/--
The order of the symmetric group S₃ is 6.
-/
example : order (Equiv.Perm (Fin 3)) = 6 := by
  rw [order_eq_fintype_card, Fintype.card_perm, Fintype.card_fin]
  rfl

/--
Lagrange's Theorem can be stated in terms of `order`: the order of a subgroup
divides the order of the ambient group.
-/
example (G : Type*) [Group G] [Fintype G] [DecidableEq G] (H : Subgroup G) : order H ∣ order G := by
  haveI : Fintype H := Fintype.ofFinite _
  simpa [order_eq_fintype_card, Nat.card_eq_fintype_card]
    using Subgroup.card_subgroup_dvd_card H

/--
For infinite groups, the order is 0 (by `Nat.card` convention).
For example, the additive group of integers has order 0.
-/
example : order ℤ = 0 := by
  dsimp [order]
  rw [Nat.card_eq_zero_of_infinite]
