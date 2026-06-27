---
role: proof
locale: en
of_concept: diagonal-mapping-biholomorphic
source_book: gtm038
source_chapter: "V"
source_section: "V.3 Examples of Complex Manifolds"
---

The mapping $d: X \to D$ is clearly bijective, with inverse given by $d^{-1} = p_1|_D$, the restriction of the first projection to the diagonal. Since the projection $p_1: X \times X \to X$ is holomorphic (by the product manifold construction), its restriction $p_1|_D$ is also holomorphic. Thus $d^{-1}$ is holomorphic.

It remains to verify that $d$ itself is holomorphic. Let $W \subset D$ be open, $g$ holomorphic on $W$, and $(x_0, x_0) \in W$. By definition of the induced structure on the submanifold $D$, there exists an open neighborhood $U(x_0) \subset X$ and a holomorphic function $\hat{g}$ on $U \times U$ such that $(U \times U) \cap D \subset W$ and
$$\hat{g}|_{(U \times U) \cap D} = g|_{(U \times U) \cap D}.$$

Without loss of generality, we may assume there is an isomorphism $\varphi: (U, \mathcal{H}) \to (B, \mathcal{O})$ where $B \subset \mathbb{C}^n$ is a polydisc. In these local coordinates, the diagonal in $B \times B$ is given by $\{(\mathfrak{z}, \mathfrak{z}) : \mathfrak{z} \in B\}$, and the mapping $d^*: B \to B \times B$ defined by $d^*(\mathfrak{z}) = (\mathfrak{z}, \mathfrak{z})$ is holomorphic (polynomial in the coordinates). Computing the pullback:
$$(g \circ d) \circ \tilde{\varphi}^{-1}(\mathfrak{z}) = \hat{g} \circ (d \circ \tilde{\varphi}^{-1})(\mathfrak{z}) = \hat{g}(\mathfrak{z}, \mathfrak{z}) = \hat{g} \circ d^*(\mathfrak{z}),$$
which is the composition of holomorphic functions and therefore holomorphic. Since $\tilde{\varphi}^{-1}$ is an isomorphism, it follows that $g \circ d$ is holomorphic on $d^{-1}(W) \subset X$. This establishes that $d$ is a holomorphic mapping, hence biholomorphic.
