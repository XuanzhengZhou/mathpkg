---
role: proof
locale: en
of_concept: coefficient-formula-for-matrix-expansion
source_book: gtm031
source_chapter: "VIII"
source_section: "1. Simplicity of $\\mathfrak{L}$"
---

Starting from the matrix expansion $A = \sum_{p,q} \bar{\alpha}_{pq} E_{pq}$, compute the right-hand side of the claimed formula:

$$\sum_k E_{ki} A E_{jk} = \sum_k E_{ki} \left(\sum_{p,q} \bar{\alpha}_{pq} E_{pq}\right) E_{jk} = \sum_{k,p,q} E_{ki} \bar{\alpha}_{pq} E_{pq} E_{jk}.$$

Using the commutation relation $\bar{\alpha}_{pq}E_{pq} = E_{pq}\bar{\alpha}_{pq}$ and the matrix unit multiplication rule $E_{pq}E_{jk} = \delta_{qj}E_{pk}$, we obtain

$$= \sum_{k,p,q} \bar{\alpha}_{pq} E_{ki} E_{pq} E_{jk} = \sum_{k,p,q} \bar{\alpha}_{pq} (\delta_{ip} E_{kq}) E_{jk} = \sum_{k,p,q} \bar{\alpha}_{pq} \delta_{ip} E_{kq} E_{jk}.$$

Now $E_{kq}E_{jk} = \delta_{qj} E_{kk}$, so

$$= \sum_{k,p,q} \bar{\alpha}_{pq} \delta_{ip} \delta_{qj} E_{kk} = \bar{\alpha}_{ij} \sum_k E_{kk} = \bar{\alpha}_{ij} \cdot 1 = \bar{\alpha}_{ij}.$$
