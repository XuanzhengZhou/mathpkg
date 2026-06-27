---
role: proof
locale: en
of_concept: parallel-translation-theorem
source_book: gtm051
source_chapter: "4"
source_section: "4.2"
---

Suppose $X(t) = \sum \xi^i(t)f_{u_i} \circ u(t)$ is parallel along $c$. Then $X(t)$ satisfies the equation (*) of (4.1.2), namely

$$\dot{\xi}^k(t) + \sum_{i,j} \xi^i(t) \dot{u}^j(t) \Gamma_{ij}^k \circ u(t) = 0, \quad k = 1, 2.$$

This is a linear system of two ordinary differential equations. By the standard theory of linear ODEs, for any initial data $t' \in [t_0, t_1]$ and $\xi'^i$, the system has a unique solution $\xi^i(t, \xi')$ satisfying $\xi^i(t', \xi') = \xi'^i$. The correspondence $(\xi'^i) \mapsto (\xi^i(t, \xi'))$ is a linear bijection.

Finally, we know from (4.2.2) that scalar products of parallel vector fields are constant under parallel translation. This means the parallel translation map $\|c\|$ preserves the inner product, hence it is an isometry between the tangent spaces $T_{u_0}f$ and $T_{u_1}f$.
