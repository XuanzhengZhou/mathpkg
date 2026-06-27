---
role: proof
locale: en
of_concept: l-function-principal-character
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

For $\chi = 1$, $\chi(n) = 1$ if $\gcd(n,m) = 1$ and $0$ otherwise. Hence
$$
L(s,1) = \sum_{\gcd(n,m)=1} \frac{1}{n^s} = \zeta(s) \prod_{p \mid m} \left(1 - \frac{1}{p^s}\right)
$$
by factoring out the Euler factors at primes dividing $m$ from the Euler product of $\zeta(s)$. Since $\zeta(s)$ has a simple pole at $s=1$ with residue $1$, and $F(1) = \prod_{p \mid m} (1-1/p) = \phi(m)/m$, the function $L(s,1)$ has a simple pole at $s=1$ with residue $\phi(m)/m$.
