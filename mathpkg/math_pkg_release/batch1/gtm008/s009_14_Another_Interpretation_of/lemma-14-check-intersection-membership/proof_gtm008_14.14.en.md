---
role: proof
locale: en
of_concept: lemma-14-check-intersection-membership
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

For $u \in V^{(B)}$,
$$[u \in (\check{k}_1 \cap \check{k}_2)] = [[(\exists x)(\exists y)][\langle x, y \rangle \in \check{k}_1 \land u = \langle x, y \rangle \land x \in \check{k}_2]]$$
$$= \sum_{\langle k_3, k_4 \rangle \in k_1} [u = \langle \check{k}_3, \check{k}_4 \rangle \land \check{k}_3 \in \check{k}_2]$$
$$= \sum_{k \in (k_1 \cap k_2)} [u = \check{k}]$$
$$= [u \in (k_1 \cap k_2)^{\vee}].$$

The reduction from ordered pairs to elements uses that $\check{k}_1$ consists of ordered pairs $\langle \check{k}_3, \check{k}_4 \rangle$ for $k_3 \in k_1$, and the condition $\check{k}_3 \in \check{k}_2$ is true exactly when $k_3 \in k_2$.
