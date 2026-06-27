import Mathlib

/-!
# Bundle Map (Homomorphism) Between Vector Bundles

A **bundle map** (or **vector bundle homomorphism**) between two vector bundles `E₁` and `E₂`
over the same base space `B` is a fiber-preserving map `f : TotalSpace F₁ E₁ → TotalSpace F₂ E₂`
that is linear on corresponding fibers.

This means:
- For each `x` in the total space, `(f x).proj = x.proj` (fiber-preserving).
- For each `b ∈ B`, the restriction `f |_{E₁ b} : E₁ b → E₂ b` is 𝕜-linear.

We define this as a family of linear maps `∀ b, E₁ b →ₗ[𝕜] E₂ b`, which is the most natural
representation in Mathlib4's vector bundle framework. The induced map on total spaces
is obtained via `TotalSpace.map`.
-/

open Bundle

variable (𝕜 : Type*) [Semiring 𝕜]
  {B : Type*} (F₁ F₂ : Type*)
  (E₁ E₂ : B → Type*)
  [∀ x, AddCommMonoid (E₁ x)] [∀ x, Module 𝕜 (E₁ x)]
  [∀ x, AddCommMonoid (E₂ x)] [∀ x, Module 𝕜 (E₂ x)]

/-- A **bundle map** (or **vector bundle homomorphism**) between two vector bundles
`E₁` and `E₂` over the same base `B`.  It is a family of 𝕜-linear maps `E₁ b → E₂ b`,
one for each base point `b`.

This definition captures the algebraic core: fiberwise linearity and fiber-preservation.
When the bundles carry smooth structures, one additionally requires the map to be smooth
on the total spaces (see `ContMDiff` in Mathlib4). -/
abbrev VectorBundleHom := ∀ b, E₁ b →ₗ[𝕜] E₂ b

namespace VectorBundleHom

variable {𝕜 F₁ F₂ E₁ E₂}

/-- Apply a bundle map to a point in the total space of `E₁`, yielding a point in the
total space of `E₂`.  The projection is preserved by construction. -/
def applyTotal (f : VectorBundleHom 𝕜 E₁ E₂) (x : TotalSpace F₁ E₁) : TotalSpace F₂ E₂ := by
  sorry
