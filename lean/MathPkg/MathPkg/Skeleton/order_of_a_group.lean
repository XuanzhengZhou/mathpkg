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
theorem order_eq_fintype_card (G : Type*) [Group G] [Fintype G] : order G = Fintype.card G := by
  sorry
