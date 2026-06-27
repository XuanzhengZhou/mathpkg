---
role: proof
locale: en
of_concept: characterization-of-pythagorean-triples
source_book: gtm050
source_chapter: "1"
source_section: "1.3"
---

Assume $(x,y,z)$ is a primitive Pythagorean triple. Modulo 4 considerations show $z$ is odd and $x, y$ are of opposite parity; assume $x$ is even. Write $x^2 = z^2 - y^2 = (z+y)(z-y)$. Set $x = 2u, z+y = 2v, z-y = 2w$ where $u,v,w$ are positive integers. Then $u^2 = vw$.

Since any common divisor of $v$ and $w$ would divide $z = v+w$ and $y = v-w$, and $y,z$ are relatively prime, $v$ and $w$ are relatively prime. Since $vw = u^2$ is a square and $v,w$ are relatively prime, each must be a square: $v = p^2, w = q^2$ with $p,q$ relatively prime. Then $z = p^2+q^2, y = p^2-q^2$, and $x = 2pq$.

The conditions $p > q$ (from $y > 0$) and opposite parity (otherwise $y, z$ would both be even, contradicting primitivity) follow. Conversely, for any such $p,q$, the formula yields a primitive Pythagorean triple by direct computation.
