---
role: proof
locale: en
of_concept: weierstrass-division-theorem
source_book: gtm059
source_chapter: "5"
source_section: "5"
---
Let $\tau$ and $\sigma$ be the projections on the tail and head of a power series: $\tau(\sum b_i X^i) = \sum_{i \ge n} b_i X^i$ and $\sigma(\sum b_i X^i) = \sum_{i < n} b_i X^i$. Note that $g = \sigma(g) + \tau(g)$ and $\tau(g)$ is divisible by $X^n$.

The equation $g = qf + r$ with $\deg r < n$ is equivalent to finding $q$ such that $\tau(g) = \tau(qf)$. Writing $f = \sigma(f) + X^n h$, we have $\tau(qf) = \tau(q \sigma(f)) + q X^n h$. Since $a_n$ is a unit, $\sigma(f)$ is a ``Weierstrass polynomial'' up to unit, and one can solve for $q$ iteratively using the completeness of $A$. The construction proceeds by successive approximation: at each step one matches the leading term of the remainder, reducing the order of the error. Uniqueness follows from the fact that if $qf + r = 0$ with $\deg r < n$, then considering lowest-degree terms forces $q = 0$ and consequently $r = 0$.
