---
role: proof
locale: en
of_concept: orthogonal-sum-abelian-finite-projections
source_book: gtm003
source_chapter: "VI"
source_section: "8"
---

Let $\{p_\alpha : \alpha \in I\}$ be a family of pairwise centrally orthogonal projections in $W$, and let $p = \sum_\alpha p_\alpha$. Let $z_\alpha = z(p_\alpha)$ be the central support of each $p_\alpha$. By central orthogonality, $z_\alpha z_\beta = 0$ for $\alpha \neq \beta$, and $p_\alpha = z_\alpha p$ for all $\alpha$.

Hence:
$$pWp = \bigoplus_{\alpha \in I} p_\alpha W p_\alpha.$$

Therefore, if each $p_\alpha W p_\alpha$ is commutative (abelian), the direct sum is also commutative, so $pWp$ is abelian.

For finiteness: suppose $p \sim q \leq p$. Then for each $\alpha$, $z_\alpha q = q_\alpha \sim z_\alpha p = p_\alpha$, and $q_\alpha \leq p_\alpha$. If each $p_\alpha$ is finite, then $p_\alpha = q_\alpha$ for all $\alpha$. But this implies $p = q$, establishing that $p$ is finite.
