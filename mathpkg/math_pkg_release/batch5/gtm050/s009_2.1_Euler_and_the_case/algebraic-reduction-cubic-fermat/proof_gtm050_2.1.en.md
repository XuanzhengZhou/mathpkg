---
role: proof
locale: en
of_concept: algebraic-reduction-cubic-fermat
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

Assume $x, y$ are odd and $z$ is even, with $x^3 + y^3 = z^3$. Since $x, y$ are odd, $x + y$ and $x - y$ are both even. Define
$$x + y = 2p, \qquad x - y = 2q,$$
so that
$$x = p + q, \qquad y = p - q.$$

Substituting into $x^3 + y^3 = z^3$:
$$(p+q)^3 + (p-q)^3 = z^3.$$
Expanding:
$$(p^3 + 3p^2q + 3pq^2 + q^3) + (p^3 - 3p^2q + 3pq^2 - q^3) = 2p(p^2 + 3q^2) = z^3.$$

Thus $z^3 = 2p(p^2 + 3q^2)$, which means $2p(p^2 + 3q^2)$ is a cube.

From $x + y = 2p$ and $x - y = 2q$, any common divisor of $p$ and $q$ would divide $x$ and $y$. Since $x$ and $y$ are coprime, $p$ and $q$ are also coprime. Moreover, $x = p + q$ is odd and $y = p - q$ is odd, so $p$ and $q$ have opposite parity.
