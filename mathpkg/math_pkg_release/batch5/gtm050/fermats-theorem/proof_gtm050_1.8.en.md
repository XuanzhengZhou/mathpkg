---
role: proof
locale: en
of_concept: fermats-theorem
source_book: gtm050
source_chapter: "1"
source_section: "1.8"
---

Consider the remainders of $1, 2, 4, 8, \ldots, 2^n, \ldots$ upon division by a prime $p$ not dividing $2$. There are only $p-1$ possible nonzero remainders, so by the pigeonhole principle there exist $n < n+m$ with $2^n \equiv 2^{n+m} \pmod{p}$. Then $p \mid 2^n(2^m - 1)$, hence $p \mid 2^m - 1$ (since $p \nmid 2$). Let $d$ be the least positive integer with $2^d \equiv 1 \pmod{p}$.

Fermat observed that $d$ must divide $p-1$. The nonzero remainders modulo $p$ can be partitioned into sets of size $d$ by multiplying a fixed set $\{1, 2, 2^2, \ldots, 2^{d-1}\}$ by elements not yet occurring. Since these sets are disjoint and cover all $p-1$ nonzero remainders, $d \mid (p-1)$.

Thus $2^{p-1} \equiv 1 \pmod{p}$. The same argument applies with any integer $a$ in place of $2$, yielding $a^{p-1} \equiv 1 \pmod{p}$ whenever $p \nmid a$.
