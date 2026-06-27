---
role: proof
locale: en
of_concept: e-birkhoff-subcategory-characterization
source_book: gtm026
source_chapter: "4"
source_section: "2. If every equalizer is in M"
---

Let $\mathcal{B}$ be an $\mathsf{E}$-Birkhoff subcategory. Then $\mathcal{B}$ is closed under $\mathsf{U}^{\mathbf{T}}$-split epimorphisms by definition. In the context of the diagram

$$
\begin{array}{ccc}
\mathcal{B} & \longrightarrow & \mathcal{K}^{\mathbf{T}} \\
\downarrow U & & \downarrow U^{\mathbf{T}} \\
\mathcal{K} & \longleftarrow & \mathcal{B}
\end{array}
$$

$U$ is algebraic by 3.3 and, by 1.28 (2), $\mathcal{B}$ is closed under limits. To prove that $\mathcal{B}$ is closed under $\mathsf{M}$, let $m : (X, \xi) \to (B, \theta)$ be a $\mathbf{T}$-homomorphism with $m \in \mathsf{M}$. Consider the reflection $(B, \theta) \to (B\bar{T}, \xi_B)$. By the definition of $\mathsf{E}$-Birkhoff subcategory, the reflection map on free algebras is in $\mathsf{E}$, and the factorization properties of $(\mathsf{E}, \mathsf{M})$ force $m$ to be reflected into $\mathcal{B}$, establishing closure under $\mathsf{M}$.

Conversely, assume $\mathcal{B}$ is closed under limits, $\mathsf{M}$, and $\mathsf{U}^{\mathbf{T}}$-split epimorphisms. For the second statement, when every equalizer is in $\mathsf{M}$, closure under limits reduces to closure under products because equalizers are in $\mathsf{M}$ and can be constructed from products and pullbacks.
