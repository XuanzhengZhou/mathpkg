---
role: proof
locale: en
of_concept: ext-vanishing-characterization-of-projective-modules
source_book: gtm052
source_chapter: "III"
source_section: "6"
---

See Matsumura [2, pp. 127--128].

(a) If $M$ is projective, then $\operatorname{Ext}^1(M, N) = 0$ for all $N$ because $\operatorname{Hom}(M, \cdot)$ is exact, so its right derived functor vanishes. Conversely, if $\operatorname{Ext}^1(M, N) = 0$ for all $N$, then for every short exact sequence $0 \to N' \to N \to N'' \to 0$, applying $\operatorname{Hom}(M, \cdot)$ gives a long exact sequence whose $\operatorname{Ext}^1$ term at the end vanishes, so $\operatorname{Hom}(M, \cdot)$ is exact, hence $M$ is projective.

(b) The forward direction follows by dimension shifting: if $\operatorname{pd}(M) \leq n$, then $M$ has a projective resolution of length $\leq n$, and computing Ext via this resolution shows $\operatorname{Ext}^i(M, N) = 0$ for $i > n$. Conversely, if $\operatorname{Ext}^i(M, N) = 0$ for all $i > n$ and all $N$, one constructs a projective resolution step by step; the vanishing forces the syzygy at the $n$-th step to be projective.
