---
role: proof
locale: en
of_concept: conditional-expectation-as-function
source_book: gtm046
source_chapter: "VIII"
source_section: "27.3"
---

If $\varphi$ is the indefinite integral of $X$ and $\varphi'$ on $\mathcal{B}'_Y$ is defined by $\varphi'(B') = \varphi(B)$ where $B' \in \mathcal{B}'_Y$ and $B = Y^{-1}(B')$, then $\varphi'$ is $\sigma$-additive and $P'_Y$-continuous. The extended Radon-Nikodym theorem applies to $\varphi'$ and $P'_Y$ and defines a measurable function $g$ on $(\Omega', \mathcal{B}'_Y)$ by

$$\int_{B'} g \, dP'_Y = \varphi'(B') = \int_B X \, dP.$$

Since $\int_B X \, dP = \int_B (E^Y X) \, dP$, it follows that $\int_B g(Y) \, dP_Y = \int_B (E^Y X) \, dP$, so the indefinite integrals of the $\mathcal{B}_Y$-measurable functions $g(Y)$ and $E^Y X$ coincide, proving the assertion.
