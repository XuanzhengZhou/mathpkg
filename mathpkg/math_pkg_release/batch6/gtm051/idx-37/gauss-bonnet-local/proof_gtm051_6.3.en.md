---
role: proof
locale: en
of_concept: gauss-bonnet-local
source_book: gtm051
source_chapter: "6"
source_section: "6.3"
---

**1.** Suppose $P$ lies entirely in one geodesic coordinate system $(u^1, u^2)$. By (4.3.8), $K$ may be written as $\operatorname{div} X$:
$$K = -\frac{(\sqrt{g_{22}})_{,11}}{\sqrt{g_{22}}} = \frac{1}{\sqrt{g_{22}}} \left\{ \frac{\partial}{\partial u^1} \left( \sqrt{g_{22}} \left( -\frac{(\sqrt{g_{22}})_{,1}}{\sqrt{g_{22}}} \right) \right) \right\}.$$
Then
$$\iint_P K \, dM = \iint_P K \sqrt{g_{22}} \, du^1 du^2 = -\int_{\partial P} (\sqrt{g_{22}})_{,1} \, du^2.$$

The boundary $\partial P$ is a closed curve $u(t) = (u^1(t), u^2(t))$, $t \in I$. Let $I_j = [a_j, b_j]$, $0 \leq j \leq k$, be sub-intervals on which $u_j = u|_{I_j}$ is smooth. By (6.3.1),
$$-\int_{u \circ \partial P} (\sqrt{g_{22}})_{,1} \, du^2 = \sum_j \left( \int_{I_j} \dot{\theta}(t) \, dt - \int_{I_j} \kappa_g(t) \, dt \right).$$

We claim that $\sum_j \int_{I_j} \dot{\theta}(t) \, dt + \sum_j \alpha_j = 2\pi$, which will prove the theorem in this special case.

**2. Proof of claim.** If the metric $g$ were the Euclidean metric, i.e., if $g_{22} = 1$, then the claim would be precisely the Umlaufsatz (2.2.1). We reduce the general case to the Euclidean case as follows. On $U$, let
$$ds_\tau^2 = (du^1)^2 + g_{\tau 22}(du^2)^2, \quad 0 \leq \tau \leq 1,$$
be a family of line elements with
$$g_{\tau 22} = \tau + (1 - \tau)g_{22}.$$
For $\tau = 0$, $ds_0^2$ is the given line element on $U$ and, for $\tau = 1$, $ds_1^2$ is the Euclidean line element. Each $ds_\tau^2$, $0 \leq \tau \leq 1$, is a line element since $g_{\tau 22}$ is always strictly positive. For any $\tau \in [0, 1]$, we can define the exterior angles $\alpha_{\tau j}$ and the functions $\theta_{\tau j}$. These functions are continuous in $\tau$, since
$$\cos \theta_\tau(t) = \frac{g_\tau(E_{\tau 1}, \dot{u})}{\sqrt{g_\tau(E_{\tau 1}, E_{\tau 1})}\sqrt{g_\tau(\dot{u}, \dot{u})}}.$$

Thus $\sum_j \int_{I_j} \dot{\theta}_\tau(t) \, dt + \sum_j \alpha_{\tau j}$ is a continuous function of $\tau$. It is constant because it can only take values that are integer multiples of $2\pi$. Its value at $\tau = 1$ is $2\pi$ by the Umlaufsatz. Hence the sum equals $2\pi$ for $\tau = 0$ as well, proving the claim.

**3.** For the general case where $P$ does not lie in a single coordinate system, subdivide $F$ into polygons $F_\rho$, each lying in a single geodesic coordinate system. Let $f$ be the number of faces, $e$ the number of edges, and $v$ the number of vertices of this subdivision. By induction, $f - e + v = 1$: adjoining a triangle to a triangulation does not change this sum, and refining a general polygonal subdivision to a triangulation preserves it.

For each $F_\rho$, letting $\beta_{j_\rho} = \pi - \alpha_{j_\rho}$ be the interior angles, we have
$$\iint_{P_\rho} K \, dM + \int_{\partial P_\rho} \kappa_g \, dt = \sum_{j_\rho} \beta_{j_\rho} + (2 - k_\rho)\pi.$$

Summing over $\rho$, the left-hand side becomes $\iint_P K \, dM + \int_{\partial P} \kappa_g \, dt$ since the inner edges are each traversed twice, once in each direction, and thus cancel out. The right-hand side is computed as follows:
$$2\pi f \cdot \sum_\rho \sum_{j_\rho} \beta_{j_\rho} = \sum_j \beta_j + 2\pi \hat{v},$$
where $\hat{v}$ is the number of inner vertices and $\sum_j$ is taken over the exterior vertices. Also,
$$\sum_\rho \sum_{j_\rho} (-\pi) = -2\pi \hat{e} + \sum_j (-\pi),$$
where $\hat{e}$ is the number of internal edges. Since $-\hat{e} + \hat{v} = -e + v$, the right-hand side is
$$2\pi(f - e + v) + \sum_j (\beta_j - \pi) = 2\pi - \sum_j \alpha_j,$$
using $f - e + v = 1$ and $\beta_j = \pi - \alpha_j$. This completes the proof.
