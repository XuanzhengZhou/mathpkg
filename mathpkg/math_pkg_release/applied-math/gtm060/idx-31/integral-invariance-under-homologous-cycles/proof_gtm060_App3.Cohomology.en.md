---
role: proof
locale: en
of_concept: integral-invariance-under-homologous-cycles
source_book: gtm060
source_chapter: "Appendix 3"
source_section: "Cohomology and homology"
---
Since $a$ and $b$ are homologous, there exists a $(k+1)$-chain $c_{k+1}$ such that $a - b = \partial c_{k+1}$. Then
$$\int_a \omega^k - \int_b \omega^k = \int_{a-b} \omega^k = \int_{\partial c_{k+1}} \omega^k.$$
By Stokes' theorem, $\int_{\partial c_{k+1}} \omega^k = \int_{c_{k+1}} d\omega^k$. Since $\omega^k$ is closed, $d\omega^k = 0$, and thus the integral vanishes. Hence $\int_a \omega^k = \int_b \omega^k$.
