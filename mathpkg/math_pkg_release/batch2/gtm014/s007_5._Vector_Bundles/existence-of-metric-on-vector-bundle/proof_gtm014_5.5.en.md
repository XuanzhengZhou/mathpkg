---
role: proof
locale: en
of_concept: existence-of-metric-on-vector-bundle
source_book: gtm014
source_chapter: "5"
source_section: "5. Vector Bundles"
---

*Proof.* First, let $E = X \times V$ be a product bundle. Then $S^2(E^*) = X \times S^2(V^*)$ is also a product bundle. Let $B$ be any positive definite symmetric bilinear form on $V$. Define $s: X \to X \times S^2(V^*)$ by $s(p) = (p, B)$. Then $s$ is smooth, and for each $p$, $s(p)$ is positive definite, so $s$ is a metric on $S^2(E^*)$.

If $E$ is a trivial bundle, there exists an isomorphism $\phi: E \to X \times V$ for some product bundle $X \times V$. The isomorphism $\phi$ induces an isomorphism $\phi^{(2)}: S^2((X \times V)^*) \to S^2(E^*)$. If $s$ is a metric on $X \times V$ (constructed as above), then $\phi^{(2)} \circ s$ is a metric on $E$.

Finally, let $E$ be an arbitrary vector bundle. For each $p \in X$, choose an open neighborhood $U_p$ of $p$ such that $E|_{U_p}$ is trivial. Let $\{V_i\}_{i=1}^{\infty}$ be a countable locally finite refinement of $\{U_p\}_{p \in X}$. Let $\{\rho_i\}_{i=1}^{\infty}$ be a partition of unity subordinate to the cover $\{V_i\}_{i=1}^{\infty}$ of $X$ (see Theorem 4.5). For each $i$, let $s_i$ be a metric on $E|_{V_i}$ (constructed via triviality). Define $\bar{s}_i: X \to S^2(E^*)$ by

$$\bar{s}_i(p) = \begin{cases} \rho_i(p) s_i(p) & \text{for } p \in V_i, \\ 0 & \text{otherwise}. \end{cases}$$

Each $\bar{s}_i$ is a smooth section. Let $s = \sum_{i=1}^{\infty} \bar{s}_i$. This sum makes sense since for each $p \in X$, only finitely many $\rho_i(p)$ are nonzero. Moreover, for each $p$, $s(p)$ is a positive definite symmetric bilinear form because it is a convex combination (with nonnegative coefficients summing to $1$) of positive definite forms. Thus $s$ is a metric on $E$. $\square$
