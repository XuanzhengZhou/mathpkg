---
role: proof
locale: en
of_concept: t-i-exactness-criterion
source_book: gtm052
source_chapter: "III"
source_section: "12"
---

In any case, $T^i$ is exact in the middle by Proposition 12.1. If $T^i$ is exact, then $T^i$ is both left exact and right exact. By Proposition 12.5, right exactness implies $T^i(M) \cong T^i(A) \otimes M$ for all $A$-modules $M$. Therefore $T^i$ is exact if and only if $T^i(A)$ is flat. But $T^i(A)$ is a finitely generated $A$-module (since $T^i(A) = H^i(X, \mathcal{F})$ and $\mathcal{F}$ is coherent and $f$ is projective), so this is equivalent to being locally free, hence projective.

Conversely, if $T^i$ is right exact, then by Proposition 12.5 we have $T^i(M) \cong T^i(A) \otimes M$ for all $M$. If furthermore $T^i(A)$ is projective, then $T^i(A)$ is flat, so $T^i(M) \cong T^i(A) \otimes M$ is exact in $M$, which means $T^i$ is exact. Note that right exactness combined with exactness in the middle (Proposition 12.1) already implies left exactness.
