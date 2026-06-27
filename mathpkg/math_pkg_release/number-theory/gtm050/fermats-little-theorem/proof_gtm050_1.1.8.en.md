---
role: proof
locale: en
of_concept: fermats-little-theorem
source_book: gtm050
source_chapter: "1"
source_section: "1.8"
---
Consider the remainders of the powers $1, a, a^2, a^3, \ldots$ when divided by $p$. Since there are only $p$ possible remainders, by the pigeonhole principle there exist $n < n+m$ such that $a^n \equiv a^{n+m} \pmod{p}$. Then $p \mid a^n(a^m-1)$. Since $p \nmid a$, we have $p \mid a^m-1$, so $a^m \equiv 1 \pmod{p}$.

Let $d$ be the smallest positive integer such that $a^d \equiv 1 \pmod{p}$. Then $a^k \equiv 1 \pmod{p}$ if and only if $d \mid k$. The $d$ remainders $1, a, a^2, \ldots, a^{d-1}$ are all distinct. Moreover, for any $b$ not divisible by $p$, the remainders of $b, ba, ba^2, \ldots, ba^{d-1}$ are also distinct and disjoint from the first set if $b$ is not among them. This partitions the $p-1$ nonzero remainders into sets of size $d$, so $d \mid (p-1)$. Hence $a^{p-1} \equiv (a^d)^{(p-1)/d} \equiv 1 \pmod{p}$.
