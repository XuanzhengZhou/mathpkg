---
role: proof
locale: en
of_concept: nullset-infinite-covering-characterization
source_book: gtm002
source_chapter: "14"
source_section: "14"
---

If $A$ is a nullset, then it can be covered for each $n$ by a sequence of intervals whose total measure is less than $1/2^n$. Concatenating these sequences for $n = 1, 2, 3, \ldots$ yields a single sequence $\{I_n\}$ that covers $A$ infinitely many times, and $\sum |I_n| < \sum 1/2^n = 1 < \infty$.

Conversely, if $A$ is covered infinitely many times by a sequence $\{I_n\}$ with $\sum |I_n|$ convergent, then $A$ is covered by the subsequence starting with the $k$-th term. Since the series converges, the sum $\sum_{n=k}^{\infty} |I_n|$ can be made arbitrarily small by choosing $k$ sufficiently large. Hence $A$ is a nullset.
