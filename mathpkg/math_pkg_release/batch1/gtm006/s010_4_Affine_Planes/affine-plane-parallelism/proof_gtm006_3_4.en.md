---
role: proof
locale: en
of_concept: affine-plane-parallelism
source_book: gtm006
source_chapter: "3"
source_section: "4"
---

**Proof.** We verify that parallelism is an equivalence relation on the lines of an affine plane $\mathcal{A}$.

*Reflexivity:* By definition, $l \parallel l$ for every line $l$.

*Symmetry:* If $l \parallel m$ and $l \neq m$, then $l$ and $m$ have no point in common, so $m$ and $l$ have no point in common, hence $m \parallel l$.

*Transitivity:* Suppose $l \parallel m$ and $m \parallel h$. We must show $l \parallel h$. Assume for contradiction that $l$ and $h$ intersect at a point $A$. If $l \neq m$, then $l \parallel m$ means $l$ and $m$ have no common point. Similarly, if $m \neq h$, then $m \parallel h$ means $m$ and $h$ have no common point. But then through $A$ (which lies on $l$ and $h$ but not on $m$) there would be two distinct lines $l$ and $h$ both parallel to $m$, contradicting axiom (ii) (Playfair's axiom). Thus $l$ and $h$ cannot intersect, so $l \parallel h$.

Therefore parallelism is an equivalence relation. $\square$
