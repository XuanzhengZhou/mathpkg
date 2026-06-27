---
role: proof
locale: en
of_concept: "undecidability-of-recursive-arithmetic"
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---
Proof. A decision process for $\mathcal{T}$ would provide a decision process for the family $\{(\exists x) \operatorname{comp}(n, n, x) \mid n \in \mathbb{N}\}$, where $\operatorname{comp}(x_1, x_2, x_3)$ defines the relation that the machine of Godel number $x_1$ applied to $x_2$ computes $x_3$ (by Theorem 6.9, this relation is strongly definable). But this family is precisely the stopping problem, which is recursively insoluble (Example 5.5). $\square$
