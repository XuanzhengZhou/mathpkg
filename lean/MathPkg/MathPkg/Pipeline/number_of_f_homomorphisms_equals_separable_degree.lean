import Mathlib

open scoped Classical

/-!
# Number of F-homomorphisms equals separable degree

Let `K` be a finite extension of `F`, and let `S` be the separable closure of `F` in `K`.
Then `[S : F]` is equal to the number of `F`-homomorphisms from `K` to an algebraic closure of `F`.

This is a fundamental result in Galois theory, linking the separable degree to the count of
field embeddings into an algebraic closure. The separable closure `separableClosure F K`
is the maximal separable subextension of `K/F`, and its degree `[separableClosure F K : F]`
is the separable degree of the extension.
-/

variable (F K : Type*) [Field F] [Field K] [Algebra F K] [FiniteDimensional F K]

/-- The number of `F`-algebra homomorphisms from `K` to the algebraic closure of `F`
equals the separable degree `[separableClosure F K : F]`. -/
theorem card_algHom_eq_finrank_separableClosure :
    Nat.card (K →ₐ[F] AlgebraicClosure F) = finrank F (separableClosure F K) := by
  sorry
