---
role: proof
locale: en
of_concept: existence-of-associated-character
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

Assume first $a = \ell_1 \cdots \ell_k$ with distinct odd primes $\ell_i$. Define
$$
\chi_a(x) = (-1)^{\varepsilon(x)\varepsilon(a)} \prod_{i=1}^k \left(\frac{x}{\ell_i}\right).
$$
For a prime $p \neq 2, \ell_i$, the quadratic reciprocity law gives $(p/\ell_i) = (\ell_i/p)(-1)^{\varepsilon(p)\varepsilon(\ell_i)}$, which combines with the $\varepsilon$ factors to yield $\chi_a(p) = \prod (\ell_i/p) = (a/p)$.

One checks $\chi_a \neq 1$: choose $x$ with $(x/\ell_1) = -1$ and $x \equiv 1 \pmod{4\ell_2 \cdots \ell_k}$; then $\chi_a(x) = -1$.

When $a = -b, 2b,$ or $-2b$, take the product of $\chi_b$ with $(-1)^{\varepsilon(x)}$, $(-1)^{\omega(x)}$, or $(-1)^{\varepsilon(x)+\omega(x)}$ respectively.
