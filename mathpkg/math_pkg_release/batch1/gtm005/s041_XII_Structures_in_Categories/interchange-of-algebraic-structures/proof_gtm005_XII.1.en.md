---
role: proof
locale: en
of_concept: interchange-of-algebraic-structures
source_book: gtm005
source_chapter: "XII"
source_section: "1. Internal Categories"
---

Both $X$-objects and $Y$-objects are defined by finite-limit diagrams — they are models of finite-limit theories (essentially algebraic theories). An $X$-object in a category $\mathcal{C}$ consists of certain objects and morphisms in $\mathcal{C}$ satisfying commutative diagram conditions expressed entirely by finite limits (products, pullbacks, equalizers, terminal object).

When we consider an $X$-object in $Y\text{-}\mathbf{Obj}$, the structure involves two families of data:
- The $Y$-structure: objects and morphisms satisfying $Y$-axioms,
- The $X$-structure: further objects and morphisms satisfying $X$-axioms, with the requirement that all $X$-structure maps are $Y$-homomorphisms (i.e., lie in $Y\text{-}\mathbf{Obj}$).

Since finite limits in $Y\text{-}\mathbf{Obj}$ are computed pointwise (they are created by the forgetful functor to $\mathbf{Set}$ when $Y$ is a finite-limit theory), the same data can be reinterpreted as a $Y$-object in $X\text{-}\mathbf{Obj}$. The key point is that the commutativity conditions stating that $X$-structure maps are $Y$-homomorphisms are symmetric: they are exactly the same as the conditions stating that $Y$-structure maps are $X$-homomorphisms.

For the concrete example: a category object in $\mathbf{Grp}$ requires $C_0, C_1$ to be groups and $i, d_0, d_1, \gamma$ to be group homomorphisms. The group multiplication $m_0, m_1$ then give a functor $m: C \times C \to C$ because the homomorphism conditions on $i, d_0, d_1, \gamma$ are precisely the naturality conditions for $m$ with respect to the categorical structure. Conversely, given a group object in $\mathbf{Cat}$, functoriality of the multiplication ensures that the category structure maps are group homomorphisms.
