---
role: proof
locale: en
of_concept: von-staudt-congruence
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

Suppose $p$ is odd. Let $c = 1 + p$. An easy induction shows that $c^k \equiv 1 + pk \pmod{p^2k\mathbf{Z}_p}$. Hence

$$\frac{1}{1 - c^k} = -\frac{1}{pk}(1 + O(p)).$$

By Theorem 2.3, we have

$$B_k \equiv -\frac{1}{p} \int_{\mathbf{Z}_p^*} x^{k-1} \, dE_{1,c}(x) \pmod{\mathbf{Z}_p},$$

because the integral over $p\mathbf{Z}_p$ is $\equiv 0 \pmod{p}$.

An approximating sum modulo $p$ for the integral over $\mathbf{Z}_p^*$ is

$$\sum_{x=1}^{p-1} x^k \equiv -1 \pmod{p},$$

where the congruence follows from the fact that the sum of $k$-th powers of the non-zero residues modulo $p$ is $-1$ modulo $p$ when $p-1 \mid k$, and $0$ otherwise. The case $p = 2$ is left as an exercise.

Thus $B_k \equiv -1/p \pmod{\mathbf{Z}_p}$ as claimed.
