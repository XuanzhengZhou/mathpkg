---
role: proof
locale: en
of_concept: euler-lagrange-equation
source_book: gtm060
source_chapter: "3"
source_section: "12"
---

The variation of $\Phi(\gamma) = \int L(x, \dot{x}, t) dt$ is
$$F(h) = \int_{t_0}^{t_1} \left(\frac{\partial L}{\partial x}h + \frac{\partial L}{\partial \dot{x}}\dot{h}\right) dt.$$

Integration by parts:
$$\int_{t_0}^{t_1} \frac{\partial L}{\partial \dot{x}}\dot{h} dt = -\int_{t_0}^{t_1} h\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} dt + \left[h\frac{\partial L}{\partial \dot{x}}\right]_{t_0}^{t_1}.$$

For fixed endpoints $h(t_0) = h(t_1) = 0$, the boundary term vanishes. Thus
$$F(h) = \int_{t_0}^{t_1} \left[\frac{\partial L}{\partial x} - \frac{d}{dt}\frac{\partial L}{\partial \dot{x}}\right] h(t) dt.$$

If $\gamma$ is an extremal, $F(h) = 0$ for all $h$ with $h(t_0) = h(t_1) = 0$. By the fundamental lemma of the calculus of variations, this implies the integrand is identically zero:
$$\frac{d}{dt}\frac{\partial L}{\partial \dot{x}} - \frac{\partial L}{\partial x} = 0.$$

Conversely, if this equation holds, $F(h) = 0$ for all such $h$.
