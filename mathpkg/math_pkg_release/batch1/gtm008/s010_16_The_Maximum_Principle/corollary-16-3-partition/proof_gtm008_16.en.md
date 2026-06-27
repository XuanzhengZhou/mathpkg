---
role: proof
locale: en
of_concept: corollary-16-3-partition
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Follows from the construction in the proof of Theorem 16.2 (the Maximum Principle). Define $v \in V^{(\mathbf{B})}$ by

$$\mathcal{D}(v) = d \land (\forall x \in d) \left[ v(x) = \sum_{\xi < \alpha} b_\xi \cdot u_\xi(x) \right].$$

Then for $\xi < \alpha$ and $x \in d$, we have $b_\xi \cdot v(x) = b_\xi \cdot u_\xi(x)$ since the $b_\xi$ are pairwise disjoint (a partition of unity). This is the mixing (or amalgamation) of the sets $u_\xi$ weighted by the orthogonal components $b_\xi$ of the Boolean algebra.
