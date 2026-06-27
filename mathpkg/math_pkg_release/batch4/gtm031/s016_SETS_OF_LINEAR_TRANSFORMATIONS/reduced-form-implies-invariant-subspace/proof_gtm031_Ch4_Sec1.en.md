---
role: proof
locale: en
of_concept: reduced-form-implies-invariant-subspace
source_book: gtm031
source_chapter: "IV"
source_section: "1"
---

Suppose that all the matrices of $(\mu)\omega(\mu)^{-1}$ have the reduced form with an $r \times (n-r)$ block of zeros in the upper right corner. Define the new basis vectors by $f_i = \sum_j \mu_{ij} e_j$ for $i = 1, 2, \ldots, n$. Then the matrices of $\Omega$ relative to $(f_1, f_2, \ldots, f_n)$ constitute the set $(\mu)\omega(\mu)^{-1}$.

Because of the reduced form of these matrices, for each $A \in \Omega$ and each $i = 1, 2, \ldots, r$, the image $f_i A$ is expressed as a linear combination of $f_1, \ldots, f_r$ only (since the coefficients for $f_{r+1}, \ldots, f_n$ in the $i$-th row are zero by the reduced form). Explicitly,

$$f_i A = \sum_{j=1}^{r} \beta_{ij} f_j \in [f_1, \ldots, f_r], \quad i = 1, 2, \ldots, r.$$

These relations show that the space $\mathfrak{S} = [f_1, f_2, \ldots, f_r]$ satisfies $\mathfrak{S}A \subseteq \mathfrak{S}$ for every $A \in \Omega$. Hence $\mathfrak{S}$ is invariant under $\Omega$. Since $0 < r < n$ (otherwise the reduced form would be trivial), $\mathfrak{S}$ is a proper invariant subspace, so $\Omega$ is reducible.
