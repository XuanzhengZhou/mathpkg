---
role: proof
locale: en
of_concept: bounded-return-probability-before-hitting
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** If ${}_j\bar{H}_{ii} = 1$, then starting from $i$, the process returns to $i$ infinitely often before hitting $j$ with probability one (by conclusion (2) of Lemma 4-19 with $k \to \infty$, or by Proposition 2-6). This contradicts the relation $R(i,j)$, which guarantees a positive probability $H_{ij} > 0$ of reaching $j$. Therefore ${}_j\bar{H}_{ii} < 1$.

For the second half of the lemma (bounding ${}_jN_{ii}$), we have, as in Proposition 4-20,
$${}_jN_{ii} = \sum_{n=0}^{\infty} ({}_j\bar{H}_{ii})^n < +\infty,$$
since ${}_j\bar{H}_{ii} < 1$.
