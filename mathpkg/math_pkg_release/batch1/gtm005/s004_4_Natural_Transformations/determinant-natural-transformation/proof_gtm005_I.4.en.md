---
role: proof
locale: en
of_concept: determinant-natural-transformation
source_book: gtm005
source_chapter: "I"
source_section: "4"
---

Let $U: \mathbf{CRng} \to \mathbf{Mon}$ be the forgetful functor to multiplicative monoids. Define $\det: \mathbf{GL}_n \Rightarrow U$ with components $\det_R: \mathbf{GL}_n(R) \to U(R)$.

For a ring homomorphism $f: R \to S$, naturality requires $\det_S \circ \mathbf{GL}_n(f) = U(f) \circ \det_R$. For $M \in \mathbf{GL}_n(R)$, the matrix $\mathbf{GL}_n(f)(M)$ is obtained by applying $f$ to each entry. The determinant is a polynomial in the entries: $\det(M) = \sum_{\sigma} \operatorname{sgn}(\sigma) \prod_i M_{i,\sigma(i)}$. Since $f$ is a ring homomorphism,
$$\det_S(f(M_{ij})) = f(\det_R(M_{ij})).$$
Thus $\det_S(\mathbf{GL}_n(f)(M)) = f(\det_R(M))$, proving naturality.
