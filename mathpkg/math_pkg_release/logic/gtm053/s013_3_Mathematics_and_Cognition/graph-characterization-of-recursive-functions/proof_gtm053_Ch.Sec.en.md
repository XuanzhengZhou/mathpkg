---
role: proof
locale: en
of_concept: graph-characterization-of-recursive-functions
source_book: gtm053
source_chapter: "V"
source_section: "4"
---

Necessity was proved in the course of Theorem 4.3. For sufficiency: since $\Gamma_g$ is r.e., it is the projection of the 1-level of a primitive recursive $G$. Then one can recover $g$ by:
$$g(x_1, \ldots, x_n) = t_1^{(2)}\left(\min\left\{z \mid G(x_1, \ldots, x_n, t_1^{(2)}(z), t_2^{(2)}(z)) = 1\right\}\right),$$
which is partial recursive because the $\mu$-operator is applied to a primitive recursive function. Corollary: every partial recursive function can be described using the $\mu$-operator exactly once.
