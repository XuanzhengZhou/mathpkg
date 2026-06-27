---
role: proof
locale: en
of_concept: proposition-5-8-quasi-coherent-pushforward-pullback
source_book: gtm052
source_chapter: "II"
source_section: "5"
---

(a) The question is local on both $X$ and $Y$, so we can assume $X$ and $Y$ both affine. In this case the result follows from (5.5) and (5.2e).

(b) In the noetherian case, the same proof works for coherent sheaves.

(c) Here the question is local on $Y$ only, so we may assume that $Y$ is affine. Then $X$ is quasi-compact (under either hypothesis) so we can cover $X$ with a finite number of open affine subsets $U_i$. In the separated case, $U_i \cap U_j$ is again affine (Ex. 4.3). Call it $U_{ij}$. In the noetherian case, $U_i \cap U_j$ is at least quasi-compact, so we can cover it with a finite number of open affine subsets $U_{ijk}$. Now for any open subset $V$ of $Y$, giving a section $s$ of $\mathcal{F}$ over $f^{-1}V$ is the same as giving a compatible family of sections over the intersections. Using the quasi-coherence property and the sheaf condition, one shows that $f_*\mathcal{F}$ corresponds to the $A$-module $\Gamma(X, \mathcal{F})$ on $Y = \operatorname{Spec} A$.
