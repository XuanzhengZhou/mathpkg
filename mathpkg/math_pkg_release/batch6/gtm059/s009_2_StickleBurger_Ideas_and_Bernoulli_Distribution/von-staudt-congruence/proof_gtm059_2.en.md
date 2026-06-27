---
role: proof
locale: en
of_concept: von-staudt-congruence
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

Assume $p$ is odd. Choose $c = 1 + p$. By induction, $c^{p^n} = 1 + p^{n+1} \pmod{p^{n+2}}$. Hence $1 - c^k \equiv -pk \pmod{p^2 \mathbb{Z}_p}$ when $k \equiv 0 \pmod{p-1}$, so that $1/(1-c^k) \equiv -1/(pk) \pmod{p^{-1}\mathbb{Z}_p}$.

From Theorem 2.3: $\frac{B_k}{k} = \frac{1}{1-c^k} \int x^{k-1} dE_{1,c}(x)$. The integral over $\mathbb{Z}_p^\times$ is $0 \pmod{p}$, and the contribution from $p\mathbb{Z}_p$ is computed via an approximating sum modulo $p$, yielding $1/p$ modulo $\mathbb{Z}_p$. Therefore $B_k/k \equiv -1/(pk) \pmod{\mathbb{Z}_p}$, giving $B_k \equiv -1/p \pmod{\mathbb{Z}_p}$.

For $p=2$, a similar direct computation confirms the result.
