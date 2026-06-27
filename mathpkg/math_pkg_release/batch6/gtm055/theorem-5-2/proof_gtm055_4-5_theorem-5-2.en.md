---
role: proof
locale: en
of_concept: theorem-5-2
source_book: gtm055
source_chapter: "4-5"
source_section: "Section 06_Section_6"
---

Proof. It clearly suffices to show that $f = 0$ identically on $\Delta$ when $f = 0$ on $M$. Let $U$ denote the subset of $\Delta$ consisting of all those points $\lambda$ in $\Delta$ such that $f$ vanishes identically on some open disc of positive radius about $\lambda$. Then $U$ is an open subset of $\Delta$ which, according to Example A, contains all of the accumulation points of $M$ that lie in $\Delta$, as well as all of the accumulation points of $U$ itself that belong to $\Delta$. Hence $U$ is a nonempty open subset of $\Delta$ such that $\partial U \cap \Delta = \varnothing$, whence it follows at once that $U = \Delta$ (Prop. 3.6).

The proof of Taylor’s theorem requires a penetrating analysis of the behavior of analytic functions on discs. In this connection, and in many others, an important role is played by certain line integrals. Accordingly, we shall give a brief account of the pertinent concepts. To begin with, we recall that an arc in $\mathbb{C}$ is a continuous complex-valued function defined on some real interval $[a, b]$, called the parameter interval of the arc. In the following discussion we shall consistently identify an arc $\alpha$ defined on an interval $[a, b]$ with the equivalent arc $\alpha(t - c)$ defined on the translated interval $[a, b] + c, -\infty < c < +\infty$. (The reader may check at each appropriate point as we go along that the concept or construction under discussion is unaffected by thus translating the parameter interval.) If $\alpha$ is an arc defined on the interval $[a, b]$, then the point $\lambda_0 = \alpha(a)$ is the initial point of $\alpha$, the point $\lambda_1 = \alpha(b)$ the terminal point of $\alpha$, and $\alpha$ is said to

the subarcs $\alpha \mid [t_{i-1}, t_i], i = 1, \ldots, n$, is smooth. If $\alpha$ is a piecewise smooth arc and if the left and right derivatives of $\alpha$ not only exist at every point where they are defined, but are also different from zero at every point, then $\alpha$ is said to be regular.

Recall (Prob. 1I) that an arc $\alpha$ defined on the interval $[a, b]$ is rectifiable if it is of bounded variation on $[a, b]$, and that, when $\alpha$ is rectifiable, the total variation of $\alpha$ over $[a, b]$ is also called the length of $\alpha$, which we shall here denote by $L(\alpha)$. It is clear that if an arc $\alpha$ is subdivided in any manner into a sum of subarcs, $\alpha = \alpha_1 + \cdots + \alpha_n$, then $\alpha$ is rectifiable if and only if all of the subarcs $\alpha_i$ are, and if this is the case, then $L(\alpha) = L(\alpha_1) + \cdots + L(\alpha_n)$. We take it as known from advanced calculus that a piecewise smooth arc $\alpha$ defined on the parameter interval $[a, b]$ is rectifiable and that $L(\alpha) = \int_a^b |\alpha'(t)| dt$.

Suppose now that $\alpha$ is a rectifiable arc defined on a parameter interval $[a, b]$, and let $f$ be a bounded complex-valued function defined on the range of $\alpha$. If $\mathcal{P} = \{t_0 < \cdots < t_n\}$ is any partition of $[a, b]$, if $\alpha = \alpha_1 + \cdots + \alpha_n$ is the corresponding subdivision of $\alpha$, and if, for each $i = 1, \ldots, n$, $\zeta_i$ denotes a point in the range of $\alpha_i$, then the sum

$$S = \sum_{i=1}^{n} f(\zeta_i) [\alpha(t_i) - \alpha(t_{i-1})]$$

is called a Riemann sum for

