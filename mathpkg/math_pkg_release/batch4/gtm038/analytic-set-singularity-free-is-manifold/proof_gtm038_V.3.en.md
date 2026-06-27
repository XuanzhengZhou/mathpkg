---
role: proof
locale: en
of_concept: analytic-set-singularity-free-is-manifold
source_book: gtm038
source_chapter: "V"
source_section: "V.3 Examples of Complex Manifolds"
---

$A$, with the relative topology induced by $X$, is clearly a Hausdorff space. A function $f$ defined on an open set $W \subset A$ will be called holomorphic if for every $x \in W$ there is an open neighborhood $U(x) \subset X$ and a holomorphic function $\hat{f}$ on $U$ such that $U \cap A \subset W$ and $\hat{f}|_{U \cap A} = f|_{U \cap A}$.

By the preceding lemma, for every $x_0 \in A$ there exist an open neighborhood $U(x_0) \subset X$ and an isomorphism $\varphi_1: (U, \mathcal{H}) \to (B, \mathcal{O})$ with
$$\varphi_1(A \cap U) = \{w \in B: w_1 = \cdots = w_d = 0\}.$$
Since the set $\{w \in B: w_1 = \cdots = w_d = 0\}$ is naturally biholomorphic to an $(n-d)$-dimensional polydisc, the restriction $\varphi_1|_{A \cap U}$ provides a complex coordinate system on $A$ of dimension $n-d$. The compatibility of these coordinate systems follows from the fact that $\varphi_1$ is an isomorphism of ringed spaces: the transition maps are holomorphic because the coordinate changes are induced by the isomorphisms of the ambient complex manifold $X$.

It remains to verify that the natural imbedding $j_A: A \hookrightarrow X$ is holomorphic. Let $W \subset X$ be open and $g$ holomorphic on $W$. Then for every $x \in A \cap W$, the function $g \circ j_A = g|_A$ is holomorphic on $A$ by the definition above: take $U = W$ and $\hat{f} = g$. Conversely, the definition of holomorphic functions on $A$ ensures that the structure sheaf $\mathcal{H}_A$ is precisely the restriction of the structure sheaf $\mathcal{H}_X$ to $A$, so $j_A$ induces a morphism of ringed spaces. This establishes that $A$ is an $(n-d)$-dimensional complex manifold and $j_A$ is holomorphic.
