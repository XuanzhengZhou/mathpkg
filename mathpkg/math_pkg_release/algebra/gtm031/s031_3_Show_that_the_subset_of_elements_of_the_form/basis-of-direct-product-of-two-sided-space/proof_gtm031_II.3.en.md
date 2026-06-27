---
role: proof
locale: en
of_concept: basis-of-direct-product-of-two-sided-space
source_book: gtm031
source_chapter: "II"
source_section: "3"
---

Let $\mathfrak{R}$ be a two-sided vector space over $\Delta$ with left basis $(e_1, \dots, e_n)$ and $\mathfrak{S}$ a left vector space over $\Delta$ with basis $(f_1, \dots, f_m)$. Consider the left vector space $\mathfrak{P} = \mathfrak{R} \times \mathfrak{S}$ with scalar multiplication defined by $\alpha(\sum x_i \times y_i) = \sum \alpha x_i \times y_i$.

**Spanning**: Any $x \in \mathfrak{R}$ can be written as $x = \sum_i \xi_i e_i$ with $\xi_i \in \Delta$. Any $y \in \mathfrak{S}$ can be written as $y = \sum_j \eta_j f_j$ with $\eta_j \in \Delta$. Then for an arbitrary element $\sum_k x_k \times y_k \in \mathfrak{P}$, each $x_k = \sum_i \xi_{ki} e_i$ and $y_k = \sum_j \eta_{kj} f_j$. Hence

$$\sum_k x_k \times y_k = \sum_k \left(\sum_i \xi_{ki} e_i\right) \times \left(\sum_j \eta_{kj} f_j\right) = \sum_{i,j} \left(\sum_k \xi_{ki} \eta_{kj}\right) e_i \times f_j,$$

where we use the bilinearity of $\times$. This proves that any vector in $\mathfrak{P}$ is a left linear combination of the vectors $e_i \times f_j$.

**Linear Independence**: Suppose $\sum_{i,j} \gamma_{ij} (e_i \times f_j) = 0$ with $\gamma_{ij} \in \Delta$. Then

$$0 = \sum_j \left(\sum_i \gamma_{ij} e_i\right) \times f_j.$$

Since the $f_j$ are linearly independent in $\mathfrak{S}$, this forces $\sum_i \gamma_{ij} e_i = 0$ for each $j = 1, 2, \dots, m$. Since the $e_i$ are linearly independent in $\mathfrak{R}$, we obtain $\gamma_{ij} = 0$ for all $i, j$.

Thus $\{e_i \times f_j\}$ is a basis of $\mathfrak{P}$.
