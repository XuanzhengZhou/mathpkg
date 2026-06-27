---
role: proof
locale: en
of_concept: number-of-ramifying-primes
source_book: gtm050
source_chapter: "7"
source_section: "7.10"
---

The primes which ramify in the quadratic order with discriminant $D$ are precisely the odd prime factors of $D$ (when $D \equiv 1 \pmod 4$), and these together with $2$ (when $D \equiv 2$ or $3 \pmod 4$). This is because a prime $p$ ramifies if and only if $p$ divides the discriminant. The number of such primes is therefore $m + \varepsilon$, where $m$ is the number of distinct odd prime factors of $D$ and $\varepsilon$ is $1$ when $D \not\equiv 1 \pmod 4$ (so 2 ramifies) and $0$ otherwise.

Each divisor of the form $(p_1,*)(p_2,*)\cdots(p_k,*)$, with each $p_i$ a ramifying prime (or $-1$ when $D > 0$), corresponds to a choice of a subset of the set of ramifying primes. Since there are $m + \varepsilon$ such primes, there are $2^{m+\varepsilon}$ possible subsets (including the empty set, which corresponds to the empty product $I$). Thus when $D < 0$, the number of such divisors is at most $2^{m+\varepsilon}$.
