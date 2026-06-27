---
role: proof
locale: en
of_concept: matrix-expansion-of-linear-transformation
source_book: gtm031
source_chapter: "VIII"
source_section: "1. Simplicity of $\\mathfrak{L}$"
---

Let $A \in \mathfrak{L}$ and write $e_i A = \sum_j \alpha_{ij} e_j$ with $\alpha_{ij} \in \Delta$. We verify that the transformation $\sum_{i,j} \bar{\alpha}_{ij} E_{ij}$ agrees with $A$ on every basis vector $e_r$:

$$e_r \left(\sum_{i,j} \bar{\alpha}_{ij} E_{ij}\right) = \sum_{i,j} e_r (\bar{\alpha}_{ij} E_{ij}) = \sum_{i,j} (e_r \bar{\alpha}_{ij}) E_{ij} = \sum_{i,j} (\alpha_{ij} e_r) E_{ij}.$$

Since $e_r E_{ij} = \delta_{ir} e_j$, we have

$$= \sum_{i,j} \alpha_{ij} \delta_{ir} e_j = \sum_j \alpha_{rj} e_j = e_r A.$$

Thus $A = \sum \bar{\alpha}_{ij} E_{ij}$. The alternative form $A = \sum E_{ij} \bar{\alpha}_{ij}$ follows from the commutation relation $\bar{\alpha}_{ij} E_{ij} = E_{ij} \bar{\alpha}_{ij}$.
