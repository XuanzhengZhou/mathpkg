---
role: proof
locale: en
of_concept: kinetic-energy-quadratic-form-in-angular-velocity
source_book: gtm060
source_chapter: "6"
source_section: "C"
---

From the lemma, $A$ is symmetric. Substituting $\Omega$ for both $\mathbf{X}$ and $\mathbf{Y}$:

$$T = \frac{1}{2}m v^2 = \frac{1}{2}m [\Omega, \mathbf{Q}]^2 = \frac{1}{2}m([\mathbf{Q}, [\Omega, \mathbf{Q}]], \Omega) = \frac{1}{2}(A\Omega, \Omega) = \frac{1}{2}(\mathbf{M}, \Omega).$$

For an extended body, the kinetic energy and angular momentum are additive over mass points:

$$T = \sum_i T_i,\qquad \mathbf{M} = \sum_i \mathbf{M}_i = \sum_i A_i \Omega = A\Omega.$$

Since each $A_i$ is symmetric by the lemma, $A = \sum_i A_i$ is also symmetric. Summing the point energies:

$$T = \sum_i \frac{1}{2}(\mathbf{M}_i, \Omega) = \frac{1}{2}(\sum_i \mathbf{M}_i, \Omega) = \frac{1}{2}(\mathbf{M}, \Omega) = \frac{1}{2}(A\Omega, \Omega).$$
