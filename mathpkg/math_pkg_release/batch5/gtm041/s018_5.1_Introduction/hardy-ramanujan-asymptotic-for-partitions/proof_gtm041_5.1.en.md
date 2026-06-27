---
role: proof
locale: en
of_concept: hardy-ramanujan-asymptotic-for-partitions
source_book: gtm041
source_chapter: "5"
source_section: "5.1"
---

This asymptotic formula was first discovered by Hardy and Ramanujan [13] in 1918 and, independently, by J. V. Uspensky [52] in 1920. The proof uses the circle method and is the subject of Rademacher's refinement developed throughout this chapter. Hardy and Ramanujan actually proved a more refined asymptotic series:

$$p(n) = \sum_{k < \alpha\sqrt{n}} P_k(n) + O(n^{-1/4}),$$

where $\alpha$ is a constant and $P_1(n)$ is the dominant term asymptotic to $e^{K\sqrt{n}}/(4n\sqrt{3})$. The terms $P_2(n), P_3(n), \ldots$ are of similar type but with smaller constants in place of $K$ in the exponential. However, the infinite series $\sum_{k=1}^{\infty} P_k(n)$ diverges for each $n$, as shown by D. H. Lehmer [21] in 1937.
