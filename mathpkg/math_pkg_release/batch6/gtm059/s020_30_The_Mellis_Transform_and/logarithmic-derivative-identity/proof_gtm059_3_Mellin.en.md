---
role: proof
locale: en
of_concept: logarithmic-derivative-identity
source_book: gtm059
source_chapter: "3"
source_section: "The Mellin Transform and p-adic L-function"
---

Take the logarithmic derivative of the polynomial

$$T^* - \left( 1 + \prod_{i=1}^{N} \left( T - i^* \right) \right),$$

where $i^*$ ranges over suitable roots of unity. The logarithmic derivative yields an expression for $\sum_{i=1}^{N} B(i)$, from which we obtain

$$\sum_{i=1}^{N} B(i) = \frac{S_{l,l}}{N} \sum_{i=1}^{N} \frac{T}{N} = \frac{T}{N}.$$

Multiplying through by $S_{l,l}$ and $Q(N)$ then gives the desired identity

$$\frac{S_{l,l}}{N} \sum_{i=1}^{N} B(i) = \frac{T}{N} = g_{l,l}(G_l(T)) - G_l(T).$$
