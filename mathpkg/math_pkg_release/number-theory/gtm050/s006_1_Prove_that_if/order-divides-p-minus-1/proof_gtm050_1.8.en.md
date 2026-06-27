---
role: proof
locale: en
of_concept: order-divides-p-minus-1
source_book: gtm050
source_chapter: "1"
source_section: "1.8"
---

Given a prime $p$ and $a$ not divisible by $p$, let $d$ be the order of $a$ modulo $p$. We must show that $d \mid (p-1)$.

Consider the $d$ distinct remainders $1, a, a^2, \ldots, a^{d-1}$ modulo $p$. If these exhaust all $p-1$ non-zero remainders, then $d = p-1$ and the statement holds.

Otherwise, pick a remainder $k_1$ not in this set. Consider the remainders of $k_1, ak_1, a^2k_1, \ldots, a^{d-1}k_1$. These are all distinct modulo $p$ (if $a^nk_1 \equiv a^mk_1$, then multiplying by $a^{d-n}$ gives $k_1 \equiv a^{m-n+d}k_1$, contradicting the definition of $d$ unless $n \equiv m \pmod{d}$). Moreover, none of these remainders is in the original set (if $a^nk_1 \equiv a^m$, then $k_1 \equiv a^{m-n} \pmod{p}$, contradicting the choice of $k_1$).

If these two sets together contain all $p-1$ non-zero remainders, then $p-1 = 2d$ and $d \mid (p-1)$. Otherwise, pick $k_2$ not in either set, and repeat. The process partitions the $p-1$ non-zero remainders into disjoint sets of size $d$ each, which implies $d \mid (p-1)$.

A simple consequence: $a^{(p-1)/2} \equiv \pm 1 \pmod{p}$. Also, the number of remainders $k$ such that the sets $k, 2k, 4k, \ldots$ contain all numbers $1, 2, \ldots, p-1$ is given by the Euler totient $\varphi(d)$, a fact used by Fermat to determine $2^{11}-1$ is not prime.
