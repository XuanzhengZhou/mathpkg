---
role: proof
locale: en
of_concept: matrix-of-bilinear-form
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

Let $(e_1, \dots, e_n)$ be a basis for $\mathfrak{R}$ and $(f_1', \dots, f_{n'}')$ be a basis for $\mathfrak{R}'$. Write $x = \sum_{i=1}^n \xi_i e_i$, $y' = \sum_{j=1}^{n'} f_j' \eta_j$. Using the bilinearity of $g$:

$$g(x, y') = g\!\left(\sum_i \xi_i e_i, \sum_j f_j' \eta_j\right) = \sum_{i,j} \xi_i \, g(e_i, f_j') \, \eta_j = \sum_{i,j} \xi_i \beta_{ij} \eta_j$$

where $\beta_{ij} = g(e_i, f_j')$. Thus the bilinear form is completely determined by the matrix $(\beta_{ij})$.

Conversely, given any $n \times n'$ matrix $(\beta_{ij})$ with entries in $\Delta$, define

$$h(x, y') = \sum_{i=1}^n \sum_{j=1}^{n'} \xi_i \beta_{ij} \eta_j.$$

We verify bilinearity: for fixed $y'$, $h(\cdot, y')$ is linear in $x$ because it is a linear combination of the coefficients $\xi_i$. For fixed $x$, $h(x, \cdot)$ is linear in $y'$ because it is a linear combination of the coefficients $\eta_j$. Explicitly,

$$h(x_1 + x_2, y') = \sum_{i,j} (\xi_i^{(1)} + \xi_i^{(2)}) \beta_{ij} \eta_j = h(x_1, y') + h(x_2, y'),$$

$$h(\alpha x, y') = \sum_{i,j} (\alpha \xi_i) \beta_{ij} \eta_j = \alpha \sum_{i,j} \xi_i \beta_{ij} \eta_j = \alpha h(x, y'),$$

and similarly for linearity in the second argument. Finally, $h(e_i, f_j') = \beta_{ij}$, so the matrix of $h$ is indeed the given matrix $(\beta_{ij})$.
