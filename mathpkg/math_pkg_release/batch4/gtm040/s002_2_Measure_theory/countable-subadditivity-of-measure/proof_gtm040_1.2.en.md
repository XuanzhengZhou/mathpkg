---
role: proof
locale: en
of_concept: countable-subadditivity-of-measure
source_book: gtm040
source_chapter: "1"
source_section: "2"
---
Write $B_n = A_n - (\bigcup_{k=1}^{n-1} A_k)$. The sets $B_n$ are disjoint in pairs, and consequently the sets $A \cap B_n$ are also disjoint. Furthermore, $\bigcup_n B_n = \bigcup_n A_n$ so that
$$A = A \cap (\bigcup_n A_n) = A \cap (\bigcup_n B_n) = \bigcup_n (A \cap B_n).$$
By hypothesis $\mu$ is a measure. It is therefore completely additive and
$$\mu(A) = \sum_n \mu(A \cap B_n) \leq \sum_n \mu(B_n) \leq \sum_n \mu(A_n),$$
where the first inequality follows since $A \cap B_n \subset B_n$ and the second since $B_n \subset A_n$.
