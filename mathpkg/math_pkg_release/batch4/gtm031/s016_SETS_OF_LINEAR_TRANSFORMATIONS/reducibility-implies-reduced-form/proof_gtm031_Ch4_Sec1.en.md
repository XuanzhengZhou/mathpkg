---
role: proof
locale: en
of_concept: reducibility-implies-reduced-form
source_book: gtm031
source_chapter: "IV"
source_section: "1"
---

Suppose $\mathfrak{S}$ is a proper invariant subspace under $\Omega$, i.e., $\mathfrak{S} \neq 0$ and $\mathfrak{S} \neq \Re$, and $\mathfrak{S}A \subseteq \mathfrak{S}$ for every $A \in \Omega$. Let $(f_1, f_2, \ldots, f_n)$ be a basis for $\Re$ such that $(f_1, f_2, \ldots, f_r)$ is a basis for $\mathfrak{S}$, where $0 < r < n$.

Since $\mathfrak{S}$ is invariant, for each $i = 1, 2, \ldots, r$ and each $A \in \Omega$, we have $f_i A \in \mathfrak{S}$. Therefore, expressing $f_i A$ as a linear combination of the basis vectors, we obtain

$$f_i A = \sum_{j=1}^{r} \beta_{ij} f_j, \quad i = 1, 2, \ldots, r.$$

The coefficients $\beta_{i,r+1}, \ldots, \beta_{in}$ are all zero because $f_i A$ lies in $\mathfrak{S}$, which is spanned by $f_1, \ldots, f_r$ alone. Thus the matrix of $A$ relative to the basis $(f_1, \ldots, f_n)$ has an $r \times (n-r)$ block of zeros in its upper right-hand corner. Such a matrix is said to have **reduced form**.

Hence the matrices of $\Omega$ relative to this basis all have reduced form. If $\omega$ is the set of matrices of $\Omega$ relative to the original basis $(e_1, \ldots, e_n)$, then there exists a non-singular matrix $(\mu)$ (the change of basis matrix) such that all matrices of $(\mu)\omega(\mu)^{-1}$ have the same reduced form with the same $r$ for all $A \in \Omega$.
