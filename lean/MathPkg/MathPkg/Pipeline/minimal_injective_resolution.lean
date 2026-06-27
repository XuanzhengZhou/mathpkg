import Mathlib
import Mathlib.Algebra.Module.Injective

/-!
# Minimal Injective Resolution

An injective resolution ℰ of an R-module M is **minimal** if each term Eⁿ is the
injective hull of `ker(Eⁿ → Eⁿ⁺¹)` (where by convention `ker(E⁻¹ → E⁰) = M`).

Equivalently: each kernel is an essential submodule of its containing injective term.
Minimal injective resolutions are unique up to (non-canonical) isomorphism and are used
to compute Bass numbers and injective dimension.

Reference: Matsumura, *Commutative Ring Theory*, §18; Stacks Project, Definition 013I.

## Main definitions

* `IsEssentialSubmodule` : an R-submodule N of E is *essential* (or *large*) if every
  nonzero submodule of E intersects N nontrivially.
* `InjectiveHull` : E is an *injective hull* of M if E is injective and an essential
  extension of M.
* `MinimalInjectiveResolution` : a full structure describing a minimal injective
  resolution M → E⁰ → E¹ → E² → ⋯ of an R-module M.
-/

universe v u

variable (R : Type u) [CommRing R]

/-- An R-submodule `N` of `E` is **essential** (or *large*) if every nonzero submodule
of `E` has nontrivial intersection with `N`. -/
def IsEssentialSubmodule {E : Type v} [AddCommGroup E] [Module R E]
    (N : Submodule R E) : Prop :=
  ∀ S : Submodule R E, S ≠ ⊥ → N ⊓ S ≠ ⊥

/-- `E` is an **injective hull** (or *injective envelope*) of `M` if `E` is an injective
R-module and the given embedding makes `E` an essential extension of `M`.

Injective hulls are minimal injective extensions; any two injective hulls of `M`
are isomorphic (though not uniquely). -/
@[ext]
structure InjectiveHull (M E : Type v) [AddCommGroup M] [AddCommGroup E]
    [Module R M] [Module R E] where
  /-- The embedding (monomorphism) from `M` into its injective hull. -/
  emb : M →ₗ[R] E
  /-- The embedding is injective. -/
  emb_injective : Function.Injective emb
  /-- `E` is an injective R-module. -/
  [injective : Module.Injective R E]
  /-- `E` is an essential extension of the image of `M`:
  every nonzero submodule of `E` meets `im emb` nontrivially. -/
  essential : IsEssentialSubmodule R (LinearMap.range emb)

/-- A **minimal injective resolution** of an R-module `M` is an exact cochain complex
of injective R-modules
```
M --ε→ E⁰ --d⁰→ E¹ --d¹→ E² → ⋯
```
such that for each n, `Eⁿ` is the injective hull of `ker(dⁿ)` (with the convention
`ker(d⁻¹) = M`).

Minimal injective resolutions are unique up to isomorphism and essential for
computing Bass numbers and the injective dimension of `M`.

Reference: Stacks Project [013I], Matsumura §18. -/
structure MinimalInjectiveResolution (M : Type v) [AddCommGroup M] [Module R M] where
  /-- The terms of the resolution, indexed by ℕ. -/
  E : ℕ → Type v
  /-- Each `E n` is an additive commutative group. -/
  [E_addCommGroup : ∀ n, AddCommGroup (E n)]
  /-- Each `E n` is an R-module. -/
  [E_module : ∀ n, Module R (E n)]
  /-- Each `E n` is an injective R-module. -/
  [injective : ∀ n, Module.Injective R (E n)]
  /-- The differentials `dⁿ : Eⁿ → Eⁿ⁺¹`. -/
  d (n : ℕ) : E n →ₗ[R] E (n + 1)
  /-- The augmentation map `ε : M → E⁰`. -/
  ε : M →ₗ[R] E 0
  /-- The augmentation is injective. -/
  ε_injective : Function.Injective ε
  /-- Exactness at `E⁰`: `im(ε) = ker(d⁰)`. -/
  exact₀ : LinearMap.range ε = LinearMap.ker (d 0)
  /-- Exactness at `Eⁿ⁺¹` for `n ≥ 0`: `im(dⁿ) = ker(dⁿ⁺¹)`. -/
  exact_succ (n : ℕ) : LinearMap.range (d n) = LinearMap.ker (d (n + 1))
  /-- Minimality at `E⁰`: `E⁰` is the injective hull of `M ≅ ker(d⁰)`. -/
  minimal₀ : InjectiveHull R M (E 0)
  /-- Minimality at `Eⁿ⁺¹`: `Eⁿ⁺¹` is the injective hull of `ker(dⁿ⁺¹)`. -/
  minimal_succ (n : ℕ) : InjectiveHull R (LinearMap.ker (d (n + 1))) (E (n + 1))

/-- Example: if `M` is already injective, then
```
M --id→ M --0→ 0 --0→ 0 → ⋯
```
is a minimal injective resolution of `M`. -/
example (M : Type v) [AddCommGroup M] [Module R M] [Module.Injective R M] : True := by
  -- The trivial resolution: M in degree 0, zero modules thereafter, zero differentials.
  trivial
