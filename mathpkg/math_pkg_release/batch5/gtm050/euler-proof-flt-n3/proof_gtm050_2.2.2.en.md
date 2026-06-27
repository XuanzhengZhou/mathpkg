---
role: proof
locale: en
of_concept: euler-proof-flt-n3
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---
Assume $x^3 + y^3 = z^3$ with $x, y, z$ pairwise relatively prime positive integers. Exactly one is even; by symmetry, assume $z$ even, $x, y$ odd. Set $x+y = 2p$, $x-y = 2q$. Then $x = p+q$, $y = p-q$, and substitution gives $x^3+y^3 = 2p(p^2+3q^2)$. Since $x, y$ odd, $p, q$ have opposite parity, and $\gcd(p,q)=1$.

If $3 \nmid p$, then $\gcd(2p, p^2+3q^2) = 1$ and since their product is a cube (equal to $z^3$), each is a cube. Using the factorization $p^2+3q^2 = (p+q\sqrt{-3})(p-q\sqrt{-3})$ and the key lemma that if $a, b$ are relatively prime and $a^2+3b^2$ is a cube, then $a+b\sqrt{-3} = (u+v\sqrt{-3})^3$ for some integers $u, v$, we obtain:
$$p = u(u^2-9v^2), \quad q = 3v(u^2-v^2).$$
This produces $2p = 2u(u-3v)(u+3v)$, a cube, and since $\gcd(2u, u-3v, u+3v)=1$ (because $3 \nmid p$), each factor is a cube. Setting $2u = \alpha^3$, $u-3v = \beta^3$, $u+3v = \gamma^3$ gives $\beta^3 + \gamma^3 = \alpha^3$, a new solution with $\alpha^3\beta^3\gamma^3 = 2p < z^3$, enabling infinite descent.

The case $3 \mid p$ is handled similarly with a modified argument.
