---
role: proof
locale: en
of_concept: bernoulli-numbers-integral-formula
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distributions"
---

From the definition of the Bernoulli distribution $E_k$ and the change of variables $x \mapsto c^{-1}x$, we have

$$\int_{\mathbf{Z}_p} dE_k(x) = \int_{\mathbf{Z}_p} dE_k(c^{-1}x).$$

Now using Theorem 2.2, which gives $E_{k,c}(x) = x^{k-1}E_{1,c}(x)$, and the relation

$$E_k = E_{k,c} + c^k E_k \circ c^{-1},$$

we obtain

$$\int_{\mathbf{Z}_p^*} dE_k = \frac{1}{1-c^k} \int_{\mathbf{Z}_p^*} dE_{k,c}
= \frac{1}{1-c^k} \int_{\mathbf{Z}_p^*} x^{k-1} dE_{1,c}(x).$$

Since $\frac{1}{k}B_k$ is the value of the Bernoulli distribution integrated over $\mathbf{Z}_p$ (up to $p$-adic limits), the desired formula follows.
