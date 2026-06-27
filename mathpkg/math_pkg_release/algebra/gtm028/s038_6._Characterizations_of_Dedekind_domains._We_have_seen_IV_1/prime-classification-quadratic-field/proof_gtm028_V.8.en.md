---
role: proof
locale: en
of_concept: prime-classification-quadratic-field
source_book: gtm028
source_chapter: "V"
source_section: "8"
---

We have $R' = \mathbb{Z} + i\mathbb{Z}$. For a prime $p$, Corollary to Theorem 21 gives $\sum_i e_i f_i = 2$, so the possible factorizations of $R'p$ are: $R'p = \mathfrak{P}_1 \mathfrak{P}_2$ (two distinct primes, $e_1=e_2=1$, $f_1=f_2=1$), $R'p = \mathfrak{P}$ (one prime, $e=1$, $f=2$), or $R'p = \mathfrak{P}^2$ (one prime, $e=2$, $f=1$).

From $R' = \mathbb{Z} + i\mathbb{Z}$, the residue field $R'/\mathfrak{P}$ is generated over $\mathbb{Z}/(p)$ by the $\mathfrak{P}$-residue of $i$, which is a root of $X^2 + 1$ in some extension of $\mathbb{Z}/(p)$. Thus:
- If $X^2 + 1$ has two distinct roots mod $p$, then $p \equiv 1 \pmod{4}$ and we have decomposition.
- If $X^2 + 1$ has a double root mod $p$, then $p = 2$ and we have ramification ($X^2+1 \equiv (X+1)^2$ mod 2).
- If $X^2 + 1$ is irreducible mod $p$, then $p \equiv 3 \pmod{4}$ and we have inertia.

For the decomposed case $p \equiv 1 \pmod{4}$: since $x \mapsto x-yi$ is an automorphism, the conjugate of $\mathfrak{P}_1 = R'(a+bi)$ is $\mathfrak{P}_2 = R'(a-bi)$, distinct. From $R'p = R'(a^2+b^2)$ and the fact that the only units in $R'$ are $1, -1, i, -i$, we obtain $p = a^2 + b^2$.
