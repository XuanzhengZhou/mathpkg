---
role: proof
locale: en
of_concept: exterior-derivative-theorem
source_book: gtm060
source_chapter: "7"
source_section: "35"
---

We carry out the proof for the case of a form $\omega^1 = a(x_1, x_2)\,dx_1$ on the $x_1, x_2$ plane. The proof in the general case is entirely analogous, but the calculations are somewhat longer.

We calculate $F(\xi, \eta)$, i.e., the integral of $\omega^1$ on the boundary of the parallelogram $\Pi$ with sides $\xi$ and $\eta$ and vertex at $0$. The chain $\partial \Pi$ is given by the mappings of the interval $0 \leq t \leq 1$ to the plane $t \mapsto \xi t$, $t \mapsto \xi + \eta t$, $t \mapsto \eta t$, and $t \mapsto \eta + \xi t$ with multiplicities $1$, $1$, $-1$, and $-1$. Therefore,

$$
\int_{\partial \Pi} \omega^1 = \int_0^1 \bigl[ a(\xi t) - a(\xi t + \eta) \bigr] \xi_1 - \bigl[ a(\eta t) - a(\eta t + \xi) \bigr] \eta_1 \, dt
$$

where $\xi_1 = dx_1(\xi)$, $\eta_1 = dx_1(\eta)$, $\xi_2 = dx_2(\xi)$, and $\eta_2 = dx_2(\eta)$ are the components of the vectors $\xi$ and $\eta$.

By Taylor expansion (with derivatives taken at $x_1 = x_2 = 0$):

$$
a(\xi t + \eta) - a(\xi t) = \frac{\partial a}{\partial x_1} \eta_1 + \frac{\partial a}{\partial x_2} \eta_2 + O(\xi^2, \eta^2)
$$

and similarly

$$
a(\eta t + \xi) - a(\eta t) = \frac{\partial a}{\partial x_1} \xi_1 + \frac{\partial a}{\partial x_2} \xi_2 + O(\xi^2, \eta^2).
$$

Substituting these expressions into the integral, the $O(\xi^2, \eta^2)$ terms contribute $o(\xi^2, \eta^2)$ after integration. The main terms give

$$
F(\xi, \eta) = \int_{\partial \Pi} \omega^1 = \frac{\partial a}{\partial x_2} (\xi_2 \eta_1 - \xi_1 \eta_2) + o(\xi^2, \eta^2).
$$

The principal bilinear part of $F$ is therefore the value of the exterior $2$-form

$$
\Omega = \frac{\partial a}{\partial x_2}\, dx_2 \wedge dx_1
$$

on the pair of vectors $\xi, \eta$. Since $da = \frac{\partial a}{\partial x_1} dx_1 + \frac{\partial a}{\partial x_2} dx_2$, we have

$$
da \wedge dx_1 = \left( \frac{\partial a}{\partial x_1} dx_1 + \frac{\partial a}{\partial x_2} dx_2 \right) \wedge dx_1 = \frac{\partial a}{\partial x_2}\, dx_2 \wedge dx_1 = \Omega,
$$

which verifies formula $d\omega^1 = da \wedge dx_1$, confirming the general coordinate expression $d\omega^k = \sum da_{i_1,\ldots,i_k} \wedge dx_{i_1} \wedge \cdots \wedge dx_{i_k}$ for the case $k = 1$.
