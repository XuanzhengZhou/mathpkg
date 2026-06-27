---
role: proof
locale: en
of_concept: generalized-cauchy-integral-formula
source_book: gtm038
source_chapter: "VII"
source_section: "3"
---

Let $w \in P$, $H_r$ a small circular disk about $w$ with $H_r \subset P$, and $T_r := \partial H_r$. If $T$ and $T_r$ are given the usual orientation, then it follows from Stokes' theorem that:

$$\operatorname{Ch}_f^{(P)}(w) = -\frac{1}{2\pi i} \int_{P - H_r} d\left(\frac{g(z)}{z-w} dz\right) + \frac{1}{2\pi i} \int_{H_r} \frac{f(z)}{z-w} dz \wedge d\bar{z}$$

$$= -\frac{1}{2\pi i} \int_{\partial(P - H_r)} \frac{g(z)}{z-w} dz + \operatorname{Ch}_f^{(H_r)}(w)$$

$$= -\frac{1}{2\pi i} \int_T \frac{g(z)}{z-w} dz + \frac{1}{2\pi i} \int_{T_r} \frac{g(z)}{z-w} dz + \operatorname{Ch}_f^{(H_r)}(w)$$

$$= -\operatorname{ch}(g|T)(w) + \operatorname{ch}(g|T_r)(w) + \operatorname{Ch}_f^{(H_r)}(w).$$

Hence the function $\rho(r) := \operatorname{ch}(g|T_r)(w) + \operatorname{Ch}_f^{(H_r)}(w)$ has the constant value $\operatorname{ch}(g|T)(w) + \operatorname{Ch}_f^{(P)}(w)$, and it suffices to consider the limit as $r \to 0$. Write

$$\rho(r) = a(r) + b(r) + c(r)$$

with
$$a(r) := \frac{1}{2\pi i} \int_{T_r} \frac{g(w)}{z-w} dz = g(w),$$
$$b(r) := \frac{1}{2\pi i} \int_{T_r} \frac{g(z) - g(w)}{z-w} dz,$$
$$c(r) := \operatorname{Ch}_f^{(H_r)}(w).$$

Since $g$ is continuously differentiable, $g(z) - g(w) = O(|z-w|)$, so the integrand in $b(r)$ is bounded. As $r \to 0$, the length of $T_r$ tends to $0$, hence $b(r) \to 0$. Also $c(r) \to 0$ as $r \to 0$ because $f$ is bounded and the area of $H_r$ is $\pi r^2$, which tends to $0$. Therefore $\rho(r) \to g(w)$, and the formula $g(w) = \operatorname{ch}(g|T)(w) + \operatorname{Ch}_f^{(P)}(w)$ follows.
