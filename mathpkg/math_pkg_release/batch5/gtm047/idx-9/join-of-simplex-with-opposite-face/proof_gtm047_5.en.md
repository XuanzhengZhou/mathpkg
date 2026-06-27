---
role: proof
locale: en
of_concept: join-of-simplex-with-opposite-face
source_book: gtm047
source_chapter: "5"
source_section: "5"
---

The join $J(v_1 v_2 \ldots v_n, v_0)$ is by definition the union of all line segments from points in the $(n-1)$-face $v_1 v_2 \ldots v_n$ to the vertex $v_0$. Since $\sigma^n$ is the convex hull of $\{v_0, v_1, \ldots, v_n\}$, and every point in $\sigma^n$ can be written as a convex combination $\sum_{i=0}^n \lambda_i v_i$ with $\lambda_i \geqslant 0$, $\sum \lambda_i = 1$, we can rewrite this as $(1 - \lambda_0) \cdot (\sum_{i=1}^n \frac{\lambda_i}{1-\lambda_0} v_i) + \lambda_0 v_0$ (when $\lambda_0 \neq 1$), which is a point on the segment joining $v_0$ to a point of the opposite face. Hence $\sigma^n = J(v_1 v_2 \ldots v_n, v_0)$.
