---
role: proof
locale: en
of_concept: different-discriminant-tower-formula
source_book: gtm028
source_chapter: "V"
source_section: "11"
---

For the different: By definition, $\mathfrak{D}_{R''/R}$ is the inverse of the complementary module $\mathcal{C}_{R''/R}$. For any $z \in K''$, we have $T_{K''/K}(zR'') \subset R$ iff $T_{K'/K}(T_{K''/K'}(zR'')R') \subset R$, using transitivity of the trace. This yields $\mathcal{C}_{R''/R} = \mathcal{C}_{R''/R'} \cdot \mathcal{C}_{R'/R} R''$, and taking inverses gives the tower formula for the different.

For the discriminant: The discriminant is the norm of the different. Using the transitivity of the norm $N_{K''/K} = N_{K'/K} \circ N_{K''/K'}$ and the tower formula for the different, we obtain $\mathfrak{d}_{R''/R} = N_{K''/K}(\mathfrak{D}_{R''/R}) = N_{K'/K}(N_{K''/K'}(\mathfrak{D}_{R''/R'} \cdot \mathfrak{D}_{R'/R}R''))$. Since $N_{K''/K'}(\mathfrak{D}_{R'/R}R'') = \mathfrak{D}_{R'/R}^{[K'':K']}$, we get the stated formula.
