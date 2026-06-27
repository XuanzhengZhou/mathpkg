---
role: proof
locale: en
of_concept: lemma-cube-in-quadratic-field
source_book: gtm050
source_chapter: "2"
source_section: "2.5"
---
The proof uses the factorization theory developed in Section 2.4 for the form $x^2+3y^2$:

(1) Factor $a^2+3b^2 = (a+b\sqrt{-3})(a-b\sqrt{-3})$. Using the classification of primes of the form $x^2+3y^2$ (every prime $p \equiv 1 \pmod{3}$ is of this form, except 3 itself), factor $a^2+3b^2 = P_1P_2\cdots P_n$ into primes.

(2) Each prime $P_i$ is either 3 (or 4) or an odd prime of the form $p = u^2+3v^2$. For each such prime factor $P$, one shows that $P$ divides either $pb+aq$ or $pb-aq$ where $p = a, q = b$ adjusted, allowing division by $P$ in $\mathbb{Z}[\sqrt{-3}]$.

(3) Iterating this division process yields a factorization:
$$a + b\sqrt{-3} = \pm(p_1 \pm q_1\sqrt{-3})(p_2 \pm q_2\sqrt{-3})\cdots(p_n \pm q_n\sqrt{-3})$$
where $p_i^2+3q_i^2 = P_i$.

(4) Since $a^2+3b^2$ is a cube, each prime factor appears with multiplicity a multiple of 3. Grouping in threes gives $a+b\sqrt{-3} = \pm(c+d\sqrt{-3})^3$, and since $-(c+d\sqrt{-3})^3 = (-c-d\sqrt{-3})^3$, the result follows.
