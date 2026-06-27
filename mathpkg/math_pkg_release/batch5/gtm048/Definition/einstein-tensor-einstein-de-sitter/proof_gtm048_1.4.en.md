---
role: proof
locale: en
of_concept: einstein-tensor-einstein-de-sitter
source_book: gtm048
source_chapter: "1"
source_section: "1.4"
---

Define an orthonormal basis of 1-forms by $\omega^\mu = (R \circ u^4) du^\mu$ for $\mu = 1, 2, 3$ and $\omega^4 = du^4$. For the Einstein–de Sitter spacetime, $R(u) = u^{2/3}$, so $\omega^\mu = (u^4)^{2/3} du^\mu$.

From the structure equations, one computes the connection forms and then the curvature forms. For the specific scale factor $R(u) = u^{2/3}$:

The connection 1-forms satisfy $\omega_\mu^4 = -\frac{2}{3}(u^4)^{-1} \omega^\mu$ and $\omega_\nu^\mu = 0$ for $\mu, \nu = 1, 2, 3$.

The curvature forms are then computed via $\Omega_j^i = d\omega_j^i + \sum_k \omega_k^i \wedge \omega_j^k$, giving:
- $\Omega_4^4 = 0$
- $\Omega_\mu^4 = -\frac{4}{9}(u^4)^{-2} \omega^4 \wedge \omega^\mu = \Omega_4^\mu$
- $\Omega_\nu^\mu = \frac{8}{9} \omega^\mu \wedge \omega^\nu = -\Omega_\mu^\nu$

The curvature tensor (1,3) is obtained from $\Omega_j^i = \frac{1}{2} \sum_{k,l} R_{jkl}^i \omega^k \wedge \omega^l$, yielding

$$R = \frac{4}{9}(u^4)^{-2} \left\{ \sum_{\rho,\sigma=1}^3 2X_\rho \otimes \omega^\sigma \otimes (\omega^\rho \wedge \omega^\sigma) - \sum_{\rho=1}^3 (X_\rho \otimes \omega^4 + X_4 \otimes \omega^\rho) \otimes (\omega^4 \wedge \omega^\rho) \right\},$$

where $\{X_i\}$ is the basis of vector fields dual to $\{\omega^i\}$.

The Ricci tensor is obtained by contraction. For the term $X_4 \otimes \omega^\mu \otimes (\omega^4 \wedge \omega^\mu)$, contracting on the first and third indices gives $\frac{1}{2} \omega^\mu \otimes \omega^\mu$. Summing all contributions yields $\operatorname{Ric} = \frac{2}{3}(u^4)^{-2} \sum_{k=1}^4 \omega^k \otimes \omega^k$.
