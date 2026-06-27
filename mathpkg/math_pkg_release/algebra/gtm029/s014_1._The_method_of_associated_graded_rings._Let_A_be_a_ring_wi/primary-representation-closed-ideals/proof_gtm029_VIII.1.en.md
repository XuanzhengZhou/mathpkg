---
role: proof
locale: en
of_concept: primary-representation-closed-ideals
source_book: gtm029
source_chapter: "VIII"
source_section: "1. The method of associated graded rings"
---

Consider the quotient ring $A_S$ where $S = 1 + \mathfrak{m}$. As $\mathfrak{a}$ is closed, we have $\hat{A}\mathfrak{a} \cap A = \mathfrak{a}$ (Corollary 2 to Theorem 5, $\S$2), whence $\mathfrak{a}A_S \cap A = \mathfrak{a}$. By using properties of quotient rings, it suffices to prove the theorem for $(\mathfrak{m}A_S, A_S, \mathfrak{a}A_S)$ instead of $(\mathfrak{m}, A, \mathfrak{a})$, so we may assume $A$ is a Zariski ring.

Any element $x$ of $\mathfrak{p}_i^*$ is a zero divisor modulo $\hat{A}\mathfrak{a}$. Since any regular element in $A/\mathfrak{a}$ is also regular in $\hat{A}/\hat{A}\mathfrak{a}$ (Corollary 6 to Theorem 11), every element of $\mathfrak{p}_i^* \cap A$ is a zero divisor modulo $\mathfrak{a}$ and therefore belongs to some associated prime ideal of $\mathfrak{a}$. On the other hand, $\mathfrak{q}_i^* \cap A$ is a primary ideal admitting $\mathfrak{p}_i^* \cap A$ as radical. Therefore, from the irredundant primary decomposition of $\hat{A}\mathfrak{a}$, we obtain by contraction a primary decomposition $\mathfrak{a} = \bigcap_i (\mathfrak{q}_i^* \cap A)$.