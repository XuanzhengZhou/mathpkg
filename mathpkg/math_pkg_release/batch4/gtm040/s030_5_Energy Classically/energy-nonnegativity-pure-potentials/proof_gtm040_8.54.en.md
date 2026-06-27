---
role: proof
locale: en
of_concept: energy-nonnegativity-pure-potentials
source_book: gtm040
source_chapter: "8"
source_section: "5"
---

We apply Proposition 8-53. The matrices involved are finite matrices so that distributivity and associativity hold. Hence

$$\mathbf{I}(g) = \nu_E g_E - \nu_E P^E g_E$$
$$= \frac{1}{2} \sum_{i \in E} \left[ \alpha_i g_i^2 + \alpha_i g_i^2 + \sum_{j \in E} \left( -2\alpha_i P^E_{ij} g_i g_j \right) \right]$$
$$= \frac{1}{2} \sum_{i \in E} \left[ \alpha_i \left( 1 - \sum_{j \in E} P^E_{ij} \right) g_i^2 + \left( \alpha_i - \sum_{k \in E} \alpha_k P^E_{ki} \right) g_i^2 \right]$$
$$+ \sum_{j \in E} \left( \alpha_i P^E_{ij} g_i^2 - 2\alpha_i P^E_{ij} g_i g_j + \alpha_i P^E_{ij} g_j^2 \right]$$
$$= \frac{1}{2} \sum_{i \in E} \left[ \left( \alpha_i m_i + \pi_i \right) g_i^2 + \sum_{j \in E} \alpha_i P^E_{ij} \left( g_i - g_j \right)^2 \right].$$

Since $P^E$ is a transition matrix and $\alpha_E$ is $P^E$-superregular, $m$ and $\pi$ are non-negative. Hence $\mathbf{I}(g) \geq 0$.
