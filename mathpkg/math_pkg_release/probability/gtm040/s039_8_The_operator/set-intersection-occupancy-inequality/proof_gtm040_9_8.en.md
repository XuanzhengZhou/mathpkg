---
role: proof
locale: en
of_concept: set-intersection-occupancy-inequality
source_book: gtm040
source_chapter: "9"
source_section: "8"
---
The left side is the mean number of times in state $j$, starting in $i$, before the intersection of sets is reached. We show that the right side is the mean number of times in $j$ before all of the sets have been reached. The former is clearly at least as large as the latter. Let $n_j(\omega)$ be the number of times on $\omega$ that the process is in $j$ before all sets are entered. On the path $\omega$ let $S_k$ be the set of times at which the process is in $j$ before $A_k$ is entered. Then $n_j(\omega)$ is the cardinal number of $S_1 \cup S_2 \cup \cdots \cup S_r$, which by the inclusion-exclusion formula equals
$$\sum_s n(S_s) - \sum_{s < t} n(S_s \cap S_t) + \sum_{s < t < u} n(S_s \cap S_t \cap S_u) - \cdots + (-1)^{r+1} n(S_1 \cap S_2 \cap \cdots \cap S_r).$$
The right-hand side expression in the lemma is precisely the expectation of this alternating sum.
