---
role: proof
locale: en
of_concept: differentiability-of-integral-functional
source_book: gtm060
source_chapter: "3"
source_section: "12"
---
Expanding $\Phi(\gamma+h) - \Phi(\gamma)$ to first order in $h$ and $\dot{h}$:

$$\Phi(\gamma+h) - \Phi(\gamma) = \int_{t_0}^{t_1} \bigl[ L(x+h, \dot{x}+\dot{h}, t) - L(x, \dot{x}, t) \bigr] dt.$$

By Taylor expansion,

$$L(x+h, \dot{x}+\dot{h}, t) - L(x, \dot{x}, t) = \frac{\partial L}{\partial x}h + \frac{\partial L}{\partial \dot{x}}\dot{h} + O(h^2, \dot{h}^2).$$

Thus

$$\Phi(\gamma+h) - \Phi(\gamma) = \int_{t_0}^{t_1} \left( \frac{\partial L}{\partial x} h + \frac{\partial L}{\partial \dot{x}} \dot{h} \right) dt + R,$$

where $F(h) = \int_{t_0}^{t_1} (\frac{\partial L}{\partial x} h + \frac{\partial L}{\partial \dot{x}} \dot{h}) dt$ is linear in $h$ and $R = O(h^2)$. Integrating the second term by parts,

$$\int_{t_0}^{t_1} \frac{\partial L}{\partial \dot{x}} \dot{h}\, dt = \left[ \frac{\partial L}{\partial \dot{x}} h \right]_{t_0}^{t_1} - \int_{t_0}^{t_1} h \frac{d}{dt}\left( \frac{\partial L}{\partial \dot{x}} \right) dt.$$

Substituting back gives the stated formula for $F(h)$. Hence $\Phi$ is differentiable.
