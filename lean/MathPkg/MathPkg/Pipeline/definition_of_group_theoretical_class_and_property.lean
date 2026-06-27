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
  refine ⟨?injective, ?surjective⟩
  case injective =>
    intro C₁ C₂ h
    -- h : C₁.toProperty = C₂.toProperty
    -- Extract equality of the underlying predicates via the .property field
    have h_pred : C₁.pred = C₂.pred := by
      calc
        C₁.pred = (C₁.toProperty).property := rfl
        _ = (C₂.toProperty).property := by rw [h]
        _ = C₂.pred := rfl
    apply GroupTheoreticalClass.ext
    exact h_pred
  case surjective =>
    intro P
    -- For any property P, the class P.toClass maps back to P
    refine ⟨GroupTheoreticalProperty.toClass P, ?_⟩
    apply GroupTheoreticalProperty.ext
    rfl

-- Example 1: The class of all groups is a group-theoretical class.
example : GroupTheoreticalClass.{u} where
  pred := fun _ _ => True
  contains_trivial := fun _ _ _ => trivial
  iso_closed := fun {G H} [Group G] [Group H] _ _ => trivial

-- Example 2: The property of being a commutative (abelian) group is a
-- group-theoretical property.
example : GroupTheoreticalProperty.{u} where
  property := fun G _ => ∀ a b : G, a * b = b * a
  trivial_satisfies := by
    intro G _ instSub a b
    have ha : a = 1 := Subsingleton.elim a 1
    have hb : b = 1 := Subsingleton.elim b 1
    simp [ha, hb]
  iso_invariant := by
    intro G H _ _ φ hAbel a b
    have h := hAbel (φ.symm a) (φ.symm b)
    apply_fun φ at h
    simpa using h

-- Example 3: The property of being a trivial group is a group-theoretical property.
example : GroupTheoreticalProperty.{u} where
  property := fun G _ => Subsingleton G
  trivial_satisfies := fun _ _ h => h
  iso_invariant := by
    intro G H _ _ φ hSub
    -- If G is Subsingleton, then H is also Subsingleton via the Equiv
    exact (Equiv.subsingleton_congr φ.toEquiv).mp hSub

-- Example 4: Apply the bijection to the class of all groups and verify it round-trips.
example : (GroupTheoreticalClass.toProperty (by
    refine {
      pred := fun _ _ => True
      contains_trivial := fun _ _ _ => trivial
      iso_closed := fun {G H} [Group G] [Group H] _ _ => trivial
    } : GroupTheoreticalClass.{u})).property = (fun (_ : Type u) _ => True) :=
  rfl
