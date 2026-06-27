---
role: proof
locale: en
of_concept: first-entrance-matrix-decomposition
source_book: gtm040
source_chapter: "4"
source_section: "6"
---

The first two assertions follow from the complete additivity of $\mu$; we have $h_j \equiv \bigvee_k f_j^{(k)}$ and $\bar{h}_j \equiv \bigvee_k \bar{f}_j^{(k)}$ disjointly.

For the third assertion we apply Theorem 4-10 with $p = \bar{h}_j$ and the random time identically one. Then $p'$ is the statement $h_j$ and

$$\bar{H}_{ij} = \Pr\nolimits_i[p] = \sum_k \Pr\nolimits_i[x_1 = k] \, \Pr\nolimits_k[p'] = \sum_k P_{ik} \, H_{kj}.$$

Thus $\bar{H} = PH$.