Moreover, it is readily established that if $\alpha$ is a rectifiable arc in $\mathbb{C}$ with range $W$, then the mapping

$$f \rightarrow \int_{\alpha} f(\zeta) d\zeta$$

is a linear functional on $\mathcal{C}(W)$ satisfying the condition

$$\left| \int_{\alpha} f(\zeta) d\zeta \right| \leq L(\alpha) \max_{\zeta \in W} |f(\zeta)|, \quad f \in \mathcal{C}(W).$$

**Example C.** If $\lambda_0$ and $\lambda_1$ are complex numbers and $[a, b]$ is a nondegenerate interval, then the linear parametrization on $[a, b]$ of the directed line segment $\sigma = \sigma(\lambda_0, \lambda_1)$ joining $\lambda_0$ to $\lambda_1$ is given by

$$\alpha(t) = \frac{1}{b-a} \left[ (t-a) \lambda_1 + (b-t) \lambda_0 \right], \quad a \leq t \leq b.$$

The length of this arc is clearly what it should be, viz., $|\lambda_1 - \lambda_0|$. Moreover, if $f$ is a continuous complex-valued function on $\sigma$, that is, on the range of $\alpha$, then the line integral of $f$ along $\alpha$ is easily seen to be independent of the choice of $a$ and $b$ (cf. Problem E or Problem F). We shall denote this integral by

$$\int_{\sigma(\lambda_0, \lambda_1)} f(\zeta) d\zeta,$$

or, when possible, simply by

$$\int_{\sigma} f(\zeta) d\zeta.$$

If $\{\lambda_0, \lambda_1, \ldots, \lambda_n\}$ is any finite sequence of complex numbers, then an arc $\pi = \pi(\lambda_0, \ldots, \lambda_n)$ obtained by forming the sum of linear parametrizations of the segments $\sigma(\lambda_{i-1}, \lambda_i)$, $i = 1, \ldots, n$, is a polygonal arc joining the given points

Example D. For each complex number $\lambda_0$ and positive number $r$ the arc

$$\gamma(t) = \lambda_0 + re^{it}, \quad 0 \leq t \leq 2\pi,$$

is the standard parametrization of the circle $C = C_r(\lambda_0)$ of radius $r$ and center $\lambda_0$. This arc is rectifiable, of course, with length $2\pi r$. In the sequel, given a continuous complex-valued function $f$ on $C_r(\lambda_0)$, we shall write

$$\int_{C_r(\lambda_0)} f(\zeta) d\zeta,$$

or, when possible, simply

$$\int_C f(\zeta) d\zeta$$

for the integral of $f$ along the arc $\gamma$ in (8).

While Proposition 5.3 assures us of the existence of the line integral $\int_\alpha f d\zeta$ whenever $\alpha$ is a rectifiable arc and $f$ is continuous on the range of $\alpha$, it gives no hint as to how such an integral is to be evaluated. It is appropriate to recall therefore that when $\alpha$ is piecewise smooth and defined, say, on the parameter interval $[a, b]$, the integral of $f$ along $\alpha$ can be evaluated, at least in principle, by the familiar formula

$$\int_\alpha f(\zeta) d\zeta = \int_a^b f(\alpha(t)) \alpha'(t) dt$$

(see Problem F). Thus, for example, if $f$ is continuous on the circle $C = C_r(\lambda_0)$, then

$$\int_C f(\zeta) d\zeta = r i \int_0^{2\pi} f(\lambda_0 + re^{it}) e^{it} dt.$$

If $\alpha, \beta,$ and $\gamma$ are any three complex numbers, then a polygonal arc joining the points $\{\alpha, \beta, \gamma\}$ will be denoted by $[\alpha, \beta, \gamma]$. (The symbol $[\alpha, \beta, \gamma]$ thus denotes an object that is unique only up to piecewise linear reparametrization; since we are interested princip

The following result is the cornerstone upon which the entire edifice of complex analysis is based.
