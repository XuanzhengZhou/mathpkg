---
role: proof
locale: en
of_concept: "infinite-definable-sets-properly-extend"
source_book: gtm022
source_chapter: "VIII"
source_section: "4"
---
Proof. If $u = \{u_1, \ldots, u_n\}$ is finite, then the formula $u(x) = (x = u_1) \lor \cdots \lor (x = u_n)$ describes $u$, and $*u = u$. If $u$ is infinite, define the concurrent binary relation $\rho(x,y) = (x \in u) \land (y \in u) \land (x \neq y)$ with $D_\rho = u$. In the enlargement, there exists $b_\rho$ with $\rho(x, b_\rho)$ for all $x \in D_\rho$, so $b_\rho \in *u$ but $b_\rho \notin u$. $\square$
