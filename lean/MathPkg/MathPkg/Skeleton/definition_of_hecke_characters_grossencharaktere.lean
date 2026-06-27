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

/-- The `CommGroup` instance for the idele class group `CK`. -/
instance (K : Type*) [Field K] [IdeleClassGroup K] : CommGroup (IdeleClassGroup.CK K) :=
  (by infer_instance : IdeleClassGroup K).instCommGroup

/-- The `TopologicalSpace` instance for `CK`. -/
instance (K : Type*) [Field K] [IdeleClassGroup K] : TopologicalSpace (IdeleClassGroup.CK K) :=
  (by infer_instance : IdeleClassGroup K).instTopologicalSpace

/-- The `IsTopologicalGroup` instance for `CK`. -/
instance (K : Type*) [Field K] [IdeleClassGroup K] : IsTopologicalGroup (IdeleClassGroup.CK K) :=
  (by infer_instance : IdeleClassGroup K).instTopologicalGroup

/-- The `LocallyCompactSpace` instance for `CK`. -/
instance (K : Type*) [Field K] [IdeleClassGroup K] : LocallyCompactSpace (IdeleClassGroup.CK K) :=
  (by infer_instance : IdeleClassGroup K).instLocallyCompact

/-- The `T2Space` instance for `CK`. -/
instance (K : Type*) [Field K] [IdeleClassGroup K] : T2Space (IdeleClassGroup.CK K) :=
  (by infer_instance : IdeleClassGroup K).instT2

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
def HeckeCharacter := IdeleClassGroup.CK K →ₜ* ℂˣ

/-- A Hecke character as a continuous homomorphism to `ℂˣ` viewed as a topological group. -/
instance : CoeFun (HeckeCharacter K) (fun _ => IdeleClassGroup.CK K → ℂˣ) := by
  sorry
