---
role: proof
locale: en
of_concept: hyperbolic-decomposition-uniqueness
source_book: gtm007
source_chapter: "IV"
source_section: "§1.3 Isotropic vectors"
---

The existence follows from Proposition 3': if $f$ represents 0, split off a hyperbolic plane; repeat until the remaining form $h$ does not represent 0. Since the dimension is finite, this process terminates.

The uniqueness follows from Theorem 4 (Witt Cancellation). Suppose $f \sim g_1 + \cdots + g_m + h \sim g'_1 + \cdots + g'_{m'} + h'$ are two such decompositions with $h, h'$ anisotropic. If $m > m'$, then cancelling $g'_1, \dots, g'_{m'}$ from both sides (using Theorem 4) leaves $h' \sim g_{m'+1} + \cdots + g_m + h$. But the right side represents 0 (since each $g_i$ is hyperbolic), contradicting that $h'$ does not represent 0. Hence $m = m'$, and cancelling all hyperbolic parts yields $h \sim h'$.

The characterization of $m$ as the dimension of maximal isotropic subspaces follows because each hyperbolic plane contributes one dimension to a maximal isotropic subspace.
