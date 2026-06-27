import Mathlib

open CategoryTheory

universe v u

variable {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜]

/- ker-coker exact sequence -/
theorem ker_coker_exact_sequence
    {A₁ A₂ A₃ B₁ B₂ B₃ : 𝒜}
    (f : A₁ ⟶ A₂) (g : A₂ ⟶ A₃)
    (f' : B₁ ⟶ B₂) (g' : B₂ ⟶ B₃)
    (φ₁ : A₁ ⟶ B₁) (φ₂ : A₂ ⟶ B₂) (φ₃ : A₃ ⟶ B₃)
    (comm_left : φ₁ ≫ f' = f ≫ φ₂)
    (comm_right : φ₂ ≫ g' = g ≫ φ₃)
    (hfg : f ≫ g = 0) (hfg' : f' ≫ g' = 0)
    (hexact_fg : Exact f g) (hexact_fg' : Exact f' g') :
    ∃ (δ : kernel φ₃ ⟶ cokernel φ₁),
      Exact (kernel.map φ₁ φ₂ f f' comm_left) (kernel.map φ₂ φ₃ g g' comm_right) ∧
      Exact (kernel.map φ₂ φ₃ g g' comm_right) δ ∧
      Exact δ (cokernel.map φ₁ φ₂ f f' comm_left) ∧
      Exact (cokernel.map φ₁ φ₂ f f' comm_left) (cokernel.map φ₂ φ₃ g g' comm_right) := by
  sorry
