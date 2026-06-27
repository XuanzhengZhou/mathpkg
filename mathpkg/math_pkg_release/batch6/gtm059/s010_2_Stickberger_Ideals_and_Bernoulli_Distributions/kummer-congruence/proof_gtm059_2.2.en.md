---
role: proof
locale: en
of_concept: kummer-congruence
source_book: gtm059
source_chapter: "2"
source_section: "2"
---

Select $c$ to be a primitive root modulo $p$, so that $c^k \not\equiv 1 \pmod{p}$ when $k \not\equiv 0 \pmod{p-1}$. Then $1 - c^k$ is a $p$-adic unit. The integral representation of Bernoulli numbers gives
$$
\frac{B_k}{k} = \frac{1}{1 - c^k} \int_{\mathbb{Z}_p^*} x^{k-1} \, dE_1(x).
$$
The integral depends only on the residue class of $k$ modulo $p-1$, since for $x \in \mathbb{Z}_p^*$, the value $x^{k-1}$ modulo $p$ depends only on $k \bmod (p-1)$. The factor $1/(1-c^k)$ multiplied by the integral yields values that are congruent for $k \equiv a \pmod{p-1}$, giving the congruence.
