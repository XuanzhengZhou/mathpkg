---
role: proof
locale: en
of_concept: stream-function-of-commutator-is-jacobian
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

Let $v_1 = I \operatorname{grad} \psi_1$ and $v_2 = I \operatorname{grad} \psi_2$ be two divergence-free vector fields on a two-dimensional oriented region. The commutator in the Lie algebra of vector fields is
$$[v_1, v_2] = (v_1 \cdot \nabla) v_2 - (v_2 \cdot \nabla) v_1.$$

In Cartesian coordinates with $I(x, y) = (-y, x)$ (clockwise $90^\circ$ rotation), we have
$$v_1 = \left(-\frac{\partial \psi_1}{\partial y}, \frac{\partial \psi_1}{\partial x}\right), \quad v_2 = \left(-\frac{\partial \psi_2}{\partial y}, \frac{\partial \psi_2}{\partial x}\right).$$

Computing the commutator directly:
$$[v_1, v_2]_x = -\frac{\partial \psi_1}{\partial y} \frac{\partial}{\partial x}\left(-\frac{\partial \psi_2}{\partial y}\right) + \frac{\partial \psi_1}{\partial x} \frac{\partial}{\partial y}\left(-\frac{\partial \psi_2}{\partial y}\right) - (1 \leftrightarrow 2)$$
$$= I \operatorname{grad} \left(\frac{\partial \psi_1}{\partial x} \frac{\partial \psi_2}{\partial y} - \frac{\partial \psi_1}{\partial y} \frac{\partial \psi_2}{\partial x}\right)_x.$$

Recognizing that $\frac{\partial \psi_1}{\partial x} \frac{\partial \psi_2}{\partial y} - \frac{\partial \psi_1}{\partial y} \frac{\partial \psi_2}{\partial x} = J(\psi_1, \psi_2)$, and noting that $[v_1, v_2]$ is also divergence-free, we conclude that its stream function is $\psi_{[v_1, v_2]} = J(\psi_1, \psi_2)$.
