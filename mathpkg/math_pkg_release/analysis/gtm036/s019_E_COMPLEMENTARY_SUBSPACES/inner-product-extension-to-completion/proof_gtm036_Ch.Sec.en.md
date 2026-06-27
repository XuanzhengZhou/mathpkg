---
role: proof
locale: en
of_concept: inner-product-extension-to-completion
source_book: gtm036
source_chapter: ""
source_section: ""
---

Let $\langle \cdot, \cdot \rangle$ be the inner product on $E$. For Cauchy sequences $(x_n)$ and $(y_n)$ in $E$, define $\langle [(x_n)], [(y_n)] \rangle_H = \lim_{n \to \infty} \langle x_n, y_n \rangle$. The limit exists because $|\langle x_n, y_n \rangle - \langle x_m, y_m \rangle| \leq |\langle x_n, y_n - y_m \rangle| + |\langle x_n - x_m, y_m \rangle| \leq \|x_n\| \|y_n - y_m\| + \|x_n - x_m\| \|y_m\|$, and $\|x_n\|$, $\|y_m\|$ are bounded since Cauchy sequences are bounded. The definition is independent of the choice of representatives. The extended function is sesquilinear, Hermitian, and positive definite by continuity. The norm induced by this extended inner product coincides with the completion norm, making $H$ a Hilbert space.
