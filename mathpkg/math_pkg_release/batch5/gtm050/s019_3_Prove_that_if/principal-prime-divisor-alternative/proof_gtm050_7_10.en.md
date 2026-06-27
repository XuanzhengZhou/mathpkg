---
role: proof
locale: en
of_concept: principal-prime-divisor-alternative
source_book: gtm050
source_chapter: "7"
source_section: "7.10"
---

Let $D = pq$ with $p, q \equiv 3 \pmod 4$. Both $p$ and $q$ are ramified primes, so $(p, *)^2 \sim I$ and $(q, *)^2 \sim I$. Thus the classes of $(p, *)$ and $(q, *)$ are ambiguous.

If both $(p, *)$ and $(q, *)$ were principal, then every divisor of the form $(p, *)^i (q, *)^j$ would also be principal, contradicting the fact that the class number for such determinants is greater than 1.

If neither were principal, then $(p, *)$ and $(q, *)$ would be distinct non-principal ambiguous classes. But since their product $(p, *)(q, *)$ corresponds to the divisor of $\sqrt{D}$ (up to equivalence), and $\sqrt{D}$ has norm $-D = -pq$, one can show that $(p, *)(q, *) \sim I$ because the norm of the product is, up to sign, $D$ itself, which is the norm of a principal divisor. This would force $(p, *) \sim (q, *)^{-1} \sim (q, *)$ (since each is of order 2), implying they are the same class, contradicting the assumption that neither is principal and they are distinct.

Therefore exactly one of $(p, *)$ or $(q, *)$ is principal, and the class group has exactly two classes: the principal class and one ambiguous class.
