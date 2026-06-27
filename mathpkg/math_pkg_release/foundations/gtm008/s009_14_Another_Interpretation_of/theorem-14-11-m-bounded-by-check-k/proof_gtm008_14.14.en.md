---
role: proof
locale: en
of_concept: theorem-14-11-m-bounded-by-check-k
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

Let $x \in V^{(B)}$. Then $x \in V_{\alpha+1}^{(B)}$ for some ordinal $\alpha$. Choose $k = R(\alpha + 1)$. Then

$$[M(x)] = \sum_{k_0 \in V} [x = \check{k}_0] = \sum_{k_0 \in R(\alpha + 1)} [x = \check{k}_0] \quad \text{by Theorem 14.2.2}$$

$$= \sum_{k_0 \in k} [x = \check{k}_0] \leq \sum_{k_0 \in k} [\check{k}_0 \in \check{k}]$$

$$\leq [x \in \check{k}].$$

The inequality $[x = \check{k}_0] \leq [\check{k}_0 \in \check{k}]$ follows because $k_0 \in k$ (since $k_0 \in R(\alpha+1) = k$), and the final inequality follows from the definition of $[x \in \check{k}]$ as $\sum_{k_0 \in k} [x = \check{k}_0]$.
