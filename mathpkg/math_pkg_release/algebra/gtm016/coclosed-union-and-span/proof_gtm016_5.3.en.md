---
role: proof
locale: en
of_concept: coclosed-union-and-span
source_book: gtm016
source_chapter: "5 Bialgebras and Hopf algebras"
source_section: "5.3 The bialgebra structure of End K"
---

**Proof.** If $x$ is in the union of coclosed subsets $H_\alpha$ of $\text{End}\,K$, then $x \in H_\alpha$ for some $\alpha$. Since $H_\alpha$ is coclosed, there exist $x_1, \ldots, x_n \in H_\alpha$ such that $x(ab) = \sum_i x(a)x_i(b)$ for all $a, b \in K$. But $x_1, \ldots, x_n$ are also in the union $\bigcup_\alpha H_\alpha$. Thus the union is coclosed.

For the $K$-span: if $x = \sum_j c_j y_j$ with $c_j \in K$ and $y_j$ in coclosed subsets $H_j$, then each $y_j$ has a decomposition $y_j(ab) = \sum_i y_j(a) y_{ji}(b)$ with $y_{ji} \in H_j$. Then

$$x(ab) = \sum_j c_j y_j(ab) = \sum_j c_j \sum_i y_j(a) y_{ji}(b) = \sum_{j,i} (c_j y_j)(a) \cdot y_{ji}(b)$$

shows that the $K$-span of the $y_j$ and $y_{ji}$ satisfies the coclosedness condition for $x$. Hence the $K$-span is coclosed.
