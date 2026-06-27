---
role: proof
locale: en
of_concept: interior-point-extension-positive-form
source_book: gtm003
source_chapter: "V"
source_section: "5"
---

If $f_0$ is the linear form in question and $x_0 \in M$ is an interior point of $C$, choose a convex $0$-neighborhood $U$ in $E$ such that $x_0 + U \subset 2x_0 - C$. Then $\operatorname{Re} f_0$ is bounded above on $M \cap (U - C)$, for we have $M \cap (U - C) \subset (x_0 - C) \cap M$. Indeed, if $y \in U - C$, then there exists $u \in U$ and $c \in C$ with $y = u - c$. From $x_0 + U \subset 2x_0 - C$, we have $u \in x_0 - C$, so $y = u - c \in x_0 - C - C = x_0 - C$. Since $f_0$ is positive on $M$, it is bounded above by $f_0(x_0)$ on $M \cap (x_0 - C)$. The condition of Theorem 5.4 is thus satisfied, yielding the desired extension.
