---
role: exercise
locale: en
chapter: "7"
section: "Differential forms"
exercise_number: 10
---

The Laplace operator on a Riemannian manifold $M$ is the operator $\Delta = \operatorname{div} \operatorname{grad}$. Find its expression in general orthogonal coordinates $x_i$ on $M$, where the Riemannian metric is $ds^2 = E_1 dx_1^2 + E_2 dx_2^2 + E_3 dx_3^2$.

*Answer:*

$$\Delta f = \frac{1}{\sqrt{E_1 E_2 E_3}} \left[ \frac{\partial}{\partial x_1} \left( \sqrt{\frac{E_2 E_3}{E_1}} \frac{\partial f}{\partial x_1} \right) + \frac{\partial}{\partial x_2} \left( \sqrt{\frac{E_1 E_3}{E_2}} \frac{\partial f}{\partial x_2} \right) + \frac{\partial}{\partial x_3} \left( \sqrt{\frac{E_1 E_2}{E_3}} \frac{\partial f}{\partial x_3} \right) \right].$$

In particular, on $\mathbb{R}^3$ in Cartesian, cylindrical, and spherical coordinates:

$$\Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2} = \frac{\partial^2 f}{\partial r^2} + \frac{1}{r} \frac{\partial f}{\partial r} + \frac{1}{r^2} \frac{\partial^2 f}{\partial \varphi^2} + \frac{\partial^2 f}{\partial z^2}$$

$$= \frac{1}{R^2 \cos \theta} \left[ \frac{\partial}{\partial R} \left( R^2 \cos \theta \frac{\partial f}{\partial R} \right) + \frac{\partial}{\partial \varphi} \left( \frac{1}{\cos \theta} \frac{\partial f}{\partial \varphi} \right) + \frac{\partial}{\partial \theta} \left( \cos \theta \frac{\partial f}{\partial \theta} \right) \right].$$
