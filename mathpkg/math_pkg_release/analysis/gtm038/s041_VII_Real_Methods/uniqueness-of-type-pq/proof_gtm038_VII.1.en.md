---
role: proof
locale: en
of_concept: uniqueness-of-type-pq
source_book: gtm038
source_chapter: "VII"
source_section: "1"
---

Suppose $\varphi$ is of type $(p, q)$ and of type $(p', q')$. Since $\varphi \neq 0$ there exist tangent vectors $\xi_1, \ldots, \xi_r$ such that $\varphi(\xi_1, \ldots, \xi_r) \neq 0$. Then

$$\varphi(c\xi_1, \ldots, c\xi_r) = \begin{cases} c^p \bar{c}^q \varphi(\xi_1, \ldots, \xi_r) \\ c^{p'} \bar{c}^{q'} \varphi(\xi_1, \ldots, \xi_r) \end{cases}$$

Therefore $c^p \bar{c}^q = c^{p'} \bar{c}^{q'}$ for each $c \in \mathbb{C}$. Let $c = e^{i\theta}$ with arbitrary $\theta \in \mathbb{R}$. Then $e^{i\theta(p-q)} = e^{i\theta(p'-q')}$. That can hold for all $\theta$ only when $p - q = p' - q'$. Since $p + q = p' + q' = r$ by assumption, it follows that $p = p'$, $q = q'$.
