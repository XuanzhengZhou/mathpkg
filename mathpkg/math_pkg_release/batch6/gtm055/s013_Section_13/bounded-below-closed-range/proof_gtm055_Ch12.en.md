---
role: proof
locale: en
of_concept: bounded-below-closed-range
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

The proof is given in the text; the key idea is that bounded-belowness together with completeness forces the range to be closed via a Cauchy sequence argument. If $\{Tx_n\}$ is a sequence in $\mathcal{R}(T)$ converging to some $y \in \mathcal{F}$, then the bounded-belowness condition $\|x_m - x_n\| \leq (1/M)\|Tx_m - Tx_n\|$ implies $\{x_n\}$ is Cauchy in the complete space $\mathcal{E}$, hence converges to some $x$. Continuity of $T$ then gives $Tx = y$, so $y \in \mathcal{R}(T)$.
