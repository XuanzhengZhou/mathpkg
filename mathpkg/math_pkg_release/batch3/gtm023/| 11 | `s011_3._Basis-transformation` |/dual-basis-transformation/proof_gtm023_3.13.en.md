---
role: proof
locale: en
of_concept: dual-basis-transformation
source_book: gtm023
source_chapter: "I"
source_section: "3.13"
---

Write the dual basis transformations as

$$\bar{x}^{*\varrho} = \sum_{\sigma} \beta_{\sigma}^{\varrho} x^{*\sigma}, \qquad x^{*\sigma} = \sum_{\tau} \check{\beta}_{\tau}^{\sigma} \bar{x}^{*\tau}.$$

From the relations

$$x_v = \sum_{\mu} \check{\alpha}_v^\mu \bar{x}_\mu$$

and the definition of the dual basis, we compute the pairing in two ways:

$$\langle \bar{x}^{*\varrho}, x_v \rangle = \left\langle \sum_{\sigma} \beta_{\sigma}^{\varrho} x^{*\sigma}, \; x_v \right\rangle = \sum_{\sigma} \beta_{\sigma}^{\varrho} \langle x^{*\sigma}, x_v \rangle = \beta_{v}^{\varrho}.$$

On the other hand,

$$\langle \bar{x}^{*\varrho}, x_v \rangle = \left\langle \bar{x}^{*\varrho}, \; \sum_{\mu} \check{\alpha}_v^\mu \bar{x}_\mu \right\rangle = \sum_{\mu} \check{\alpha}_v^\mu \langle \bar{x}^{*\varrho}, \bar{x}_\mu \rangle = \check{\alpha}_{v}^{\varrho}.$$

Comparing both expressions yields

$$\beta_{v}^{\varrho} = \check{\alpha}_{v}^{\varrho}.$$

Thus the dual basis transforms by the inverse of the original basis transformation matrix.
