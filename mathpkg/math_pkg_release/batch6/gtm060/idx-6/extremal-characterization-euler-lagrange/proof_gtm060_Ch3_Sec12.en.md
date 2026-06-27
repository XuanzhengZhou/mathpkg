---
role: proof
locale: en
of_concept: extremal-characterization-euler-lagrange
source_book: gtm060
source_chapter: "3"
source_section: "12"
---
From the differentiability theorem, the differential of $\Phi$ is

$$F(h) = \int_{t_0}^{t_1} \left[ \frac{\partial L}{\partial x} - \frac{d}{dt} \frac{\partial L}{\partial \dot{x}} \right] h\, dt + \left( \frac{\partial L}{\partial \dot{x}} h \right) \Bigg|_{t_0}^{t_1}.$$

For curves with fixed endpoints, $h(t_0) = h(t_1) = 0$, so the boundary term vanishes. Then

$$F(h) = \int_{t_0}^{t_1} f(t) h(t)\, dt, \quad \text{where } f(t) = \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{x}} \right) - \frac{\partial L}{\partial x}.$$

If $\gamma$ is an extremal, then $F(h) = 0$ for all such $h$, i.e., $\int_{t_0}^{t_1} f(t) h(t)\, dt = 0$. By the fundamental lemma of the calculus of variations, this implies $f(t) \equiv 0$, which is precisely the Euler–Lagrange equation.

Conversely, if $f(t) \equiv 0$, then clearly $F(h) \equiv 0$ for all $h$ with $h(t_0) = h(t_1) = 0$, so $\gamma$ is an extremal.
