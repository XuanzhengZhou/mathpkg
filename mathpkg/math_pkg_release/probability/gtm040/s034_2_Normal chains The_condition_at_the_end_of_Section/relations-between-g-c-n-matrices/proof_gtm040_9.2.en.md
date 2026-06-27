---
role: proof
locale: en
of_concept: relations-between-g-c-n-matrices
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

The first two expressions follow directly from Theorem 9-7 and Definition 9-24. Theorem 9-7 provides identities for the finite-$n$ quantities $N_{ij}^{(n)}$; taking limits as $n \to \infty$ and using the definitions of $G_{ij}$ and $C_{ij}$ as the limiting differences yields the stated formulas.

Specifically, for the first identity, Theorem 9-7 gives an expression relating $N_{ij}^{(n)}$ to $N_{ik}^{(n)}$, $N_{kj}^{(n)}$, and $N_{kk}^{(n)}$. Factoring the $\alpha$-weights as in Definition 9-24 and taking limits produces
$$G_{ik} \frac{\alpha_j}{\alpha_k} + G_{kj} - G_{ij} = {}^kN_{ij}.$$

The second identity for $C$ follows by the same reasoning applied to the unweighted differences. For the diagonal identities (third and fourth), set $i = j$ in the first two expressions, noting that $G_{ii} = C_{ii} = 0$ (by Lemma 9-25) and ${}^kN_{ii}$ is the diagonal entry of the fundamental matrix relative to $k$.
