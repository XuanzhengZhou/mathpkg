---
role: proof
locale: en
of_concept: eigenvalues-of-sl2-modules
source_book: gtm009
source_chapter: "II"
source_section: "7"
---

If $V = 0$, there is nothing to prove. Otherwise, by Weyl's Theorem (6.3), $V$ decomposes as a direct sum of irreducible $L$-submodules. Each irreducible module is described by the classification theorem: it has highest weight $m$ (a nonnegative integer) and weights $m, m-2, \ldots, -m$, each occurring with multiplicity 1. Summing over all irreducible components, the eigenvalues of $h$ on $V$ are all integers, and each $\mu$ occurs with the same multiplicity as $-\mu$.

For the second assertion: each irreducible $L$-module has a unique occurrence of either the weight 0 (when $m$ is even) or the weight 1 (when $m$ is odd), but not both. Specifically, if $m$ is even then the weights include 0 (exactly once), and if $m$ is odd then 1 appears exactly once. Therefore, the number of irreducible summands equals $\dim V_0 + \dim V_1$.
