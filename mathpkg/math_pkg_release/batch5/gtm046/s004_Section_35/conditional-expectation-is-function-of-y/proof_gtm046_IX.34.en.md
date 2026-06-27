---
role: proof
locale: en
of_concept: conditional-expectation-is-function-of-y
source_book: gtm046
source_chapter: "IX"
source_section: "34"
---

First verify for $g=I_{A'}$: set $A=Y^{-1}(A')$, then $g(Y)=I_A$ and $\int_{B'}I_{A'}dP'_Y=P'_Y(A'B')=P_Y(AB)=\int_B I_A dP_Y$. Extend to simple functions by linearity, then to nonnegative measurable $g$ by monotone convergence, then to general $g$ by decomposition.

Now let $\varphi$ be the indefinite integral of $X$, define $\varphi'(B')=\varphi(B)$ with $B=Y^{-1}(B')$. Then $\varphi'$ is $\sigma$-additive and $P'_Y$-continuous. Radon-Nikodym gives $g$ with $\int_{B'}g dP'_Y=\varphi'(B')=\int_B X dP$. Since $\int_B X dP=\int_B(E^Y X)dP$, the first part gives $\int_B g(Y)dP_Y=\int_{B'}g dP'_Y=\int_B(E^Y X)dP$. The indefinite integrals of $g(Y)$ and $E^Y X$ coincide, so $E^Y X=g(Y)$ a.s.
