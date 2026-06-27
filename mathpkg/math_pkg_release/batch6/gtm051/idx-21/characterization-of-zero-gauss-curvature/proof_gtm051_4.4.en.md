---
role: proof
locale: en
of_concept: characterization-of-zero-gauss-curvature
source_book: gtm051
source_chapter: "4"
source_section: "4.4"
---

**Proof of Theorem 4.4.2.**

$(i) \Rightarrow (ii)$: Since $K \equiv 0$, in a geodesic coordinate system the Gauss curvature formula $K = -(\sqrt{g_{22}})_{,11} / \sqrt{g_{22}}$ (see 4.3.8) implies $(\sqrt{g_{22}})_{,11} = 0$. Hence $\sqrt{g_{22}}(u^1, u^2) = a(u^2) u^1 + b(u^2)$. Since $g_{22}(0, u^2) = 1$ and $g_{22,1}(0, u^2) = 0$ for the geodesic basis curve, we have $a(u^2) = 0$ and $b(u^2) = 1$, so $g_{22} \equiv 1$. Together with $g_{11} = 1$ and $g_{12} = 0$ from Lemma 4.3.6, we obtain $g_{ik} = \delta_{ik}$.

$(ii) \Rightarrow (iii)$: If $g_{ik} = \delta_{ik}$ are constants, then all Christoffel symbols $\Gamma_{ij}^k = 0$. The equation for parallel translation $\dot{X}^k + \sum_{i,j} \Gamma_{ij}^k \dot{u}^i X^j = 0$ reduces to $\dot{X}^k = 0$, meaning a parallel vector field has constant components in these coordinates. Hence parallel translation depends only on the initial and final coordinate values, not on the path.

$(iii) \Rightarrow (iv)$: Let $(u^1, u^2)$ be geodesic parallel coordinates based on a geodesic $(0, u^2)$. We wish to show that the curves $u^1 = u_0^1$ are also geodesics. Consider the unit vector $a = e_2/\sqrt{g_{22}}(u_0^1, 0) \in T_{(u_0^1, 0)} \mathbb{R}^2$. Since the curve $u^2 = 0$ is a geodesic and $e_2$ is perpendicular to it, the parallel translation of $a$ along $u^2 = 0$ to the point $(0, 0)$ must be a unit vector perpendicular to $u^2 = 0$ at $(0, 0)$, hence $e_2/\sqrt{g_{22}}(0, 0)$. Since $u^1 = 0$ is a unit-speed geodesic, the parallel translate of $e_2/\sqrt{g_{22}}(0, 0)$ along this curve is simply the tangent vector to this curve, with value $e_2/\sqrt{g_{22}}(0, u_0^2)$ at $u_0^2$. Parallel translation of this vector along $u^2 = u_0^2$ to $(u_0^1, u_0^2)$ preserves orthogonality and length, giving $e_2/\sqrt{g_{22}}(u_0^1, u_0^2)$.

Since parallel translation is independent of path, the parallel translate of $a$ along $u^1 = u_0^1$ at $(u_0^1, u_0^2)$ must equal $e_2/\sqrt{g_{22}}(u_0^1, u_0^2)$. Thus $e_2/\sqrt{g_{22}}$ is a parallel vector field along $u^1 = u_0^1$, and the curves $u^1 = \text{constant}$ are geodesics. Both families of coordinate curves are geodesics, hence the surface is locally isometric to a plane.

$(iv) \Rightarrow (i)$: If a surface is locally isometric to the Euclidean plane, then by the Gauss Theorema Egregium, its Gauss curvature equals that of the plane, which is identically zero. Hence $K \equiv 0$.

The equivalence of all four conditions is established.
