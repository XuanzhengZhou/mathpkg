---
role: proof
locale: en
of_concept: mean-relative-acceleration-ricci
source_book: gtm048
source_chapter: "4"
source_section: "4.2"
---

The proof relies on the definition of the map $\psi_z$ given above Proposition 2.3.3. If $\gamma : \mathcal{E} \to M$ is an observer in $Q$ with $\gamma(0) = z$ and $W$ is any neighbor of $\gamma$ in $Q$, then $\psi_z W(0)$ is the 3-acceleration of $W$ relative to $\gamma$ at proper time zero.

An alternative, conceptually more satisfactory definition expresses $\alpha$ as an integral mean over the unit sphere $S^2$ of the local rest space $\mathcal{T}$:

$$\alpha(z) = \frac{1}{\sigma} \int_{X \in S^2} g(\psi_z X, X) \, \zeta,$$

where $\zeta$ is the standard volume element on $S^2$ and $\sigma = \int_{S^2} \zeta = 4\pi$ (see Optional exercise 8.1.11). The equality of the trace definition and the integral definition follows from the self-adjointness of $\psi_z$ and elementary properties of integration over the sphere.

The relation $\alpha(z) = -\frac{1}{3} \operatorname{Ric}(Z, Z)$ is then derived by connecting $\psi_z$ to the curvature tensor through the Jacobi equation for geodesic deviation. Specifically, the relative acceleration of neighboring geodesics is governed by the Riemann curvature tensor contracted with the tangent vector, and the trace over the spatial directions yields the Ricci component $\operatorname{Ric}(Z, Z)$.

(Note: The full proof of this proposition is completed earlier in the text via Proposition 2.3.3 and the geodesic deviation equation. The statement as recorded here is applied in the subsequent argument to show that in vacuum $\operatorname{Ric}(Z, Z) = 0$ implies zero mean relative-acceleration.)
