---
role: proof
locale: en
of_concept: cohomology-ring-real-grassmannian-mod-2
source_book: gtm020
source_chapter: "3"
source_section: "5"
---

The proof parallels that of Theorem 3.2, working mod 2. By Proposition 5.1, the map $h_n: RP^\infty \times \dots \times RP^\infty \rightarrow G_n(R^\infty)$ is a splitting map and induces a monomorphism $h_n^*$ on $\mathbb{Z}_2$ cohomology. The pullback splits $h_n^*(\gamma_n) \cong \gamma \times \dots \times \gamma$, and by the Whitney product formula, $h_n^*(w_k)$ is the $k$-th elementary symmetric polynomial in the $x_i = w_1(\gamma)$ of the factors. Since $H^*(RP^\infty; \mathbb{Z}_2) = \mathbb{Z}_2[x]$ with $x = w_1(\gamma)$, the product has cohomology $\mathbb{Z}_2[x_1, \dots, x_n]$. The image of $h_n^*$ consists of symmetric polynomials in the $x_i$, and by injectivity this forces $H^*(G_n(R^\infty);\mathbb{Z}_2)$ to be isomorphic to the ring of symmetric polynomials, which is $\mathbb{Z}_2[w_1, \dots, w_n]$.
