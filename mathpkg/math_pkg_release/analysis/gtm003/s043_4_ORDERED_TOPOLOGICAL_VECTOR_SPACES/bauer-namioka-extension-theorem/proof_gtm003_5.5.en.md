---
role: proof
locale: en
of_concept: bauer-namioka-extension-theorem
source_book: gtm003
source_chapter: "V"
source_section: "5"
---

It suffices to consider the case $\mathbb{K} = \mathbb{R}$. If $f$ is a linear extension of $f_0$ to $E$ which is positive and continuous and if $U$ is a convex $0$-neighborhood such that $f(U) \subset [-1, 1]$, then $f$ is bounded above by $1$ on $U - C$, hence $f_0 = f|_M$ is bounded above on $M \cap (U - C)$. Conversely, assume that $\operatorname{Re} f_0$ is bounded above on $M \cap (U - C)$ for some convex $0$-neighborhood $U$ in $E$. Let $p$ be the gauge (Minkowski functional) of $U - C$; then $p$ is a sublinear functional on $E$, and $f_0 \leq \alpha \cdot p$ on $M$ for some $\alpha > 0$. By the Hahn-Banach theorem, $f_0$ extends to a linear form $f$ on $E$ such that $f \leq \alpha \cdot p$ on $E$. This inequality implies that $f(x) \leq 0$ for $x \in -C$ (since $p(x) = 0$ for $x \in -C$), hence $f$ is positive. Moreover, $f$ is bounded above by $\alpha$ on $U$ (since $U \subset U - C$ implies $p \leq 1$ on $U$), hence $f$ is continuous.
