---
role: proof
locale: en
of_concept: euler-method-square-case
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

For ordinary integers $p, q \in \mathbb{Z}$: if $pq$ is a square, write the prime factorization $pq = \prod p_i^{e_i}$. Since $pq$ is a square, each exponent $e_i$ is even. Because $\gcd(p, q) = 1$ in the simplest case, the prime factors of $p$ and $q$ are disjoint, so the exponents in each of $p$ and $q$ must themselves be even, giving $p = r^2$, $q = s^2$. More generally, if $\gcd(p, q) = m$, then $p = mr^2$ and $q = ms^2$.

For surds $x + y\sqrt{-c}$: Euler sets $x + y\sqrt{-c} = (p + q\sqrt{-c})^2$. Expanding:

$$
(p + q\sqrt{-c})^2 = p^2 + 2pq\sqrt{-c} + q^2(-c) = (p^2 - cq^2) + 2pq\sqrt{-c}.
$$

Comparing real and imaginary parts gives $x = p^2 - cq^2$ and $y = 2pq$. (The book states $x = cq^2 - p^2$, which corresponds to using $- (p + q\sqrt{-c})^2$ instead, giving $x = -(p^2 - cq^2) = cq^2 - p^2$ and $y = -2pq$. The sign of $y$ can be absorbed by redefining $q$.)

The argument is incomplete because the assumption that $p$ and $q$ are relatively prime does not imply that $cq^2 - p^2$ and $2pq$ are relatively prime, so the factorization principle may not apply.
