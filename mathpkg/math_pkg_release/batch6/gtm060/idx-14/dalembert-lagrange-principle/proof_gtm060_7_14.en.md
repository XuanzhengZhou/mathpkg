---
role: proof
locale: en
of_concept: dalembert-lagrange-principle
source_book: gtm060
source_chapter: "7"
source_section: "14"
---

For the simplest case of a single mass point $\mathbf{x}$ constrained to a smooth surface $M$, consider the holonomic system as the limit of a system with potential $U + N U_1$ as $N \to \infty$, where $U_1$ is a potential that grows rapidly away from $M$. The force $\mathbf{F} = -N \partial U_1 / \partial \mathbf{x}$ oscillates as the particle moves near $M$, and in the limit $N \to \infty$, its average value is the constraint force $\mathbf{R}$, which is perpendicular to $M$.

Hence, for every tangent vector $\xi \in TM_{\mathbf{x}}$,

$$(\mathbf{R}, \xi) = 0.$$

Substituting $\mathbf{R} = m\ddot{\mathbf{x}} + \partial U / \partial \mathbf{x}$ yields

$$\left( m \ddot{\mathbf{x}} + \frac{\partial U}{\partial \mathbf{x}}, \xi \right) = 0$$

for all $\xi \in TM_{\mathbf{x}}$.

For a system of $n$ points $\mathbf{x}_i$ with masses $m_i$, the same reasoning applied to each point gives

$$\sum_i (\mathbf{R}_i, \xi_i) = 0,$$

which is equivalent to

$$\sum_i \left( m_i \ddot{\mathbf{x}}_i + \frac{\partial U}{\partial \mathbf{x}_i}, \xi_i \right) = 0.$$

In the coordinates $\bar{\mathbf{x}}_i = \sqrt{m_i} \mathbf{x}_i$, the kinetic energy takes the Euclidean form $T = \frac{1}{2} \sum m_i \dot{\mathbf{x}}_i^2 = \frac{1}{2} \dot{\bar{\mathbf{x}}}^2$, and the D'Alembert-Lagrange principle becomes

$$\left( \ddot{\bar{\mathbf{x}}} + \frac{\partial U}{\partial \bar{\mathbf{x}}}, \xi \right) = 0,$$

i.e., the $3n$-dimensional reaction force is orthogonal to the manifold $M$ in the metric defined by the kinetic energy $T$. Returning to the original coordinates $\mathbf{x}_i$ recovers the familiar form of the principle.
