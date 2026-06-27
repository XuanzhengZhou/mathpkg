---
role: proof
locale: en
of_concept: adjoint-matrix-orthonormal-transpose
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

Under the assumption of orthonormal bases, the metric tensors satisfy $g_{v\lambda} = \delta_{v\lambda}$ and $h_{\kappa\mu} = \delta_{\kappa\mu}$. Substituting into the general formula

$$\tilde{\alpha}_\mu^\varphi = \sum_{v,\kappa} \alpha_v^\kappa h_{\kappa\mu} g^{v\varphi},$$

the inverse metric tensor is also the identity: $g^{v\varphi} = \delta_{v\varphi}$. The sum collapses:

$$\tilde{\alpha}_\mu^\varphi = \sum_{v,\kappa} \alpha_v^\kappa \delta_{\kappa\mu} \delta_{v\varphi} = \alpha_\varphi^\mu.$$

Thus $\tilde{\alpha}_\mu^v = \alpha_v^\mu$, i.e., the matrix of $\tilde{\varphi}$ is the transpose of the matrix of $\varphi$.
