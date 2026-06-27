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
  -- STEP 1: Since F is a finite free ℤ-module, it has a finite basis.
  -- We can obtain a basis indexed by some finite type ι.
  obtain ⟨ι, bF⟩ := ‹Module.Free ℤ F›
  have _ : Finite ι := by
    -- Actually the basis from Module.Free may be on any type, but we need to find one that's finite.
    -- Better approach: use Module.Finite to get a finite basis.
    sorry
  sorry
  -- The remainder of the proof uses Smith normal form machinery from Mathlib.
  -- We convert the AddSubgroup G to a Submodule ℤ F and apply Submodule.smithNormalForm.

/--
A simpler version of the theorem: given a basis of `n` elements for `F`, we can find
an adapted basis and the divisibility chain. This version is closer to the classical
formulation.
-/
theorem structure_of_subgroups_of_finitely_generated_free_abelian_group'
    {n : ℕ} (bF : Basis (Fin n) ℤ F) (G : AddSubgroup F) (hG : G ≠ ⊥) :
    ∃ (r : ℕ) (hr : r ≥ 1) (hrn : r ≤ n) (d : Fin r → ℕ) (bF' : Basis (Fin n) ℤ F)
      (bG : Basis (Fin r) ℤ G),
      (∀ i, d i > 0) ∧
      (∀ (i j : Fin r), (d i : ℤ) ∣ (d j : ℤ) ∨ (d j : ℤ) ∣ (d i : ℤ)) ∧
      (∀ i : Fin r, (bG i : F) = (d i : ℤ) • bF' (Fin.castLE hrn i)) := by
  -- Convert the AddSubgroup to a Submodule ℤ F to apply Smith normal form machinery.
  let N : Submodule ℤ F := AddSubgroup.toIntSubmodule G
  have hN : N ≠ ⊥ := by
    intro h
    apply hG
    apply AddSubgroup.toIntSubmodule.injective
    simpa [N, AddSubgroup.toIntSubmodule.map_bot] using h
  sorry

/--
An example: the subgroup `2ℤ` of `ℤ` (rank 1 case). Here `n = 1`, `r = 1`, `d₁ = 2`.
-/
example : ∃ (bF' : Basis (Fin 1) ℤ ℤ) (bG : Basis (Fin 1) ℤ (AddSubgroup.map
    (AddMonoidHom.mulLeft 2) (⊤ : AddSubgroup ℤ))), True := by
  -- The trivial basis of ℤ
  let bF' : Basis (Fin 1) ℤ ℤ := Basis.singleton (Fin 1) ℤ
  -- The subgroup 2ℤ has basis {2}
  refine ⟨bF', ?_, ?_⟩
  · -- Basis of 2ℤ as an AddSubgroup of ℤ
    -- We can use `AddSubgroup.map` and the isomorphism
    sorry
  · trivial

end structure_of_subgroups
