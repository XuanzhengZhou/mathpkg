import Mathlib

/-- Test -/
def TestProp {R A B C : Type*} [CommSemiring R] [AddCommMonoid A] [Module R A] [AddCommMonoid B] [Module R B] [AddCommMonoid C] (f : A →+ B →+ C) : Prop := by
  sorry
