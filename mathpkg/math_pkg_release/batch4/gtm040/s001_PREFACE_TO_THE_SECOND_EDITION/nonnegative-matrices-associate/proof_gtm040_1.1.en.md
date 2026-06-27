---
role: proof
locale: en
of_concept: nonnegative-matrices-associate
source_book: gtm040
source_chapter: "1"
source_section: "1"
---

Since we are interested in each entry separately of a triple product, we may assume that we are to show that $\pi(Af) = (\pi A)f$, where $\pi \geq 0$, $A \geq 0$, $f \geq 0$, $\pi$ is a row vector, $f$ is a column vector, and the index sets are subsets of the non-negative integers. Then

$$\pi(Af) = \sum_m \sum_n \pi_m A_{mn} f_n, \qquad (\pi A)f = \sum_n \sum_m \pi_m A_{mn} f_n.$$

Set $b_{ij} = \sum_{m=0}^{i} \sum_{n=0}^{j} \pi_m A_{mn} f_n$. Then $\{b_{ij}\}$ is nondecreasing in $i$ and $j$, and by Lemma 1-3,

$$\lim_i \lim_j b_{ij} = \lim_j \lim_i b_{ij}.$$

But the left side equals $\pi(Af)$ and the right side equals $(\pi A)f$, so the two are equal.
