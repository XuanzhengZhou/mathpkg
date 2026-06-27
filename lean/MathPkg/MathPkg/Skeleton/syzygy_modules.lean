import Mathlib
open CategoryTheory
open CategoryTheory.Limits

/-!
# Syzygy Modules

Given an exact sequence `0 → N → F → M → 0` with `F` projective, `N` is called a
**first syzygy module** of `M`. The nth syzygy module is defined inductively as the
first syzygy module of the (n−1)st syzygy module. Syzygy modules are unique up to
projective summands.

Mathlib4 defines `Projective.syzygies f` for any morphism `f : X ⟶ Y` in an abelian
category with enough projectives:
* `Projective.syzygies f : C` is a projective object over `kernel f`
* `Projective.d f : Projective.syzygies f ⟶ X` is the map `π (kernel f) ≫ kernel.ι f`

This file specializes the construction to `ModuleCat R`.
-/

universe u

/-- The first syzygy module of `M` in `ModuleCat R`, defined as the kernel of a
projective presentation `Projective.π M : Projective.over M ⟶ M`.

In Mathlib4, `Projective.syzygies (Projective.π M)` gives a projective object
covering `kernel (Projective.π M)`, which is the first syzygy. The first syzygy
itself is `kernel (Projective.π M)`. -/
noncomputable def FirstSyzygy (R : Type u) [Ring R] (M : ModuleCat.{u} R) :
    ModuleCat.{u} R := by
  sorry
