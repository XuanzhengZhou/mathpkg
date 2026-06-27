---
role: proof
locale: en
of_concept: theorem-d-radon-nikodym-jacobian
source_book: gtm018
source_chapter: "VIII"
source_section: "39. Measurable Transformations"
---
Write $\phi = \frac{d(\mu T^{-1})}{d\nu}$ (cf. §32). By Theorem C,
$$\int g \, d(\mu T^{-1}) = \int (gT) \, d\mu.$$
Since $\mu T^{-1} \ll \nu$, the Radon-Nikodym theorem (32.B) gives
$$\int g \, d(\mu T^{-1}) = \int g \, \phi \, d\nu.$$
Combining yields $\int (gT) \, d\mu = \int g \, \phi \, d\nu$, the desired result. The function $\phi$ plays the role of the Jacobian (or, rather, the absolute value of the Jacobian) in the theory of transformations of multiple integrals.
