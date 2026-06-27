---
role: proof
locale: en
of_concept: finite-dim-linear-function-continuous
source_book: gtm023
source_chapter: "VII"
source_section: "5 (unnumbered)"
---

Let $e_v$ ($v = 1, \ldots, n$) be a basis of $E$ and write $x = \sum_v \xi^v e_v$. From $N_2$ and $N_3$,
$$\|x\| = \left\| \sum_v \xi^v e_v \right\| \leq \sum_v |\xi^v| \|e_v\|.$$
This implies that the norm function $x \mapsto \|x\|$ is continuous in the natural (coordinate) topology.

Consider the compact set
$$Q = \left\{ x = \sum_v \xi^v e_v \;\middle|\; \sum_v |\xi^v| = 1 \right\}.$$
Since $Q$ is compact and $\|x\| \neq 0$ for $x \in Q$, there exists a constant $m > 0$ such that $\|x\| \geq m$ for all $x \in Q$. By $N_3$,
$$\|x\| \geq m \sum_v |\xi^v| \quad \text{for all } x \in E,$$
and consequently $|\xi^v| \leq \|x\|/m$.

Now let $f$ be a linear function on $E$. Then
$$|f(x)| = \left| \sum_v \xi^v f(e_v) \right| \leq \frac{\|x\|}{m} \sum_v |f(e_v)| \leq M \|x\|$$
with $M = (1/m) \sum_v |f(e_v)|$. Hence $f$ is bounded, therefore continuous.

Since every linear transformation $\varphi$ of a finite-dimensional space $E$ is continuous (see sec. 1.22), it follows that $\varphi$ is bounded, so $B(E;E) = L(E;E)$. Moreover, since the unit sphere is compact in finite dimensions, the supremum in the definition of $\|\varphi\|$ is actually attained: $\|\varphi\| = \max_{\|x\|=1} \|\varphi x\|$.
