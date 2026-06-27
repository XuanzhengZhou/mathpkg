---
role: proof
locale: en
of_concept: principle-of-inclusion-exclusion-e13-e13
source_book: gtm054
source_chapter: "1"
source_section: "ID"
---

As remarked above, it suffices to prove (a) alone.

If $A \in \mathcal{P}(E)$, then by E8c, $s^*(A)$ represents the number of vertices which belong to every block in $A$ but to no other block. Thus the number of vertices which belong to precisely $r$ blocks is $\sum_{|A|=r} s^*(A)$. By applying Proposition E6 to $s^*$, we get

$$\sum_{|A|=r} s^*(A) = \sum_{|A|=r} \sum_{C \in \mathcal{P}(E)} (-1)^{|C+A|}[A, C] \bar{s}^*(C)$$

$$= \sum_{|C| \geq r} \left( \sum_{|A|=r} (-1)^{|C+A|}[A, C] \right) \bar{s}^*(C)$$

$$= \sum_{|C| \geq r} (-1)^{|C|-r} \binom{|C|}{r} \bar{s}^*(C)$$

$$= \sum_{i=0}^{|E|-r} \sum_{|C|=i+r} (-1)^{|C|-r} \binom{|C|}{r} \bar{s}^*(C)$$

$$= \

of blocks containing $S$, part (b) gives the number of blocks of fixed size $k$ in terms of the number of blocks containing subset $S$ of $V$ of size at least $k$.

The Principle of Inclusion–Exclusion has a wide range of applications. The remainder of this chapter is devoted to some of them. We begin by completing the answer to the question raised just after C12.
