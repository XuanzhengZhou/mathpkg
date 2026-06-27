---
role: proof
locale: en
of_concept: fermats-theorem-on-triangle-area
source_book: gtm050
source_chapter: "1"
source_section: "1.6"
---
Assume $(x, y, z)$ is a primitive Pythagorean triple with $x$ even and $\frac{1}{2}xy$ a square. Then $x = 2pq, y = p^2-q^2, z = p^2+q^2$ with $p, q$ relatively prime of opposite parity, $p > q$. Then $\frac{1}{2}xy = pq(p^2-q^2) = pq(p+q)(p-q)$ is a square.

Since $p, q, p+q, p-q$ are pairwise relatively prime (any common divisor would divide two of them, hence all, contradicting relative primality of $p$ and $q$), each must be a square: $p = r^2, q = s^2, p+q = t^2, p-q = u^2$.

Then $r^2 + s^2 = t^2$ and $r^2 - s^2 = u^2$. From these, one defines $u_1 = (r-s)/2, v_1 = (r+s)/2$, which are relatively prime and satisfy $u_1v_1 = q/2 = s^2/2$. Further descent leads to a smaller Pythagorean triangle with square area, completing the infinite descent.
