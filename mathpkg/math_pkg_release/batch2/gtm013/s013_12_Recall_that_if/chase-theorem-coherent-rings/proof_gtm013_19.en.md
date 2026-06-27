---
role: proof
locale: en
of_concept: chase-theorem-coherent-rings
source_book: gtm013
source_chapter: "5"
source_section: "19"
---

(a) $\Rightarrow$ (d): First show via (19.19) (the Equational Criterion) that $(R^{(B)})^A$ is flat for all sets $A, B$ when $R$ is left coherent. Given $v_j \in (R^{(B)})^A$ and $a_j \in R$ with $\sum v_j a_j = 0$, let $F$ be free on $x_1, \ldots, x_n$ and $K = \operatorname{Ker}(F \to \sum R a_j)$. By left coherence, $K = \sum_{i=1}^m R k_i$ with $k_i = \sum c_{ij} x_j$. By analyzing the coordinates in $(R^{(B)})^A$, one finds $u_i$ such that $v_j = \sum u_i c_{ij}$, satisfying the equational criterion.

(d) $\Rightarrow$ (c) $\Rightarrow$ (b) are straightforward.

(b) $\Rightarrow$ (a): Given a finitely generated left ideal $I$ and a free presentation $0 \to K \to F \to I \to 0$ with $F$ free of finite rank, apply (19.18) to the product of flat modules argument. The condition $KI = K \cap FI$ forces $K$ to be finitely generated.
