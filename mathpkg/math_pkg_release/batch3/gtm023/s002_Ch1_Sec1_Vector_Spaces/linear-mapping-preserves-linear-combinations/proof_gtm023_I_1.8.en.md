---
role: proof
locale: en
of_concept: linear-mapping-preserves-linear-combinations
source_book: gtm023
source_chapter: "I"
source_section: "1.8"
---

If $\varphi$ satisfies (1.8) and (1.9), then by induction on the number of terms,
$$\varphi\left(\sum_i \lambda^i x_i\right) = \sum_i \varphi(\lambda^i x_i) = \sum_i \lambda^i \varphi x_i.$$
Conversely, if $\varphi$ preserves all finite linear combinations, then taking a single term $x+y = 1\cdot x + 1\cdot y$ gives $\varphi(x+y) = \varphi x + \varphi y$, and taking $\lambda x = \lambda \cdot x$ gives $\varphi(\lambda x) = \lambda \varphi x$.
