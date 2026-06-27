---
role: proof
locale: en
of_concept: kummer-congruence
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

Select $c$ to be a primitive root modulo $p$ so that $c^k \neq 1 \pmod{p}$. Then $1 - c^k$ is a $p$-adic unit.

By Theorem 2.3, we have the integral representation

$$\frac{1}{k}B_k \equiv \frac{1}{1-c^k} \int_{\mathbf{Z}_p^*} x^{k-1} \, dE_{1,c}(x) \pmod{p}.$$

For $k$ in a fixed residue class $\alpha \not\equiv 0 \pmod{p-1}$, the value $c^k \pmod{p}$ is constant, hence $1-c^k \pmod{p}$ is constant. Moreover, $x^{k-1} \pmod{p}$ depends only on the residue class of $k$ modulo $p-1$ (since $x^{p-1} \equiv 1$ for $x \in \mathbf{Z}_p^*$). Therefore the integral expression modulo $p$ is independent of the choice of $k$ in the given residue class, and the congruence follows. The $p$-integrality follows from the fact that the denominator $1-c^k$ is a $p$-adic unit and the distribution $E_{1,c}$ is $p$-integral.
