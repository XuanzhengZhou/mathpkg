---
role: proof
locale: en
of_concept: properties-of-c-and-g-matrices
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

By Lemma 9-2, the quantities $N_{jj}^{(n)} - N_{ij}^{(n)}$ and $N_{ii}^{(n)} \alpha_j/\alpha_i - N_{ij}^{(n)}$ are bounded and non-negative for all $n$. Therefore, whenever the limits defining $C_{ij}$ and $G_{ij}$ exist, the limits are finite and non-negative.

For $i = j$, the defining expressions are identically zero for every $n$, so $C_{ii} = G_{ii} = 0$.

The duality relation follows from the definition of the dual chain: $\hat{N}_{ij}^{(n)} = N_{ji}^{(n)} \alpha_j / \alpha_i$. Substituting into the definition of $\hat{G}_{ij}$ yields
$$\hat{G}_{ij} = \lim_n \left( \hat{N}_{ii}^{(n)} \frac{\alpha_j}{\alpha_i} - \hat{N}_{ij}^{(n)} \right) = \lim_n \left( N_{ii}^{(n)} \frac{\alpha_j}{\alpha_i} - N_{ji}^{(n)} \frac{\alpha_j}{\alpha_i} \right) = \frac{\alpha_j}{\alpha_i} \lim_n (N_{ii}^{(n)} - N_{ji}^{(n)}) = \frac{\alpha_j}{\alpha_i} C_{ji}.$$

The connection to ${}^0\nu_j$ follows from the identity $G_{0j} = {}^0\nu_j$ (established in Lemma 9-23's proof context), and similarly the dual version yields ${}^0\hat{\nu}_j$.
