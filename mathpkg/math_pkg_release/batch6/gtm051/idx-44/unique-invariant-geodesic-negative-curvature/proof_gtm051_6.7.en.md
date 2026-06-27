---
role: proof
locale: en
of_concept: unique-invariant-geodesic-negative-curvature
source_book: gtm051
source_chapter: "6"
source_section: "6.7"
---

**Proof.** Suppose $K < 0$. Let $\tilde{c}(t)$ and $\tilde{c}'(t)$, $t \in \mathbb{R}$, be $\gamma$-invariant geodesics in $\tilde{M}$ satisfying

$$\gamma \tilde{c}(t) = \tilde{c}(t + \omega), \quad \gamma \tilde{c}'(t) = \tilde{c}'(t + \omega').$$

We must show that $\tilde{c}'(t) = \tilde{c}(t + t_0)$ for some fixed $t_0 \in \mathbb{R}$.

Consider the geodesic quadrilateral with vertices $A = \tilde{c}(0)$, $B = \tilde{c}(\omega)$, $C = \tilde{c}'(\omega')$, and $D = \tilde{c}'(0)$. The edges are the geodesic segments joining consecutive vertices: $AB$ along $\tilde{c}$, $BC$ (the unique geodesic connecting $B$ and $C$), $CD$ along $\tilde{c}'$ (in reverse direction), and $DA$ (the unique geodesic connecting $D$ and $A$).

If the quadrilateral is degenerate (i.e., all four vertices lie on a common geodesic), then $\tilde{c}$ and $\tilde{c}'$ must coincide up to parameter translation, and we are done.

Suppose for contradiction that the quadrilateral is nondegenerate. Since $\gamma$ is an isometry, it maps the geodesic $\tilde{c}$ to itself and the geodesic $\tilde{c}'$ to itself. Moreover, $\gamma$ maps the edge $DA$ (joining $\tilde{c}'(0)$ to $\tilde{c}(0)$) to the edge $CB$ (joining $\tilde{c}'(\omega')$ to $\tilde{c}(\omega)$), because $\gamma \tilde{c}'(0) = \tilde{c}'(\omega')$ and $\gamma \tilde{c}(0) = \tilde{c}(\omega)$. Since $\gamma$ preserves angles, the interior angles at $D$ and $B$ are equal, and similarly the interior angles at $A$ and $C$ are equal. Therefore the sum of the four interior angles of the quadrilateral equals $2(\angle A + \angle D) = 2\pi$, because the angles around the intersection of the geodesics at each vertex sum appropriately.

However, by the Gauss-Bonnet theorem (Corollary 6.3.3(ii)), for a geodesic quadrilateral in a surface of strictly negative Gauss curvature $K < 0$, the sum of the interior angles satisfies

$$\sum_{i=1}^4 \alpha_i < 2\pi.$$

This contradiction shows that the quadrilateral must be degenerate. Hence $\tilde{c}'(t) = \tilde{c}(t + t_0)$ for some $t_0 \in \mathbb{R}$.
