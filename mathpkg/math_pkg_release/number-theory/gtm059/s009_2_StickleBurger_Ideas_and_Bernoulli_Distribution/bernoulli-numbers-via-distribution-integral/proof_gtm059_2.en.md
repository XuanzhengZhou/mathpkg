---
role: proof
locale: en
of_concept: bernoulli-numbers-via-distribution-integral
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

The formula follows from taking the trivial character $\psi = 1$ in Theorem 2.1. For the trivial character, the generalized Bernoulli number $B_{k,1}$ equals the classical Bernoulli number $B_k$, with the caveat that the Euler factor at $p$ must be accounted for. The integral over $\mathbb{Z}_p^\times$ of $x^{k-1} dE_{1,c}(x)$ yields $(1 - c^k) B_k/k$. Alternatively, one can compute directly from the definition of the Bernoulli distribution using approximating Riemann sums:

$$\int_{\mathbb{Z}_p} x^{k-1} dE_1(x) = \lim_{n \to \infty} \frac{1}{p^n} \sum_{a=0}^{p^n-1} a^{k-1} E_1^{(p^n)}(a) = \frac{B_k}{k}.$$

The regularization by $1 - c^k$ then gives the stated formula.
