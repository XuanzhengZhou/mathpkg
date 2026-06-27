---
role: proof
locale: en
of_concept: l-function-principal-character
source_book: gtm007
source_chapter: "VI"
source_section: "3"
---

Since the principal character satisfies $\chi_0(n) = 1$ if $\gcd(n,m) = 1$ and $0$ otherwise, the Euler product gives
$$L(s,1) = \prod_{p \nmid m} \frac{1}{1-p^{-s}} = \prod_{p} \frac{1}{1-p^{-s}} \cdot \prod_{p \mid m} (1-p^{-s}) = \zeta(s) \prod_{p \mid m} (1-p^{-s}).$$

The factor $F(s) = \prod_{p \mid m} (1-p^{-s})$ is entire and nonzero at $s = 1$, so $L(s,1)$ inherits the simple pole of $\zeta(s)$ at $s = 1$.

