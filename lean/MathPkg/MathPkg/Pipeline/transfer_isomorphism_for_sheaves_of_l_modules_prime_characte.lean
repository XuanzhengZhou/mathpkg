import Mathlib

open CategoryTheory

/-!
# Transfer Isomorphism for Sheaves of L-Modules (Prime Characteristic)

Let ℱ be a sheaf of L-modules on X/G, where L is a field whose characteristic
is relatively prime to the order of G. Then the pullback map
π* : H^n(X/G; ℱ) → H^n(X; π*ℱ)^G
is an isomorphism of L-modules.

From the relations μ* ○ π*(b) = (ord G) b and π* ○ μ*(a) = Σ g*(a), the image
of π* lies in the G-invariants. Since ord G is invertible in L, multiplication
by ord G is an isomorphism, hence π* is injective and its image is exactly the
invariant subgroup, yielding the isomorphism.
-/

noncomputable section

universe u

variable {X : Type u} [TopologicalSpace X]
  (G : Type u) [Group G] [Fintype G] [MulAction G X] [ContinuousSMul G X]
  (L : Type u) [Field L]

/-- The `n`-th sheaf cohomology group `H^n(Y; ℱ)` of a topological space `Y`
with coefficients in a sheaf `ℱ` of `L`-modules, as an `L`-module. -/
def sheafCohomology (Y : Type u) [TopologicalSpace Y]
    (ℱ : TopCat.Sheaf (ModuleCat.{u} L) Y) (n : ℕ) : ModuleCat.{u} L := by
  sorry

/-- The pullback (inverse image) sheaf `π*ℱ` on `X`, where `π : X → X/G` is the
quotient map and `ℱ` is a sheaf of `L`-modules on `X/G`. -/
def pullbackSheaf (ℱ : TopCat.Sheaf (ModuleCat.{u} L) (Quotient (MulAction.orbitRel G X))) :
    TopCat.Sheaf (ModuleCat.{u} L) X := by
  sorry

/-- The subspace of `G`-invariants in the cohomology `H^n(X; ℱ)`, consisting of
cohomology classes fixed under the natural `G`-action induced by the `G`-action
on `X`. -/
def cohomologyInvariants {ℱ : TopCat.Sheaf (ModuleCat.{u} L) X} (n : ℕ) :
    ModuleCat.{u} L := by
  sorry

/-- The **transfer isomorphism** for sheaf cohomology of `L`-modules:
when `ringChar L` is coprime to `|G|`, the pullback map `π*` induces an
`L`-linear isomorphism between the degree-`n` sheaf cohomology of the quotient
space `X/G` (with coefficients in `ℱ`) and the `G`-invariant part of the
degree-`n` sheaf cohomology of `X` (with coefficients in the pullback sheaf `π*ℱ`).

Formally: `π* : H^n(X/G; ℱ) ≅ H^n(X; π*ℱ)^G`. -/
theorem transfer_isomorphism_for_sheaves_of_l_modules_prime_characte
    (h_coprime : ¬ ringChar L ∣ Fintype.card G)
    (n : ℕ)
    (ℱ : TopCat.Sheaf (ModuleCat.{u} L) (Quotient (MulAction.orbitRel G X))) :
    sheafCohomology G L (Quotient (MulAction.orbitRel G X)) ℱ n ≃ₗ[L]
    cohomologyInvariants G L (pullbackSheaf G L ℱ) n := by
  sorry
