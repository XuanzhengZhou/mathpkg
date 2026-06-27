---
role: proof
locale: en
of_concept: localization-of-strong-topology
source_book: gtm036
source_chapter: "5"
source_section: "22.11"
---

The first half is evident. For the converse, let $\{B_n\}$ be a co-base for strongly bounded sets in $E^*$ such that each $B_n$ is convex and circled and $B_n \subset B_{n+1}$. By the assumption, for each $n$, there is a convex circled strong neighborhood $U_n$ of $0$ in $E^*$ such that $A \cap B_n \supset U_n \cap B_n$. Let $V_n = (A \cap B_n) + U_n$. Then $V_n \cap B_n \subset 3(A \cap B_n)$, for the following reason. If $h \in V_n \cap B_n$, then $h = f + g$, where $f \in A \cap B_n$ and $g \in U_n$, hence $g = h - f \in B_n + A \cap B_n \subset 2B_n$, and therefore $g \in 2(B_n \cap U_n) \subset 2(A \cap B_n)$ and $h = f + g \in 3(A \cap B_n)$. Consequently $V_n \cap B_n \subset 3A$, and since $B_n$ absorbs $B_{n-1}$, it follows that $V = \bigcap \{V_n : n = 1, 2, \cdots\}$ is a strong neighborhood of $0$ which is contained in $3A$. Hence $A$ is a strong neighborhood of $0$.
