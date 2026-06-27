---
role: proof
locale: en
of_concept: tangent-space-as-complex-vector-space
source_book: gtm038
source_chapter: "VII"
source_section: "1"
---

If $f$ is holomorphic at $x_0$, then

$$\left( i \cdot \frac{\partial}{\partial x_v} \right)(f) = i \left( \frac{\partial}{\partial x_v}(f) \right) = i \cdot f_{z_v} = \frac{\partial}{\partial y_v}(f).$$

Thus the definition of complex scalar multiplication is consistent with the action on holomorphic functions. The axioms of a $\mathbb{C}$-vector space are clearly satisfied; in particular

$$i \cdot \frac{\partial}{\partial y_v} = i \cdot \left( i \cdot \frac{\partial}{\partial x_v} \right) = (i \cdot i) \cdot \frac{\partial}{\partial x_v} = -\frac{\partial}{\partial x_v}.$$

Therefore $\left\{ \frac{\partial}{\partial x_1}, \ldots, \frac{\partial}{\partial x_n} \right\}$ forms a system of generators of $T_{x_0}$ over $\mathbb{C}$.

If $\sum_{v=1}^{n} c_v \cdot \frac{\partial}{\partial x_v} = 0$ with $c_v = a_v + i b_v$ for $v = 1, \ldots, n$, then evaluating on the real-valued function $x_{\mu}$ yields $a_{\mu} = 0$, and evaluating on $y_{\mu}$ yields $b_{\mu} = 0$. Hence the set is $\mathbb{C}$-linearly independent. Thus $\{\partial/\partial x_1, \ldots, \partial/\partial x_n\}$ is a $\mathbb{C}$-basis. The compatibility with the real structure means that for any complex scalar $c$, the action of $c \cdot D$ as a real linear map equals $(\operatorname{Re} c) D + (\operatorname{Im} c)(i \cdot D)$.
