---
role: proof
locale: en
of_concept: exterior-square-dimension-two
source_book: gtm051
source_chapter: "5"
source_section: "5.6"
---

Let $e_1, e_2$ be a basis for $T$, and let $e^1 \wedge e^2 \in \Lambda^2 T^*$ be defined by
$$e^1 \wedge e^2(X, Y) = \xi^1 \eta^2 - \xi^2 \eta^1 = \det(\xi, \eta),$$
where $X = \sum_i \xi^i e_i$ and $Y = \sum_j \eta^j e_j$. For an arbitrary element $\Omega \in \Lambda^2 T^*$, we compute
$$\Omega(X, Y) = \sum_{i,j=1,2} \xi^i \eta^j \Omega(e_i, e_j)$$
$$= \xi^1 \eta^1 \Omega(e_1, e_1) + \xi^1 \eta^2 \Omega(e_1, e_2) + \xi^2 \eta^1 \Omega(e_2, e_1) + \xi^2 \eta^2 \Omega(e_2, e_2).$$
By the alternating property $\Omega(e_i, e_i) = 0$, and $\Omega(e_2, e_1) = -\Omega(e_1, e_2)$. Hence
$$\Omega(X, Y) = \xi^1 \eta^2 \Omega(e_1, e_2) + \xi^2 \eta^1 (-\Omega(e_1, e_2)) = (\xi^1 \eta^2 - \xi^2 \eta^1) \Omega(e_1, e_2) = A (e^1 \wedge e^2)(X, Y),$$
where $A = \Omega(e_1, e_2)$. Therefore $e^1 \wedge e^2$ spans $\Lambda^2 T^*$, and since a non-zero 2-form exists (e.g., $e^1 \wedge e^2$ itself), $\dim \Lambda^2 T^* = 1$.
