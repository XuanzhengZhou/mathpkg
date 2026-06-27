---
role: proof
locale: en
of_concept: galois-group-structure-iwasawa-theory
source_book: gtm059
source_chapter: "5"
source_section: "Iwasawa Theory and Ideal Class Groups"
---

We have an exact sequence

$$
1 \to G_1 \to G \to I \to 1
$$

where $G_1 = \operatorname{Gal}(M_\infty/K_1)$ and $I$ is the inertia group. The image of $I$ in $G_1$ by restriction to $K_1$ is surjective because $K_1$ is totally ramified over $K_0$. Moreover, $K_1$ is algebraic over $K_0$ and $M_\infty$ is unramified over $K_1$, so

$$
I \cap G_1 = \{1\}.
$$

This shows that $G$ is a semidirect product $G = G_1 \rtimes I$.

The group $I$ operates on $G_1$ by conjugation. Since $G_1$ is abelian (as the Galois group of an abelian extension), the commutator subgroup $[G, G]$ is contained in $G_1$, and $G^{\text{ab}} = G/[G,G]$ has $I$ as a quotient.

Furthermore, $G_1$ is the maximal $p$-primary abelian subgroup of $G$, and the inertia group $I$ is isomorphic to $\mathbb{Z}_p$ (being a quotient of the Galois group of the $\mathbb{Z}_p$-extension). Therefore $I \cong \mathbb{Z}_p$ operates on the finite $p$-group $G_n$, and for sufficiently large $n$, the restriction map gives an isomorphism. This completes the proof.
