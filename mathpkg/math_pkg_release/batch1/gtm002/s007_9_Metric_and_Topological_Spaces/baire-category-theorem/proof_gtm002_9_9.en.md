---
role: proof
locale: en
of_concept: baire-category-theorem
source_book: gtm002
source_chapter: "9"
source_section: "Metric and Topological Spaces"
---

Let $A = \bigcup A_n$, where $A_n$ is nowhere dense, let $\varrho$ be a metric with respect to which $X$ is complete, and let $S_0$ be a non-empty open set. Choose a nested sequence of balls $S_n$ of radius $r_n < 1/n$ such that $\overline{S}_n \subset S_{n-1} - A_n$ ($n \geq 1$). This can be done step by step, taking for $S_n$ a ball with center $x_n$ in $S_{n-1} - \overline{A}_n$ (which is non-empty because $\overline{A}_n$ is nowhere dense) and with sufficiently small radius. Then $\{x_n\}$ is a Cauchy sequence, since

$$\varrho(x_i, x_j) \leq \varrho(x_i, x_n) + \varrho(x_n, x_j) < 2r_n \quad \text{for} \quad i, j \geq n.$$

Hence $x_n \rightarrow x$ for some $x$ in $X$. Since $x_i \in \overline{S}_n$ for $i \geq n$, it follows that $x \in \bigcap \overline{S}_n \subset S_0 - A$. This shows that $X - A$ is dense in $X$.
