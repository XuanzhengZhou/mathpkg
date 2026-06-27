---
role: proof
locale: en
of_concept: permutation-invariance-forcing
source_book: gtm008
source_chapter: "12"
source_section: "12. The Independence of the AC"
---

The proof proceeds by transfinite induction on $\text{Ord}(\varphi)$, the order of the formula in the ramified language. The permutation $\pi$ of $\omega$ is extended to terms and formulas by conditions 1--7 (given in the text), which ensure that $\pi$ respects the syntactic structure. For atomic formulas, the result follows from the definition of $\pi$ on terms and the forcing relation for atomic statements. For compound formulas (negation, conjunction, quantifiers), one applies the induction hypothesis. The key observation is that $\pi$ merely permutes the indices of the generic sets $F_i$, and the Boolean algebra of regular open sets in $\prod_{i \in \omega}^{w} P_i$ is symmetric under such permutations. Thus the forcing relation is preserved: a condition $p$ forces $\varphi$ exactly when the permuted condition $\pi(p)$ forces the permuted formula $\pi(\varphi)$.
