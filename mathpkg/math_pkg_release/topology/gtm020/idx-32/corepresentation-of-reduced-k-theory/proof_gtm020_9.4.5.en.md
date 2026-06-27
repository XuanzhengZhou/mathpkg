---
role: proof
locale: en
of_concept: corepresentation-of-reduced-k-theory
source_book: gtm020
source_chapter: "9"
source_section: "4.5"
---

The proof proceeds in two parts: first establishing that $\phi^n_X: [X, G_n(F^{2n})] \to \tilde{K}_F(X)$ is a bijection for sufficiently large $n$, and then showing that this extends to the inductive limit $B_{(F)}$.

By (3.8), if $f^*(\gamma_n^{2n})$ and $g^*(\gamma_n^{2n})$ are $s$-equivalent and of the same dimension, then they are isomorphic over $X$. By 7(7.2), this implies $[f] = [g]$. Therefore $\phi_{X^n}$ is a bijection for each $X$, and $\phi^n$ is an isomorphism.

For the $H$-space structure, there exists a unique map $\psi: B_{(F)} \times B_{(F)} \rightarrow B_{(F)}$ such that the diagram

$$G_n(F^{2n}) \times G_n(F^{2n}) \xrightarrow{\psi_n} G_{2n}(F^{4n})$$

commutes with the vertical inclusion maps. For $[f], [g] \in [X, B_{(F)}]$, choose $n$ such that $f, g: X \rightarrow G_n(F^{2n})$. Then:

$$\theta([f]) = f^*(\gamma_n^{2n}) - n, \quad \theta([g]) = g^*(\gamma_n^{2n}) - n$$

Moreover, $(\psi_n(f \times g)\Delta)^*(\gamma_n^{4n}) = \Delta^*(f^*(\gamma_n^{2n}) \times g^*(\gamma_n^{2n})) = f^*(\gamma_n^{2n}) \oplus g^*(\gamma_n^{2n})$. Therefore, in $\tilde{K}_F(X)$:

$$\theta([\psi_n(f \times g)\Delta]) = f^*(\gamma_n^{2n}) \oplus g^*(\gamma_n^{2n}) - 2n = (f^*(\gamma_n^{2n}) - n) + (g^*(\gamma_n^{2n}) - n) = \theta([f]) + \theta([g])$$

This proves that $\theta$ is a group isomorphism.
