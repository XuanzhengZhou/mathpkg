---
role: proof
locale: en
of_concept: ultrafilter-correspondence-equality
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** If $b \in F'$, then $b = b^{-0}$ and $b \cap G \neq 0$, so $(\exists p \in G)[p \in b]$. Then $(\exists p)[[p]^{-0} \in F \land [p]^{-0} \leq b]$, hence $b \in F$ (since $F$ is upward-closed). Thus $F' \subseteq F$. By Theorem 2.17, $G$ is $P$-generic over $M$, and by Theorem 2.16, $F'$ is a proper ultrafilter. Since $F$ is also a proper ultrafilter and $F' \subseteq F$, by maximality $F = F'$.
