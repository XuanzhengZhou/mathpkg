---
role: proof
locale: en
of_concept: euler-step-five-divisibility
source_book: gtm050
source_chapter: "2"
source_section: "2.6"
---

Consider the $4n$ numbers $1^{2n}, 2^{2n}, \ldots, (4n)^{2n}$ modulo $p$. Since $p = 4n+1$ is prime, by Fermat's little theorem, each number $k$ not divisible by $p$ satisfies $k^{4n} \equiv 1 \pmod{p}$, so $k^{2n} \equiv \pm 1 \pmod{p}$.

If all of $1^{2n}, 2^{2n}, \ldots, (4n)^{2n}$ were congruent to $+1$ modulo $p$, then the $(4n)$ numbers $1^{2n}-1, 2^{2n}-1, \ldots, (4n)^{2n}-1$ would all be divisible by $p$. But a polynomial of degree $2n$ over a field can have at most $2n$ roots, and here we would have $4n$ distinct residues each giving a root. Since $4n > 2n$, this is impossible.

Thus at least one of the numbers $k^{2n}$ must satisfy $k^{2n} \equiv -1 \pmod{p}$. Moreover, if any $k^{2n} \equiv -1$, then among the consecutive pairs $(1^{2n}+2^{2n}), (2^{2n}+3^{2n}), \ldots$, there must be a transition where one term is congruent to $+1$ and the next is congruent to $-1$ (or vice versa), making their sum divisible by $p$. More directly, since not all $k^{2n}$ are congruent, there exists some $k$ such that $k^{2n} \not\equiv (k+1)^{2n} \pmod{p}$, and hence $k^{2n} + (k+1)^{2n} \not\equiv 2k^{2n} \pmod{p}$. The pigeonhole principle then guarantees the existence of a pair whose sum is divisible by $p$.

In practice, one computes $2^{n} \bmod p$; if $2^{n} \equiv \pm 1 \pmod{p}$, then $2^{2n} \equiv 1 \pmod{p}$ and one tries $3^{n}$, continuing until an integer $c$ is found with $c^{n} \not\equiv \pm 1 \pmod{p}$ while $(c-1)^{n} \equiv \pm 1 \pmod{p}$. Then $p$ divides $c^{2n} + (c-1)^{2n}$.
