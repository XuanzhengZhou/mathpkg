---
role: proof
locale: en
of_concept: prop-s006-proposition-2
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: When either $x = 0$ or $y = 0$ or both we get $g(x,y) = A(0,0) = 0$, as we should, according to D10.1. When $x = y$, $g(x,y) = g(x,x)$ is the expected number of returns to $x$ before visiting 0, or

(2) $g(x,x) = 1 + \sum_{k=1}^{\infty} (1 - \Pi)^k = \Pi^{-1},$

where $\Pi = \Pi_{(0,x)}(x,0)$. Therefore the result of P6 is verified in this case by consulting the formula for $\Pi$ in P5. Finally, when $x \neq y$, and neither is 0,

(3) $g(x,y) = H_{(0,y)}(x,y)g(y,y)$

by an obvious probabilistic argument. But now the substitution of the formula (1) for $H_B(x,y)$ and of equation (2) for $g(y,y)$ into equation (3) completes the proof.

We need one last auxiliary result before proceeding to draw conclusions from P4 for finite sets $B$ of arbitrary size. It is a subtler result than perhaps appears at first sight—in fact there are one-dimensional aperiodic random walks for which it is false, as we shall discover in Chapter VII.
