---
role: proof
locale: en
of_concept: power-sum-over-finite-field
source_book: gtm007
source_chapter: "I. Finite Fields"
source_section: "2. Equations over a finite field"
---

If $u = 0$, all terms of the sum equal $1$, so $S(X^0) = q \cdot 1 = 0$ (since $K$ has characteristic $p$ dividing $q$).

If $u \geq 1$ and $(q-1) \mid u$, then $0^u = 0$ and for every $x \in K^*$, $x^{q-1} = 1$ implies $x^u = 1$. Hence
$$S(X^u) = \sum_{x \in K^*} 1 = (q-1) \cdot 1 = -1$$
in $K$ (since $q \equiv 0$ in $K$, we have $q-1 \equiv -1$).

If $u \geq 1$ and $(q-1) \nmid u$, then since $K^*$ is cyclic of order $q-1$ (Theorem 2), there exists $y \in K^*$ such that $y^u \neq 1$. Then
$$S(X^u) = \sum_{x \in K^*} x^u = \sum_{x \in K^*} (yx)^u = y^u \sum_{x \in K^*} x^u = y^u S(X^u),$$
where the second equality uses that multiplication by $y$ permutes $K^*$. Hence $(1 - y^u) S(X^u) = 0$, and since $1 - y^u \neq 0$ in the field $K$, we obtain $S(X^u) = 0$.
