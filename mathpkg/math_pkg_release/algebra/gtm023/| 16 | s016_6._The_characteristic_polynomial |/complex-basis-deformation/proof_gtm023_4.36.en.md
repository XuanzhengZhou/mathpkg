---
role: proof
locale: en
of_concept: complex-basis-deformation
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§8. Oriented vector spaces"
---

As in the real case, we may assume the vector $n$-tuples $(a_1, \ldots, a_i, b_{i+1}, \ldots, b_n)$ are linearly independent for each $i$. Write $b_n = \sum_{v=1}^{n} \beta^v a_v$ with $\beta^n \neq 0$. Write $\beta^n = r e^{i\vartheta}$ in polar form with $r > 0$. Choose continuous functions $r(t) > 0$ and $\vartheta(t)$ on $[0,1]$ such that $r(0) = 1$, $r(1) = r$, $\vartheta(0) = 0$, $\vartheta(1) = \vartheta$.

Define for $0 \leq t \leq 1$:
$$x_v(t) = a_v \quad (v = 1, \ldots, n-1),$$
$$x_n(t) = t \sum_{v=1}^{n-1} \beta^v a_v + r(t) e^{i\vartheta(t)} a_n.$$

If $\sum_{v=1}^{n} \lambda^v x_v(t) = 0$, then substituting gives equations implying $\lambda^n = 0$ (since $r(t) \neq 0$) and consequently all $\lambda^v = 0$. Thus the vectors remain linearly independent. We have $x_n(0) = a_n$ and $x_n(1) = b_n$, giving a deformation $(a_1, \ldots, a_n) \to (a_1, \ldots, a_{n-1}, b_n)$. Iterating yields a full deformation to $(b_1, \ldots, b_n)$.
