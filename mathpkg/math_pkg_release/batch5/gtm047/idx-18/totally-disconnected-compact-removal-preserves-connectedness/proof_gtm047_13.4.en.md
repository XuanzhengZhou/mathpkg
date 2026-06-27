---
role: proof
locale: en
of_concept: totally-disconnected-compact-removal-preserves-connectedness
source_book: gtm047
source_chapter: "13"
source_section: "13"
---

**Proof.** Let $Q$ and $S$ be points of $U - M$. Then $Q$ and $S$ can be joined by a broken line in $U$. It follows, by an easy construction, that there is a (polyhedral) $2$-cell $C^2$, with $\operatorname{Bd} C^2 = B_1 \cup B_2$ and $B_1 \cap B_2 = \{Q, S\}$. For $i = 1, 2$, let $A_i = M \cap \operatorname{Int} B_i = M \cap B_i$. Then $A_1$ and $A_2$ are disjoint and closed. Since $M \cap C^2$ is compact and totally disconnected, it follows by Theorem 12.3 that $M \cap C^2$ is the union of two disjoint closed sets $M_1, M_2$, containing $A_1$ and $A_2$. By Theorem 3, $Q$ and $S$ lie in the same component of $C^2 - (M_1 \cup M_2) = C^2 - (M \cap C^2)$. Therefore $Q$ and $S$ lie in the same component of $U - M$, establishing that $U - M$ is connected.
