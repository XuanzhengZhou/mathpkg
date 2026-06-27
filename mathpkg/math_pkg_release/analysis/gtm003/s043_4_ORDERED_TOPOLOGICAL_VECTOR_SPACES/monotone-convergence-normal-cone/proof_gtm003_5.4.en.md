---
role: proof
locale: en
of_concept: monotone-convergence-normal-cone
source_book: gtm003
source_chapter: "V"
source_section: "4"
---

Without loss of generality we can suppose that $S$ is directed for $\geq$, and that $\lim \mathfrak{J}(S) = 0$ for $\sigma(E, E')$; it follows now from (4.2) that $S \subset C$. Assume that the assertion is false; then there exists a $0$-neighborhood $U$ in $E$ that contains no section of $S$, and since $C$ is normal we can suppose that $U$ is convex and $C$-saturated. Since $x \in S \cap U$ implies $S_x \subset U$, it follows that $S \cap U = \varnothing$; moreover, $(S + C) \cap U = \varnothing$, since $U$ is $C$-saturated, and $S + C$ is convex, since it is the union of the family $\{x + C : x \in S\}$ of convex sets which is directed under inclusion. Hence by (II, 9.2) $U$ and $S$ can be separated by a closed real hyperplane in $E$, and this contradicts the weak convergence of $\mathfrak{J}(S)$ to $0$.
