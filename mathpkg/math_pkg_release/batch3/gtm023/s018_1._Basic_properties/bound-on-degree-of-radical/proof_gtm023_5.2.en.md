---
role: proof
locale: en
of_concept: bound-on-degree-of-radical
source_book: gtm023
source_chapter: "5"
source_section: "§2. Ideals"
---

Choose a basis $e_1, \ldots, e_r$ of $\operatorname{rad} A$. Each $e_i$ is nilpotent; let $k = \max(\deg e_i)$. Consider the ideal $(\operatorname{rad} A)^{rk}$. An arbitrary element in this ideal is a sum of terms $e_1^{k_1} \ldots e_r^{k_r}$ with $k_1 + \cdots + k_r = kr$. By the pigeonhole principle, for some $i$, $k_i \geq k$, so each term vanishes. Hence $(\operatorname{rad} A)^{rk} = 0$, proving $\operatorname{rad} A$ is nilpotent. Moreover, $r k - 1 \leq r$ gives the bound $\deg(\operatorname{rad} A) \leq r + 1 = \dim(\operatorname{rad} A) + 1 \leq n + 1$.
