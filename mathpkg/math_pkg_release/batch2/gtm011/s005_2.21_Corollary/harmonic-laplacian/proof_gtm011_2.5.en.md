---
role: proof
locale: en
of_concept: harmonic-laplacian
source_book: gtm011
source_chapter: "2"
source_section: "5"
---

Suppose that $u$ and $v$ have continuous second partial derivatives. Differentiating the Cauchy-Riemann equations again:

From $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$, differentiate with respect to $x$:

$$\frac{\partial^2 u}{\partial x^2} = \frac{\partial^2 v}{\partial x \partial y}.$$

From $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$, differentiate with respect to $y$:

$$\frac{\partial^2 u}{\partial y^2} = -\frac{\partial^2 v}{\partial y \partial x}.$$

Since the mixed partial derivatives are equal ($v_{xy} = v_{yx}$) by continuity of the second partials, adding the two equations yields

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0.$$

A similar computation for $v$ gives $\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$. Thus both $u$ and $v$ are harmonic.
