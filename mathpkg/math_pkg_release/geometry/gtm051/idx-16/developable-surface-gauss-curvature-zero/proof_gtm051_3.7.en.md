---
role: proof
locale: en
of_concept: developable-surface-gauss-curvature-zero
source_book: gtm051
source_chapter: "3"
source_section: "3.7"
---

**Proof.**

If $f$ is developable, we know by Proposition 3.7.5 that $K = 0$.

Conversely, let $K = 0$. The absence of planar points allows us to assert the existence of unique (up to sign) mutually orthogonal principal curvature vector fields in a neighborhood of each point $u_0$ (see (3.5.3)). Using (3.6.6), we may introduce new coordinates $(v^1, v^2)$ on a neighborhood $U_0$ of $u_0$ such that the $v^1$-coordinate curves are integral curves of the principal curvature vector field corresponding to the principal curvature $\kappa_1 = 0$. Without loss of generality, we may assume that $(0, 0) \mapsto u_0$.

We change variables once more. Let $(s, t) \to (v^1(s), t)$, where $v^1(s)$ is the inverse of the arc-length function along the curve $f(v^1, 0)$. Clearly, $\partial v^1(s)/\partial s \neq 0$. Therefore $\tilde{f} = f \circ \phi$ is a new coordinatization defined in a neighborhood of $(0, 0)$ with $\phi(0, 0) = 0$. In this new coordinatization, both $\tilde{f}(s, 0)$ and $\tilde{f}(0, t)$ are parameterized by arc length. The vector $\tilde{f}_s(0, 0)$ is a principal direction corresponding to $\kappa_1 = 0$.

Agreeing to write $f(s, t)$ instead of $\tilde{f}(s, t)$, we show that $f_{ss} = 0$. First observe that the principal direction condition $\kappa_1 = 0$ along the $s$-curves implies that the normal curvature in that direction vanishes, so $h_{11} = 0$. Using the Codazzi equations and the fact that $K = 0$, one can then deduce that $f_{ss}$ is orthogonal to the surface normal $n$ and lies in the tangent plane. Since the $(s, t)$-coordinates are chosen along principal directions, a computation shows $f_{ss} = 0$ identically near $(0, 0)$.

Thus $f$ is ruled in these coordinates, being linear in $s$: $f(s, t) = s X(t) + c(t)$ locally. By the construction, the normal $n$ is constant along the $s$-direction (generators), so $n_s = 0$, and $f$ is developable. $\square$
