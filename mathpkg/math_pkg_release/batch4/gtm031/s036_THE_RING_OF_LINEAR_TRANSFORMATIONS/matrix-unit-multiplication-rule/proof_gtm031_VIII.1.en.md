---
role: proof
locale: en
of_concept: matrix-unit-multiplication-rule
source_book: gtm031
source_chapter: "VIII"
source_section: "1. Simplicity of $\\mathfrak{L}$"
---

The rules are verified by checking their action on the basis vectors $(e_1, e_2, \cdots, e_n)$. For the multiplication rule, compute the action of $E_{ij}E_{kl}$ on an arbitrary basis vector $e_r$:

$$e_r(E_{ij}E_{kl}) = (e_r E_{ij})E_{kl} = (\delta_{ir} e_j)E_{kl} = \delta_{ir} (e_j E_{kl}) = \delta_{ir} \delta_{jk} e_l.$$

On the other hand,

$$e_r (\delta_{jk} E_{il}) = \delta_{jk} (e_r E_{il}) = \delta_{jk} \delta_{ir} e_l.$$

Since both sides agree on every basis vector $e_r$, we have $E_{ij}E_{kl} = \delta_{jk}E_{il}$.

For the identity property, compute the action of $\sum_i E_{ii}$ on $e_r$:

$$e_r \left(\sum_i E_{ii}\right) = \sum_i e_r E_{ii} = \sum_i \delta_{ri} e_i = e_r.$$

Thus $\sum_{i=1}^n E_{ii} = 1$.
