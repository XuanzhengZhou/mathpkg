---
role: proof
locale: en
of_concept: orthogonal-change-of-basis-matrix
source_book: gtm023
source_chapter: "7"
source_section: "2. Orthonormal bases"
---

Let \(\bar{x}_{\nu} = \sum_{\lambda} \alpha_{\nu}^{\lambda} x_{\lambda}\) be the basis transformation. Since both bases are orthonormal, we have

$$(x_{\nu}, x_{\mu}) = \delta_{\nu\mu} \quad \text{and} \quad (\bar{x}_{\nu}, \bar{x}_{\mu}) = \delta_{\nu\mu}.$$

Computing the inner product \((\bar{x}_{\nu}, \bar{x}_{\mu})\) using the expansion:

$$(\bar{x}_{\nu}, \bar{x}_{\mu}) = \left( \sum_{\lambda} \alpha_{\nu}^{\lambda} x_{\lambda}, \sum_{\rho} \alpha_{\mu}^{\rho} x_{\rho} \right) = \sum_{\lambda, \rho} \alpha_{\nu}^{\lambda} \alpha_{\mu}^{\rho} (x_{\lambda}, x_{\rho}).$$

Since \((x_{\lambda}, x_{\rho}) = \delta_{\lambda\rho}\), the sum collapses to a single index:

$$(\bar{x}_{\nu}, \bar{x}_{\mu}) = \sum_{\lambda} \alpha_{\nu}^{\lambda} \alpha_{\mu}^{\lambda}.$$

But \((\bar{x}_{\nu}, \bar{x}_{\mu}) = \delta_{\nu\mu}\) by orthonormality, hence

$$\sum_{\lambda} \alpha_{\nu}^{\lambda} \alpha_{\mu}^{\lambda} = \delta_{\nu\mu}.$$

This is precisely the condition that the product of the matrix \((\alpha_{\nu}^{\mu})\) and its transpose equals the identity matrix. In other words, the transpose coincides with the inverse, and the matrix is orthogonal.
