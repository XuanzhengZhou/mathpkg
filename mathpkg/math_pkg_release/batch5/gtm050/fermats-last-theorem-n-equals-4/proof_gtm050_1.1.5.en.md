---
role: proof
locale: en
of_concept: fermats-last-theorem-n-equals-4
source_book: gtm050
source_chapter: "1"
source_section: "1.5"
---
Assume $x^4 + y^4 = z^4$ for positive integers with $\gcd(x,y,z)=1$. Then $(x^2)^2 + (y^2)^2 = (z^2)^2$, so $(x^2, y^2, z^2)$ is a primitive Pythagorean triple. By the classification theorem, there exist relatively prime $p, q$ of opposite parity, $p > q > 0$, such that:
$$x^2 = 2pq, \quad y^2 = p^2 - q^2, \quad z^2 = p^2 + q^2.$$

From $y^2 = p^2 - q^2$ we get $y^2 + q^2 = p^2$, so $(y, q, p)$ is a primitive Pythagorean triple with $q$ even (since $y$ is odd and $p, q$ have opposite parity). Thus there exist relatively prime $a, b$ of opposite parity, $a > b > 0$, such that:
$$q = 2ab, \quad y = a^2 - b^2, \quad p = a^2 + b^2.$$

Then $x^2 = 2pq = 2(a^2+b^2)(2ab) = 4ab(a^2+b^2)$, so $ab(a^2+b^2) = (x/2)^2$ is a square. Since $\gcd(ab, a^2+b^2) = 1$, both $ab$ and $a^2+b^2$ are squares. Since $ab$ is a square and $a, b$ are relatively prime, each is a square: $a = X^2$, $b = Y^2$.

Then $X^4 + Y^4 = a^2 + b^2 = p < p^2 + q^2 = z^2 < z^4 = x^4 + y^4$. This gives a new solution with strictly smaller sum $X^4+Y^4$. By infinite descent, no solution exists.
