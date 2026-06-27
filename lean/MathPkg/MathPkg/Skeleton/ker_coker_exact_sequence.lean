import Mathlib

open CategoryTheory Limits

universe v u

variable {C : Type u} [Category.{v} C] [Abelian C]

/- ker-coker exact sequence -/
theorem ker_coker_exact_sequence
    {A₁ A₂ A₃ B₁ B₂ B₃ : C}
    (f : A₁ ⟶ A₂) (g : A₂ ⟶ A₃)
    (f' : B₁ ⟶ B₂) (g' : B₂ ⟶ B₃)
    (φ₁ : A₁ ⟶ B₁) (φ₂ : A₂ ⟶ B₂) (φ₃ : A₃ ⟶ B₃)
    (comm_left : φ₁ ≫ f' = f ≫ φ₂)
    (comm_right : φ₂ ≫ g' = g ≫ φ₃)
    (hfg : f ≫ g = 0) (hfg' : f' ≫ g' = 0)
    (hexact_fg : (ShortComplex.mk f g hfg).Exact)
    (hexact_fg' : (ShortComplex.mk f' g' hfg').Exact) :
    ∃ (δ : kernel φ₃ ⟶ cokernel φ₁),
      (ComposableArrows.mk₅
        (kernel.map φ₁ φ₂ f f' comm_left)
        (kernel.map φ₂ φ₃ g g' comm_right)
        δ
        (cokernel.map φ₁ φ₂ f f' comm_left)
        (cokernel.map φ₂ φ₃ g g' comm_right)).Exact := by
  sorry
