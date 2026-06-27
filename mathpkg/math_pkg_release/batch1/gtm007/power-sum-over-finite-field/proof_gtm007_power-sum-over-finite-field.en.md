---
role: proof
locale: en
of_concept: "power-sum-over-finite-field"
source_book: gtm007
source_chapter: "I"
source_section: "2.1"
---
If $u = 0$, all terms equal $1$, so $S(X^u) = q \cdot 1 = 0$ in characteristic $p$.

If $u \geq 1$ and $(q-1) \mid u$, then $0^u = 0$ and $x^u = 1$ for $x \neq 0$. Hence $S(X^u) = (q-1) \cdot 1 = -1$.

If $u \geq 1$ and $(q-1) \nmid u$, since $\mathbb{F}_q^*$ is cyclic of order $q-1$ (Theorem 2), there exists $y \in \mathbb{F}_q^*$ with $y^u \neq 1$. Then

$$S(X^u) = \sum_{x \in \mathbb{F}_q^*} x^u = \sum_{x \in \mathbb{F}_q^*} y^u x^u = y^u S(X^u),$$

so $(1 - y^u) S(X^u) = 0$, which gives $S(X^u) = 0$.
