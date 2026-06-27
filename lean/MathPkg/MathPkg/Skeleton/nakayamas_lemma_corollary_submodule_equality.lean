import Mathlib

/-!
# Nakayama's Lemma Corollary: Submodule Equality

Let `R` be a local ring with maximal ideal `m`, let `M` be a finitely generated `R`-module,
and let `N` be a submodule of `M`. If `M = m • M + N`, then `M = N`.

This is a standard corollary of Nakayama's lemma.
-/

open scoped Classical
open IsLocalRing

/-- **Nakayama's Lemma Corollary (Submodule Equality)**.
If `R` is a local ring, `M` is a finitely generated `R`-module, and `N` is a submodule
of `M` such that `M = mM + N`, then `N = M`. -/
theorem nakayamas_lemma_corollary_submodule_equality {R : Type*} [CommRing R] [IsLocalRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (N : Submodule R M) (h : (maximalIdeal R) • (⊤ : Submodule R M) ⊔ N = ⊤) : N = ⊤ := by
  sorry
