---
role: proof
locale: en
of_concept: power-sums-finite-field
source_book: gtm007
source_chapter: "I"
source_section: "2"
---

If $u = 0$, all the terms of the sum are equal to $1$; hence $S(X^u) = q \cdot 1 = 0$ because $K$ is of characteristic $p$.

If $u \geq 1$ and $u$ is divisible by $q-1$, we have $0^u = 0$ and $x^u = 1$ if $x \neq 0$ (since $K^*$ is cyclic of order $q-1$ by Theorem 2). Hence

$$S(X^u) = \sum_{x \in K^*} 1 = (q-1) \cdot 1 = -1.$$

Finally, if $u \geq 1$ and $u$ is not divisible by $q-1$, the fact that $K^*$ is cyclic of order $q-1$ (Theorem 2) shows that there exists $y \in K^*$ such that $y^u \neq 1$. One has:

$$S(X^u) = \sum_{x \in K} x^u = 0^u + \sum_{x \in K^*} x^u = \sum_{x \in K^*} x^u = \sum_{x \in K^*} (yx)^u = \sum_{x \in K^*} y^u x^u = y^u \sum_{x \in K^*} x^u = y^u S(X^u).$$

Thus $(1 - y^u)S(X^u) = 0$, which implies that $S(X^u) = 0$.

(Variant: Use the fact that, if $d \geq 2$ is prime to $p$, the sum of the $d$-th roots of unity is zero.)
