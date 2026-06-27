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
def contravariantFunctorFromTo (C D : Type u₁) [Category.{v₁} C] [Category.{v₁} D] :=
  Cᵒᵖ ⥤ D

/--
The induced covariant functor `S̄ : Cᵒᵖ → D` from a contravariant functor `S : C → D`.

In Mathlib4, `S` is already `Cᵒᵖ ⥤ D`, so `S̄ := S`.  This is the identity map.
-/
noncomputable def inducedCovariant (S : Cᵒᵖ ⥤ D) : Cᵒᵖ ⥤ D := S

/--
The converse direction: from a covariant functor `T : Cᵒᵖ → D`, construct a
contravariant functor `S : C → D`.  Again, `S := T` in Mathlib4.
-/
noncomputable def inducedContravariant (T : Cᵒᵖ ⥤ D) : Cᵒᵖ ⥤ D := T

/--
The correspondence is a bijection: applying `inducedCovariant` then
`inducedContravariant` (or vice versa) recovers the original functor.

Concretely:
* If you start with a contravariant functor `S`, obtain `S̄` and then turn `S̄`
  back into a contravariant functor, you get `S`.
* If you start with a covariant functor `T` on `Cᵒᵖ`, obtain the associated
  contravariant functor and then the induced covariant functor, you get `T`.
-/
theorem correspondence_between_contravariant_and_covariant_functors :
    Function.Bijective (id : (Cᵒᵖ ⥤ D) → (Cᵒᵖ ⥤ D)) := by
  refine ⟨?_, ?_⟩
  · intro f g h
    exact h
  · intro f
    exact ⟨f, rfl⟩

/-- Round-trip: starting from a contravariant functor `S`, the induced covariant
functor `S̄` satisfies `S̄ = S` (definitional equality in Mathlib4). -/
example (S : Cᵒᵖ ⥤ D) : inducedCovariant S = S := rfl

/-- Round-trip: starting from a covariant functor `T` on `Cᵒᵖ`, the induced
contravariant functor satisfies `S = T` (definitional equality in Mathlib4). -/
example (T : Cᵒᵖ ⥤ D) : inducedContravariant T = T := rfl

/-- The two constructions (`S ↦ S̄` then inverse) compose to the identity. -/
example (S : Cᵒᵖ ⥤ D) : inducedContravariant (inducedCovariant S) = S := rfl

/-- The two constructions in reverse order also compose to the identity. -/
example (T : Cᵒᵖ ⥤ D) : inducedCovariant (inducedContravariant T) = T := rfl

end correspondence

section explicit_operation

/-! ### The operation of a contravariant functor on objects and morphisms

We show how the functorial action of `Cᵒᵖ ⥤ D` encodes exactly the
contravariant behaviour: it sends `f : A ⟶ B` in `C` to a map `S(B) ⟶ S(A)` in `D`.
-/

variable (C D)

/-- A contravariant functor acts on objects of `C` by assigning objects of `D`. -/
example (S : Cᵒᵖ ⥤ D) (A : C) : D :=
  S.obj (Opposite.op A)

/-- A contravariant functor `S` sends a morphism `f : A ⟶ B` in `C` to a morphism
`S(B) ⟶ S(A)` in `D`.  This is the contravariance: the direction is reversed. -/
example (S : Cᵒᵖ ⥤ D) {A B : C} (f : A ⟶ B) : S.obj (Opposite.op B) ⟶ S.obj (Opposite.op A) :=
  S.map f.op

/-- The contravariant functor preserves identities. -/
example (S : Cᵒᵖ ⥤ D) (A : C) : S.map (𝟙 (Opposite.op A)) = 𝟙 (S.obj (Opposite.op A)) :=
  S.map_id (Opposite.op A)

/-- The contravariant functor reverses composition:
in `Cᵒᵖ` the composition `g.op ≫ f.op` (for `f : A → B`, `g : B → C` in `C`)
is mapped to `S.map g.op ≫ S.map f.op`, which is `S(f ≫ g) = S(g) ∘ S(f)` in `C`. -/
example (S : Cᵒᵖ ⥤ D) {A B C : C} (f : A ⟶ B) (g : B ⟶ C) :
    S.map (g.op ≫ f.op) = S.map g.op ≫ S.map f.op :=
  S.map_comp g.op f.op

