---
role: proof
locale: en
of_concept: normal-field-lemma
source_book: gtm060
source_chapter: "7"
source_section: "14"
---

Suppose, for contradiction, that there exists a point $t_* \in (t_0, t_1)$ and a vector $\mathbf{h} \in TM_{\mathbf{x}(t_*)}$ such that $(\mathbf{f}(t_*), \mathbf{h}) \neq 0$. Without loss of generality, assume $(\mathbf{f}(t_*), \mathbf{h}) > 0$.

By continuity of $\mathbf{f}$, there exists an interval $[t_*, t_* + \varepsilon]$ on which $(\mathbf{f}(t), \mathbf{h}) > 0$. Choose a smooth scalar function $\varphi(t)$ supported on $[t_*, t_* + \varepsilon]$ with $\varphi(t) > 0$ on the interior and $\varphi(t_0) = \varphi(t_1) = 0$.

Extend $\mathbf{h}$ to a continuous tangent vector field $\mathbf{h}(t)$ along $\mathbf{x}(t)$ in a neighborhood of $t_*$ (this is possible since $M$ is a smooth submanifold). Define the tangent vector field $\xi(t) = \varphi(t) \mathbf{h}(t)$. Then $\xi(t_0) = \xi(t_1) = 0$ by construction.

Now compute the integral:

$$\int_{t_0}^{t_1} \mathbf{f}(t) \cdot \xi(t) \, dt = \int_{t_*}^{t_* + \varepsilon} \varphi(t) (\mathbf{f}(t), \mathbf{h}(t)) \, dt > 0,$$

since the integrand is strictly positive on a set of positive measure. This contradicts the hypothesis that the integral vanishes for all such $\xi$. Therefore, $(\mathbf{f}(t), \mathbf{h}) = 0$ for all $\mathbf{h} \in TM_{\mathbf{x}(t)}$ at every $t$, i.e., $\mathbf{f}$ is everywhere normal to $M$ along the curve $\mathbf{x}(t)$.
