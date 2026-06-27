---
role: proof
locale: en
of_concept: von-staudt-congruence
source_book: gtm059
source_chapter: "2"
source_section: "2"
---

For simplicity, assume $p$ is odd. Let $c = 1 + p$. An easy induction shows that $c^k \equiv 1 + pk \pmod{p^2 \mathbb{Z}_p}$. Hence
$$
\frac{1}{1 - c^k} \equiv -\frac{1}{pk} \pmod{\mathbb{Z}_p}.
$$
Using the integral representation
$$
\frac{B_k}{k} = \frac{1}{1 - c^k} \int_{\mathbb{Z}_p^*} x^{k-1} \, dE_1(x),
$$
the integral over $p\mathbb{Z}_p$ is congruent to $0$ modulo $p$, and approximating the integral over $\mathbb{Z}_p^*$ by a sum gives
$$
B_k \equiv -\frac{1}{p} \pmod{\mathbb{Z}_p}.
$$
The case $p = 2$ is handled similarly.
