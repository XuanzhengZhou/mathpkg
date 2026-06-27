---
role: proof
locale: en
of_concept: transitivity-of-different-and-discriminant
source_book: gtm028
source_chapter: "V"
source_section: "§11. Different and discriminant"
---

For the different formula, introduce the least normal extension $K^*$ of $K$ containing $K''$ and the integral closure $R^*$ of $R$ in $K^*$. Working in the normal case where formulas for the different via ramification groups are available, the transitivity follows from the tower property of ramification groups.

Alternatively, using the complementary module definition: for a tower $K \subset K' \subset K''$, the trace satisfies $T_{K''/K} = T_{K'/K} \circ T_{K''/K'}$. From the definition $\mathcal{C}_{R''/R} = \{z \in K'' : T_{K''/K}(zR'') \subset R\}$, one obtains the relation $\mathcal{C}_{R''/R} = \mathcal{C}_{R''/R'} \cdot \mathcal{C}_{R'/R}$, where the product is interpreted appropriately as fractionary ideals.

Taking inverses gives the different formula. For the discriminant formula, apply the norm $N_{K''/K}$ to both sides of the different transitivity formula and use $N_{K''/K} = N_{K'/K} \circ N_{K''/K'}$ together with $N_{K''/K}(N_{K''/K'}(\mathfrak{D}_{R'/R})) = N_{K'/K}(\mathfrak{D}_{R'/R})^{[K'':K']}$.
