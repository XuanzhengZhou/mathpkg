import Mathlib

/-!
# Five-term Exact Sequence for Tor

If `0 → A → B → C → 0` is a short exact sequence of `R`-modules
and `M` is an `R`-module, then there is an exact sequence

    Tor₁(A, M) → Tor₁(B, M) → Tor₁(C, M) → A ⊗ M → B ⊗ M → C ⊗ M → 0

where the maps are:
- `Tor₁(A, M) → Tor₁(B, M)` and `Tor₁(B, M) → Tor₁(C, M)` induced by
  functoriality of `Tor` in the first argument
- `Tor₁(C, M) → A ⊗ M` the **connecting homomorphism** arising from the
  long exact sequence of left-derived functors
- `A ⊗ M → B ⊗ M` and `B ⊗ M → C ⊗ M` induced by tensoring with `M`
- `C ⊗ M → 0` the zero map, which is equivalent to the surjectivity of
  `B ⊗ M → C ⊗ M`

This is a standard result in homological algebra, obtained by truncating
the long exact sequence of `Tor` at the zeroth term (the tensor product).

## Mathlib4 References

* `Mathlib/CategoryTheory/Monoidal/Tor.lean` — defines `Tor C n`
* `Mathlib/Algebra/Category/ModuleCat/Monoidal.lean` — monoidal structure on `ModuleCat`
* `Mathlib/CategoryTheory/Abelian/LeftDerived.lean` — left-derived functors
-/

open CategoryTheory

universe u

variable {R : Type u} [CommRing R]

/--
**Five-term exact sequence for Tor.**

Given a short exact sequence `0 → A → B → C → 0` of `R`-modules
(represented by an exact pair `f : A ⟶ B`, `g : B ⟶ C` with `f` mono and `g` epi)
and an `R`-module `M`, there exist natural maps

    α : Tor₁(A, M) → Tor₁(B, M)
    β : Tor₁(B, M) → Tor₁(C, M)
    γ : Tor₁(C, M) → A ⊗ M   (connecting homomorphism)
    δ : A ⊗ M → B ⊗ M
    ε : B ⊗ M → C ⊗ M

such that the sequence

    Tor₁(A, M)  ─α→  Tor₁(B, M)  ─β→  Tor₁(C, M)  ─γ→  A⊗M  ─δ→  B⊗M  ─ε→  C⊗M  →  0

is exact.
-/
theorem five_term_exact_sequence_tor (A B C M : ModuleCat.{u} R)
    (f : A ⟶ B) (g : B ⟶ C)
    (h_exact : Exact f g) (h_mono : Mono f) (h_epi : Epi g) :
    ∃ (α : ((Tor (ModuleCat.{u} R) 1).obj A).obj M ⟶ ((Tor (ModuleCat.{u} R) 1).obj B).obj M)
      (β : ((Tor (ModuleCat.{u} R) 1).obj B).obj M ⟶ ((Tor (ModuleCat.{u} R) 1).obj C).obj M)
      (γ : ((Tor (ModuleCat.{u} R) 1).obj C).obj M ⟶ A ⊗ M)
      (δ : A ⊗ M ⟶ B ⊗ M)
      (ε : B ⊗ M ⟶ C ⊗ M),
      Exact α β ∧ Exact β γ ∧ Exact γ δ ∧ Exact δ ε ∧ Epi ε := by
  sorry
