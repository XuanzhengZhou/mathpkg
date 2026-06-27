---
role: proof
locale: en
of_concept: kummer-congruence
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

Select $c$ to be a primitive root modulo $p$, so that $c^{p-1} \equiv 1 \pmod{p}$ but $c^k \not\equiv 1 \pmod{p}$ for $k \not\equiv 0 \pmod{p-1}$. Then $1 - c^k$ is a $p$-adic unit. By Theorem 2.3, $(1-c^k) B_k/k = \int x^{k-1} dE_{1,c}(x)$. Since $x^{k-1} \equiv x^{k+p-1-1} \pmod{p}$ for $x \in \mathbb{Z}_p^\times$, the integrals for different $k$ in the same residue class modulo $p-1$ are $p$-adically close. Iterating this argument with higher powers of $p$ yields the full Kummer congruence.

More precisely, if $k_1 = k_2 + (p-1)p^{a-1}t$, then $x^{k_1-1} \equiv x^{k_2-1} \pmod{p^a}$ for all $x \in \mathbb{Z}_p^\times$, and the congruence of the integrals follows.
