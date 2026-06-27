---
role: proof
locale: en
of_concept: quadratic-residue-primes-density-half
source_book: gtm007
source_chapter: "VI"
source_section: "4"
---

We may assume $a$ is square-free. Let $m = 4|a|$ and let $\chi_a$ be the character modulo $m$ constructed in Proposition 5, which satisfies $\chi_a(p) = \left(\frac{a}{p}\right)$ for $p \nmid m$. Let $H = \ker(\chi_a) \subset G(m)$, so that $[G(m):H] = 2$.

For a prime $p \nmid m$, $\left(\frac{a}{p}\right) = 1$ if and only if $\chi_a(p) = 1$, i.e., $p \bmod m$ lies in $H$. Since $H$ has index $2$ in $G(m)$, the density of primes whose residue class lies in $H$ is $|H|/\phi(m) = 1/2$ by the density theorem. Hence the set of such primes has density $1/2$.

