---
role: proof
locale: en
of_concept: projection-equivalence-conditions
source_book: gtm003
source_chapter: "5"
source_section: "5.2"
---

(a) $\Rightarrow$ (b): If $q \leq p$, then $q = q^* = pqp$ by the definition of the order. Since $q$ and $p$ are projections, $q = q^*q = (pqp)^*(pqp) = pqpqp \leq p$, which implies $pq = qp = q$.

(b) $\Rightarrow$ (c): If $pq = qp = q$, then $(p - q)^2 = p - pq - qp + q = p - q - q + q = p - q$, and $(p - q)^* = p^* - q^* = p - q$, so $p - q$ is a projection.

(c) $\Rightarrow$ (a): If $p - q$ is a projection, then $p - q \geq 0$, so $q \leq p$.
