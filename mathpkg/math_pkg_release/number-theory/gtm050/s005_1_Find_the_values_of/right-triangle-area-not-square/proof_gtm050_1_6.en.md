---
role: proof
locale: en
of_concept: right-triangle-area-not-square
source_book: gtm050
source_chapter: "1"
source_section: "1.6"
---

The proposition can be reformulated: there is no Pythagorean triple $x^2 + y^2 = z^2$ such that $\frac{1}{2}xy$ is a square. (Note that $x, y$ cannot both be odd, so $\frac{1}{2}xy$ is necessarily an integer.)

Using the general parametrization of Pythagorean triples, write $x = (2pq)d$, $y = (p^2 - q^2)d$, $z = (p^2 + q^2)d$, where $p, q$ are relatively prime positive integers of opposite parity with $p > q$, and $d$ is a positive integer. Then

$$\frac{1}{2}xy = pq(p^2 - q^2)d^2.$$

This is a square if and only if $pq(p^2 - q^2)$ is a square (since if $Ad^2$ is a square, then $A$ must be a square).

Now set $p + q = r^2$, $p - q = s^2$. Since $p$ and $q$ have opposite parity, both $r^2$ and $s^2$ are odd, so $r$ and $s$ are odd. Moreover, $r$ and $s$ are relatively prime because $p+q$ and $p-q$ are relatively prime.

Define positive integers $u, v$ by

$$u = \frac{r - s}{2}, \quad v = \frac{r + s}{2}.$$

Then $u$ and $v$ are relatively prime because any common factor would divide both the sum $r = u + v$ and the difference $s = v - u$, which are relatively prime. Moreover,

$$uv = \frac{r^2 - s^2}{4} = \frac{(p+q) - (p-q)}{4} = \frac{q}{2}.$$

Since $q$ is a square (from $pq(p^2-q^2)$ being a square and $p, q$ relatively prime), $\frac{1}{2}q$ is an even integer, and $\frac{1}{4}q = \frac{1}{2}uv$ is an integer and a square (as a quotient of squares).

The proof then proceeds through a descent argument: one can construct smaller positive integers with the same properties, leading to an infinite descending sequence, which is impossible.
