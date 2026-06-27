---
role: proof
locale: en
of_concept: fermat-little-theorem
source_book: gtm050
source_chapter: "1"
source_section: "1.8"
---

Consider the remainders left by the successive powers $1, 2, 4, 8, \ldots$ (i.e., $2^0, 2^1, 2^2, 2^3, \ldots$) when divided by a prime $p$ that does not divide 2. Since there are only $p$ possible remainders, among the sequence of powers of 2 there must be at least one repetition. Suppose $2^n$ and $2^{n+m}$ leave the same remainder. Then $p$ divides their difference:

$$2^{n+m} - 2^n = 2^n(2^m - 1).$$

Since $p$ is prime and does not divide 2 (so $p \nmid 2^n$), it follows that $p$ divides $2^m - 1$, hence $2^m \equiv 1 \pmod{p}$. Therefore 1 occurs as a remainder.

Let $d$ be the least positive integer such that $2^d \equiv 1 \pmod{p}$. Then $2^{md}$ also leaves remainder 1 for any $m$, because $2^{md} - 1 = (2^d - 1)(2^{(m-1)d} + \cdots + 2^d + 1)$ is divisible by $p$. Conversely, if $2^m \equiv 1 \pmod{p}$, write $m = qd + r$ with $0 \leq r < d$. Then $2^m = 2^{qd} \cdot 2^r$. Since $2^{qd} \equiv 1 \pmod{p}$, we must have $2^r \equiv 1 \pmod{p}$. By the minimality of $d$, necessarily $r = 0$, so $d \mid m$.

Thus the $d$ distinct remainders $1, 2^1, 2^2, \ldots, 2^{d-1} \pmod{p}$ occur in a cyclic pattern, and $2^m \equiv 1 \pmod{p}$ if and only if $d \mid m$.

This argument works for any integer $a$ not divisible by $p$. To prove $a^{p-1} \equiv 1 \pmod{p}$, it remains to show that $d \mid (p-1)$. This is proved by a partitioning argument: consider the remainders of $k, ak, a^2k, \ldots, a^{d-1}k$ for each remainder $k$ not yet covered. Each such set has size $d$, and the sets are disjoint and partition the $p-1$ non-zero remainders. Therefore $d \mid (p-1)$, and in particular $a^{p-1} \equiv 1 \pmod{p}$.

This argument establishes Fermat's theorem for arbitrary $a$ coprime to $p$ (by replacing 2 with $a$ throughout the reasoning).
