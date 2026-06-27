---
role: proof
locale: en
of_concept: stickelbergers-theorem
source_book: gtm059
source_chapter: "1"
source_section: "2"
---

The proof proceeds by induction on $k$. 

For $k = 0$, the result follows from the fact that $S(1) = -1$ has trivial valuation.

Assume $1 \leq k < q-1$. Write $k$ in base $p$: $k = k_0 + k_1 p + \dots + k_t p^t$ with $0 \leq k_i \leq p-1$. The proof uses properties of the Gauss sum $S(\chi)$ under the action of the Galois group. Specifically, one considers the expression
$$\frac{S(\chi^k)}{S(\chi)^k}$$
and studies its behavior under the automorphisms $\sigma_{i,j}$ sending $\zeta_p \mapsto \zeta_p^i$ and $\zeta_{q-1} \mapsto \zeta_{q-1}^j$.

The key congruence established is:
$$\frac{S(\chi^k)}{S(\chi)^k} \equiv \frac{1}{\prod_{i=0}^{t} k_i!} \pmod{\mathfrak{P}}.$$

This is proved by induction on the $p$-adic valuation, using the fact that $\zeta_p - 1$ is a uniformizer at $\mathfrak{P}$ and that $\operatorname{ord}_{\mathfrak{P}}(\zeta_p - 1) = 1/(p-1)$.

The argument involves analyzing sums of the form $\sum \chi(x)^k$ modulo powers of $\mathfrak{P}$, using the $p$-adic expansion to reduce the problem to the case where $k < p$. For $k < p$, one uses the congruence
$$\sum_{x \in F_q^*} \chi(x)^k \equiv 0 \pmod{\mathfrak{P}^k},$$
which follows from the fact that the sum of $k$-th powers in the finite field vanishes modulo higher powers of $p$ for $k$ not divisible by $q-1$.

By induction on the sum of $p$-adic digits and careful manipulation of the Gauss sum quotients, one obtains the full formula for $\operatorname{ord}_{\mathfrak{P}} S(\chi)$. The proof concludes by verifying that the congruence yields the stated valuation, thereby establishing the theorem.
