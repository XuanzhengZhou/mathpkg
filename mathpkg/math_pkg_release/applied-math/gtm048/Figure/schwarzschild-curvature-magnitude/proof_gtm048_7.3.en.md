---
role: proof
locale: en
of_concept: schwarzschild-curvature-magnitude
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

Let $\tilde{T}$ be the $(4,0)$-tensor field physically equivalent on $U$ to $T$ in Proposition 7.3.2; let $A$ be the $(2,0)$-tensor field physically equivalent to $P^* \zeta$. Using the Lorentzian metric $g$ we find that the $(4,0)$ tensor field $\tilde{R}$ physically equivalent to $\hat{R}$ on $U$ is given by

$$\tilde{R} = \frac{4\mu}{r^3}\Big[2\Big(\frac{\partial}{\partial r} \wedge \frac{\partial}{\partial t}\Big) \otimes \Big(\frac{\partial}{\partial r} \wedge \frac{\partial}{\partial t}\Big) - r^{-2}\tilde{T} + 2r^{-4}A \otimes A\Big].$$

Now the curvature magnitude $f$ is obtained by taking the appropriate four traces of $\tilde{R} \otimes \tilde{R}: M \to T_4^4 M$. Computing these traces using the algebraic expression above yields

$$f = \frac{144\mu^2}{r^6}.$$

The equivalence between escape to infinity and $r \to \infty$ follows directly: since $f = 144\mu^2/r^6$, we have $\lim_{u \to b} f \circ \gamma(u) = 0$ iff $\lim_{u \to b} r \circ \gamma(u) = \infty$.
