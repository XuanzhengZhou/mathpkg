---
role: proof
locale: en
of_concept: geodesic-curvature-in-geodesic-coordinates
source_book: gtm051
source_chapter: "6"
source_section: "6.3"
---

In geodesic coordinates $(u^1, u^2)$, the line element is $ds^2 = (du^1)^2 + g_{22}(du^2)^2$. Let $E_1 = \partial/\partial u^1$ and $E_2 = (1/\sqrt{g_{22}}) \partial/\partial u^2$ be the orthonormal frame. Since $g(E_i, E_k) = \delta_{ik}$, we have
$$g(\nabla E_i/dt, E_k) + g(E_i, \nabla E_k/dt) = 0,$$
and in particular $g(\nabla E_i/dt, E_i) = 0$. Therefore the geodesic curvature decomposes as
$$\kappa_g(t) = \dot{\theta}(t) + g(\nabla E_1/dt, E_2)(t),$$
where $\theta(t)$ is the angle between $E_1$ and $\dot{u}(t)$.

Now $\nabla E_1/dt = \sum_{i,k} \dot{u}^i \Gamma_{1i}^k e_k$. In geodesic coordinates (see (4.2.4)), the Christoffel symbols satisfy
$$\Gamma_{12}^2 = \frac{(\sqrt{g_{22}})_{,1}}{\sqrt{g_{22}}}, \quad \Gamma_{11}^1 = \Gamma_{11}^2 = \Gamma_{21}^1 = 0.$$
Substituting these into the expression for $\kappa_g(t)$ yields the simplified formula
$$\kappa_g(t) = \dot{\theta}(t) - (\sqrt{g_{22}})_{,1} \cdot \dot{u}^2(t).$$
