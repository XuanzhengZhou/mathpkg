---
role: proof
locale: en
of_concept: approximation-sigma-compact-gdelta
source_book: gtm025
source_chapter: "3"
source_section: "10"
---

**Proof.** (I) If $\iota(A) < \infty$, use inner regularity (10.30) to find compact $F_n \subset A$ with $\iota(A \cap F_n') < 1/n$. Then $B = \bigcup F_n$ is $\sigma$-compact and $\iota(A \cap B') = 0$. For the $G_\delta$ approximation, use outer regularity to find open $U_n \supset A$ with $\iota(U_n \cap A') < 1/n$ and set $C = \bigcap U_n$.

(II) If $\iota(A) = \infty$, write $A = \bigcup A_n$ with $\iota(A_n) < \infty$, apply (I) to each $A_n$, and take unions/intersections. $\square$
