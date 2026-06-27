---
role: proof
locale: en
of_concept: generating-cone-positive-element-characterization
source_book: gtm036
source_chapter: "23"
source_section: "ORDERED LINEAR SPACES"
---

If $C$ generates $E$, then for each $x \in E$ there exist $u, v \in C$ such that $x = u - v$. Then $u - x = v \in C$, so $u - x \geq 0$, i.e., $u \geq x$, and $u \geq 0$ since $u \in C$.

Conversely, if for each $x \in E$ there exists $u \in C$ such that $u \geq x$ (and $u \geq 0$ automatically since $u \in C$), then $x = u - (u - x)$. Now $u - x \geq 0$ because $u \geq x$, so $u - x \in C$. Since $u \in C$ and $u - x \in C$, we have $x = u - (u - x) \in C - C$. This holds for every $x \in E$, hence $C - C = E$.
