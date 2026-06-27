---
role: proof
locale: en
of_concept: developable-iff-zero-gauss-curvature
source_book: gtm051
source_chapter: "3"
source_section: "3.7"
---

If $f$ is developable, we know by Proposition 3.7.5 that $K = 0$.

Conversely, let $K = 0$. The absence of planar points allows us to assert the existence of unique (up to sign) mutually orthogonal principal curvature vector fields in a neighborhood of each point $u_0$ (see (3.5.3)). Using (3.6.6), we may introduce new coordinates $(v^1, v^2)$ on a neighborhood $U_0$ of $u_0$ such that the $v^1$-coordinate curves are integral curves of the principal curvature vector field corresponding to the principal curvature $\kappa_1 = 0$. Without loss of generality, we may assume that $(0, 0) \mapsto u_0$.

We change variables once more. Let $(s, t) \mapsto (v^1(s), t)$, where $v^1(s)$ is the inverse of the arc-length function along the curve $f(v^1, 0)$. Clearly, $\partial v^1(s)/\partial s \neq 0$. Therefore $\tilde{f} = f \circ \phi$ is a new coordinatization defined in a neighborhood of $(0, 0)$ with $\phi(0, 0) = 0$. In this new coordinatization, both $\tilde{f}(s, 0)$ and $\tilde{f}(0, t)$ are parameterized by arc length. The vector $\tilde{f}_s(0, 0)$ is a principal direction corresponding to $\kappa_1 = 0$.

Writing $f(s, t)$ instead of $\tilde{f}(s, t)$, we show that $f_{ss} = 0$. Indeed, along the curve $f(s, 0)$, $f_s$ is a principal direction with $\kappa_1 = 0$, so $n_s = -\kappa_1 f_s = 0$ along this curve. Since $f_{ss}$ is the acceleration of a unit-speed curve, and the curve $f(s, 0)$ is an asymptotic line (by $\kappa_1 = 0$), we obtain $f_{ss} = 0$ identically in a neighborhood. Thus $f(s, t) = s X(t) + c(t)$ for some $X(t)$ and $c(t)$, i.e., $f$ is a ruled surface.

Moreover, $n_s = 0$ along all generators, because $n_s \cdot f_s = -h_{11} = 0$ (since the $s$-curves are asymptotic) and $n_s \cdot f_t = -h_{12} = 0$ (since $K = h_{11}h_{22} - h_{12}^2 = 0 \cdot h_{22} - h_{12}^2 = -h_{12}^2$ implies $h_{12} = 0$). Therefore $n_s = 0$ everywhere, which means $f$ is developable.
