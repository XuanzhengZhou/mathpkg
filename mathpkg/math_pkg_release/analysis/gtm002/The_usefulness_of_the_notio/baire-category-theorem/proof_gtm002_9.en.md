---
role: proof
locale: en
of_concept: baire-category-theorem
source_book: gtm002
source_chapter: "9"
source_section: "Metric and Topological Spaces"
---
Let $A = \bigcup_{n=1}^{\infty} A_n$, where each $A_n$ is nowhere dense, let $\varrho$ be a metric with respect to which $X$ is complete, and let $S_0$ be a non-empty open set.

Choose a nested sequence of balls $S_n$ of radius $r_n < 1/n$ such that
$$\overline{S}_n \subset S_{n-1} \setminus A_n \quad (n \geq 1).$$
This can be done step by step, taking for $S_n$ a ball with center $x_n$ in $S_{n-1} \setminus \overline{A}_n$ (which is non-empty because $A_n$ is nowhere dense, so $\overline{A}_n$ has empty interior, hence its complement is dense) and with sufficiently small radius.

Then $\{x_n\}$ is a Cauchy sequence, since for $i, j \geq n$,
$$\varrho(x_i, x_j) \leq \varrho(x_i, x_n) + \varrho(x_n, x_j) < 2r_n.$$

Hence $x_n \to x$ for some $x \in X$, by completeness of $X$ with respect to $\varrho$.

Since $x_i \in \overline{S}_n$ for $i \geq n$, it follows that $x \in \bigcap_{n=1}^{\infty} \overline{S}_n$. But by construction,
$$\bigcap_{n=1}^{\infty} \overline{S}_n \subset S_0 \setminus \bigcup_{n=1}^{\infty} A_n = S_0 \setminus A.$$

Thus $x \in S_0 \setminus A$, showing that every non-empty open set $S_0$ contains a point of $X \setminus A$. Therefore $X \setminus A$ is dense in $X$.
