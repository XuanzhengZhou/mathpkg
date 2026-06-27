---
role: proof
locale: en
of_concept: theorem-14-16-existence-formula-pairsets
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

By Theorem 13.13.1,
$$[(\exists x)(\exists y)[\{x, y\} = \check{k}_1 \land \varphi(x, y)]] = \sum_{\{k_2, k_3\} \in k_1} [\{\check{k}_2, \check{k}_3\} = \check{k}_1] \cdot [\varphi(\check{k}_2, \check{k}_3)]$$
$$= \sum_{\{k_2, k_3\} = k_1} [\varphi(\check{k}_2, \check{k}_3)]$$
by Theorem 14.15, since $[\{\check{k}_2, \check{k}_3\} = \check{k}_1] = 1$ when $\{k_2, k_3\} = k_1$ and 0 otherwise.
