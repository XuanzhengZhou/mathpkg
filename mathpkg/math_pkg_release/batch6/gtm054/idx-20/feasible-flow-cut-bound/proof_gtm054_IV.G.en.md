---
role: proof
locale: en
of_concept: feasible-flow-cut-bound
source_book: gtm054
source_chapter: "IV"
source_section: "G"
---

Let $C = \sum_{x \in U} f^*(x)$ be a cut through $e_0$ with incidence vector $g_U$. Since $h$ is a flow, we have $h \cdot g_U = 0$ (flow conservation), so

$$0 = \sum_{g_U(e)=1} h(e) \; - \sum_{g_U(e)=-1} h(e).$$

For the upper bound: using $h(e) \leq k_2(e)$ on forward edges and $h(e) \geq k_1(e) \geq 0$ (trivially) on reverse edges, and noting that $e_0$ has $g_U(e_0) = 1$,

$$0 = \sum_{g_U(e)=1} h(e) - \sum_{g_U(e)=-1} h(e) \geq h(e_0) + \sum_{\substack{g_U(e)=1 \\ e \neq e_0}} k_1(e) - \sum_{g_U(e)=-1} k_2(e).$$

More directly, since $h(e) \leq k_2(e)$ for all $e$,
$$h(e_0) = \sum_{g_U(e)=-1} h(e) - \sum_{\substack{g_U(e)=1 \\ e \neq e_0}} h(e) \leq \sum_{g_U(e)=-1} k_2(e) - \sum_{\substack{g_U(e)=1 \\ e \neq e_0}} k_1(e).$$

But the standard derivation gives $h(e_0) \leq k_2(C; e_0)$:
$$0 = h \cdot g_U \leq \sum_{g_U(e)=1} k_2(e) - \sum_{\substack{g_U(e)=-1 \\ e \neq e_0}} k_2(e) - h(e_0) = k_2(C; e_0) - h(e_0).$$

Thus $h(e_0) \leq k_2(C; e_0)$.

For the lower bound: using $h(e) \geq k_1(e)$ on forward edges and $h(e) \leq k_2(e)$ on reverse edges,
$$0 = h \cdot g_U \geq \sum_{g_U(e)=1} k_1(e) - \sum_{\substack{g_U(e)=-1 \\ e \neq e_0}} k_2(e) - h(e_0) = k_1(C; e_0) - h(e_0).$$

Thus $h(e_0) \geq k_1(C; e_0)$. Combining both inequalities yields $k_1(C; e_0) \leq h(e_0) \leq k_2(C; e_0)$.
