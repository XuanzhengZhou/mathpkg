---
role: proof
locale: en
of_concept: characterization-of-geodesics-by-geodesic-curvature
source_book: gtm051
source_chapter: "4"
source_section: "4.3"
---

The geodesic curvature is invariant under reparametrization by (4.2.6), so $\kappa_g(t) = 0$ if and only if $\kappa_g(s) = 0$ for the unit-speed parameter $s$.

For a unit-speed curve $\tilde{c}(s)$, the geodesic curvature formula simplifies. Since $|\tilde{c}'(s)| = 1$, we have $e_1(s) = \tilde{c}'(s)$, and

$$\kappa_g(s) = e_2(s) \cdot \frac{\nabla e_1(s)}{ds} = e_2(s) \cdot \frac{\nabla \tilde{c}'(s)}{ds}.$$

But $e_2(s)$ is orthogonal to $e_1(s) = \tilde{c}'(s)$, and the covariant derivative $\nabla \tilde{c}'(s)/ds$ is orthogonal to $\tilde{c}'(s)$ (since $|\tilde{c}'(s)|^2 = 1$ implies $\frac{d}{ds}|\tilde{c}'(s)|^2 = 2 \tilde{c}'(s) \cdot \nabla \tilde{c}'(s)/ds = 0$). Hence $\nabla \tilde{c}'(s)/ds$ is parallel to $e_2(s)$, and the equality $\kappa_g(s) = 0$ is equivalent to $\nabla \tilde{c}'(s)/ds = 0$, which is precisely the condition that $\tilde{c}(s)$ is a geodesic.

Thus we have the chain of equivalences:

$$\kappa_g(t) = 0 \;\Longleftrightarrow\; \kappa_g(s) = 0 \;\Longleftrightarrow\; \frac{\nabla \tilde{c}'(s)}{ds} = 0,$$

which proves the proposition.
