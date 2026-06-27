---
role: proof
locale: en
of_concept: dirichlet-lemma-fifth-power
source_book: gtm050
source_chapter: "3"
source_section: "3.3"
---
Using the theory of factorization in $\mathbb{Z}[\sqrt{5}]$ (granted for the purpose of this argument), one can write:
$$P + Q\sqrt{5} = (p_1 + q_1\sqrt{5})^{n_1} \cdots (p_k + q_k\sqrt{5})^{n_k} (t + u\sqrt{5})$$
where $p_i^2 - 5q_i^2$ are primes and $t^2 - 5u^2 = \pm 1$ (a unit).

Since $P^2 - 5Q^2$ is a fifth power, each $n_i$ is a multiple of 5, and the unit factor equals $(9+4\sqrt{5})^r$ for some $r$. Thus $P + Q\sqrt{5} = (A + B\sqrt{5})^5 (9+4\sqrt{5})^r$ with $0 \leq r \leq 4$.

Expanding: $Q = 5A^4B + 50A^2B^3 + 25B^5$ (from the $(A+B\sqrt{5})^5$ part), times the unit factor $E+F\sqrt{5} = (9+4\sqrt{5})^r$. Since $D \equiv 0 \pmod{5}$ (where $D$ is the coefficient from $(A+B\sqrt{5})^5$), and $Q = CF + DE \equiv 0 \pmod{5}$ with $C \not\equiv 0 \pmod{5}$, we must have $F \equiv 0 \pmod{5}$.

But if $r \geq 1$, then $F = r \cdot 9^{r-1} \cdot 4$ plus multiples of 5, which cannot be divisible by 5. Hence $r = 0$, and $P + Q\sqrt{5} = (A+B\sqrt{5})^5$ as desired.
