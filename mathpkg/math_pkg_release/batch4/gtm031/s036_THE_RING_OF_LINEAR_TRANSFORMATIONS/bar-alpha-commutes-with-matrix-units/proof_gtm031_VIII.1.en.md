---
role: proof
locale: en
of_concept: bar-alpha-commutes-with-matrix-units
source_book: gtm031
source_chapter: "VIII"
source_section: "1. Simplicity of $\\mathfrak{L}$"
---

It is easy to verify the commutation by checking the action on basis vectors. Compute $e_r(\bar{\alpha} E_{ij})$:

$$e_r(\bar{\alpha}E_{ij}) = (e_r \bar{\alpha})E_{ij} = (\alpha e_r)E_{ij} = \alpha (e_r E_{ij}) = \alpha(\delta_{ir} e_j) = \delta_{ir}(\alpha e_j).$$

Now compute $e_r(E_{ij}\bar{\alpha})$:

$$e_r(E_{ij}\bar{\alpha}) = (e_r E_{ij})\bar{\alpha} = (\delta_{ir} e_j)\bar{\alpha} = \delta_{ir}(e_j \bar{\alpha}) = \delta_{ir}(\alpha e_j).$$

Both sides agree on every basis vector $e_r$, hence $\bar{\alpha}E_{ij} = E_{ij}\bar{\alpha}$.
