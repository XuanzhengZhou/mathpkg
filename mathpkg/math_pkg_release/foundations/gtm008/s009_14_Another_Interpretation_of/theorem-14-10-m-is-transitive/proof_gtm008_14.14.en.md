---
role: proof
locale: en
of_concept: theorem-14-10-m-is-transitive
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

By Theorem 13.13.2, it suffices to show $\prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow [M(u) \rightarrow M(x)]) = 1$, i.e., $u(x) \cdot [M(u)] \leq [M(x)]$ for all $x \in \mathcal{D}(u)$.

For $x \in \mathcal{D}(u)$: $[u = \check{k}] \leq (u(x) \Rightarrow [x \in \check{k}])$, so $u(x) \cdot [u = \check{k}] \leq [x \in \check{k}]$. Also $[x \in \check{k}] = \sum_{k_1 \in k} [x = \check{k}_1] \leq \sum_{k_1 \in V} [x = \check{k}_1] = [M(x)]$. Combining: $u(x) \cdot [M(u)] = u(x) \cdot \sum_{k \in V} [u = \check{k}] = \sum_{k \in V} u(x) \cdot [u = \check{k}] \leq \sum_{k \in V} [x \in \check{k}] \leq [M(x)]$.
