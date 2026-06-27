---
role: proof
locale: en
of_concept: distinguished-frenet-frame
source_book: gtm051
source_chapter: "1"
source_section: "1.2"
---

We use the Gram-Schmidt orthogonalization process.

Since $\dot{c}(t) \neq 0$ (by the linear independence assumption), define
$$e_1(t) := \frac{\dot{c}(t)}{|\dot{c}(t)|}.$$

Suppose $e_1(t), \ldots, e_{j-1}(t)$, $j < n$, have been defined. Set
$$\tilde{e}_j(t) := c^{(j)}(t) - \sum_{k=1}^{j-1} \left( c^{(j)}(t) \cdot e_k(t) \right) e_k(t).$$
By the linear independence assumption, $\tilde{e}_j(t) \neq 0$, so we may define
$$e_j(t) := \frac{\tilde{e}_j(t)}{|\tilde{e}_j(t)|}.$$

By construction, $e_i(t) \cdot e_j(t) = \delta_{ij}$ for all $i,j$, and each $e_k(t)$ is a linear combination of $\dot{c}(t), \ldots, c^{(k)}(t)$. Conversely, $c^{(k)}(t)$ is a linear combination of $e_1(t), \ldots, e_k(t)$. This gives property (i) — the two families have the same orientation since the transition matrix has positive diagonal entries.

Finally, define $e_n(t)$ so that $e_1(t), \ldots, e_n(t)$ has positive orientation (there are exactly two choices; choose the one with determinant $+1$). The differentiability of all $e_i(t)$ follows from the differentiability of $c$ and the algebraic operations involved.

Uniqueness: Any Frenet frame with properties (i) and (ii) must satisfy the same Gram-Schmidt construction. Starting from $e_1 = \dot{c}/|\dot{c}|$, the orthonormality and the condition that $c^{(k)}$ lies in the span of $e_1, \ldots, e_k$ forces each $e_k$ to be determined up to sign. The orientation conditions fix all signs uniquely.
