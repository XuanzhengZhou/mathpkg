---
role: proof
locale: en
of_concept: vanishing-small-set-measures
source_book: gtm040
source_chapter: "9"
source_section: "3"
---

$$\lim_j \,^{i}\!\lambda_j = \lim_j \sum_k \alpha_k \,^{i}\!H_{kj} \quad \text{by Proposition 9-55}$$
$$= \sum_k \alpha_k \lim_j \,^{i}\!H_{kj} \quad \text{by dominated convergence}$$
$$= 0 \quad \text{by Lemma 9-59}.$$

The interchange of limit and sum is justified by dominated convergence since $^{i}\!H_{kj} \leq 1$ and $\sum_k \alpha_k = 1$.
