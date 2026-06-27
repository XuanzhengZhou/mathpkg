---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.2"
proof_technique: basis-multiplication
locale: en
content_hash: ""
written_against: ""
---
Let $U$ be a basis of $T$ over $S$ and $V$ a basis of $S$ over $R$. Show $\{vu \mid v \in V, u \in U\}$ is a basis of $T$ over $R$. Spanning: any $t = \sum s_i u_i$ with $s_i \in S$, each $s_i = \sum r_{ij} v_j$, so $t = \sum \sum r_{ij} v_j u_i$. Linear independence: if $\sum \sum r_{ij}(v_j u_i) = 0$, let $s_i = \sum r_{ij} v_j$. Then $\sum s_i u_i = 0$, so each $s_i = 0$ (independence of $U$), then each $r_{ij} = 0$ (independence of $V$). Thus $\dim_R T = |U||V| = (\dim_S T)(\dim_R S)$.
