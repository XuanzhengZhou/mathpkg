---
role: proof
locale: en
of_concept: finite-transient-visits
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** If the chain were in a finite set $S'$ infinitely often with positive probability, then by the pigeonhole principle it would be in some state $j \in S'$ infinitely often with positive probability.

If such an occurrence had positive probability, then $N_{ij}$ (the expected number of visits to $j$ starting from some $i$) would be infinite, since infinite visits with positive probability implies infinite expected visits.

However, if $j$ is transient, Corollary 4-21 gives $N_{ij} < \infty$ for all $i$. This contradiction establishes that the chain cannot visit any finite subset of transient states infinitely often with positive probability. Hence the chain is in such a finite set only finitely often with probability one.
