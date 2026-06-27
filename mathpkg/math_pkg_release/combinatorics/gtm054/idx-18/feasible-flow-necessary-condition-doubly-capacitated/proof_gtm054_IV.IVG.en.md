---
role: proof
locale: en
of_concept: feasible-flow-necessary-condition-doubly-capacitated
source_book: gtm054
source_chapter: "IV"
source_section: "IVG"
---

Let $h$ be a feasible flow in the doubly-capacitated network $(V, k_1, k_2)$. Let $e_0 \in W$ and let $C = \sum_{x \in U} f^*(x)$ be a cut through $e_0$, where $\varnothing \subset U \subset V$. By G2, we have the inequalities

$$k_2(C; e_0) \geq h(e_0) \geq k_1(e_0).$$

Subtracting $k_1(e_0)$ from the first inequality yields

$$0 \leq k_2(C; e_0) - k_1(e_0) = \sum_{g_U(e)=1} k_2(e) - \sum_{g_U(e)=-1} k_1(e) = k(U).$$

Thus the condition $k(U) \geq 0$ for all $\varnothing \subset U \subset V$ is necessary for the existence of a feasible flow. The sufficiency of this condition is established in Exercise G6 by constructing an auxiliary network and applying the max-flow min-cut theorem.
