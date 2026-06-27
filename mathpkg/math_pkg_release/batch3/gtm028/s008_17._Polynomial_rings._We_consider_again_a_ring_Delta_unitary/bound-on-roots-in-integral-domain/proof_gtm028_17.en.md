---
role: proof
locale: en
of_concept: bound-on-roots-in-integral-domain
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** The first statement is true for $m = 1$ by the Factor Theorem. Assume it holds for $m - 1$ roots, so that $f(X) = (X - a_1) \cdots (X - a_{m-1}) q(X)$. Then

$$f(a_m) = (a_m - a_1) \cdots (a_m - a_{m-1}) q(a_m).$$

Since the $a_i$ are distinct, each factor $a_m - a_i \neq 0$. Since $R$ is an integral domain (no zero divisors) and $f(a_m) = 0$, we must have $q(a_m) = 0$. By the Factor Theorem, $X - a_m$ divides $q(X)$, so $q(X) = (X - a_m) q_1(X)$. Hence $f(X) = (X - a_1) \cdots (X - a_m) q_1(X)$.

If $f(X) \neq 0$ and had $m > \partial f$ distinct roots, then the product $(X - a_1) \cdots (X - a_m)$ would have degree $m > \partial f$ and divide $f(X)$, which is impossible in an integral domain. Hence $m \leq \partial f$.
