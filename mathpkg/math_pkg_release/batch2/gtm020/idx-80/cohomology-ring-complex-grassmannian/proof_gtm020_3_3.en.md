---
role: proof
locale: en
of_concept: cohomology-ring-complex-grassmannian
source_book: gtm020
source_chapter: "3"
source_section: "3"
---

The proof follows from the splitting principle. By Proposition 3.1, the map $h_n: CP^\infty \times \dots \times CP^\infty \rightarrow G_n(C^\infty)$ is a splitting map for $\gamma_n$, and $h_n^*$ is a monomorphism on cohomology. The pullback $h_n^*(\gamma_n) \cong \gamma \times \dots \times \gamma$ splits as a sum of line bundles. By the Whitney sum formula, $h_n^*(c_k) = \sigma_k(c_1(\gamma \otimes 1), \dots, c_1(1 \otimes \gamma))$ where $\sigma_k$ is the $k$-th elementary symmetric polynomial. Since the cohomology of the product $CP^\infty \times \dots \times CP^\infty$ is a polynomial ring $\mathbb{Z}[x_1, \dots, x_n]$ where $x_i = c_1$ of the $i$-th factor, and the image of $h_n^*$ consists of symmetric polynomials in the $x_i$, the injectivity of $h_n^*$ forces $H^*(G_n(C^\infty), \mathbb{Z})$ to be isomorphic to the ring of symmetric polynomials, which is $\mathbb{Z}[c_1, \dots, c_n]$ with $c_k$ corresponding to the $k$-th elementary symmetric polynomial.
