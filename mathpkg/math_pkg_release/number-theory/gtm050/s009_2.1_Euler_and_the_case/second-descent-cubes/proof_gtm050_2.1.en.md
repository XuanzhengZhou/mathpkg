---
role: proof
locale: en
of_concept: second-descent-cubes
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

From the factorization lemma, we have $2p = 2a(a - 3b)(a + 3b)$, which is a cube (since $2p$ is a cube under the assumption $3 \nmid p$). The integers $a$ and $b$ are coprime and of opposite parity.

Consider the three factors $2a$, $a - 3b$, and $a + 3b$.

First, since $a$ and $b$ have opposite parity, $a - 3b$ and $a + 3b$ are both odd. Therefore $2a$ is even while $a \pm 3b$ are odd, so any common factor of $2a$ and $a \pm 3b$ must divide $a$ and $a \pm 3b$, hence must divide $a$ and $\pm 3b$. Since $\gcd(a, b) = 1$, the only possible common prime factor is 3.

Second, any common divisor of $a + 3b$ and $a - 3b$ divides their sum $2a$ and their difference $6b$, hence divides $\gcd(2a, 6b) = 2\gcd(a, 3b)$. Since $\gcd(a, b) = 1$, any common prime factor dividing both $a + 3b$ and $a - 3b$ must divide 3.

But 3 does not divide $a$, because if $3 \mid a$ then $3 \mid p = a(a - 3b)(a + 3b)$, contrary to the assumption $3 \nmid p$ (Case 1 of the proof). Therefore no prime factor, including 3, can divide any pair of the three factors.

Thus $2a$, $a - 3b$, and $a + 3b$ are pairwise coprime. Since their product $2a(a - 3b)(a + 3b) = 2p$ is a cube, each factor must itself be a cube:
$$2a = \alpha^3, \qquad a - 3b = \beta^3, \qquad a + 3b = \gamma^3.$$

Adding the last two equations yields
$$\beta^3 + \gamma^3 = (a - 3b) + (a + 3b) = 2a = \alpha^3,$$
a new solution of $x^3 + y^3 = z^3$.
