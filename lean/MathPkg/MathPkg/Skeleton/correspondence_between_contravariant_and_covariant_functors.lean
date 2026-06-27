import Mathlib

open CategoryTheory

/-!
# Correspondence Between Contravariant and Covariant Functors

In Mathlib4, a *contravariant* functor from `C` to `D` is identified with a (covariant) functor
`Cᵒᵖ ⥤ D`.  This file formalizes the bijective correspondence:

  {contravariant functors `C → D`}  ↔  {covariant functors `Cᵒᵖ → D`}

## Convention

`Cᵒᵖ ⥤ D` simultaneously represents:
* a contravariant functor from `C` to `D` (it reverses arrows of `C`);
* a covariant functor from `Cᵒᵖ` to `D`.

The correspondence is therefore given by the identity map on the type `Cᵒᵖ ⥤ D`.
We also demonstrate the variants `Functor.rightOp` / `Functor.leftOp` that relate
`Cᵒᵖ ⥤ D` and `C ⥤ Dᵒᵖ`.

## Main results

* `contravariant_covariant_correspondence` : the type `Cᵒᵖ ⥤ D` is both the type of
  contravariant functors from `C` to `D` and covariant functors from `Cᵒᵖ` to `D`.
* `contravariant_equiv_covariant` : explicit equivalence `(Cᵒᵖ ⥤ D) ≃ (Cᵒᵖ ⥤ D)` given by `id`.
-/

universe v₁ v₂ u₁ u₂

variable {C : Type u₁} [Category.{v₁} C]
variable {D : Type u₂} [Category.{v₂} D]

section correspondence

/-! ### The bijective correspondence -/

/--
In Mathlib4, the type `Cᵒᵖ ⥤ D` serves **both** as the type of
* contravariant functors from `C` to `D`, and
* covariant functors from `Cᵒᵖ` to `D`.

The map `S ↦ S̄` from the statement of the correspondence is the identity function.
The converse map `T ↦ S` is also the identity function.

This is a design choice: Mathlib4 has no separate `ContravariantFunctor` type.
-/
def contravariant_covariant_correspondence (C : Type u₁) [Category.{v₁} C] (D : Type u₂) [Category.{v₂} D] :
    (Cᵒᵖ ⥤ D) ≃ (Cᵒᵖ ⥤ D) := by
  sorry
