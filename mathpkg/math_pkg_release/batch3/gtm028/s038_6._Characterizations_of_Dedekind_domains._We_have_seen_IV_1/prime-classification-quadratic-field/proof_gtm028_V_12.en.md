---
role: proof
locale: en
of_concept: prime-classification-quadratic-field
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

The minimal polynomial of a generator of $R$ over $\mathbb{Z}$ is $X^2 - m$ (when $m \equiv 2,3 \bmod 4$) or $X^2 - X - (m-1)/4$ (when $m \equiv 1 \bmod 4$). For an odd prime $p \nmid m$, reducing modulo $p$ gives a quadratic polynomial over $\mathbb{F}_p$. Its factorization determines the decomposition: two distinct linear factors mean $p$ splits (decomposed), an irreducible quadratic means $p$ is inertial. This happens precisely when $m$ is a square mod $p$, i.e., $\left(\frac{m}{p}\right) = 1$.

For $p=2$: when $m \equiv 2,3 \pmod{4}$, $2$ divides the discriminant, so $2$ ramifies. When $m \equiv 1 \pmod{4}$, the minimal polynomial is $X^2 - X - (m-1)/4$. Modulo $2$, this is reducible iff $(m-1)/4$ is even, i.e., $m \equiv 1 \pmod{8}$ (decomposed); otherwise it is irreducible, i.e., $m \equiv 5 \pmod{8}$ (inertial).
