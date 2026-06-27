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
  rw [Ideal.isPrimary_iff]
  constructor
  · -- Show A.colon Set.univ ≠ ⊤
    intro htop
    have h_one_mem : (1 : R) ∈ A.colon Set.univ := htop.symm ▸ Submodule.mem_top
    rw [Submodule.mem_colon] at h_one_mem
    have hA_top : A = ⊤ := Submodule.eq_top_iff'.mpr fun m =>
      by simpa [one_smul] using h_one_mem m (Set.mem_univ m)
    exact hA.ne_top hA_top
  · -- Show ∀ x y, x*y ∈ A.colon Set.univ → x ∈ A.colon Set.univ ∨ y ∈ radical(A.colon Set.univ)
    intro x y hxy
    rw [Submodule.mem_colon] at hxy
    by_cases hx : x ∈ A.colon Set.univ
    · exact Or.inl hx
    · rw [Submodule.mem_colon] at hx
      push_neg at hx
      rcases hx with ⟨m, _, hxm⟩
      -- hxm : x • m ∉ A
      have hxym : (x * y) • m ∈ A := hxy m (Set.mem_univ m)
      rw [mul_comm x y, mul_smul] at hxym
      -- hxym : y • (x • m) ∈ A
      rcases hA.mem_or_mem hxym with (hx_sm_mem | hy_rad)
      · exact absurd hx_sm_mem hxm
      · exact Or.inr hy_rad
