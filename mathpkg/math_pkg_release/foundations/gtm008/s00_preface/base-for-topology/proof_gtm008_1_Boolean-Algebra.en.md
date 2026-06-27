---
role: proof
locale: en
of_concept: base-for-topology
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** If $T = \{B \subseteq X \mid (\exists C \subseteq T') [B = \bigcup (C)]\}$, then $0 = \bigcup (0) \in T$ and $X = \bigcup (T') \in T$, establishing property 1 of Definition 1.13.

To prove property 2, if $S \subseteq T$, then for each $B \in S$ there exists $C_B \subseteq T'$ such that $B = \bigcup (C_B)$. Then $\bigcup_{B \in S} B = \bigcup_{B \in S} \bigcup (C_B) = \bigcup (\bigcup_{B \in S} C_B)$. Since $\bigcup_{B \in S} C_B \subseteq T'$, we have $\bigcup (S) \in T$.

For property 3, if $B_1, B_2 \in T$, then there exist $C_1, C_2 \subseteq T'$ with $B_1 = \bigcup (C_1)$ and $B_2 = \bigcup (C_2)$. Then $B_1 \cap B_2 = (\bigcup_{A_1 \in C_1} A_1) \cap (\bigcup_{A_2 \in C_2} A_2) = \bigcup_{A_1 \in C_1, A_2 \in C_2} (A_1 \cap A_2)$. By the second condition on $T'$, each $A_1 \cap A_2$ is a union of elements of $T'$, so $B_1 \cap B_2 \in T$. Hence $T$ is a topology on $X$, and clearly $T'$ is a base for $T$.
