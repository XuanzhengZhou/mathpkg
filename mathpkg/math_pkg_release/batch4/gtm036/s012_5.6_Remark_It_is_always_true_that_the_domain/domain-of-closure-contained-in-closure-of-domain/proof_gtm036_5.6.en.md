---
role: proof
locale: en
of_concept: domain-of-closure-contained-in-closure-of-domain
source_book: gtm036
source_chapter: "5"
source_section: "5.6"
---

It is always true that $D_{\bar{T}} \subset \bar{D}_T$ because every point of $D_{\bar{T}}$ is, by definition of the graph closure, a limit of points from $D_T$.

For the reverse inclusion when $H$ is complete: let $x \in \bar{D}_T$. There exists a net $\{x_\alpha, \alpha \in A\}$ in $D_T$ such that $x_\alpha \to x$. Then $\{x_\alpha, \alpha \in A\}$ is a Cauchy net. Since $T$ is continuous (hence uniformly continuous), the image net $\{T(x_\alpha), \alpha \in A\}$ is also a Cauchy net. Because $H$ is complete, there exists $z \in H$ such that $T(x_\alpha) \to z$. Then $(x, z)$ belongs to the closure $\bar{G}_T$ of the graph, which by definition is the graph $G_{\bar{T}}$ of $\bar{T}$. Hence $x \in D_{\bar{T}}$. Thus $\bar{D}_T \subset D_{\bar{T}}$, and together with $D_{\bar{T}} \subset \bar{D}_T$ we obtain $D_{\bar{T}} = \bar{D}_T$.
