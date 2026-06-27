---
role: proof
locale: en
of_concept: boolean-valued-subalgebra-embedding
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

(By induction.)

1. Obvious: any function into $B$ is also a function into $B'$ (since $B \subseteq B'$). The definition of $V_\alpha^{(B)}$ then yields $V_\alpha^{(B)} \subseteq V_\alpha^{(B')}$ by induction on $\alpha$.

2. The definitions of $[\![u \in v]\!]$ and $[\![u = v]\!]$ involve only Boolean sums, products, and complements over values in $B$. Since $B$ is a complete subalgebra of $B'$, the infinite sums and products computed in $B$ yield the same results when computed in $B'$. By induction on the rank, the Boolean values agree.
