---
role: proof
locale: en
of_concept: asymptotic-properties-of-mean-first-passage-times
source_book: gtm040
source_chapter: "9"
source_section: "3"
---

By Lemma 9-62,
$$\frac{M_{ji}}{M_{ij}} = \frac{\,^{i}\!\hat{\lambda}_j}{\,^{j}\!\hat{\lambda}_i}.$$
By Proposition 9-60 the numerator tends to 0 and the denominator tends to 1. Hence the first assertion follows. Therefore, for all but finitely many states $j$,
$$2M_{ij} \geq M_{ji} + M_{ij} \geq \bar{M}_{jj} = \frac{1}{\alpha_j}.$$
Since $\sum \alpha_j < \infty$, $\alpha_j \to 0$ and $M_{ij} \to \infty$. Finally
$$(C_{ij} - G_{ij})/\alpha_j = M_{ij} - \frac{\,^{i}\!\nu_j}{\alpha_j} = M_{ij} - \frac{1}{\alpha_j} \,^{i}\!\lambda_j \,^{i}\!N_{jj}$$
$$= M_{ij} - \,^{i}\!\lambda_j S_{ij} = M_{ij} - \,^{i}\!\lambda_j (M_{ij} + M_{ji})$$
$$= M_{ij} \left[ 1 - \,^{i}\!\lambda_j \left( 1 + \frac{M_{ji}}{M_{ij}} \right) \right].$$
The factor in brackets tends to 1 since $^{i}\!\lambda_j \to 0$ and $M_{ji}/M_{ij} \to 0$. Thus the third assertion follows from $M_{ij} \to \infty$.
