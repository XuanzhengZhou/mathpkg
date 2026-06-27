---
role: proof
locale: en
of_concept: no-countable-set-cofinal-in-w
source_book: gtm043
source_chapter: "5"
source_section: "5.12"
---

If $S$ is cofinal in $W$, then $W = \bigcup_{\sigma \in S} W(\sigma)$. Computing cardinalities:

$$\aleph_1 = |W| = \left|\bigcup_{\sigma \in S} W(\sigma)\right| \leq \sum_{\sigma \in S} |\sigma| \leq |S| \cdot \aleph_0.$$

Thus $|S| \cdot \aleph_0 \geq \aleph_1$, which forces $|S| \geq \aleph_1$. No countable set can have cardinality $\aleph_1$, so no countable set can be cofinal in $W$.
