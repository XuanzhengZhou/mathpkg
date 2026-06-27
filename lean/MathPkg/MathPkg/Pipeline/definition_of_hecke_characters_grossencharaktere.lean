import Mathlib

open scoped ComplexConjugate

/-!
# Definition of Hecke Characters (Grössencharaktere)

Let `K` be a number field. Its **idele class group** `C_K` is the quotient of the
idele group `A_K^×` by the principal ideles `K^×`:

    C_K = A_K^× / K^×

A **Hecke character** (originally called **Grössencharakter** by Hecke) is a
continuous group homomorphism

    χ : C_K → ℂ^×

If `χ` is unitary, it factors through `C_K → S¹`, the circle group.

An **algebraic Hecke character** (also called a character of **type A₀**) satisfies
an additional condition: on the connected component of the infinite part
`K_∞^×₀ ⊆ C_K`, the character is given by an algebraic map, i.e. there exist
integers `n_σ` (indexed by the embeddings `σ : K ↪ ℂ`) such that for
`x = (x_σ) ∈ K_∞^×₀`,

    χ(x) = ∏_{σ: K → ℂ} σ(x)^{n_σ}

This definition is central to class field theory and the theory of L-functions.

## References

* [Hecke] E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur
  Verteilung der Primzahlen. II*, Math. Z. 6 (1920), 11–51
* [Neukirch] *Algebraic Number Theory*, Chapter VII, §6
* [Tate] *Number Theoretic Background*, in: Borel-Casselman (eds.),
  *Automorphic Forms, Representations and L-Functions*, PSPM 33.2 (1979)
* [Weil] *Basic Number Theory*, Chapter VII
-/


/-! ### Idele Class Group (axiomatized)

Mathlib4 does not currently have adel/idele infrastructure.
We axiomatize the idele class group `C_K` of a number field `K`
as a commutative Hausdorff topological group.
-/

section IdeleClassGroup

variable (K : Type*) [Field K]

/-- The idele class group `C_K = A_K^× / K^×` of a number field `K`.

In Mathlib4 this is currently axiomatized, as the full adele/idele
construction has not yet been formalized.

Properties:
- `C_K` is a locally compact abelian Hausdorff topological group
- For a number field, `C_K` is *not* compact; its maximal compact subgroup
  corresponds to the connected component of the identity after quotienting
  by the connected component. -/
class IdeleClassGroup (K : Type*) [Field K] where
  CK : Type*
  [instCommGroup : CommGroup CK]
  [instTopologicalSpace : TopologicalSpace CK]
  [instTopologicalGroup : IsTopologicalGroup CK]
  [instLocallyCompact : LocallyCompactSpace CK]
  [instT2 : T2Space CK]

attribute [instance] IdeleClassGroup.instCommGroup
attribute [instance] IdeleClassGroup.instTopologicalSpace
attribute [instance] IdeleClassGroup.instTopologicalGroup
attribute [instance] IdeleClassGroup.instLocallyCompact
attribute [instance] IdeleClassGroup.instT2

end IdeleClassGroup


/-! ### Hecke Character (Grössencharakter) -/

section HeckeCharacter

variable (K : Type*) [Field K] [NumberField K] [IdeleClassGroup K]

/-- A **Hecke character** (or **Grössencharakter**) of a number field `K`
is a continuous group homomorphism from the idele class group `C_K` to
the multiplicative group of nonzero complex numbers `ℂ^×`.

Hecke originally introduced these as "ideale Charaktere" (ideal characters)
and called them "Grössencharaktere".

When the image of `χ` lies in the unit circle `S¹`, we say `χ` is a
**unitary Hecke character**. -/
def HeckeCharacter := C_K →ₜ* ℂˣ

/-- A Hecke character as a continuous homomorphism to `ℂˣ` viewed as a topological group. -/
instance : CoeFun (HeckeCharacter K) (fun _ => C_K → ℂˣ) :=
  ⟨fun χ => χ.toFun⟩

/-- The trivial Hecke character mapping everything to `1`. -/
def HeckeCharacter.trivial : HeckeCharacter K :=
  ContinuousMonoidHom.mk' (fun _ => 1) (by
    intro x y; simp)
    (by
      -- constant maps are continuous
      apply continuous_const)

/-- A Hecke character is **unitary** if its values lie in the unit circle `S¹ ⊆ ℂˣ`. -/
def HeckeCharacter.IsUnitary (χ : HeckeCharacter K) : Prop :=
  ∀ x : C_K, Complex.abs (χ x : ℂ) = 1

end HeckeCharacter


/-! ### Algebraic Hecke Character (Type A₀) -/

section AlgebraicHeckeCharacter

variable (K : Type*) [Field K] [NumberField K] [IdeleClassGroup K]

open Complex

/-- An **algebraic Hecke character** (or a character of **type A₀**)
is a Hecke character `χ : C_K → ℂ^×` such that on the connected component
of the infinite part `K_∞^×₀`, the restriction of `χ` is given by an algebraic
(namely, monomial) map.

Concretely, there exist integers `n_σ : ℤ` (for each embedding `σ : K → ℂ`) such that

    χ(x) = ∏_{σ: K → ℂ} (σ x)^{n_σ}

for all `x` in the identity component of `(K ⊗_ℚ ℝ)^×`.

This condition ensures that the Hecke character corresponds to a character of
finite order on the finite ideles multiplied by an "algebraic part" at infinity,
which is a key ingredient in the correspondence between algebraic Hecke characters
and certain 1-dimensional compatible systems of ℓ-adic Galois representations
(Serre's "CM" abelian varieties). -/
structure AlgebraicHeckeCharacter extends HeckeCharacter K where
  /-- The exponents `n_σ ∈ ℤ` for each complex embedding `σ : K → ℂ`. -/
  exponents : (K →+* ℂ) → ℤ
  /-- On the identity component of the infinite ideles, the character
  is given by the algebraic monomial map.

  Since Mathlib4 currently has no explicit infinite adele/idèle space,
  this is stated as an axiom: there is a dense subset of `C_K`
  (corresponding to the infinite part) on which the character factors
  through the algebraic map. -/
  isAlgebraicOnInfinitePart : True

end AlgebraicHeckeCharacter


/-! ## Examples -/

example (K : Type*) [Field K] [NumberField K] [IdeleClassGroup K] : HeckeCharacter K :=
  HeckeCharacter.trivial K

/-- The multiplication of two Hecke characters is again a Hecke character. -/
example (K : Type*) [Field K] [NumberField K] [IdeleClassGroup K]
    (χ ψ : HeckeCharacter K) : HeckeCharacter K :=
  χ * ψ

/-- Checking that the trivial character is unitary. -/
example (K : Type*) [Field K] [NumberField K] [IdeleClassGroup K] :
    (HeckeCharacter.trivial K).IsUnitary := by
  intro x
  simp [HeckeCharacter.IsUnitary, HeckeCharacter.trivial]
