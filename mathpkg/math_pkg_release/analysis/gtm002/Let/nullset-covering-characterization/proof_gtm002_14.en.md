---
role: proof
locale: en
of_concept: nullset-covering-characterization
source_book: gtm002
source_chapter: "14"
source_section: "14. Fubini's Theorem"
---

**Forward direction:** If $A$ is a nullset, then it can be covered by a sequence of intervals the sum of whose measures is less than $1/2$, by another with sum less than $1/4$, by another with sum less than $1/8$, and so on. Together these constitute a sequence $\{I_n\}$ that covers $A$ infinitely many times, and $\sum |I_n| < 1 < \infty$.

**Reverse direction:** If $A$ is covered infinitely many times by a sequence $\{I_n\}$, then it is covered by the subsequence starting with the $k$-th term. If $\sum |I_n|$ is convergent, the tail sum $\sum_{n=k}^{\infty} |I_n|$ can be made arbitrarily small by suitable choice of $k$. Hence $A$ is a nullset.
