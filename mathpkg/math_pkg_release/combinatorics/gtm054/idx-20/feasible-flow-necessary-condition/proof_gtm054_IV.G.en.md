---
role: proof
locale: en
of_concept: feasible-flow-necessary-condition
source_book: gtm054
source_chapter: "IV"
source_section: "G"
---

Let $h$ be a feasible flow in $(V, k_1, k_2)$. Let $e_0 \in W$ and let $C = \sum_{x \in U} f^*(x)$ be a cut through $e_0$ with $\varnothing \subset U \subset V$. By Proposition G2, we have
$$k_2(C; e_0) \geq h(e_0) \geq k_1(e_0).$$

Therefore,
$$k_2(C; e_0) - k_1(e_0) \geq 0.$$

Now expanding $k_2(C; e_0)$:
$$k_2(C; e_0) = \sum_{g_U(e)=1} k_2(e) \; - \!\! \sum_{\substack{e \neq e_0 \\ g_U(e)=-1}} k_2(e).$$

Since $g_U(e_0) = 1$ by definition of a cut through $e_0$, we have $k_1(e_0)$ appearing in the first sum for the $k_1$-part. Reorganizing,
$$0 \leq k_2(C; e_0) - k_1(e_0) = \sum_{g_U(e)=1} k_2(e) \; - \!\! \sum_{\substack{e \neq e_0 \\ g_U(e)=-1}} k_2(e) \; - \; k_1(e_0).$$

Equivalently, defining
$$k(U) = \sum_{g_U(e)=1} k_2(e) \; - \!\! \sum_{g_U(e)=-1} k_1(e),$$
the inequality $k_2(C; e_0) \geq k_1(e_0)$ yields $k(U) \geq 0$. Since this must hold for every nonempty proper subset $U$, the condition $k(U) \geq 0$ for all $\varnothing \subset U \subset V$ is necessary for the existence of a feasible flow.
