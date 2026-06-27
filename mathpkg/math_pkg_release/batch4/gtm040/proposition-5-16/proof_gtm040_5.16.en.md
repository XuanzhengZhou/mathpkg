---
role: proof
locale: en
of_concept: proposition-5-16
source_book: gtm040
source_chapter: "5"
source_section: "16"
---

**Proof:**

$$(N1)_i = \sum_j N_{ij} \quad \text{summed over the transient states}$$

$$= \sum_j M_i[n_j]$$

$$= M_i \left[ \sum_j n_j \right] \quad \text{by monotone convergence.}$$

But $a = \sum_j n_j$, where the sum is taken over transient states $j$. Thus $(N1)_i = M_i[a] = a_i$.
