import Mathlib

/-!
# Definition of Group-Theoretical Class and Property

A **group-theoretical class** is a class of groups X such that:
1. X contains a group of order 1 (the trivial group)
2. If G₁ ≅ G ∈ X then G₁ ∈ X (closed under isomorphism)

A **group-theoretical property** is a property of groups such that:
1. A group of order 1 has it
2. If a group has it, so does any isomorphic copy

There is a natural bijection between group-theoretical properties and
group-theoretical classes: map a class to the property "is in the class",
and map a property to the class "groups with the property".

## Mathlib4 References
- `Group` typeclass: `Algebra/Group/Defs.lean`
- `MulEquiv` (≃*): `Algebra/Group/Equiv/Defs.lean`
- `Subsingleton` for trivial groups
-/

open Function

universe u

/-- A group-theoretical class is a class of groups that contains the trivial group
and is closed under group isomorphism. -/
@[ext]
structure GroupTheoreticalClass : Type (u+1) where
  /-- The underlying predicate: which groups belong to this class. -/
  pred : (G : Type u) → [Group G] → Prop
  /-- Every trivial group (group of order 1) belongs to the class. -/
  contains_trivial : ∀ (G : Type u) [Group G] [Subsingleton G], pred G
  /-- The class is closed under isomorphism: if G ≃* H and G is in the class, then H is too. -/
  iso_closed : ∀ {G H : Type u} [Group G] [Group H], G ≃* H → pred G → pred H

/-- A group-theoretical property is a property of groups that is satisfied by
the trivial group and is invariant under isomorphism. -/
@[ext]
structure GroupTheoreticalProperty : Type (u+1) where
  /-- The underlying property predicate. -/
  property : (G : Type u) → [Group G] → Prop
  /-- The trivial group satisfies the property. -/
  trivial_satisfies : ∀ (G : Type u) [Group G] [Subsingleton G], property G
  /-- The property is invariant under isomorphism: if G ≃* H and G has the property,
  then H has it too. -/
  iso_invariant : ∀ {G H : Type u} [Group G] [Group H], G ≃* H → property G → property H

/-- The natural map from a group-theoretical class to its corresponding property.
Given a class C, the associated property is "G belongs to C". -/
def GroupTheoreticalClass.toProperty (C : GroupTheoreticalClass) : GroupTheoreticalProperty where
  property := C.pred
  trivial_satisfies := C.contains_trivial
  iso_invariant := C.iso_closed

/-- The natural map from a group-theoretical property to its corresponding class.
Given a property P, the associated class is "groups with property P". -/
def GroupTheoreticalProperty.toClass (P : GroupTheoreticalProperty) : GroupTheoreticalClass where
  pred := P.property
  contains_trivial := P.trivial_satisfies
  iso_closed := P.iso_invariant

/-- The natural bijection between group-theoretical properties and group-theoretical classes.
Mapping a class to its property and back recovers the original class, and vice versa. -/
theorem class_property_bijection :
    Function.Bijective (GroupTheoreticalClass.toProperty) := by
  sorry
