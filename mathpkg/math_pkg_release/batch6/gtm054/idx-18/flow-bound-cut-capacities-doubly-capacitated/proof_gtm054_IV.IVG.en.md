---
role: proof
locale: en
of_concept: flow-bound-cut-capacities-doubly-capacitated
source_book: gtm054
source_chapter: "IV"
source_section: "IVG"
---

If $h$ is a feasible flow, then for the characteristic vector $g_U$ of the cut $C$, we have the orthogonality relation $h \cdot g_U = 0$. Expanding this gives

$$0 = h \cdot g_U = \sum_{g_U(e)=1} h(e) - \sum_{g_U(e)=-1} h(e).$$

Using the upper bound $h(e) \leq k_2(e)$ for forward edges and the lower bound $h(e) \geq k_1(e)$ for backward edges, we obtain

$$0 = \sum_{g_U(e)=1} h(e) - \sum_{\substack{e \neq e_0 \\ g_U(e)=-1}} h(e) - h(e_0) \leq \sum_{g_U(e)=1} k_2(e) - \sum_{\substack{e \neq e_0 \\ g_U(e)=-1}} k_1(e) - h(e_0) = k_2(C; e_0) - h(e_0).$$

Thus $h(e_0) \leq k_2(C; e_0)$. Similarly, using the lower bound $h(e) \geq k_1(e)$ for forward edges and the upper bound $h(e) \leq k_2(e)$ for backward edges,

$$0 \geq \sum_{g_U(e)=1} k_1(e) - \sum_{\substack{e \neq e_0 \\ g_U(e)=-1}} k_2(e) - h(e_0) = k_1(C; e_0) - h(e_0),$$

which yields $h(e_0) \geq k_1(C; e_0)$. Combining both inequalities gives the desired result.
