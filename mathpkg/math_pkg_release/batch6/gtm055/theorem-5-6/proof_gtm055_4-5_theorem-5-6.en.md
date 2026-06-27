---
role: proof
locale: en
of_concept: theorem-5-6
source_book: gtm055
source_chapter: "4-5"
source_section: "Section 06_Section_6"
---

Proof. Since $W$ is compact it is easily seen that $w_{\gamma}(\lambda)$ tends to zero as $\lambda$ tends to infinity. Similarly it is easy to verify that $w_{\gamma}$ is continuous on $\mathbb{C} \setminus W$. (If $\lambda_0 \notin W$ and if $\lambda$ is sufficiently close to $\lambda_0$, then $1/(\zeta - \lambda)$ tends uniformly to $1/(\zeta - \lambda_0)$ on $W$ as $\lambda$ tends to $\lambda_0$.) Hence it is enough to prove that $w_{\gamma}$ assumes only integral values on $\mathbb{C} \setminus W$. Moreover (Prob. D(iii)) we may, and do, assume that $\gamma$ is piecewise smooth. Suppose $\gamma$ is defined on the parameter interval $[a, b]$, so that

$$w_{\gamma}(\lambda) = \frac{1}{2\pi i} \int_{a}^{b} \frac{\gamma'(t)}{\gamma(t) - \lambda} dt$$

(Prob. F). If we define

$$\varphi(s) = \exp \left\{ \int_{a}^{s} \frac{\gamma'(t)}{\gamma(t) - \lambda} dt \right\}, \quad a \leq s \leq b,$$

then straightforward calculation shows that

$$\frac{\varphi'(s)}{\varphi(s)} = \frac{\gamma'(s)}{(\gamma(s) - \lambda)},$$

and hence that the function $\

Thus the winding number of $\gamma$ about every point inside $C_r(\alpha)$ is one, while the winding number of $\gamma$ about every point outside $C_r(\alpha)$ is zero. For this reason the standard parametrization of a circle is said to be positive. Note that in this positive parametrization the inward tending normal vector to $C_r(\alpha)$ (i.e., the vector $-(\gamma(t) - \alpha)$) is $\pi/2$ ahead of the tangent vector $(= \gamma'(t))$ (cf. Problem X).

**Example G.** Let $Q$ be a square region in $\mathbb{C}$ with sides parallel to the real and imaginary axes. In other words, $Q$ is the intersection of a closed strip of some width $w$ in $\mathbb{C}$ parallel to the real axis, and a closed strip of the same width parallel to the imaginary axis. Let $\lambda_0$ denote the center of $Q$, and let $C$ denote the circle with center $\lambda_0$ and radius $w/\sqrt{2}$, so that, if $\gamma$ is the standard parametrization of $C$, then $\kappa_1 = \gamma(\pi/4)$, $\kappa_2 = \gamma(3\pi/4)$, $\kappa_3 = \gamma(5\pi/4)$, and $\kappa_4 = \gamma(7\pi/4)$, are the four vertices of $\partial Q$. Then a polygonal arc $\pi = \pi(\kappa_1, \kappa_2, \kappa_3, \kappa_4, \kappa_1)$ is a standard parametrization of the square $\partial Q$. Since $\lambda_0$ is in the unbounded component of the complement of the range of each of the four closed arcs formed by adding an edge of $\partial Q$ to the shorter subarc of $\tilde{\gamma}$ joining the end points of that edge, it is clear that the winding number about $\lambda_0$ of a standard parametrization $\pi$ of $\partial Q$ is one. Thus $\pi$ has winding number one at each point of $Q^\circ = \text{Int}(\partial Q)$ and winding number zero

PROOF. For each point $\lambda$ in $D$ we define $F(\lambda) = \int_{\sigma} f(\zeta) d\zeta$, where $\sigma$ denotes the directed line segment $\sigma(\alpha, \lambda)$. Then according to Theorem 5.4 we have $F(\lambda) - F(\lambda_0) = \int_{\tau} f(\zeta) d\zeta$ for any two points $\lambda$ and $\lambda_0$ of $D$, where $\tau$ denotes the segment $\sigma(\lambda_0, \lambda)$. Hold $\lambda_0$ fixed, let $\varepsilon$ be an arbitrary positive number, and let $\delta$ be chosen so that $|f(\lambda) - f(\lambda_0)| < \varepsilon$ whenever $|\lambda - \lambda_0| < \delta$. For each such $\lambda$ we have

$$F(\lambda) - F(\lambda_0) - f(\lambda_0)(\lambda - \lambda_0) = \int_{\tau}[f(\zeta) - f(\lambda_0)] d\zeta,$$

and therefore

$$|F(\lambda) - F(\lambda_0) - f(\lambda_0)(\lambda - \lambda_0)| < \varepsilon |\lambda - \lambda_0|$$

by virtue of Proposition 5.5 and the estimate (7). Thus

$$\left| \frac{F(\lambda) - F(\lambda_0)}{\lambda - \lambda_0} - f(\lambda_0) \right| < \varepsilon$$

whenever $0 < |\lambda - \lambda_0| < \delta$, which shows that $F'(\lambda_0) = f(\lambda_0)$, and hence that $F$ is a primitive of $f$ on $D$. $\square$