end explicit_operation

section categorical_interpretation

/-! ### Categorical interpretation

A contravariant functor `S : Cᵒᵖ ⥤ D` is equivalently a covariant functor `C ⥤ Dᵒᵖ`
via `Functor.rightOp`.  This provides a second correspondence:

`(Cᵒᵖ ⥤ D)  ≃  (C ⥤ Dᵒᵖ)`
-/

variable (C) (D)

/-- `Functor.rightOp` turns `Cᵒᵖ ⥤ D` into `C ⥤ Dᵒᵖ`.
This is another way to see the correspondence: a contravariant functor `C → D`
(represented as `Cᵒᵖ ⥤ D`) can also be viewed as a covariant functor `C → Dᵒᵖ`. -/
example (F : Cᵒᵖ ⥤ D) : C ⥤ Dᵒᵖ :=
  F.rightOp

/-- `Functor.leftOp` turns `C ⥤ Dᵒᵖ` back into `Cᵒᵖ ⥤ D`. -/
example (F : C ⥤ Dᵒᵖ) : Cᵒᵖ ⥤ D :=
  F.leftOp

/-- `rightOp` and `leftOp` are mutually inverse isomorphisms of functors:
`F.rightOp.leftOp ≅ F`. -/
example (F : Cᵒᵖ ⥤ D) : F.rightOp.leftOp ≅ F :=
  F.rightOpLeftOpIso

/-- `leftOp` and `rightOp` are mutually inverse isomorphisms of functors:
`F.leftOp.rightOp ≅ F`. -/
example (F : C ⥤ Dᵒᵖ) : F.leftOp.rightOp ≅ F :=
  F.leftOpRightOpIso

/-- `rightOp_leftOp_eq` gives a strict equality (not just isomorphism)
when the functor is defined definitionally.  In practice the isomorphism is preferred. -/
example (F : Cᵒᵖ ⥤ D) : F.rightOp.leftOp = F := by
  rw [F.rightOp_leftOp_eq]

/-- The equivalence of functor categories `(Cᵒᵖ ⥤ D)ᵒᵖ ≌ C ⥤ Dᵒᵖ` from Mathlib4. -/
example : (Cᵒᵖ ⥤ D)ᵒᵖ ≌ C ⥤ Dᵒᵖ :=
  Functor.leftOpRightOpEquiv (C := C) (D := D)

end categorical_interpretation

section concrete_categories

/-! ### Concrete example: the contravariant Hom functor

A prototypical contravariant functor is `Hom(-, X) : Cᵒᵖ ⥤ Type v₁`, which sends
an object `A` (viewed as `Opposite.op A` in `Cᵒᵖ`) to the set of morphisms `A ⟶ X`
and a morphism `f.op : B.op → A.op` (where `f : A → B` in `C`) to the
precomposition map `(-) ∘ f : (B ⟶ X) → (A ⟶ X)`.

In Mathlib4 this is the Yoneda embedding restricted to a single object.
-/

open Opposite

/-- The contravariant Hom functor `Hom(-, X) : Cᵒᵖ ⥤ Type v₁`.
Uses Mathlib's `yoneda` which is `C ⥤ Cᵒᵖ ⥤ Type v₁`. -/
def contravariantHom (X : C) : Cᵒᵖ ⥤ Type v₁ :=
  yoneda.obj X

/-- On objects, `contravariantHom X` sends `A` to `A.unop ⟶ X`. -/
example (X : C) (A : Cᵒᵖ) : (contravariantHom X).obj A = (A.unop ⟶ X) := rfl

/-- On morphisms, `contravariantHom X` acts by precomposition.
For `f : A ⟶ B` in `C`, the associated morphism `f.op` in `Cᵒᵖ`
is mapped to `(-) ∘ f : (B ⟶ X) → (A ⟶ X)`. -/
example (X : C) {A B : C} (f : A ⟶ B) :
    (yoneda.obj X).map f.op = (fun (g : B ⟶ X) => f ≫ g) := by
  ext g
  simp

end concrete_categories