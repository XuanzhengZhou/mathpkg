---
role: proof
locale: en
of_concept: relative-implies-absolute-integral-invariant
source_book: gtm060
source_chapter: "7"
source_section: "38"
---

Let $c$ be a $k+1$-chain. Then

$$\int_c d\omega \stackrel{1}{=} \int_{\partial c} \omega \stackrel{2}{=} \int_{g\partial c} \omega \stackrel{3}{=} \int_{\partial gc} \omega \stackrel{4}{=} \int_{gc} d\omega.$$

Equality 1 holds by Stokes' formula, equality 2 by the definition of a relative integral invariant (since $\partial c$ is a closed $k$-chain), equality 3 by the naturality of the boundary operator under the map $g$ (i.e., $g(\partial c) = \partial(gc)$), and equality 4 again by Stokes' formula. Thus $\int_c d\omega = \int_{gc} d\omega$ for every $(k+1)$-chain $c$, which means $d\omega$ is an absolute integral invariant of $g$.
