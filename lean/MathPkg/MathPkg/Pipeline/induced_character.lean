import Mathlib

/-!
# Induced Character

If a representation `ρ` of a group `G` has character `χ`, the character of the induced
representation $\rho^H$ is denoted $\chi^H$ and is called the **induced character**.

Given a group homomorphism `φ : G →* H` and a finite-dimensional `G`-representation `V`,
the induced character is the function `H → k` giving the trace of the induced `H`-action
on $k[H] \otimes_{k[G]} V$.

## Main definition

* `inducedCharacter φ ρ` : the induced character of a representation `ρ` of `G`
  along a group homomorphism `φ : G →* H`. Evaluated at `h : H`, this is
  `LinearMap.trace k` of the action of `h` on the induced representation space.

## References

* https://en.wikipedia.org/wiki/Induced_character
-/

noncomputable section

open Representation

variable {k G H : Type*} [Field k] [Group G] [Group H]
variable {V : Type*} [AddCommGroup V] [Module k V]

/-- The induced character of a finite-dimensional representation.
Given a group homomorphism `φ : G →* H` and a finite-dimensional `G`-representation `ρ`,
its induced character `inducedCharacter φ ρ` is the character of the induced
`H`-representation `Representation.ind φ ρ`. In representation theory texts this is
denoted $\chi^H$ or $\operatorname{Ind}_G^H(\chi)$. -/
noncomputable def inducedCharacter [Fintype G] [Fintype H]
    [Module.Finite k V] (φ : G →* H) (ρ : Representation k G V) : H → k :=
  fun h => LinearMap.trace k (IndV φ ρ) ((ind φ ρ) h)

/-- The induced character at a group element `h : H` equals the trace of the
action of `h` on the induced representation space. This is a restatement of the definition. -/
theorem inducedCharacter_apply [Fintype G] [Fintype H]
    [Module.Finite k V] (φ : G →* H) (ρ : Representation k G V) (h : H) :
    inducedCharacter φ ρ h = LinearMap.trace k (IndV φ ρ) ((ind φ ρ) h) :=
  rfl

/--
Example: the induced character of the trivial one-dimensional representation
is a well-defined function `H → k`.
-/
example [Fintype G] [Fintype H] (φ : G →* H) : True := by
  let ρ : Representation k G k := Representation.trivial k G (V := k)
  have h_type : H → k := inducedCharacter φ ρ
  trivial
