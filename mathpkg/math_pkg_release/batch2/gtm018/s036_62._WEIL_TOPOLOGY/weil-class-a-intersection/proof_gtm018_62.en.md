---
role: proof
locale: en
of_concept: weil-class-a-intersection
source_book: gtm018
source_chapter: "62"
source_section: "Weil Topology"
---

**Theorem D.** Let $E$ and $F$ be measurable sets of positive, finite measure such that $A = EE^{-1}$ and $B = FF^{-1}$. By 59.E, there exists a measurable set $G$ of positive, finite measure and there exist two elements $x$ and $y$ in $X$ such that 

$$G \subset xE \cap yF.$$

Then it follows that

$$GG^{-1} \subset (xE)(xE)^{-1} = xEE^{-1}x^{-1}$$

and similarly $GG^{-1} \subset yFF^{-1}y^{-1}$. Therefore

$$GG^{-1} \subset xEE^{-1}x^{-1} \cap yFF^{-1}y^{-1}.$$

By the invariance properties of the measure group structure, we can translate back to obtain a set $C = z^{-1}(GG^{-1})z \in \mathbf{A}$ for an appropriate $z$, with $C \subset A \cap B$. $\blacksquare$
