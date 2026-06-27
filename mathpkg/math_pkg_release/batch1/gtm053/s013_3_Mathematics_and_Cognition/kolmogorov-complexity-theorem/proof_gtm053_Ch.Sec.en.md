---
role: proof
locale: en
of_concept: kolmogorov-complexity-theorem
source_book: gtm053
source_chapter: "VI"
source_section: "9"
---

Choose a recursive embedding $\theta: \mathbb{Z}^+ \times \mathbb{Z}^+ \to \mathbb{Z}^+$ with recursive inverse satisfying $\theta(k, j) \leqslant k \cdot \phi(j)$. Let $U$ be any versal family of $(m+1)$-functions. Define $u$ by $u(x_1, \ldots, x_m, k) = U(x_1, \ldots, x_m, \theta^{-1}(k))$. Then $u$ is optimal with $c_{u,v} \leqslant \phi(C_U(v))$.
