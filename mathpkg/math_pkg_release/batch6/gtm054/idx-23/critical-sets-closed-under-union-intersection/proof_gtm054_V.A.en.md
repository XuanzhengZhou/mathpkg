---
role: proof
locale: en
of_concept: critical-sets-closed-under-union-intersection
source_book: gtm054
source_chapter: "V"
source_section: "A"
---

If $U_1$ and $U_2$ are critical sets, then by definition $\delta(U_1) = \delta(U_2) = \delta_1$. Applying the inequality

$$\delta(U_1) + \delta(U_2) \leq \delta(U_1 \cup U_2) + \delta(U_1 \cap U_2)$$

yields

$$2\delta_1 \leq \delta(U_1 \cup U_2) + \delta(U_1 \cap U_2).$$

Since $\delta_1$ is the maximum possible deficiency of any subset of $V_1$, we have $\delta(U_1 \cup U_2) \leq \delta_1$ and $\delta(U_1 \cap U_2) \leq \delta_1$. Consequently,

$$\delta(U_1 \cup U_2) = \delta_1 = \delta(U_1 \cap U_2),$$

which means both $U_1 \cup U_2$ and $U_1 \cap U_2$ are critical subsets.
