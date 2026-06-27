---
role: proof
locale: en
of_concept: fine-partial-order-basic-opens-regular-open
source_book: gtm008
source_chapter: "5"
source_section: "5"
---
We need only to show $[p]^{-0} \subseteq [p]$, since $[p] \subseteq [p]^{-0}$ always holds by general topology.

Let $q \in P$ such that $q \notin [p]$, i.e., $q \not\leq p$. Then, by Definition 5.21 (fineness), $(\exists r \in P)[r \leq q \land \neg \text{Comp}(r, p)]$. Therefore $[r] \cap [p] = 0$ (since $r$ and $p$ are incompatible) and hence $r \notin [p]^{-}$. This implies $[q] \not\subseteq [p]^{-}$, because $r \in [q]$ but $r \notin [p]^{-}$. Consequently $q \notin [p]^{-0}$.

Thus $q \notin [p]$ implies $q \notin [p]^{-0}$, i.e., $[p]^{-0} \subseteq [p]$. Hence $[p]^{-0} = [p]$.
