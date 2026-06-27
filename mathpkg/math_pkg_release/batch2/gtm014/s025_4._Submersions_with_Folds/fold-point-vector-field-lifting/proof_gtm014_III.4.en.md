---
role: proof
locale: en
of_concept: fold-point-vector-field-lifting
source_book: gtm014
source_chapter: "III"
source_section: "4. Submersions with Folds"
---

**Proof of Lemma 4.7.** Choose coordinates $x_1, \ldots, x_n$ centered at $p$ and coordinates $y_1, \ldots, y_m$ centered at $f(p)$ satisfying the local normal form of Theorem 4.5. In these coordinates, the map $f$ has the form
$$f(x_1, \ldots, x_n) = \bigl(x_1, \ldots, x_{m-1}, \pm x_m^2 \pm \cdots \pm x_n^2\bigr).$$

The singular set $S_1(f)$ is given locally by the equations $x_m = \cdots = x_n = 0$, so a vector field $\tau$ along $f$ vanishing on $S_1(f) \cap U$ is described by functions
$$\tau = \sum_{j=1}^{m} \tau_j(x_1, \ldots, x_n) \, \frac{\partial}{\partial y_j}$$
where each $\tau_j$ vanishes when $x_m = \cdots = x_n = 0$.

The condition $\tau = (df)(\zeta)$ means we must solve for a vector field
$$\zeta = \sum_{i=1}^{n} \zeta_i(x_1, \ldots, x_n) \, \frac{\partial}{\partial x_i}$$
satisfying
$$\tau_j = \zeta_j \quad (1 \leq j \leq m-1),$$
$$\tau_m = \sum_{i=m}^{n} (\pm 2 x_i) \, \zeta_i.$$

Since the $\tau_j$ vanish along the singular set $x_m = \cdots = x_n = 0$, each $\tau_m(x)$ is divisible by the ideal $(x_m, \ldots, x_n)$. The nondegeneracy of the quadratic form $\pm x_m^2 \pm \cdots \pm x_n^2$ (guaranteed by the fold point condition, which implies the Hessian matrix is nonsingular) allows us to divide by the gradient and solve for $\zeta_i$ ($m \leq i \leq n$) on a possibly smaller neighborhood $V \subset U$. This yields the desired vector field $\zeta$. $\square$
