---
role: proof
locale: en
of_concept: euler-characteristic-handles-crosscaps
source_book: gtm047
source_chapter: "22"
source_section: "1"
---

Using the open cell-decomposition of $M$ induced by the classification (as in Figure 22.10), choose a point $v$ in $\operatorname{Int} D$ as the single vertex. The $1$-skeleton consists of $2h + m$ edges: $2h$ edges forming $h$ handles (each handle contributes two edges meeting at the vertex) and $m$ edges for the $m$ cross-caps. The single $2$-face is the complement of the $1$-skeleton in $M$.

Thus $V = 1$, $E = 2h + m$, $F = 1$, and
$$\chi(M) = V - E + F = 1 - (2h + m) + 1 = 2 - (2h + m).$$
$\square$
