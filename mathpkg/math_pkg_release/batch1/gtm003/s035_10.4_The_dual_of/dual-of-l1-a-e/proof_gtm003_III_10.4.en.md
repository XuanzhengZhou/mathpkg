---
role: proof
locale: en
of_concept: dual-of-l1-a-e
source_book: gtm003
source_chapter: "III"
source_section: "10.4"
---
If $\mathbf{x}' = \{x'_\alpha : \alpha \in \mathbf{A}\}$ is a prenuclear family in $E'$, there exists a $U \in \mathfrak{U}$ and a positive Radon measure $\mu$ on $U^\circ$ such that

$$|\langle x, x'_\alpha \rangle| \leq \int_{U^\circ} |\langle x, x' \rangle| \, d\mu(x') \qquad (x \in E,\; \alpha \in \mathbf{A}).$$

Now if $\mathbf{x} = \{x_\alpha : \alpha \in \mathbf{A}\} \in S$, the definition of summability implies that $\sum_\alpha |\langle x_\alpha, x' \rangle|$ converges uniformly for $x' \in U^\circ$ (hence to a continuous function on $U^\circ$), whence

$$\sum_\alpha |\langle x_\alpha, x'_\alpha \rangle| \leq \int_{U^\circ} \sum_\alpha |\langle x_\alpha, x' \rangle| \, d\mu(x') < +\infty.$$

Thus $\sum_\alpha \langle x_\alpha, x'_\alpha \rangle$ converges absolutely, and the linear form $\mathbf{x} \mapsto \sum_\alpha \langle x_\alpha, x'_\alpha \rangle$ is continuous on $l^1(\mathbf{A}, E)$.

Conversely, let $f$ be a continuous linear form on $l^1(\mathbf{A}, E)$. For each $\alpha \in \mathbf{A}$, define $x'_\alpha \in E'$ by $\langle x, x'_\alpha \rangle = f(\mathbf{x}^{(\alpha)})$ where $\mathbf{x}^{(\alpha)}$ is the family with $x$ in position $\alpha$ and zero elsewhere. One verifies that $\{x'_\alpha\}$ is a prenuclear family and that $f$ is given by the canonical bilinear form. This establishes the identification.
