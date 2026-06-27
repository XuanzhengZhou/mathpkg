---
role: proof
locale: en
of_concept: continuous-function-on-curve-is-integrable
source_book: gtm003
source_chapter: "Appendix 1"
source_section: "Vector-Valued Holomorphic Functions"
---

Since $f: \delta \to E$ is continuous and $\delta$ is compact, the image $f(\delta)$ is compact in $E$. By hypothesis, the closed, convex, circled hull of $f(\delta)$ is compact in $E$. For each $x' \in E'$, the scalar function $\zeta \mapsto \langle f(\zeta), x' \rangle$ is continuous on $\delta$ and hence Riemann integrable. It remains to verify that the linear form

$$x' \mapsto \int_\delta \langle f(\zeta), x' \rangle \, d\zeta$$

is $\sigma(E', E)$-continuous. The compactness of the closed convex circled hull of $f(\delta)$ implies that the set $\{\int_\delta \langle f(\zeta), \cdot \rangle \, d\zeta\}$ lies in the polar of an equicontinuous set, yielding the required continuity.
