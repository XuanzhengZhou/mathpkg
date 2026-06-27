---
role: proof
locale: en
of_concept: integral-basis-cyclotomic-field
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

Let $p$ be an odd prime and $z$ a primitive $p$-th root of unity. The minimal polynomial of $z$ is $F(Z) = Z^{p-1} + \cdots + Z + 1$. Its discriminant is $p^{p-2}$ (a standard computation).

The ring of integers $R'$ of $\mathbb{Q}(z)$ contains $\{1, z, \cdots, z^{p-2}\}$. For $r = 2, \cdots, p-1$, the element $(1-z^r)/(1-z) = 1+z+\cdots+z^{r-1} \in R'$. Its inverse $(1-z)/(1-z^r)$ is also in $R'$ since taking $r'$ with $rr' \equiv 1 \pmod{p}$ gives $z = z^{rr'}$, so $(1-z)/(1-z^r) = 1+z^r+\cdots+z^{(r'-1)r} \in R'$. Thus these are units.

From $p = F(1) = \prod_{r=1}^{p-1} (1-z^r)$, we deduce the prime factorization $R'p = R'(1-z)^{p-1}$, showing $[ \mathbb{Q}(z): \mathbb{Q} ] = p-1$. Hence $\{1, z, \cdots, z^{p-2}\}$ is an integral basis, and the discriminant of $R'$ over $\mathbb{Z}$ is $p^{p-2}$.
