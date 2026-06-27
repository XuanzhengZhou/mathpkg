---
role: proof
locale: en
of_concept: distributivity-of-matrix-multiplication
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

We prove only the first assertion. We may assume that $A$ is a row vector $\pi$ and that $B$ and $C$ are column vectors $f$ and $g$. Then

$$\pi f + \pi g = \sum_{m \in M} \pi_m f_m + \sum_{m \in M} \pi_m g_m
= \sum_{m \in M} (\pi_m f_m + \pi_m g_m)
= \sum_{m \in M} \pi_m (f_m + g_m)
= \pi(f + g).$$

The second assertion follows by the same reasoning applied row-by-row and column-by-column.
