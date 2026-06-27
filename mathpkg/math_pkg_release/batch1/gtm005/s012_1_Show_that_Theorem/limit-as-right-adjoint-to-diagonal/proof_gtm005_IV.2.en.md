---
role: proof
locale: en
of_concept: limit-as-right-adjoint-to-diagonal
source_book: gtm005
source_chapter: "IV"
source_section: "2"
---

For a small category $J$, the diagonal functor $\Delta: C \to C^J$ sends $c$ to the constant functor $\Delta c: J \to C$ (all objects to $c$, all arrows to $1_c$). 

If every functor $F: J \to C$ has a limit, then $\varprojlim: C^J \to C$ is right adjoint to $\Delta$:
$$C^J(\Delta c, F) = \operatorname{Nat}(\Delta c, F) \cong C(c, \varprojlim F).$$
A natural transformation $\Delta c \Rightarrow F$ is precisely a cone over $F$ with vertex $c$, which corresponds uniquely to a morphism $c \to \varprojlim F$ by the universal property of the limit.

Dually, $\varinjlim \dashv \Delta$: $C(\varinjlim F, c) \cong \operatorname{Nat}(F, \Delta c)$.
