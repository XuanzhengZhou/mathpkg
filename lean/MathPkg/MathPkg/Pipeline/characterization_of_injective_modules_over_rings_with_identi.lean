import Mathlib

open scoped Classical

/-!
# Characterization of Injective Modules over Rings with Identity (Baer's Criterion)

Let `R` be a ring with identity. A unitary `R`-module `J` is **injective** if and only if
for every left ideal `L` of `R`, any `R`-module homomorphism `f : L → J` may be extended to
an `R`-module homomorphism `R → J`.

Mathlib4 formalizes this in `Algebra/Module/Injective.lean`:
- `Module.Injective R Q` : the property that every injective linear map `X → Y` descends to `Q`
- `Module.Baer R Q` : the property that any linear map from an ideal extends to `R → Q`
- `Module.Baer.iff_injective` : Baer's criterion, establishing their equivalence

The proof uses Zorn's lemma (via `zorn_le_nonempty` from `Mathlib/Order/Zorn.lean`)
to find a maximal extension of the homomorphism.
-/

/-! ### Baer's Criterion from Mathlib4 -/

section baer_criterion

variable (R : Type u) [Ring R] (Q : Type v) [AddCommGroup Q] [Module R Q]

/-- **Baer's Criterion**: An `R`-module `Q` is injective if and only if it satisfies
Baer's criterion, i.e., every `R`-linear map from an ideal of `R` extends to `R`.

This is the main equivalence: `Module.Injective` ↔ `Module.Baer`. -/
theorem baer_criterion [Small.{v} R] :
    Module.Injective R Q ↔ Module.Baer R Q :=
  (Module.Baer.iff_injective (R := R) (Q := Q)).symm

/-- The forward direction: injective implies Baer. -/
example [Small.{v} R] (h : Module.Injective R Q) : Module.Baer R Q :=
  Module.Baer.of_injective h

/-- The reverse direction: Baer implies injective. -/
example [Small.{v} R] (h : Module.Baer R Q) : Module.Injective R Q :=
  Module.Baer.injective h

end baer_criterion

/-! ### Concrete examples with `ℤ`-modules -/

section examples_over_int

/-- Divisible abelian groups are Baer `ℤ`-modules.
For example, `ℚ` is a divisible group, hence satisfies Baer's criterion. -/
example : Module.Baer ℤ ℚ :=
  Module.Baer.of_divisible ℚ

/-- Since `ℚ` is a Baer `ℤ`-module, it is an injective `ℤ`-module. -/
example : Module.Injective ℤ ℚ :=
  (Module.Baer.of_divisible ℚ).injective

/-- The circle group `ℚ/ℤ` (i.e., `AddCircle (1 : ℚ)`) is a divisible abelian group
and hence an injective `ℤ`-module. -/
example : Module.Injective ℤ (AddCircle (1 : ℚ)) :=
  (Module.Baer.of_divisible (AddCircle (1 : ℚ))).injective

/-- By Baer's criterion, an injective `ℤ`-module is also a Baer `ℤ`-module. -/
example (h : Module.Injective ℤ ℚ) : Module.Baer ℤ ℚ :=
  Module.Baer.of_injective h

end examples_over_int

/-! ### Usage of the lifting/extension property -/

section extension_property

variable (R : Type u) [Ring R] [Small.{v} R]
variable (Q : Type v) [AddCommGroup Q] [Module R Q]
variable (M N : Type v) [AddCommGroup M] [AddCommGroup N] [Module R M] [Module R N]

/-- For a Baer module `Q`, any linear map `M → Q` extends along an injection `M → N`.
This is the extension property derived from Baer's criterion. -/
example (h : Module.Baer R Q) (f : M →ₗ[R] N) (hf : Function.Injective f) (g : M →ₗ[R] Q) :
    ∃ h' : N →ₗ[R] Q, h' ∘ₗ f = g :=
  Module.Baer.extension_property h f hf g

/-- The extension property also holds for `AddMonoidHom` over `ℤ`-modules
(using the additive version). -/
example (h : Module.Baer ℤ Q) (f : M →+ N) (hf : Function.Injective f) (g : M →+ Q) :
    ∃ h' : N →+ Q, h'.comp f = g :=
  Module.Baer.extension_property_addMonoidHom h f hf g

end extension_property

/-! ### Relationship with ideal extension property -/

section ideal_extension

/-- Baer's criterion in terms of surjectivity of the restriction map:
an `R`-module `M` over a commutative ring `R` is Baer iff for every ideal `I`,
the restriction map `Hom_R(R, M) → Hom_R(I, M)` is surjective. -/
example {R : Type u} [CommRing R] (M : Type v) [AddCommGroup M] [Module R M] :
    Module.Baer R M ↔ ∀ (I : Ideal R), Function.Surjective (LinearMap.lcomp R M I.subtype) :=
  Module.Baer.iff_surjective

end ideal_extension
