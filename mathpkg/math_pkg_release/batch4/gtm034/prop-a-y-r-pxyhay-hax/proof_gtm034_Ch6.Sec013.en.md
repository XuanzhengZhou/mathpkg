---
role: proof
locale: en
of_concept: prop-a-y-r-pxyhay-hax
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: Part (a) follows from the first identity in the proof of P1 by simply summing $y$ over the set $A$. Part (b), on the other hand, is just the result of P1 when $x \in A$, for then

$$H_A(x,y) = \delta(x,y) = \sum_{t \in A} G(x,t)[\delta(t,y) - \Pi_A(t,y)]$$

To finish up, one looks at the reversed random walk with $G^*(x,y) = G(y,x)$, $\Pi^*(x,y) = \Pi(y,x)$, so that when $x \in A$, $y \in A$,

$$\delta(x,y) = \sum_{t \in A} G^*(x,t)[\delta(t,y) - \Pi_A^*(t,y)]$$

$$= \sum_{t \in A} [\delta(y,t) - \Pi_A(y,t)]G(t,x).$$

Since $\delta(x,y) = \delta(y,x)$ the proof of P2 is complete.

Another corollary of P1, but a far deeper and more important one than P2, concerns the hitting probabilities $H_A(x,y)$ when $A$ is a finite subset of $R$. Then one can assert
