---
role: proof
locale: en
of_concept: primitive-pythagorean-triple-parametrization
source_book: gtm050
source_chapter: "1"
source_section: "1.3"
---

**Proof.** By considering congruences modulo 4, one shows that in a primitive triple $x^2 + y^2 = z^2$, the number $z$ cannot be even. The square of an odd number $2n+1$ is $4n^2+4n+1 \equiv 1 \pmod{4}$, while the square of an even number $2n$ is $4n^2 \equiv 0 \pmod{4}$. If $x, y$ were odd and $z$ even, then $x^2+y^2 \equiv 2 \pmod{4}$ would not equal $z^2 \equiv 0 \pmod{4}$. Therefore $z$ is odd and $x, y$ have opposite parity. Without loss, assume $x$ is even.

Rewrite the equation as $x^2 = z^2 - y^2 = (z+y)(z-y)$. Since $x, z+y, z-y$ are all even, define $u,v,w$ by $x = 2u$, $z+y = 2v$, $z-y = 2w$. Then $(2u)^2 = (2v)(2w)$ gives $u^2 = vw$. Moreover, $\gcd(v,w)=1$ because any common divisor of $v$ and $w$ would divide their sum $v+w = z$ and their difference $v-w = y$, hence would divide $x$ as well, contradicting primitivity.

Since $v$ and $w$ are coprime and their product is a square, each must be a square: $v = p^2$, $w = q^2$ for relatively prime positive integers $p, q$. Then
$$z = v+w = p^2+q^2, \quad y = v-w = p^2-q^2, \quad x = \sqrt{(2v)(2w)} = 2pq.$$
Since $y > 0$, we have $p > q$. The condition that $p, q$ have opposite parity follows from $z = p^2+q^2$ being odd, which requires one of $p,q$ even and the other odd.

The converse follows from the algebraic identity $(2pq)^2 + (p^2-q^2)^2 = (p^2+q^2)^2$ together with the observation that under conditions (1)-(3), $2pq$ and $p^2-q^2$ are relatively prime. If a prime $P$ divided both, then $P \neq 2$ (since $p^2-q^2$ is odd), so $P$ must divide $p$ or $q$ (it divides $2pq$) but not both (since $p, q$ are coprime). This would contradict $P \mid p^2-q^2$. $\square$
