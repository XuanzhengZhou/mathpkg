---
role: exercise
locale: en
chapter: "5"
section: "5.4"
exercise_number: 1
---
# Exercise 5.4

Prove Lemma 5.4: Let $\Omega = \{ z \in \mathbb{C}^n \mid |z_j| < R_j,\; j = 1, \ldots, n \}$ be a polydisk. Assume $f \in C^1(\Omega)$ satisfies

$$\frac{\partial f}{\partial \bar{z}_j} = 0, \qquad j = 1, \ldots, n,$$

on $\Omega$. Then $f$ is given by an absolutely convergent power series

$$f(z) = \sum_{\nu} A_\nu z^\nu$$

where $\nu = (\nu_1, \ldots, \nu_n)$ ranges over all multi-indices of nonnegative integers, $z^\nu = z_1^{\nu_1} \cdots z_n^{\nu_n}$, and the series converges uniformly on every compact subset of $\Omega$.

*Hint.* Use the iterated Cauchy integral formula: fix all variables but one, apply the one-variable Cauchy formula on circles, then iterate over all $n$ coordinates. Expand each factor $1/(\zeta_j - z_j)$ as a geometric series and integrate term by term.
