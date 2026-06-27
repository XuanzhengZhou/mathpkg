---
role: exercise
locale: en
chapter: "8"
section: "8.5.2"
exercise_number: 1
---

**(a)** Suppose $0 < a < c$ and for all $u \in (a, c)$ we have a Lorentzian metric $g_u$ on $\mathbb{R}^4$. Assume that for all $i, j \in (1, \ldots, 4)$ the function $g_{ij} : \mathbb{R}^4 \times (a, c) \to \mathbb{R}$ defined by $g_{ij}(x, u) = g_u(\partial_i x, \partial_j x)$ is $C^\infty$. Regard $(M, g_u)$ as a spacetime for all $u \in (a, c)$. With $b \in (a, c)$, abbreviate $g_b$ by $g$. Note that

$$
h = \sum_{i,j=1}^4 \left.\frac{\partial g_{ij}}{\partial u}\right|_{u=b} du^i \otimes du^j
$$

is a symmetric $(0, 2)$-tensor field on $\mathbb{R}^4$. Show that if each spacetime $(\mathbb{R}^4, g_u)$ is Ricci flat, $h$ obeys the following equation:

$$
g^{ij}(h_{ki|j|\ell} - h_{k\ell|i|j} - h_{ki|\ell|j} + h_{ij|k|\ell}) = 0
$$

where we use covariant derivative notation of Section 3.6.1.

**(b)** Let $(M, g)$ be a Ricci flat spacetime, and let $h$ be a symmetric $(0, 2)$-tensor field on $M$. By definition, $h$ obeys the vacuum Einstein equation linearized about $(M, g)$ iff $h$ obeys the equation at the end of (a) in each local coordinate system. An example can be constructed as follows. Let $(M, g_u)$ be the Kruskal spacetime of active mass $u$. By formally differentiating $g_u$ with respect to $u$, find an $h$ on $M$ which obeys the vacuum Einstein equation linearized about $(M, g)$.

*Hint for (a):* Differentiate the Ricci flatness condition $\operatorname{Ric}(g_u) = 0$ with respect to $u$ at $u = b$ and express the result in terms of $h$ and the covariant derivatives of the background metric $g$.
