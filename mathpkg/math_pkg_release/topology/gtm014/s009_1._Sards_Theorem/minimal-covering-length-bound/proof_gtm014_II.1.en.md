---
role: proof
locale: en
of_concept: minimal-covering-length-bound
source_book: gtm014
source_chapter: "II"
source_section: "§1. Sard's Theorem"
---

Order the intervals of a minimal covering $[a_1, b_1], \ldots, [a_m, b_m]$ so that $a_1 \leq a_2 \leq \cdots \leq a_m$. Then minimality implies that $b_1 \leq b_2 \leq \cdots \leq b_m$.

Moreover, $[a_k, b_k] \cap [a_{k+2}, b_{k+2}] = \emptyset$ for $1 \leq k \leq m-2$. Otherwise $a_{k+2} \leq b_k$ and $[a_{k+1}, b_{k+1}] \subset [a_k, b_k] \cup [a_{k+2}, b_{k+2}]$ since $a_k \leq a_{k+1}$ and $b_{k+1} \leq b_{k+2}$, contradicting minimality.

Hence the sum of the lengths of $[a_1, b_1], [a_3, b_3], [a_5, b_5], \ldots$ is at most $b - a$ (since these intervals are disjoint and contained in $I$). Similarly, the sum of the lengths of $[a_2, b_2], [a_4, b_4], [a_6, b_6], \ldots$ is at most $b - a$. Therefore,
$$\sum_{i=1}^{m} (b_i - a_i) \leq 2(b-a).$$
Since the covering is minimal, the inequality is strict, giving the desired bound of less than $2(b-a)$.
