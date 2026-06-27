---
role: proof
locale: en
of_concept: symmetric-random-walk-normality
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

Put $j$ for $k$ and $i$ for $i$ and $j$ in Theorem 9-7. We obtain
$$\lim_{n \to \infty} \left[ \left(N_{jj}^{(n)} - N_{ij}^{(n)}\right) \frac{\alpha_i}{\alpha_j} + \left(N_{ii}^{(n)} - N_{ji}^{(n)}\right) \right] = {}^jN_{ii}.$$

Now $\alpha_i = \alpha_j$ and $N_{ii}^{(n)} = N_{jj}^{(n)}$ in sums of independent random variables, and $N_{ij}^{(n)} = N_{ji}^{(n)}$ in a symmetric process. Hence
$$\lim_n \left[ 2\left(N_{jj}^{(n)} - N_{ij}^{(n)}\right) \right] = {}^jN_{ii}.$$

Therefore $C_{ij} = \frac{1}{2}\,{}^jN_{ii}$. By Theorem 9-26, $C_{j0}$ exists, so condition (2) of Theorem 9-26 is satisfied and $P$ is normal. Moreover, $G_{ij} = C_{ij} = \frac{1}{2}\,{}^jN_{ii}$ by the symmetry and the relation established in Theorem 9-26. Finally, ${}^i\lambda_j = {}^i\nu_j / {}^iN_{jj} = G_{ij} / {}^iN_{jj} = \frac{1}{2}$.
