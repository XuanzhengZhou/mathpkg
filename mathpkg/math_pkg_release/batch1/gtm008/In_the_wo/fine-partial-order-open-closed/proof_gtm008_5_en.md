---
role: proof
locale: en
of_concept: fine-partial-order-open-closed
source_book: gtm008
source_chapter: "5"
source_section: "Partial Order Structures and Topological Spaces"
---

**Proof.** We have only to show $[p]^{-0} \subseteq [p]$. Let $q \in P$ such that $q \notin [p]$, i.e., $q \not\leq p$. Then, by Definition 5.21, $(\exists r \in P)[r \leq q \land \neg \operatorname{Comp}(r, p)]$. Therefore $[r] \cap [p] = 0$ and hence $r \notin [p]^{-}$. This implies $[q] \not\subseteq [p]^{-}$. Consequently $q \notin [p]^{-0}$. Thus if $q \in [p]^{-0}$ then $q \in [p]$. $\square$
