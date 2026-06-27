---
locale: en
of_concept: if-sn-1-has-k-orthonormal-tangent-vector-fields-v-1-ldots-v
role: proof
source_book: gtm020
source_chapter: 12. Clifford Algebras
source_section: '1'
---

We can view $v_i: S^{n-1} \rightarrow \mathbf{R}^n$ such that $(x|v_i(x)) = 0$ and $(v_i(x)|v_j(x)) = \delta_{i,j}$ for all $x \in S^{n-1}$ and $1 \leq i, j \leq k$. Next, the sphere $S^{nq-1}$ can be considered as the join of $q$ spheres $S^{n-1}$; that is, for $x \in S^{nq-1}$ we can write $x = (\alpha(1)x(1), \ldots, \alpha(q)x(q))$, where $x(i) \in S^{n-1}$ and $\sum_i \alpha(i)^2 = 1, \alpha(i) \geq 0$. We define $v_i^*: S^{nq-1} \rightarrow \mathbf{R}^{nq}$ by the relation $v_i^*(\alpha(1)x(1), \ldots, \alpha(q)x(q)) = \alpha(1)v_i(x(1)) + \cdots + \alpha(q)v_i(x(q))

Proof. Since $m = 2q$, it suffices, in view of (1.1), to prove that $S^1$ has a unit vector field defined on it. Let $v(x_1, x_2) = (-x_2, x_1)$. Then $(x|v(x)) = 0$ and $\|v(x)\| = 1$ for each $x = (x_1, x_2) \in S^1$. The map $v$ is a $90^\circ$ rotation.

See Exercise 1 for a similar application.

In the next proposition we derive a property of $S^n$ with unit vector fields.
