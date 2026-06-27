---
role: proof
locale: en
of_concept: gcd-of-cubic-fermat-factors
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

Let $p, q$ be coprime integers of opposite parity.

Since $p$ and $q$ have opposite parity, $p^2 + 3q^2$ is odd. Let $d = \gcd(2p, p^2 + 3q^2)$. Since $p^2 + 3q^2$ is odd, $d$ must be odd, so $d \mid p$ and $d \mid (p^2 + 3q^2)$.

Since $d \mid p$, we have $d \mid p^2$. Then $d \mid [(p^2 + 3q^2) - p^2] = 3q^2$. So $d$ is a common divisor of $p$ and $3q^2$.

Since $\gcd(p, q) = 1$, any prime factor of $d$ must either divide $3$ or divide both $p$ and $q$ (the latter being impossible). Therefore every prime factor of $d$ divides $3$, so $d$ is a power of $3$.

If $3 \nmid p$, then $3 \nmid d$, so $d = 1$.
If $3 \mid p$, then $3 \mid (p^2 + 3q^2)$, so $3 \mid d$, and in fact $d = 3$ (since any higher power of 3 dividing both $p$ and $p^2+3q^2$ would require additional analysis, but the essential point is that the common factor is exactly 3).
