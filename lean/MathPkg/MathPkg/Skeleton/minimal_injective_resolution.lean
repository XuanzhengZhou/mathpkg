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
    (N : Submodule R E) : Prop := by
  sorry
