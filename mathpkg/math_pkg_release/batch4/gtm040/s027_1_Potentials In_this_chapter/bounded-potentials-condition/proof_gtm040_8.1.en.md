---
role: proof
locale: en
of_concept: bounded-potentials-condition
source_book: gtm040
source_chapter: "8"
source_section: "1"
---

The dual of $N_{ij} \leq N_{jj}$ is $N_{ij} \leq (N_{ii}/\alpha_i)\alpha_j$. If $\alpha_i \geq k N_{ii}$, then
$$|g_i| \leq \sum_j N_{ij}|f_j| \leq \frac{N_{ii}}{\alpha_i} \sum_j \alpha_j|f_j| \leq \frac{1}{k} \sum_j \alpha_j|f_j|.$$
Thus $g$ is bounded. Now suppose $\lim_i N_{ij} = 0$. By Proposition 8-6 we may assume $g$ is a pure potential. Define $h_j^{(i)} = N_{ij}/\alpha_j$ and a measure $\mu_j = \alpha_j f_j$. Then $\mu$ is a finite measure, and $h_j^{(i)} \leq N_{jj}/\alpha_j \leq 1/k$ is bounded independently of $i$ and $j$. Hence, by dominated convergence,
$$\lim_i g_i = \lim_i \sum_j h_j^{(i)}\mu_j = \sum_j (\lim_i N_{ij})f_j = 0.$$
