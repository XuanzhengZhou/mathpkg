---
role: proof
locale: en
of_concept: tangent-vector-determined-by-holomorphic-values
source_book: gtm038
source_chapter: "VII"
source_section: "1"
---

If $c_v = a_v + i b_v$ for $v = 1, \ldots, n$, we set

$$D := \sum_{v=1}^{n} a_v \frac{\partial}{\partial x_v} + \sum_{v=1}^{n} b_v \frac{\partial}{\partial y_v}.$$

The axioms for a tangent vector are clearly satisfied. Then for each function $f$ holomorphic at $x_0$, using the Cauchy-Riemann equations $f_{y_v} = i f_{x_v}$, we compute

$$D(f) = \sum_{v=1}^{n} a_v f_{x_v} + \sum_{v=1}^{n} b_v f_{y_v} = \sum_{v=1}^{n} (a_v + i b_v) f_{x_v} = \sum_{v=1}^{n} c_v \frac{\partial}{\partial x_v}(f).$$

For the uniqueness claim: suppose $D$ and $D'$ agree on all holomorphic functions at $x_0$. Then they agree on the real and imaginary parts of holomorphic coordinate functions, hence on all coordinate functions $x_v = \operatorname{Re}(z_v)$ and $y_v = \operatorname{Im}(z_v)$. Since the partial derivatives form a basis of $T_{x_0}$, we must have $D = D'$. The local coordinate representation follows from evaluating $D$ on the holomorphic functions $z_v$ and using the Cauchy-Riemann relations.
