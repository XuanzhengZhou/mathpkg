---
role: proof
locale: en
of_concept: legendre-submanifold-via-generating-function
source_book: gtm060
source_chapter: "Appendix 4"
source_section: "Contact Structures"
---
One verifies by direct computation that the submanifold defined by the formulas

$$y_I = -\frac{\partial S}{\partial x_I}, \quad x_J = \frac{\partial S}{\partial y_J}, \quad z = S - x_I\frac{\partial S}{\partial x_I}$$

is integral for the contact form $$\omega = x\,dy + dz$$. Indeed,

$$x\,dy + dz = x_I dy_I + x_J dy_J + dS - dx_I\frac{\partial S}{\partial x_I} - x_I d\left(\frac{\partial S}{\partial x_I}\right)$$

$$= x_I\left(-\frac{\partial^2 S}{\partial x_I^2}dx_I - \frac{\partial^2 S}{\partial x_I\partial y_J}dy_J\right) + \frac{\partial S}{\partial y_J}dy_J + \frac{\partial S}{\partial x_I}dx_I + \frac{\partial S}{\partial y_J}dy_J - \frac{\partial S}{\partial x_I}dx_I - x_I\left(\frac{\partial^2 S}{\partial x_I^2}dx_I + \frac{\partial^2 S}{\partial x_I\partial y_J}dy_J\right) = 0.$$

The dimension of this integral submanifold is $$n$$, which is maximal for a $$(2n+1)$$-dimensional contact manifold. Thus it is a Legendre submanifold. Different partitions $$I + J$$ of the index set give different coordinate representations (different Legendre charts) of the same Legendre submanifold.
