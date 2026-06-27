---
role: proof
locale: en
of_concept: rademacher-convergent-series-for-partitions
source_book: gtm041
source_chapter: "5"
source_section: "5.1"
---

Hans Rademacher, while preparing lecture notes in 1937 on the work of Hardy and Ramanujan, made a small change in the analysis which resulted in slightly different terms $R_k(n)$ in place of the $P_k(n)$. This had a profound effect on the final result since, instead of a divergent asymptotic series, Rademacher obtained the convergent series

$$p(n) = \sum_{k=1}^{\infty} R_k(n).$$

The exact form of the Rademacher terms $R_k(n)$ is described below in Theorem 5.10. Rademacher [35] also showed that the remainder after $N$ terms is $O(n^{-1/4})$ when $N$ is of order $\sqrt{n}$, in agreement with the Hardy-Ramanujan formula. This chapter is devoted to a proof of Rademacher's exact formula using the circle method and the Dedekind modular function $\eta(\tau)$.
