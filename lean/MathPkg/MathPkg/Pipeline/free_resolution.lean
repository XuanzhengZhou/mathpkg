import Mathlib

open AddMonoidHom

/-!
# Free Resolution

An exact sequence `0 → R → F → A → 0` of abelian groups in which `F` and `R` are free
is called a **free resolution** of `A`.

## Definition

A `FreeResolution` of an abelian group `A` consists of:
- Free abelian groups `F` and `R` (i.e., `Module.Free ℤ F` and `Module.Free ℤ R`)
- An injective homomorphism `φ : R →+ F`
- A surjective homomorphism `ψ : F →+ A`
- The exactness condition: `ker ψ = range φ`

The zero maps at the ends (`0 → R` and `A → 0`) are implicit: injectivity of `φ`
encodes `0 → R` is exact, and surjectivity of `ψ` encodes `A → 0` is exact.

## Mathlib4 references

- `AddMonoidHom` provides the homomorphism structure
- `AddMonoidHom.ker` and `AddMonoidHom.range` provide kernel and image
- `Module.Free ℤ M` states that `M` is a free ℤ-module (free abelian group)
- Mathlib already has `ProjectiveResolution` (in `CategoryTheory/Preadditive/Projective/Resolution.lean`)
  as a full ℕ-indexed chain complex — this is a more general categorical notion,
  whereas `FreeResolution` here is the simple concrete version for abelian groups
-/

universe u

/-- A free resolution of an abelian group `A` is a short exact sequence
`0 → R →-φ F →-ψ A → 0` where `F` and `R` are free abelian groups.

The data consists of:
- `F`, `R` : free abelian groups (`Module.Free ℤ`)
- `φ : R →+ F` : the first map (injective)
- `ψ : F →+ A` : the second map (surjective)
- `exact` : `ker ψ = range φ`
-/
structure FreeResolution (A : Type u) [AddCommGroup A] : Type (u + 1) where
  /-- The middle free abelian group `F`. -/
  (F : Type u)
  [strF : AddCommGroup F]
  [freeF : Module.Free ℤ F]
  /-- The left free abelian group `R`. -/
  (R : Type u)
  [strR : AddCommGroup R]
  [freeR : Module.Free ℤ R]
  /-- The map `φ` from the relation group `R` to `F`. -/
  (φ : R →+ F)
  /-- The map `ψ` from `F` onto `A`. -/
  (ψ : F →+ A)
  /-- `φ` is injective. -/
  (hφ_inj : Function.Injective φ)
  /-- `ψ` is surjective. -/
  (hψ_surj : Function.Surjective ψ)
  /-- Exactness at `F`: the kernel of `ψ` equals the image of `φ`. -/
  (exact : ψ.ker = φ.range)

attribute [instance] FreeResolution.strF FreeResolution.strR
attribute [instance] FreeResolution.freeF FreeResolution.freeR

section examples

open FreeAbelianGroup

/--
**Example 1**: A free abelian group `FreeAbelianGroup α` has a trivial free
resolution with `F = FreeAbelianGroup α` and `R = 0` (the zero group,
represented as `FreeAbelianGroup Empty`).

This corresponds to the short exact sequence
`0 → 0 → FreeAbelianGroup α →= FreeAbelianGroup α → 0`.
-/
example (α : Type u) : FreeResolution (FreeAbelianGroup α) where
  F := FreeAbelianGroup α
  R := FreeAbelianGroup Empty
  φ := 0
  ψ := .id (FreeAbelianGroup α)
  hφ_inj := by
    intro x y h
    apply FreeAbelianGroup.ext
    intro e
    exfalso
    exact e.elim
  hψ_surj := fun a => ⟨a, rfl⟩
  exact := by
    ext x
    constructor
    · intro hx
      rw [mem_ker, AddMonoidHom.id_apply] at hx
      subst hx
      exact ⟨0, map_zero _⟩
    · intro hx
      rcases mem_range.1 hx with ⟨y, rfl⟩
      simp

/--
**Example 2**: A free resolution of `ℤ` (the integers) as an abelian group.

Since `ℤ ≅ FreeAbelianGroup Unit`, we have the trivial resolution
`0 → 0 → ℤ →= ℤ → 0`.
-/
example : FreeResolution ℤ where
  F := ℤ
  R := FreeAbelianGroup Empty
  φ := 0
  ψ := .id ℤ
  hφ_inj := by
    intro x y h
    apply FreeAbelianGroup.ext
    intro e
    exact e.elim
  hψ_surj := fun a => ⟨a, rfl⟩
  exact := by
    ext x
    constructor
    · intro hx
      rw [mem_ker, AddMonoidHom.id_apply] at hx
      subst hx
      exact ⟨0, map_zero _⟩
    · intro hx
      rcases mem_range.1 hx with ⟨y, rfl⟩
      simp

/--
**Example 3**: A free resolution of the zero group `0`.

The zero group has the trivial resolution `0 → 0 → 0 → 0 → 0` where all
groups are the free abelian group on the empty set.
-/
example : FreeResolution (FreeAbelianGroup Empty) where
  F := FreeAbelianGroup Empty
  R := FreeAbelianGroup Empty
  φ := 0
  ψ := 0
  hφ_inj := by
    intro x y h
    apply FreeAbelianGroup.ext
    intro e
    exact e.elim
  hψ_surj := by
    intro a
    have ha : a = 0 := by
      apply FreeAbelianGroup.ext
      intro e
      exact e.elim
    subst ha
    exact ⟨0, map_zero _⟩
  exact := by
    ext x
    constructor
    · intro _
      exact ⟨0, map_zero _⟩
    · intro hx
      rcases mem_range.1 hx with ⟨y, rfl⟩
      simp

end examples
