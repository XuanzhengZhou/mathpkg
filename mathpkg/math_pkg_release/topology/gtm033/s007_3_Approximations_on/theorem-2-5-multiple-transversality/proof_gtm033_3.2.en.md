---
role: proof
locale: en
of_concept: theorem-2-5-multiple-transversality
source_book: gtm033
source_chapter: "3"
source_section: "2. Transversality"
---

# Proof of Theorem 2.5: Simultaneous Transversality to Multiple Submanifolds

**Theorem 2.5.** Let $A_0, \ldots, A_q$ be $C^r$ submanifolds of $N$, $1 \leqslant r \leqslant \infty$. The set $\bigcap^{\,r}(M,N; A_0, \ldots, A_q)$ of $C^r$ maps $M \to N$ that are transverse to each $A_i$, $i = 0, \ldots, q$, is residual in $C^r_S(M,N)$.

*Proof.* By the Transversality Theorem 2.1, for each individual closed submanifold $A_k$, the set $\bigcap^{\,r}(M,N; A_k)$ is residual (and in fact open and dense when $A_k$ is closed). For non-closed $A_k$, the set $\bigcap^{\,r}(M,N; A_k)$ is still residual (by the version of Theorem 2.1 that handles not-necessarily-closed submanifolds).

Since each set $\bigcap^{\,r}(M,N; A_k)$ is residual for $k = 0, \ldots, q$, and the intersection of finitely many residual sets is residual (a fundamental consequence of the Baire category theorem: a countable intersection of residual sets is residual), it follows that

$$\bigcap^{\,r}(M,N; A_0, \ldots, A_q) = \bigcap_{k=0}^{q} \bigcap^{\,r}(M,N; A_k)$$

is residual in $C^r_S(M,N)$.

**Remark.** When the $A_k$ are closed, the set is actually open and dense (finite intersection of open dense sets). When some $A_k$ are not closed, openness may be lost (as noted in the text) but the residual property persists.

QED
