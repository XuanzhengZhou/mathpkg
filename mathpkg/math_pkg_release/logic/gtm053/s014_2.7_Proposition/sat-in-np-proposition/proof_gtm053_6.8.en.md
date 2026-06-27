---
role: proof
locale: en
of_concept: sat-in-np-proposition
source_book: gtm053
source_chapter: "6"
source_section: "6.8"
---
Let $E' = \{(u,v) \mid b_u(v) = 1\} \subset U \times (\oplus_{i=1}^{\infty} \mathbf{F}_2)$. Clearly, SAT is the full projection of $E'$. One verifies that $E' \in P$: we can calculate $b_u(v)$ performing $O(Nm)$ Boolean multiplications and additions, where $N$ is the number of clauses and $m$ the number of variables. The projection to SAT can be replaced by a polynomially truncated projection, because we need only check $v$ of bit size $|v| \leq m$. Thus SAT $\in$ NP by definition.
