---
role: proof
locale: en
of_concept: generic-equivalent-definitions
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** $(3 \rightarrow 2)$: If $S \in A$ is dense in $P$, then $(\forall p)[[p] \cap S \neq 0]$. By (3), $(\exists p \in G)[p \in S]$, i.e., $G \cap S \neq 0$.

$(2 \rightarrow 3)$: Suppose $S \in A$ and $S \subseteq P$. Let $S' = S \cup \{p \mid [p] \cap S = 0\}$. Then $S' \in A$ and $S'$ is dense in $P$ (if not, there is $p$ with $[p] \cap S' = 0$, but then $[p] \cap S = 0$, so $p \in S'$, contradiction). By (2), $G \cap S' \neq 0$, so $(\exists p \in G)[p \in S \lor [p] \cap S = 0]$.
