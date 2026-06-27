---
role: proof
locale: en
of_concept: gcd-domain-properties
source_book: gtm057
source_chapter: "VIII"
source_section: "2"
---

**(2.4) Every UFD is a GCD domain.** Let $R$ be a UFD. For any nonzero elements $a_1, \dots, a_n$, factor each into primes: $a_i = u_i \prod_j p_j^{n_{ij}}$ (up to associates). Set $d = \prod_j p_j^{\min_i n_{ij}}$. Then $d \mid a_i$ for all $i$. If $e \mid a_i$ for all $i$, then in the prime factorization of $e$, each prime appears with exponent at most $\min_i n_{ij}$, so $e \mid d$. Thus $d$ is a GCD.

**(2.10) GCD via principal ideals.** If $d$ generates the smallest principal ideal containing $a_1, \dots, a_n$, then $d \mid a_i$ (since $a_i$ is in that ideal). For any $e$ with $e \mid a_i$, the principal ideal $(e)$ contains each $a_i$, so $(e) \supset (d)$ by minimality, hence $e \mid d$. Conversely, if $d = \gcd(a_1, \dots, a_n)$, then $(d)$ is the intersection of all principal ideals containing $\{a_i\}$.
