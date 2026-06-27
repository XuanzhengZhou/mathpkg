---
role: proof
locale: en
of_concept: matrix-form-composition-series
source_book: gtm031
source_chapter: "III"
source_section: "3"
---

Let $n_i = \dim(\mathfrak{S}_i/\mathfrak{S}_{i-1})$ and let $f_1, \dots, f_N$ be a basis of $\mathfrak{R}$ adapted to the composition series, so that the first $n_1$ vectors span $\mathfrak{S}_1$, the next $n_2$ together with the first $n_1$ span $\mathfrak{S}_2$, and so on. For a coset $\bar{f}_r = f_r + \mathfrak{S}_{i-1}$ with $f_r$ in $\mathfrak{S}_i$, the induced transformation $\bar{A}$ on $\mathfrak{S}_i/\mathfrak{S}_{i-1}$ acts by
$$\bar{f}_r \bar{A} = \sum_{s = n_1+\cdots+n_{i-1}+1}^{n_1+\cdots+n_i} \beta_{rs} \bar{f}_s.$$

Lifting to $\mathfrak{S}_i$, this means
$$f_r A = \sum_{s = n_1+\cdots+n_{i-1}+1}^{n_1+\cdots+n_i} \beta_{rs} f_s + (\text{terms in } \mathfrak{S}_{i-1}).$$

In the full matrix of $A$, the coordinates relative to basis vectors in $\mathfrak{S}_{i-1}$ contribute entries below the diagonal block $(\beta_i)$, which fill the $*$ positions. No terms from $\mathfrak{S}_i$ map into vectors whose leading component lies in $\mathfrak{S}_j$ with $j > i$, since $A$ preserves each $\mathfrak{S}_i$. Consequently, all entries above the diagonal blocks are zero. The diagonal block $(\beta_i)$ is precisely the matrix of $\bar{A}$ on $\mathfrak{S}_i/\mathfrak{S}_{i-1}$ relative to the coset basis.

The irreducibility of $\mathfrak{S}_i$ over $\mathfrak{S}_{i-1}$ means that there is no invertible matrix $(\mu_i)$ such that all the conjugates $(\mu_i)(\beta_i)(\mu_i)^{-1}$ (for all $A \in \Omega$) simultaneously take a common nontrivial reduced block form.
