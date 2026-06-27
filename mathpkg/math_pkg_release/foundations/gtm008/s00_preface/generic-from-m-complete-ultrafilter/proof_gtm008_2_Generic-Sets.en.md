---
role: proof
locale: en
of_concept: generic-from-m-complete-ultrafilter
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** Define $G = \{p \mid [p]^{-0} \in F\}$. If $S \in M$ is dense in $P$, then $S \subseteq \bigcup_{p \in S} [p]^{-0}$, and hence $(\bigcup_{p \in S} [p]^{-0})^{-0} = P$, i.e., $\sum_{p \in S} [p]^{-0} = 1 \in F$. If $G \cap S = 0$, then $(\forall p \in S)[p \notin G]$, so $[p]^{-0} \notin F$. Since $F$ is an ultrafilter, $-([p]^{-0}) \in F$ for all $p \in S$. By $M$-completeness, $\prod_{p \in S} -([p]^{-0}) \in F$, but this product equals $-\sum_{p \in S} [p]^{-0} = -1 = 0$, contradicting $F$ being proper. Therefore $G \cap S \neq 0$, and $G$ is $P$-generic over $M$.
