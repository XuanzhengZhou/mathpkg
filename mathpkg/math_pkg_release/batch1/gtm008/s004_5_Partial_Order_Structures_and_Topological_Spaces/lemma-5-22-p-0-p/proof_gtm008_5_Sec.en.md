---
role: proof
locale: en
of_concept: lemma-5-22-p-0-p
source_book: gtm008
source_chapter: "5"
source_section: "5 Partial Order Structures and Topological Spaces

In the work"
---
We have only to show $[p]^{-0} \subseteq [p]$. Let $q \in P$ such that $q \notin [p]$, i.e., $q \not\leq p$. Then, by Definition 5.21, $(\exists r \in P)[r \leq q \land \neg \text{Comp}(r, p)]$. Therefore, $[r] \cap [p] = 0$ and hence $r \notin [p]^{-}$. This implies $[q] \not\subseteq [p]^{-}$. Consequently $q \notin [p]^{-0}$, i.e., if $q \in [p]^{-0}$ then $q \in [p]$.

Remark. Many $P$'s used in later sections are fine.

6. Boolean-Valued Structures

The notion of a Boolean-valued structure is obtained from the definition of an ordinary 2-valued structure by replacing the Boolean algebra 2 of two truth values "truth" and "falsehood" by any complete Boolean algebra B. While some of the basic definitions and theorems can be generalized to the B-valued case almost mechanically the intuitive ideas behind these general notions are more difficult to perceive.

Throughout this section $B = \langle B, +, \cdot, -, 0, 1 \rangle$ denotes a complete Boolean algebra.
