---
role: proof
locale: en
of_concept: characterization-convex-curves
source_book: gtm051
source_chapter: "2"
source_section: "2.3"
---

**Proof of Theorem 2.3.2.**

*Step 1.* Without loss of generality (after possibly a change of variables), we may assume $|\dot{c}(t)| = 1$ (arc length parametrization). Let $\theta: I \to \mathbb{R}$ be the angle function defined in (2.1.3). By (1.4.1), we have $\dot{\theta}(t) = \kappa(t)$.

*Step 2.* Suppose $c$ is convex. We show $\kappa$ does not change sign by proving $\theta(t)$ is weakly monotone. If $\theta(t') = \theta(t'')$ and $t' < t''$, we claim $\theta$ is constant on $[t', t'']$.

Since $c$ is simple, there exists at least one point $t'''$ where $\theta(t''') = -\theta(t'') = -\theta(t')$. Using convexity, two of the tangent lines at $c(t'), c(t''), c(t''')$ must coincide.

Let $p_1 = c(t_1)$, $p_2 = c(t_2)$ with $t_1 < t_2$ be the two points of tangency for these coincident tangent lines, and consider the line segment $\overline{p_1 p_2}$. This segment must lie entirely on the image of $c$: suppose $q$ is a point on $\overline{p_1 p_2}$ not on the image. The line perpendicular to $\overline{p_1 p_2}$ through $q$ intersects $c$ in at least two points, which (by convexity) lie on the same side of $\overline{p_1 p_2}$. Let $r, s$ be the closest and farthest intersection points from $\overline{p_1 p_2}$. Then $r$ lies in the interior of triangle $p_1 p_2 s$. The tangent at $r$ would have points of $c$ on both sides, contradicting convexity.

Hence $\overline{p_1 p_2} = \{c(t) \mid t_1 \leq t \leq t_2\}$, which forces $\theta(t_1) = \theta(t) = \theta(t_2)$ for $t \in [t_1, t_2]$. In particular, $t_1 = t'$ and $t_2 = t''$, so $\theta$ is monotone, and $\kappa = \dot{\theta}$ does not change sign.

*Step 3.* Conversely, suppose $\kappa(t) \geq 0$ for all $t$ (the case $\kappa \leq 0$ is symmetric). Then $\theta$ is non-decreasing. Assume $c$ is not convex; then there exists $t_0$ and points on both sides of the tangent. A geometric argument using the monotonicity of $\theta$ leads to a contradiction with the simplicity of $c$. Therefore $c$ must be convex.
