---
role: proof
locale: en
of_concept: existence-of-generic-subsets
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** Since $A$ is countable, enumerate the dense subsets in $A$: $S_1, S_2, \ldots$. Given $a \in P$:
Choose $p_1 \in S_1$ with $p_1 \leq a$ (density of $S_1$).
Choose $p_2 \in S_2$ with $p_2 \leq p_1$ (density of $S_2$).
Continue inductively to obtain a sequence $p_1 \geq p_2 \geq \cdots$ with $p_n \in S_n$.
Define $G = \{q \mid (\exists p_i)[p_i \leq q]\}$. Then $a \in G$, $G$ is compatible (all elements lie above some $p_i$), upward-closed by construction, and meets every dense set $S_n$ since $p_n \in G \cap S_n$.
