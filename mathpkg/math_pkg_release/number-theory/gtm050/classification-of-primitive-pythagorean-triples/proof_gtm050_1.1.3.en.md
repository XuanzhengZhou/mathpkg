---
role: proof
locale: en
of_concept: classification-of-primitive-pythagorean-triples
source_book: gtm050
source_chapter: "1"
source_section: "1.3"
---
Assume $(x, y, z)$ is a primitive Pythagorean triple with $x$ even. Then $y$ and $z$ are odd. Write $x^2 = z^2 - y^2 = (z+y)(z-y)$. Since $z+y$ and $z-y$ are even, set $x = 2u$, $z+y = 2v$, $z-y = 2w$. Then $(2u)^2 = (2v)(2w)$, so $u^2 = vw$.

Since any common divisor of $v$ and $w$ would divide $v+w = z$ and $v-w = y$, and $\gcd(y,z)=1$, we have $\gcd(v,w)=1$. Since their product $vw = u^2$ is a square and they are relatively prime, both $v$ and $w$ must be squares. Write $v = p^2$, $w = q^2$ with $p, q$ positive, relatively prime, and $p > q$.

Then $z = v+w = p^2+q^2$, $y = v-w = p^2-q^2$, and $x^2 = (2u)^2 = 4vw = 4p^2q^2$, so $x = 2pq$. The parity condition on $p, q$ follows because if both were odd or both even, $y = p^2-q^2$ would be even, contradiction.

Conversely, for any such $p, q$, direct computation shows $(2pq)^2 + (p^2-q^2)^2 = (p^2+q^2)^2$, and the conditions on $p, q$ guarantee primitivity.
