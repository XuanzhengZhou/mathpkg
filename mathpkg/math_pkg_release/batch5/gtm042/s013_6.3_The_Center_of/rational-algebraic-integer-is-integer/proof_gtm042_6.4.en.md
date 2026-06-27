---
role: proof
locale: en
of_concept: rational-algebraic-integer-is-integer
source_book: gtm042
source_chapter: "6"
source_section: "6.4"
---

Suppose $x \in \mathbb{Q}$ is an algebraic integer but $x \notin \mathbb{Z}$. Then we can write $x = p/q$ with $p, q \in \mathbb{Z}$, $q \geqslant 2$, and $\gcd(p, q) = 1$. Since $x$ is an algebraic integer, it satisfies an equation
$$x^n + a_1 x^{n-1} + \cdots + a_n = 0, \quad a_i \in \mathbb{Z}.$$
Substituting $x = p/q$ and multiplying by $q^n$ yields
$$p^n + a_1 q p^{n-1} + \cdots + a_n q^n = 0.$$
Reducing modulo $q$, we obtain $p^n \equiv 0 \pmod{q}$, which means $q \mid p^n$. Since $\gcd(p, q) = 1$, this forces $q = 1$, contradicting $q \geqslant 2$. Therefore $x \in \mathbb{Z}$.
