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
structure VectorBundleHom where
  /-- The fiberwise linear map at each base point. -/
  toFun : (b : B) → E₁ b →ₗ[𝕜] E₂ b

/-- Notation `E₁ →ᵛ E₂` for a bundle map over the same base. -/
infixr:25 " →ᵛ " => VectorBundleHom

namespace VectorBundleHom

variable {𝕜 F₁ F₂ E₁ E₂}

/-- Apply a bundle map to a point in the total space of `E₁`, yielding a point in the
total space of `E₂`.  The projection is preserved by construction. -/
def applyTotal (f : VectorBundleHom 𝕜 F₁ F₂ E₁ E₂) (x : TotalSpace F₁ E₁) : TotalSpace F₂ E₂ :=
  TotalSpace.mk' F₂ x.proj (f.toFun x.proj x.2)

/-- The bundle map induced on total spaces is indeed fiber-preserving. -/
theorem applyTotal_proj (f : VectorBundleHom 𝕜 F₁ F₂ E₁ E₂) (x : TotalSpace F₁ E₁) :
    (f.applyTotal x).proj = x.proj :=
  rfl

/-- The identity bundle map. -/
def id : VectorBundleHom 𝕜 F₁ F₁ E₁ E₁ where
  toFun b := LinearMap.id

/-- Composition of two bundle maps. -/
def comp (g : VectorBundleHom 𝕜 F₂ F₃ E₂ E₃) (f : VectorBundleHom 𝕜 F₁ F₂ E₁ E₂) :
    VectorBundleHom 𝕜 F₁ F₃ E₁ E₃ where
  toFun b := (g.toFun b).comp (f.toFun b)

/-- Extensionality: two bundle maps are equal if they agree on all fibers. -/
theorem ext {f g : VectorBundleHom 𝕜 F₁ F₂ E₁ E₂} (h : ∀ b x, f.toFun b x = g.toFun b x) :
    f = g := by
  cases f; cases g; congr; ext b x; exact h b x

end VectorBundleHom

/-! ## Examples -/

section Examples

variable {𝕜 : Type*} [Semiring 𝕜]
  {B : Type*} {F : Type*} [AddCommMonoid F] [Module 𝕜 F]
  (E : B → Type*) [∀ x, AddCommMonoid (E x)] [∀ x, Module 𝕜 (E x)]

/-- Example: the zero bundle map sends every fiber element to zero. -/
example : VectorBundleHom 𝕜 F F E E where
  toFun b := 0

/-- Example: the identity bundle map. -/
example : VectorBundleHom 𝕜 F F E E where
  toFun b := LinearMap.id

/-- Example: for a trivial bundle `B × F`, scaling by a smooth function `φ : B → 𝕜`
gives a bundle map (fiberwise scalar multiplication). -/
example (φ : B → 𝕜) : VectorBundleHom 𝕜 F F (fun _ : B => F) (fun _ : B => F) where
  toFun b :=
    { toFun := fun v => φ b • v
      map_add' := fun x y => smul_add (φ b) x y
      map_smul' := fun r x => by
        simp [mul_smul, smul_comm r (φ b)] }

/-- Example: on the tangent bundle of a manifold (here modeled trivially),
scalar multiplication in each fiber by a constant `c : 𝕜` is a bundle map. -/
example (c : 𝕜) : VectorBundleHom 𝕜 F F E E where
  toFun b := c • LinearMap.id

/-- Example: for product bundles `E₁ × E₂` and `F₁ × F₂`, a block-diagonal
bundle map. -/
example {E₂ F₂ E₁₂ F₁₂ : B → Type*}
    [∀ x, AddCommMonoid (E₂ x)] [∀ x, Module 𝕜 (E₂ x)]
    [∀ x, AddCommMonoid (E₁₂ x)] [∀ x, Module 𝕜 (E₁₂ x)]
    [∀ x, AddCommMonoid (F₁₂ x)] [∀ x, Module 𝕜 (F₁₂ x)]
    (f₁ : VectorBundleHom 𝕜 F F₁₂ E E₁₂) (f₂ : VectorBundleHom 𝕜 F₂ F₁₂ E₂ F₁₂) :
    VectorBundleHom 𝕜 (F × F₂) (F₁₂ × F₁₂) (fun b => E b × E₂ b) (fun b => E₁₂ b × F₁₂ b) where
  toFun b :=
    { toFun := fun p => (f₁.toFun b p.1, f₂.toFun b p.2)
      map_add' := by
        intro x y
        simp [Prod.mk_add_mk, f₁.toFun, f₂.toFun]
      map_smul' := by
        intro r x
        simp [Prod.smul_mk, f₁.toFun, f₂.toFun] }

end Examples
