---
role: proof
locale: en
of_concept: nullset
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
The text shows that the class of nullsets is a $\sigma$-ideal:

\textbf{Singletons are nullsets:} For any singleton $\{x\}$, cover it by an interval of length $\varepsilon/2$ centered at $x$.

\textbf{Subsets of nullsets are nullsets:} If $B \subset A$ and $A$ is covered by intervals $I_n$ with $\sum |I_n| < \varepsilon$, then the same cover works for $B$.

\textbf{Countable unions of nullsets are nullsets:} Suppose $A_i$ is a nullset for $i = 1, 2, \dots$. For each $i$ there is a sequence of intervals $I_{ij}$ ($j = 1, 2, \dots$) such that $A_i \subset \bigcup_j I_{ij}$ and $\sum_j |I_{ij}| < \varepsilon/2^i$. The set of all the intervals $I_{ij}$ covers $\bigcup_i A_i$, and
$$\sum_{i,j} |I_{ij}| = \sum_{i=1}^{\infty} \left(\sum_{j=1}^{\infty} |I_{ij}|\right) < \sum_{i=1}^{\infty} \frac{\varepsilon}{2^i} = \varepsilon.$$
Hence $\bigcup_i A_i$ is a nullset. This shows that the class of nullsets is a $\sigma$-ideal.
