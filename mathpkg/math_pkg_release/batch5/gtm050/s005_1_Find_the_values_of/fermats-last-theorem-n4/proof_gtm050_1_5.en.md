---
role: proof
locale: en
of_concept: fermats-last-theorem-n4
source_book: gtm050
source_chapter: "1"
source_section: "1.5"
---

Suppose $x, y, z$ are positive integers with no common divisor greater than $1$ such that $x^4 + y^4 = z^4$. It can be assumed that no two of them have a common divisor greater than $1$, because then by $x^4 + y^4 = z^4$ the third one would share that divisor and its fourth power could be divided out.

Since $x$ and $y$ cannot both be odd (otherwise $x^4 + y^4 \equiv 2 \pmod{4}$ cannot be a fourth power), one of them is even. Assume $x$ is even. Then $x^2, y^2, z^2$ form a primitive Pythagorean triple. By the parametrization of Pythagorean triples, there exist relatively prime integers $p > q > 0$ of opposite parity such that

$$x^2 = 2pq, \quad y^2 = p^2 - q^2, \quad z^2 = p^2 + q^2.$$

From $x^2 = 2pq$ and the general form of Pythagorean triples, we can write $p = a^2 + b^2$, $q = 2ab$ where $a, b$ are relatively prime of opposite parity and $a > b > 0$. Thus

$$x^2 = 2pq = 4ab(a^2 + b^2).$$

This shows that $ab(a^2 + b^2)$ is a square, namely the square of half the even number $x$. Now $ab$ and $a^2 + b^2$ are relatively prime because any prime $P$ dividing $ab$ must divide $a$ or $b$ but not both, and could not therefore divide $a^2 + b^2$. Since $ab$ and $a^2 + b^2$ are relatively prime and their product is a square, each must be a square.

Since $ab$ is a square and $a$ and $b$ are relatively prime, $a$ and $b$ must both be squares, say $a = X^2$, $b = Y^2$. Therefore

$$X^4 + Y^4 = a^2 + b^2$$

is a square. Crucially, the only fact used about the original assumption $x^4 + y^4 = z^4$ was that $z^4$ was a square, not that it was a fourth power. Thus if $x, y$ are positive integers such that $x^4 + y^4$ is a square, the above construction produces new positive integers $X, Y$ such that $X^4 + Y^4$ is also a square. Moreover,

$$X^4 + Y^4 = a^2 + b^2 = p < p^2 + q^2 = z^2 < z^4 = x^4 + y^4.$$

This establishes an infinite strictly decreasing sequence of positive integers, which is impossible by the method of infinite descent. Therefore the sum of two fourth powers cannot be a square, much less a fourth power. This proves Fermat's Last Theorem for fourth powers.
