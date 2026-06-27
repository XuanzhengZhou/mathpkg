---
role: proof
locale: en
of_concept: gravitational-plane-wave-vacuum-not-flat
source_book: gtm048
source_chapter: "7"
source_section: "7.6"
---

Let $\{\omega^i\}$ be the basis dual to the orthonormal frame $\{X_i\}$. By algebra, $\omega^1 = du^1$, $\omega^2 = du^2$, $\omega^3 = \frac{1}{2}(du^4 + du^3) - F d\phi$, $\omega^4 = d\phi$.

To compute the connection forms, note that $(\omega^1, \omega^2, (\omega^3 - \omega^4)/2, (\omega^3 + \omega^4)/2)$ is also orthonormal. Computing the exterior derivatives $d\omega^i$ and using Cartan's first structure equation $d\omega^i = -\omega_j^i \wedge \omega^j$, one finds the connection 1-forms.

From the connection forms, the curvature 2-forms $\Omega_j^i = d\omega_j^i + \omega_k^i \wedge \omega_j^k$ are computed. The only non-vanishing components are those involving $f''(\phi)$ and $g''(\phi)$. The Ricci tensor is obtained by contraction and vanishes identically because the only non-zero curvature components have the structure where each index pair contributes canceling terms.

However, the full Riemann tensor does not vanish (specifically $R_{1414}$ and $R_{1424}$ are non-zero when $f''$ or $g''$ are non-zero), so the spacetime is not flat.
