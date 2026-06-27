---
role: proof
locale: en
of_concept: theorem-8-anti-automorphism-scalar-product
source_book: gtm031
source_chapter: "IX"
source_section: "12"
---
By Theorem 6', we may assume $\mathfrak{L}(\mathfrak{R}' \mid \mathfrak{R}) \supseteq \mathfrak{A} \supseteq \mathfrak{J}(\mathfrak{R}' \mid \mathfrak{R})$ where $\mathfrak{R}$ and $\mathfrak{R}'$ are dual relative to a non-degenerate bilinear form $g$. Let $A'$ denote the transpose of $A$ relative to $g$. Then $A \mapsto A'$ is an anti-isomorphism of $\mathfrak{A}$ onto a ring $\mathfrak{A}'$ satisfying $\mathfrak{L}(\mathfrak{R} \mid \mathfrak{R}') \supseteq \mathfrak{A}' \supseteq \mathfrak{J}(\mathfrak{R} \mid \mathfrak{R}')$.

The mapping $A' \mapsto A\Psi$ is an isomorphism of $\mathfrak{A}'$ onto $\mathfrak{A}$. By Theorem 7, there exists a semi-linear transformation $V$ of the left vector space $\mathfrak{R}'$ (over $\Delta'$, the division ring anti-isomorphic to $\Delta$) onto the left vector space $\mathfrak{R}$ such that $A\Psi = V^{-1} A' V$ for all $A \in \mathfrak{A}$.

Define $h(x, y) = g(x, yV^{-1})$ for $x, y \in \mathfrak{R}$. Then $h$ is a scalar product in $\mathfrak{R}$ relative to the anti-automorphism $\alpha \mapsto \bar{\alpha} = \alpha^{v^{-1}t^{-1}}$ where $t: \Delta \to \Delta'$ is the fixed anti-isomorphism and $v$ is the automorphism associated with $V$. One verifies $h(x\alpha, y) = h(x, y)\bar{\alpha}$ and the non-degeneracy of $h$ follows from that of $g$ and the bijectivity of $V$.

To show $h$ is weakly hermitian, define $Q: \mathfrak{R} \to \mathfrak{R}$ as the mapping corresponding to the canonical isomorphism identifying $\mathfrak{R}$ with its double dual. One checks that $Q$ is $1$-$1$, onto, semi-linear with associated automorphism $a^2$, and satisfies $\overline{h(y, x)} = h(x, yQ)$. The verification that $\mathfrak{A} \subseteq \mathfrak{L}(\mathfrak{R} \mid \mathfrak{R})$ with transpose given by $\Psi$ follows from:
$$h(xA, y) = g(xA, yV^{-1}) = g(x, yV^{-1}A') = g(x, yV^{-1}A'VV^{-1}) = g(x, yA\Psi V^{-1}) = h(x, yA\Psi).$$
Similarly, any $F \in \mathfrak{J}(\mathfrak{R} \mid \mathfrak{R})$ has a transpose relative to $g$ and thus belongs to $\mathfrak{A}$.
