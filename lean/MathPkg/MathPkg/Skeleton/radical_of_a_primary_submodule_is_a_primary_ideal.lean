import Mathlib

open scoped Pointwise

/-!
# Radical of a Primary Submodule is a Primary Ideal

Let R be a commutative ring with identity and A a primary submodule of an R-module B.
Then QA = { r ∈ R ∣ rB ⊆ A } is a primary ideal in R.

In Mathlib4, `A.colon Set.univ` is the colon ideal `(A :_R M) = {r : R ∣ r • M ⊆ A}`,
which corresponds exactly to QA where B is the ambient module M.
-/

/--
**Theorem**: If A is a primary submodule of an R-module M, then the colon ideal
`A.colon Set.univ` (i.e., (A :_R M)) is a primary ideal of R.

Proof sketch:
1. Since A ≠ ⊤ (A is primary), 1 ∉ A.colon Set.univ, so the colon ideal is proper.
2. Given x*y ∈ A.colon Set.univ and x ∉ A.colon Set.univ, there exists m with x•m ∉ A.
   From (x*y)•m ∈ A we get y•(x•m) ∈ A. By the primary submodule condition on A
   (applied to r = y, element = x•m), we obtain x•m ∈ A (contradiction) or
   y ∈ radical(A.colon Set.univ).
-/
theorem colon_of_primary_submodule_is_primary_ideal {R M : Type*} [CommRing R] [AddCommGroup M]
    [Module R M] (A : Submodule R M) (hA : A.IsPrimary) :
    Ideal.IsPrimary (A.colon Set.univ) := by
  sorry
