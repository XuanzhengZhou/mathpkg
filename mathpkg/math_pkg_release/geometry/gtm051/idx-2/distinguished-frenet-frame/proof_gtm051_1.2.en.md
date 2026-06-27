---
role: proof
locale: en
of_concept: distinguished-frenet-frame
source_book: gtm051
source_chapter: "1"
source_section: "1.2"
---

We use the Gram-Schmidt orthogonalization process. The assumption that $\dot{c}(t), \ddot{c}(t), \ldots, c^{(n-1)}(t)$ are linearly independent implies $\dot{c}(t) \neq 0$, so we may set $e_1(t) = \dot{c}(t) / |\dot{c}(t)|$.

Suppose $e_1(t), \ldots, e_{j-1}(t)$ (for $j < n$) have been defined. Define

$$\tilde{e}_j(t) := -\sum_{k=1}^{j-1} \left( c^{(j)}(t) \cdot e_k(t) \right) e_k(t) + c^{(j)}(t)$$

and let $e_j(t) := \tilde{e}_j(t) / |\tilde{e}_j(t)|$. By the linear independence assumption, $\tilde{e}_j(t) \neq 0$, so $e_j(t)$ is well defined.

By construction, $e_j(t)$ is orthogonal to $e_1(t), \ldots, e_{j-1}(t)$ and the span of $e_1(t), \ldots, e_j(t)$ equals the span of $\dot{c}(t), \ldots, c^{(j)}(t)$ with the same orientation (the coefficients in the Gram-Schmidt process preserve orientation). Finally, define $e_n(t)$ to complete the basis with positive orientation in $\mathbb{R}^n$. The differentiability of all $e_i(t)$ follows from the differentiability of $c$ and the algebraic operations involved.
