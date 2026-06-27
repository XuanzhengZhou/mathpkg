---
role: proof
locale: en
of_concept: undecidability-of-recursive-arithmetic
source_book: gtm022
source_chapter: "IX"
source_section: "6"
---

Since every partial recursive function is strongly definable, there is a formula $\operatorname{comp}(x_1, x_2, x_3)$ defining the relation that $M_{x_1}$ on input $x_2$ computes $x_3$. If $\mathcal{T}$ were decidable, then for each $n$, one could decide $\mathcal{T} \vdash (\exists x)\operatorname{comp}(n, n, x)$, which would solve the Stopping Problem.
