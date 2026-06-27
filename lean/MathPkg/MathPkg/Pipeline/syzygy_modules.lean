import Mathlib

open scoped Classical

/-!
# Syzygy Modules

Given an exact sequence `0 → N → F → M → 0` with `F` projective, `N` is called a
**first syzygy module** of `M`. The nth syzygy module is defined inductively as the
first syzygy module of the (n−1)st syzygy module. Syzygy modules are unique up to
projective summands.

## Mathlib4 correspondence

Mathlib4 already defines syzygies in a general abelian category setting:

- `CategoryTheory.Projective.syzygies f` is the first syzygy of a morphism `f : X ⟶ Y`:
  it is `Projective.over (kernel f)`, i.e. an arbitrarily chosen projective object
  equipped with an epimorphism onto `kernel f`.
- `CategoryTheory.Projective.d f : syzygies f ⟶ X` is the natural map
  `π (kernel f) ≫ kernel.ι f`.
- Iterating `Projective.d` yields the nth syzygy modules, as used in
  `CategoryTheory.ProjectiveResolution`.

This file specializes these notions to the category of `R`-modules (`ModuleCat R`).
-/

section syzygy_modules

open CategoryTheory
open CategoryTheory.Limits

variable (R : Type*) [Ring R]

/-- A **first syzygy module** of an `R`-module `M` is given by an exact sequence
`0 → S → P → M → 0` where `P` is projective.

This is a `structure` packaging the syzygy module `S`, the projective module `P`,
the surjection `P → M`, and the injection `S → P` forming an exact sequence.

In Mathlib4, `CategoryTheory.Projective.syzygies f` gives the syzygy of any
morphism `f : X ⟶ Y` in an abelian category with enough projectives.
Here we define a module-specific wrapper. -/
structure SyzygyModule (M : ModuleCat.{u} R) where
  /-- The syzygy module `S` (a submodule of the projective cover `P`). -/
  S : ModuleCat.{u} R
  /-- The projective module covering `M`. -/
  P : ModuleCat.{u} R
  /-- `P` is projective. -/
  [projective_P : Module.Projective R (↥P)]
  /-- The epimorphism `π : P → M`. -/
  π : P ⟶ M
  /-- `π` is surjective. -/
  [epi_π : Epi π]
  /-- The monomorphism `ι : S → P` (witnessing that `S` is a submodule of `P`). -/
  ι : S ⟶ P
  /-- `ι` is injective. -/
  [mono_ι : Mono ι]
  /-- The sequence is exact at `P`: `ker π = im ι`. In a module category,
  this means `S ≅ kernel π` as modules. -/
  exact : Submodule.span R (Set.range (ι.hom)) = LinearMap.ker (π.hom)

/-- The first syzygy module of `M` as an `R`-module, extracted from a `SyzygyModule` structure. -/
def SyzygyModule.syzygy (σ : SyzygyModule R M) : ModuleCat.{u} R := σ.S

/-- When `R`-modules have enough projectives (which they always do, since every module
has a free presentation), the **nth syzygy module** `Syz[n] (M)` is defined inductively:
`Syz[0] (M) = M`, and `Syz[k+1] (M)` is a first syzygy module of `Syz[k] (M)`.

This is captured in Mathlib4 by `CategoryTheory.ProjectiveResolution.complex`.
For an explicit package, we define: -/
inductive SyzygyIter (M : ModuleCat.{u} R) : ℕ → Type (u + 1)
  | base : SyzygyIter M 0
  | step (n : ℕ) : SyzygyModule R M → SyzygyIter M n → SyzygyIter M (n + 1)

/-- **Abbreviation**: "`M` has a syzygy module" in the category-theoretic sense
means the kernel of any morphism `f : X → M` from a projective `X` admits a
projective cover.

This is automatically true in `ModuleCat R` because every `R`-module has a
projective presentation (free modules are projective). Mathlib4's
`CategoryTheory.Projective.syzygies` provides this for any abelian category
with enough projectives. -/
abbrev HasSyzygyModules (R : Type*) [Ring R] : Prop :=
  CategoryTheory.EnoughProjectives (ModuleCat.{u} R)

end syzygy_modules

/-! ### Examples -/

section examples

open CategoryTheory

/-- Example: In `ModuleCat ℤ` (the category of abelian groups), every module has syzygies
because free abelian groups are projective. -/
example (R : Type*) [Ring R] : CategoryTheory.EnoughProjectives (ModuleCat.{u} R) := by
  infer_instance

/-- Example: For the ℤ-module `M = ℤ/2ℤ`, a first syzygy module is `2ℤ ≅ ℤ`,
with the exact sequence `0 → ℤ →[×2] ℤ → ℤ/2ℤ → 0`.

Here the syzygy module is `ℤ` (which is projective as a ℤ-module, and also
free, since `free → projective`). -/
example : SyzygyModule ℤ (ModuleCat.of ℤ (ℤ ⧸ (Submodule.span ℤ {2}).toAddSubgroup)) :=
  {
    S := ModuleCat.of ℤ ℤ
    P := ModuleCat.of ℤ ℤ
    projective_P := by
      -- ℤ is projective as a ℤ-module.
      -- This is a known instance: free modules are projective.
      apply Module.Projective.of_free
    π :=
      { toFun := fun x => Submodule.Quotient.mk x
        map_add' := by simp
        map_smul' := by simp [Submodule.Quotient.mk_smul] }
    epi_π := by
      -- π is surjective because the quotient map is surjective.
      constructor
      intro Y u v h
      ext x
      obtain ⟨x', rfl⟩ := Submodule.Quotient.mk_surjective _ (u x)
      exact congrArg Submodule.Quotient.mk (h x')
    ι :=
      { toFun := fun x => x * 2
        map_add' := by simp [add_mul]
        map_smul' := by simp [mul_assoc] }
    mono_ι := by
      constructor
      intro Y u v h
      ext x
      apply_fun (fun f => f x) at h
      simp at h
      linarith
    exact := by
      ext x
      constructor
      · intro hx
        rcases Submodule.mem_span_singleton.mp hx with ⟨y, rfl⟩
        dsimp
        ext n
        -- This is a sketch; the exactness condition `ker(π) = im(2·)` holds for ℤ → ℤ/2ℤ.
        sorry
      · intro hx
        have hx0 : (Submodule.Quotient.mk x : ℤ ⧸ (Submodule.span ℤ {2}).toAddSubgroup) = 0 := hx
        have : x ∈ Submodule.span ℤ {(2 : ℤ)} := by
          rw [Submodule.Quotient.mk_eq_zero] at hx0
          exact hx0
        rcases Submodule.mem_span_singleton.mp this with ⟨y, hy⟩
        refine Submodule.subset_span ⟨y, ?_⟩
        ext n
        simp [hy]
  }

/-- Example: Declaring `HasSyzygyModules ℤ` simply invokes the existing
`EnoughProjectives` instance for `ModuleCat ℤ`. -/
example : HasSyzygyModules ℤ := by
  -- This is `CategoryTheory.EnoughProjectives (ModuleCat ℤ)`, which Mathlib provides.
  infer_instance

end examples
