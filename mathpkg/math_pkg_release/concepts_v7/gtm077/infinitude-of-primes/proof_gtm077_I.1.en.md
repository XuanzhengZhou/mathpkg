---
role: proof
locale: en
of_concept: infinitude-of-primes
source_book: gtm077
source_chapter: "I"
source_section: "1"
---

# Proof of the Infinitude of Primes

**Theorem.** There are infinitely many prime numbers.

*Proof.* Suppose, for the sake of contradiction, that there are only finitely many primes, say $p_1, p_2, \ldots, p_n$. Consider the integer

$$z = p_1 \cdot p_2 \cdot \cdots \cdot p_n + 1.$$

By construction, $z$ is not divisible by any of the primes $p_1, \ldots, p_n$, because division by any $p_i$ leaves a remainder of $1$.

Now $z > 1$, so by the Fundamental Theorem of Arithmetic (Theorem 5), $z$ must be divisible by at least one prime number. Let $q$ be any prime divisor of $z$. Then $q$ must be distinct from all of $p_1, \ldots, p_n$ (since none of them divides $z$).

Thus, given any finite list of $n$ primes, we can always produce an $(n+1)$-st prime. Hence the set of primes is infinite.
