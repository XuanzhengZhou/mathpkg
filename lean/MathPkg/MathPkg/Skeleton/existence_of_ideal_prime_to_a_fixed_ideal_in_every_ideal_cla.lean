import Mathlib

open scoped NumberField nonZeroDivisors

/-!
# Existence of Ideal Prime to a Fixed Ideal in Every Ideal Class

Let `K` be an algebraic number field, `𝓞 K` its ring of integers, and `M ⊂ 𝓞 K` a fixed
nonzero ideal. Then every ideal class in `K` contains an ideal that is relatively prime to `M`.

In Mathlib4 this is expressed using `ClassGroup (𝓞 K)` and `ClassGroup.mk0`
for the class of a nonzero integral ideal. Two ideals are relatively prime
(coprime / comaximal) when their sum is the whole ring: `A ⊔ M = ⊤`.
-/

theorem existence_of_ideal_prime_to_a_fixed_ideal_in_every_ideal_cla (K : Type*) [Field K]
    [NumberField K] (M : Ideal (𝓞 K)) (hM : M ≠ ⊥) (I : ClassGroup (𝓞 K)) :
    ∃ (A : (Ideal (𝓞 K))⁰), ClassGroup.mk0 A = I ∧ (A : Ideal (𝓞 K)) ⊔ M = ⊤ := by
  sorry
