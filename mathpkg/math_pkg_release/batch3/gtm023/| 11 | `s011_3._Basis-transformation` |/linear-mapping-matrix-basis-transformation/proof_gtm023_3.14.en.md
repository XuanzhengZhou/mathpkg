---
role: proof
locale: en
of_concept: linear-mapping-matrix-basis-transformation
source_book: gtm023
source_chapter: "I"
source_section: "3.14"
---

Introduce the basis-transformation matrices

$$A = (\alpha_v^\lambda), \quad B = (\beta_\mu^\kappa)$$

with inverses $\check{A} = (\check{\alpha}_v^\lambda)$ and $\check{B} = (\check{\beta}_\mu^\kappa)$ satisfying

$$\bar{x}_v = \sum_\lambda \alpha_v^\lambda x_\lambda, \quad x_\lambda = \sum_\nu \check{\alpha}_\lambda^\nu \bar{x}_\nu,$$
$$\bar{y}_\mu = \sum_\kappa \beta_\mu^\kappa y_\kappa, \quad y_\mu = \sum_\kappa \check{\beta}_\mu^\kappa \bar{y}_\kappa.$$

Now compute $\varphi \bar{x}_v$ using the matrix of $\varphi$ relative to the original bases:

$$\varphi \bar{x}_v = \sum_\lambda \alpha_v^\lambda \varphi x_\lambda = \sum_{\lambda, \mu} \alpha_v^\lambda \gamma_\lambda^\mu y_\mu.$$

Expressing $y_\mu$ in terms of the new basis $\bar{y}_\kappa$:

$$y_\mu = \sum_\kappa \check{\beta}_\mu^\kappa \bar{y}_\kappa.$$

Substituting:

$$\varphi \bar{x}_v = \sum_{\lambda, \mu, \kappa} \alpha_v^\lambda \gamma_\lambda^\mu \check{\beta}_\mu^\kappa \bar{y}_\kappa.$$

By definition, $\varphi \bar{x}_v = \sum_\kappa \bar{\gamma}_v^\kappa \bar{y}_\kappa$. Comparing coefficients of $\bar{y}_\kappa$ yields

$$\bar{\gamma}_v^\kappa = \sum_{\lambda, \mu} \check{\beta}_\mu^\kappa \, \gamma_\lambda^\mu \, \alpha_v^\lambda.$$

In matrix notation this reads $\bar{\Gamma} = \check{B}^T \, \Gamma \, A^T$.
