---
role: proof
locale: en
of_concept: lemma-9-62
source_book: gtm040
source_chapter: "9"
source_section: "62"
---

**Proof:** The first result is a restatement of Proposition 9-58. Since $i\hat{N}_{jj} = iN_{jj}$, we have $S_{ij} = \hat{S}_{ij}; S_{ij} = S_{ji}$ by definition. Finally, the last two results follow from the identities

$$M_{ij} = \frac{C_{ij}}{\alpha_j} = \frac{1}{\alpha_i} j\hat{\nu}_i = j\hat{\lambda}_i S_{ji},$$

which are consequences of Theorem 9-49 and Lemma 9-25.

From this lemma we see that

$$\hat{M}_{ij} = j\lambda_i S_{ji} = j\lambda_i \hat{S}_{ij} = j\lambda_i (M_{ij} + M_{ji}),$$

a formula which gives a means of computing $\hat{M}$ from quantities in $P$. Moreover, from Proposition 9-61 we have

$$j\hat{\lambda}_i = \alpha_i \bar{M}_{i,(i,j)},$$

so that the lemma gives, on multiplication by $S_{ji},$

$$M_{ij} = j\hat{\lambda}_i S_{ji} = \alpha_i \frac{iN_{ii}}{\alpha_i} \bar{M}_{i,(i,j)}$$

or

$$M_{ij} = jN_{ii} \bar{M}_{i,(i,j)}.$$
