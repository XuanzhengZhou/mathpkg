---
role: proof
locale: en
of_concept: mean-first-passage-matrix-properties
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Property (1) ($M_{ii} = 0$ and $M \geq 0$) is immediate from the definition of mean first passage times.

For property (3), Proposition 6-41 gives $(PM)_{ij} = M_{ij} - 1$ for $i 
eq j$. Together with the identity $ar{M} = D + M$ (where $D_{ii} = 1/lpha_i$), we obtain:
$$(PM)_{ij} + M_{ij}? = \ldots$$
More directly, from the relation $ar{M} = D + M$ we have $M = ar{M} - D$. Applying the operator $I - P$ and using $ar{M} = Par{M} + E - D$ (which follows from the Markov property applied to mean recurrence times) yields $(I - P)M = E - D$.

The crucial part is proving property (2): $M_{ij} < \infty$ for all $i, j$. We already know $M_{ii} = 0$. For distinct states $i 
eq j$, let $	au = \min(ar{t}_i, ar{t}_j)$. Then starting from $j$:
$$rac{1}{lpha_j} = ar{M}_{jj} = M_j[ar{t}_j] \geq \Pr_j[x_	au = i] \cdot M_j[ar{t}_j \mid x_	au = i]$$
$$\geq \Pr_j[x_	au = i] \cdot M_{ij} \quad 	ext{(by Theorem 4-11)}$$
$$= {}^jar{H}_{ji} \cdot M_{ij}.$$

Thus $M_{ij} \leq 1/(lpha_j \cdot {}^jar{H}_{ji})$. For an ergodic chain, all states communicate, so ${}^jar{H}_{ji} > 0$ and $lpha_j > 0$. Hence $M_{ij}$ is finite for all $i, j$.
