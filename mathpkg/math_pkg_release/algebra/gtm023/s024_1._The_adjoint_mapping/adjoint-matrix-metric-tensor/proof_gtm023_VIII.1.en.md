---
role: proof
locale: en
of_concept: adjoint-matrix-metric-tensor
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

Substituting $x = x_v$ and $y = y_\mu$ into the defining relation of the adjoint $(\varphi x, y) = (x, \tilde{\varphi} y)$ yields

$$(\varphi x_v, y_\mu) = (x_v, \tilde{\varphi} y_\mu).$$

Expanding $\varphi x_v$ and $\tilde{\varphi} y_\mu$ in terms of the bases:

$$\left(\sum_\kappa \alpha_v^\kappa y_\kappa,\; y_\mu\right) = \left(x_v,\; \sum_\lambda \tilde{\alpha}_\mu^\lambda x_\lambda\right).$$

By bilinearity of the inner product:

$$\sum_\kappa \alpha_v^\kappa (y_\kappa, y_\mu) = \sum_\lambda \tilde{\alpha}_\mu^\lambda (x_v, x_\lambda).$$

Introducing the metric tensor components $g_{v\lambda} = (x_v, x_\lambda)$ and $h_{\kappa\mu} = (y_\kappa, y_\mu)$, and using the symmetry of the inner product so that $h_{\kappa\mu} = h_{\mu\kappa}$, we obtain

$$\sum_\kappa \alpha_v^\kappa h_{\kappa\mu} = \sum_\lambda \tilde{\alpha}_\mu^\lambda g_{v\lambda}.$$

Multiplying both sides by the inverse matrix $g^{v\varphi}$ and summing over $v$ gives the explicit formula for $\tilde{\alpha}_\mu^\varphi$.
