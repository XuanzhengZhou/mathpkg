---
role: proof
locale: en
of_concept: pythagorean-triangle-area-not-square
source_book: gtm050
source_chapter: "1"
source_section: "1.6"
---

The proof proceeds by infinite descent. Assume a Pythagorean triangle with integer sides $x, y, z$ satisfying $x^2 + y^2 = z^2$ and having area $\frac12 xy$ equal to a square.

From the properties of primitive Pythagorean triples, one can write $x = 2pq$, $y = p^2 - q^2$, $z = p^2 + q^2$ (up to swapping $x$ and $y$) where $p, q$ are coprime integers of opposite parity. The area is $\frac12 xy = pq(p^2 - q^2) = pq(p-q)(p+q)$. For this to be a square, each of the pairwise coprime factors $p, q, p-q, p+q$ must be a square.

Writing $p = P^2$, $q = Q^2$, $p - q = U^2$, $p + q = V^2$, we obtain $P^2 - Q^2 = U^2$ and $P^2 + Q^2 = V^2$. These equations give a new Pythagorean triple $(U, Q, P)$ or similar, whose associated area involves a quantity smaller than the original.

Specifically, $P + Q \leq (P+Q)PQ(P-Q) = \frac12 uv = q/4 < q < p+q$, allowing the process to be repeated to find $P', Q'$ with $P'+Q' < P+Q$, producing an infinite descending sequence $p+q > P+Q > P'+Q' > \cdots$.

Since an infinite descending sequence of positive integers is impossible, no such Pythagorean triangle can exist. Therefore, the area of a Pythagorean triangle can never be a square. This also proves the case $n=4$ of Fermat's Last Theorem, because it shows that $z^4 - x^4$ cannot be a square.
