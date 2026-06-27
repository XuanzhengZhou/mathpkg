---
role: proof
locale: en
of_concept: geodesic-reparametrization-affine
source_book: gtm048
source_chapter: "0"
source_section: "0.0.6"
---

Let $\gamma = \xi \circ \phi$, where $\phi: E \to F$ is a surjective $C^\infty$ map with $\phi' > 0$, and both $\gamma$ and $\xi$ are geodesics. Computing the tangent vector of $\gamma$:

$$\gamma_* = \xi_* \circ \phi \cdot \phi'.$$

Taking the covariant derivative along $\gamma$:

$$D_{\gamma_*} \gamma_* = D_{\gamma_*} (\xi_* \circ \phi \cdot \phi') = \phi' D_{\gamma_*} (\xi_* \circ \phi) + (\xi_* \circ \phi) \cdot \phi''.$$

By the chain rule for the covariant derivative, $D_{\gamma_*} (\xi_* \circ \phi) = \phi' (D_{\xi_*} \xi_*) \circ \phi$. Since $\xi$ is a geodesic, $D_{\xi_*} \xi_* = 0$, hence

$$D_{\gamma_*} \gamma_* = (\xi_* \circ \phi) \cdot \phi''.$$

Since $\gamma$ is also a geodesic, $D_{\gamma_*} \gamma_* = 0$. Because $\xi_* \circ \phi \neq 0$ (as a tangent vector of a curve), we must have $\phi'' \equiv 0$. Therefore $\phi(u) = au + b$ with $a, b \in \mathbb{R}$. The condition $\phi' > 0$ gives $a > 0$.
