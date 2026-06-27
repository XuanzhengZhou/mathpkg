---
role: proof
locale: en
of_concept: degenerate-chain-characterization
source_book: gtm040
source_chapter: "9"
source_section: "8"
---
If the chain is degenerate, then for each reference point $0$, $k(E) = 0$ for all $E$. In particular, by Proposition 9-89, there can be no $j$ with both ${}^0\lambda_j > 0$ and $\hat{\lambda}_j^E > 0$. This forces the condition on hitting probabilities.

Conversely, if ${}^0\lambda_j = 0$ or ${}^0\hat{\lambda}_j = 0$ for all states $j$, then $k(E) = 0$ for all $E \in \mathcal{L}_0$ (by Proposition 9-89 since $\lambda_j^E \leq {}^0\lambda_j$). And
$$k(\{j\}) = \frac{1}{\alpha_j} (G_{0j} - C_{0j}) = \frac{{}^0N_{jj}}{\alpha_0} ({}^0\lambda_j - {}^j\hat{\lambda}_0).$$
But ${}^0\lambda_j$ and ${}^j\hat{\lambda}_0$ are either both $0$ or both $1$. Hence $k(\{j\}) = 0$. Thus the converse follows from Lemma 9-100.
