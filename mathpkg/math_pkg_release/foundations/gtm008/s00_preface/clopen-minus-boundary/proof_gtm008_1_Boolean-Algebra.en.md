---
role: proof
locale: en
of_concept: clopen-minus-boundary
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** If $x \in B^- - C$, then since $B^- - B^0 \subseteq C$, we have $x \in B^0$ and $x \notin C$. Since $C$ is closed, $X - C$ is open. Since $B^0$ is open, $(B^- - C) \subseteq B^0 \subseteq B^-$. Moreover, $B^- - C = B^- \cap (X - C)$, which is the intersection of a closed set and an open set, and under the given condition, this intersection is in fact clopen. (The source text proof is partially cut off; the argument follows from the fact that the boundary $B^- - B^0$ being contained in the clopen $C$ forces $B^- - C$ to equal $B^0 - C$, which is open, while also being closed as the intersection of a closed set with a closed set.)
