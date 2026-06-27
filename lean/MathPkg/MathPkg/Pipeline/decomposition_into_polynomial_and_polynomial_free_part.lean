import Mathlib

open Polynomial

variable {K : Type*} [Field K]

/-
Every rational fraction can be written uniquely as the sum
of a polynomial and a polynomial-free fraction in reduced form.
-/
lemma decomposition_into_polynomial_and_polynomial_free_part (f : RatFunc K) :
    ∃! (pg : Polynomial K × RatFunc K),
      f = (algebraMap (Polynomial K) (RatFunc K)) pg.1 + pg.2 ∧
      (pg.2 = 0 ∨
        ((RatFunc.den pg.2).degree > (RatFunc.num pg.2).degree ∧
         IsCoprime (RatFunc.num pg.2) (RatFunc.den pg.2))) := by
  sorry
