---
role: proof
locale: en
of_concept: autotopism-as-semilinear-transformation
source_book: gtm006
source_chapter: "VIII"
source_section: "6"
---

**Proof.** Let $x \in D$ and $n \in N_l$. From the autotopism identity $xP \cdot yQ = (xy)R$, together with the fact that $n$ associates on the left (i.e., $n(xy) = (nx)y$), one computes:

$$(nx)P = (nx)R \cdot (b)R^{-1} = (n(xa)R_b^{-1})R = n^l \cdot xP,$$

where $n^l$ is the companion automorphism of $N_l$ induced by the autotopism. Thus $P$ is semi-linear with respect to the automorphism $n \mapsto n^l$ on $N_l$.

Similarly, if $n \in N_m$, then from $n$ associating in the middle position one obtains $(xn)P = xP \cdot n^m$, showing that $P$ is a semi-linear transformation of the right vector space $D$ over $N_m$. The same reasoning applies to $Q$ and $R$ with the appropriate semi-nuclei. For an automorphism, $P = Q = R$, and the statement follows as a special case. $\square$
