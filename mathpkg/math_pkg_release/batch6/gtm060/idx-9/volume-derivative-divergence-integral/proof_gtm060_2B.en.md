---
role: proof
locale: en
of_concept: volume-derivative-divergence-integral
source_book: gtm060
source_chapter: "2"
source_section: "B"
---

For any $t$, the formula for changing variables in a multiple integral gives

$$v(t) = \int_{D(0)} \det \frac{\partial g^t \mathbf{x}}{\partial \mathbf{x}} \, d\mathbf{x}.$$

From the expansion $g^t(\mathbf{x}) = \mathbf{x} + \mathbf{f}(\mathbf{x})t + O(t^2)$ as $t \to 0$, we compute the Jacobian matrix:

$$\frac{\partial g^t \mathbf{x}}{\partial \mathbf{x}} = E + \frac{\partial \mathbf{f}}{\partial \mathbf{x}} t + O(t^2) \quad \text{as } t \to 0.$$

By Lemma 2, $\det(E + At) = 1 + t \, \text{tr } A + O(t^2)$ for any matrix $A$. Applying this with $A = \frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ yields

$$\det \frac{\partial g^t \mathbf{x}}{\partial \mathbf{x}} = 1 + t \, \text{tr } \frac{\partial \mathbf{f}}{\partial \mathbf{x}} + O(t^2).$$

But $\text{tr } \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \sum_{i=1}^{n} \frac{\partial f_i}{\partial x_i} = \text{div } \mathbf{f}$. Therefore,

$$v(t) = \int_{D(0)} [1 + t \, \text{div } \mathbf{f} + O(t^2)] \, d\mathbf{x}.$$

Differentiating with respect to $t$ and evaluating at $t = 0$ gives

$$\left. \frac{dv}{dt} \right|_{t=0} = \int_{D(0)} \text{div } \mathbf{f} \, d\mathbf{x}.$$
