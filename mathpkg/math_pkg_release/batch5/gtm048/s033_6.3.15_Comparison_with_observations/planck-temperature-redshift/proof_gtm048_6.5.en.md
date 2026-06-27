---
role: proof
locale: en
of_concept: planck-temperature-redshift
source_book: gtm048
source_chapter: "6"
source_section: "6.5"
---

Suppose $y \in \mathbb{R}^3 \times \mathcal{E}$ and $Y \in \mathcal{L}_y^+$. Let $\lambda: \mathcal{F} \rightarrow M$ be the inextendible freely falling photon for which $\lambda 0 = y$ and $\lambda_* 0 = Y$.

Then there is a unique $b \in \mathbb{R}$ such that $u^4 \lambda b = a$, and $\lambda[0, b] \subset \mathbb{R}^3 \times \mathcal{E}$ (Exercise 6.4.8b).

Since $F$ is conserved in $\mathbb{R}^3 \times \mathcal{E}$, we have
$$
F(y, Y) = F(\lambda b, \lambda_* b).
$$

Now since $F$ is Planck for $(\lambda b, \partial_4 \lambda b)$ by hypothesis,
$$
F(\lambda b, \lambda_* b) = P(e'/kT_a),
$$
where $P$ is the Planck function (Example 5.5.4), $k$ is the Boltzmann constant, and $e'$ is the energy $(\lambda b, \partial_4 \lambda b)$ measures for $\lambda$.

Hence $F(y, Y) = P(e'/kT_a)$.

But from Exercise 6.0.17d,
$$
g(\lambda_* b, \partial_4 \lambda b) = \frac{R(u^4 y)}{R(a)} g(\partial_4 y, Y),
$$
so
$$
e' = -g(\lambda_* b, \partial_4 \lambda b) = \frac{R(u^4 y)}{R(a)} e,
$$
where $e$ is the energy $(y, \partial_4 y)$ measures for $\lambda$.

Therefore,
$$
F(y, Y) = P\left( \frac{R(u^4 y)}{R(a)} \cdot \frac{e}{k T_a} \right) = P\left( \frac{e}{k \cdot \frac{R(a)}{R(u^4 y)} T_a} \right),
$$
which shows that $F$ is Planck with temperature $T = \frac{R(a)}{R(u^4 y)} T_a$ for $(y, \partial_4 y)$.
