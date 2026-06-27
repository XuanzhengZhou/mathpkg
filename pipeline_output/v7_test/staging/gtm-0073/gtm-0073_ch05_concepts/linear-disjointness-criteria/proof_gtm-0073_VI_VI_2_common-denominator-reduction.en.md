---
role: proof
source_book: gtm-0073
chapter: VI
section: "VI.2"
proof_technique: common-denominator-reduction
locale: en
content_hash: ""
written_against: ""
---
(i) $\Rightarrow$ (ii) and (i) $\Rightarrow$ (iii) are trivial.

(ii) $\Rightarrow$ (i): Let $X = \{u_1, \ldots, u_n\} \subset E$ be linearly independent over $K$.
Since $u_i \in E = K(R)$, each $u_i = c_i d_i^{-1}$ where $c_i, d_i \in R$ and $d_i \neq 0$.
Let $d = d_1 d_2 \cdots d_n$. Then $du_i \in R$ for all $i$. The set $\{du_1, \ldots, du_n\}$
is linearly independent over $K$ (multiplying by $d \neq 0$ preserves independence),
hence by (ii) it is linearly independent over $F$. Since $d^{-1} \in E \subset C$,
$\{u_1, \ldots, u_n\}$ is linearly independent over $F$.

(iii) $\Rightarrow$ (i): Let $U$ be a basis of $R$ over $K$ which is linearly independent over $F$.
Since $R$ generates $E$, $U$ spans $E$ over $K$ and is $K$-linearly independent, hence a $K$-basis
of $E$. By hypothesis $U$ is linearly independent over $F$. Since any $K$-linearly independent
subset of $E$ can be extended to a basis of $E$ over $K$, and $U$ serves as such a basis,
the result follows.
