---
role: proof
locale: en
of_concept: lemma-9-9
source_book: gtm040
source_chapter: "9"
source_section: "1. Potentials"
---

We compute:
$${}_j N_{ki} + {}_i N_{kj} \frac{\alpha_i}{\alpha_j} = {}_j H_{ki} \cdot {}_j N_{ii} + {}_i H_{kj} \cdot {}_i N_{jj} \frac{\alpha_i}{\alpha_j}$$
$$= ({}_j H_{ki} + {}_i H_{kj}) \, {}_j N_{ii} \quad \text{by Lemma 9-8}$$
$$= {}_j N_{ii}.$$
The last equality follows because ${}_j H_{ki}$ (hitting probability of $i$ starting from $k$ before hitting $j$) and ${}_i H_{kj}$ (hitting probability of $j$ starting from $k$ before hitting $i$) together account for all paths from $k$.
