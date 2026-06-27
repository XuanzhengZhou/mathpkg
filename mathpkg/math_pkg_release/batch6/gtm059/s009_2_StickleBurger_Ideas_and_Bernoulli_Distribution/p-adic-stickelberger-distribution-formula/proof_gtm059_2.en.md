---
role: proof
locale: en
of_concept: p-adic-stickelberger-distribution-formula
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

The proof uses the explicit formula for $E_k(x)$ in terms of Bernoulli polynomials and analyzes denominators. Using $E_k(x) = N^{k-1} B_k(\langle x/N \rangle)$ and the distribution relation B.3, one computes $E_{k,c}(x) = E_k(x) - c^k E_k(c^{-1}x)$. The key observation is that the Bernoulli polynomial $B_k(X)$ has denominator dividing the least common multiple of integers up to the denominator of $B_k$, and the subtraction $E_k(x) - c^k E_k(c^{-1}x)$ cancels the problematic fractional part when evaluated at level $N$. The congruence modulo $p^n \mathbb{Z}_p[c]$ follows from analyzing the $p$-adic valuations of the coefficients.

A more precise analysis using the formula $E_1(x) = \langle x \rangle - 1/2$ for $k=1$ and the property that $B_k(\langle x \rangle) - c^k B_k(\langle c^{-1}x \rangle)$ eliminates denominators yields the result.
