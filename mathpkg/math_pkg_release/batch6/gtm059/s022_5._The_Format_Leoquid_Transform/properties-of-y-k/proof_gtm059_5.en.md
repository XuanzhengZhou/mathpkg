---
role: proof
locale: en
of_concept: properties-of-y-k
source_book: gtm059
source_chapter: ""
source_section: "5"
---

As to the first assertion, it is immediate by induction that

$$(T D_T)^k T^k = k! T^k.$$

Hence

$$y_k(k) = (T D_T)^k T^k + (T D_T)^k \sum_{i=1}^{k-1} (-1)^{i-1} \binom{k}{i} T^i$$

has the expression as stated. On the other hand, by induction it follows that given an integer $f$ for each integer $k$ there exist integers $a_1, \dots, a_k$ such that $a_i = 0$ if $i > k$, and

$$(T D_T)^k T^k - T^k = \sum_{i=1}^{k} a_i T^i.$$

Putting $T = 1$ yields the second assertion.
