---
role: proof
locale: en
of_concept: separable-elements-form-a-field
source_book: gtm028
source_chapter: "II"
source_section: "5. Separable and inseparable algebraic extension"
---

The proof uses Theorem 8 (the criterion $kK^p = K$). Let $k_0$ be the set of all elements of $K$ that are separable algebraic over $k$. To show $k_0$ is a field, it suffices to prove that $k_0$ is closed under the field operations.

For any finite set of elements $x_1, \ldots, x_r \in k_0$, consider the subfield $k(x_1, \ldots, x_r)$. This is a finite separable extension of $k$ (by Theorem 9 on transitivity of separable extensions, which is proved using Theorem 8 and the characterization that separability is preserved under composition of separable extensions). The sum, product, and inverse of separable elements lie in a finitely generated separable extension, hence are themselves separable over $k$.

More formally, using Theorem 8: if $L = k(x_1, \ldots, x_r)$ where each $x_i$ is separable over $k$, then $L$ is a finite separable extension, so by Theorem 8, $kL^p = L$. Any element of $L$ is then separable over $k$ by the converse direction of Theorem 8. Thus $k_0$ is closed under addition, multiplication, and taking inverses, and is therefore a field containing $k$.
