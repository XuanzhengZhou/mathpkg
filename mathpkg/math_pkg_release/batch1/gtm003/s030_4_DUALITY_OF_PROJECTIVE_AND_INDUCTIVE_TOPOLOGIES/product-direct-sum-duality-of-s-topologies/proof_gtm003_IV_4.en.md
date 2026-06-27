---
role: proof
locale: en
of_concept: product-direct-sum-duality-of-s-topologies
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

Let $p_\alpha: F \to F_\alpha$ be the projection and $q_\alpha: G_\alpha \to G$ the injection. For polars with respect to $\langle F_\alpha, G_\alpha \rangle$ denote by $^\circ_\alpha$, and with respect to $\langle F, G \rangle$ by $^\bullet$.

For $S \in \mathfrak{S}$ with $S \subset \bigoplus_{\alpha \in H} S_\alpha$, we compute its polar in $F$:
$$S^\bullet = \left\{ x \in F : \sum_{\alpha} |\langle x_\alpha, y_\alpha \rangle| \leq 1 \text{ for all } y \in S \right\}.$$

For $x = (x_\alpha) \in S^\bullet$, letting $\lambda_\alpha = \sup\{|\langle x_\alpha, y_\alpha \rangle| : y \in S\}$ yields that $\lambda_\alpha = 0$ except for finitely many $\alpha$, and $\sum_\alpha \lambda_\alpha \leq 1$. This implies $S^\bullet$ equals the product of the polars $S_\alpha^{\circ_\alpha}$, giving the product topology.

Conversely, for the dual statement, if $S$ is a $\sigma(F, G)$-bounded subset of $F$, its polar $S^\bullet$ in $G$ satisfies $S^\bullet = \Gamma_\alpha S_\alpha^{\circ_\alpha}$ (the convex circled hull), which yields the locally convex direct sum topology as described in Chapter II, (6.2).
