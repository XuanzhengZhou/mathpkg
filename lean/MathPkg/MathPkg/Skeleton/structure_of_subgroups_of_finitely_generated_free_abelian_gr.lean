import Mathlib

open scoped Classical
open scoped BigOperators
open Module

/-!
# Structure of Subgroups of Finitely Generated Free Abelian Groups

If `F` is a free abelian group of finite rank `n` and `G` is a nonzero subgroup of `F`,
then there exists a basis `{x₁, …, xₙ}` of `F`, an integer `r` (`1 ≤ r ≤ n`),
and positive integers `d₁, …, dᵣ` such that `d₁ ∣ d₂ ∣ … ∣ dᵣ` and `G` is free abelian
with basis `{d₁x₁, …, dᵣxᵣ}`.

This is a special case of the structure theorem for finitely generated modules over
a principal ideal domain, applied to `ℤ`-modules. The proof uses Mathlib's Smith normal
form for submodules of a finite free module over a PID (`Submodule.smithNormalForm`).

## Main Theorem

* `structure_of_subgroups_of_finitely_generated_free_abelian_group`:
  the existence of the adapted basis and the chain of divisible positive integers.

## References

* Mathlib: `LinearAlgebra/FreeModule/PID.lean` for `Submodule.smithNormalForm`
* Standard textbook: Structure theorem for finitely generated modules over a PID
-/

section structure_of_subgroups

/-! We work with finite free `ℤ`-modules, i.e., finitely generated free abelian groups. -/

variable {F : Type*} [AddCommGroup F]

/-- The main theorem: structure of nonzero subgroups of finitely generated free abelian groups.

Given a finite free `ℤ`-module `F` (a free abelian group of finite rank) and a nonzero
additive subgroup `G`, there exist:
- a basis `bF'` of `F` indexed by some finite type `ι`
- a natural number `r` with `1 ≤ r ≤ n` (where `n` is the rank)
- positive integers `d₁, …, dᵣ` with the divisibility chain `d₁ ∣ d₂ ∣ … ∣ dᵣ`
- a basis `bG` of `G` indexed by `Fin r`

such that each basis vector of `G` is `dᵢ` times the corresponding basis vector of `F`.

We formulate the theorem in terms of `Module.Finite ℤ F` and `Module.Free ℤ F`,
which implies `F` is a free ℤ-module of some finite rank.
-/
theorem structure_of_subgroups_of_finitely_generated_free_abelian_group
    [Module ℤ F] [Module.Finite ℤ F] [Module.Free ℤ F]
    (G : AddSubgroup F) (hG : G ≠ ⊥) :
    ∃ (n : ℕ) (bF' : Basis (Fin n) ℤ F) (r : ℕ) (hr : r ≥ 1) (hrn : r ≤ n)
      (d : Fin r → ℕ),
      (∀ i, d i > 0) ∧
      (∀ (i j : Fin r), (d i : ℤ) ∣ (d j : ℤ) ∨ (d j : ℤ) ∣ (d i : ℤ)) ∧
      (∃ (bG : Basis (Fin r) ℤ G),
        ∀ i : Fin r, (bG i : F) = (d i : ℤ) • bF' (Fin.castLE hrn i)) := by
  sorry
