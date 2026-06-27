---
role: proof
locale: en
of_concept: homomorphic-relation-isomorphism
source_book: gtm004
source_chapter: "VIII"
source_section: "7"
---

# Proof of Isomorphism Condition for the Homomorphic Relation $\Theta$

From Theorem 7.3 we have the limit diagram with exact rows and columns. In particular, looking at the rightmost column and the top row, it is evident that $\Gamma^+ \cong E_\infty$ via a natural isomorphism if and only if $\text{coker}\,\bar{\alpha}' = 0$ and $\ker \alpha'' = 0$. Indeed, if $\text{coker}\,\bar{\alpha}' = 0$ then $\bar{\beta}_*$ is monic, and if $\ker \alpha'' = 0$ then $\gamma_*$ is epic; together with the exactness of the diagram these force the natural map to be an isomorphism.

To make this statement precise, we introduce the notion of a **homomorphic relation** between two objects $X$ and $Y$ of an abelian category $\mathfrak{A}$: this is simply a subobject of $X \oplus Y$. From Theorem 7.3 we extract the exact sequence

$$\text{coker}\,\alpha' \xrightarrow{(\beta_*, \varphi^+)} E_\infty \oplus \Gamma^+ \xrightarrow{\langle \gamma_*, -\bar{\varphi}^+ \rangle} \ker \bar{\alpha}'',$$

obtained by combining the morphisms from the diagram. The image of $(\beta_*, \varphi^+)$ is a subobject of $E_\infty \oplus \Gamma^+$, hence defines a homomorphic relation

$$\Theta = \text{im}\{\beta_*, \varphi^+\}$$

from $E_\infty$ to $\Gamma^+$. Evidently $\Theta$ is natural, since all morphisms in the construction are natural.

Now a homomorphic relation can only be an isomorphism if it is actually the graph of a morphism (for the general theory of homomorphic relations, see [22]). This happens precisely when $\beta_*$ is an isomorphism and $\varphi^+$ is an isomorphism, which by the exactness of the limit diagram is equivalent to the vanishing of $\text{coker}\,\bar{\alpha}'$ and $\ker \alpha''$. Thus:

$$\Theta \text{ is an isomorphism} \iff \text{coker}\,\bar{\alpha}' = 0 \text{ and } \ker \alpha'' = 0.$$

Furthermore, in the case of a filtered (graded) differential object, these conditions translate to the concrete criteria (7.8): for all $p$,

$$I_p \cap \alpha^{-1}(0) = 0, \quad \bar{\alpha}' \bar{U}_p = \bar{U}_{p+1},$$

where $I_p$ consists of elements of filtration $-\infty$ (those in the image of $H_q(C^{(r)})$ for all $r \leq p$) and $\bar{U}_p$ encodes the stable elements of the cofiltration. $\square$
