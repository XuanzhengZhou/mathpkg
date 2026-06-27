---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.2"
proof_technique: matrix-rank-exchange
locale: en
content_hash: ""
written_against: ""
---
Assume $E$ and $F$ are linearly disjoint over $K$ and suppose $X \subset F$ is linearly
independent over $K$ but linearly dependent over $E$. Then there exist $u_1, \ldots, u_n \in X$
and not-all-zero $e_1, \ldots, e_n \in E$ such that $\sum e_i u_i = 0$.
Choose such a relation with the minimal number $t$ of nonzero $e_i$.
Renumbering, let $e_1, \ldots, e_t \neq 0$ and $e_{t+1} = \cdots = e_n = 0$.
Then $u_1 = -\sum_{i=2}^{t} e_i e_1^{-1} u_i$, so $u_1$ is in the $E$-span of $\{u_2, \ldots, u_t\}$.
Now consider a basis of $E$ over $K$ and express $e_i$ in terms of it. Since $\{u_2, \ldots, u_n\}$
is linearly independent over $E$ (by minimality), a linear algebra argument yields a contradiction
to the linear disjointness assumption. Therefore $X$ is linearly independent over $E$,
so $F$ and $E$ are linearly disjoint over $K$.
