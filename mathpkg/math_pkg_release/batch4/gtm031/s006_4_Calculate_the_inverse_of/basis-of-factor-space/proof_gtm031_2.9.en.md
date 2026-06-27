---
role: proof
locale: en
of_concept: basis-of-factor-space
source_book: gtm031
source_chapter: "II: Finite Dimensional Vector Spaces"
source_section: "9: Factor Spaces"
---

Let $(f_1, f_2, \cdots, f_r)$ be a basis for $\mathfrak{S}$ and extend to a basis $(f_1, f_2, \cdots, f_r, f_{r+1}, \cdots, f_n)$ for $\mathfrak{R}$. We show that $\{\bar{f}_{r+1}, \cdots, \bar{f}_n\}$ is a basis for $\bar{\mathfrak{R}} = \mathfrak{R} / \mathfrak{S}$.

**Spanning:** For any $\bar{x} \in \bar{\mathfrak{R}}$ with representative $x \in \mathfrak{R}$, write $x = \sum_{i=1}^n \alpha_i f_i$. Then
$$
\bar{x} = \sum_{i=1}^n \alpha_i \bar{f}_i = \sum_{i=r+1}^n \alpha_i \bar{f}_i
$$
since $\bar{f}_1 = \cdots = \bar{f}_r = \bar{0}$ (because $f_1, \ldots, f_r \in \mathfrak{S}$). Thus $\{\bar{f}_{r+1}, \cdots, \bar{f}_n\}$ spans $\bar{\mathfrak{R}}$.

**Linear independence:** Suppose $\sum_{i=r+1}^n \beta_i \bar{f}_i = \bar{0}$. Then $\sum_{i=r+1}^n \beta_i f_i \in \mathfrak{S}$, so there exist $\gamma_1, \ldots, \gamma_r$ such that
$$
\sum_{i=r+1}^n \beta_i f_i = \sum_{j=1}^r \gamma_j f_j.
$$
Rearranging: $\sum_{j=1}^r (-\gamma_j) f_j + \sum_{i=r+1}^n \beta_i f_i = 0$. By linear independence of the full basis, all coefficients are zero, hence $\beta_i = 0$ for all $i = r+1, \ldots, n$.

Thus $\dim(\mathfrak{R} / \mathfrak{S}) = n - r = \dim \mathfrak{R} - \dim \mathfrak{S}$.
