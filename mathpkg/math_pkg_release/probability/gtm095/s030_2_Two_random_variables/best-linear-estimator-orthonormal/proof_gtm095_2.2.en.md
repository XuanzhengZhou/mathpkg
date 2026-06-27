---
role: proof
locale: en
of_concept: best-linear-estimator-orthonormal
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Best Mean-Square Linear Estimator for an Orthonormal System

Let $M = \{\eta_1, \ldots, \eta_n\}$ be an orthonormal system and $\xi$ any random variable in $L^2$. We seek the best mean-square estimator for $\xi$ in the class of linear estimators $\sum_{i=1}^{n} a_i \eta_i$.

A simple computation shows that

$$\begin{aligned}
E \left| \xi - \sum_{i=1}^{n} a_i \eta_i \right|^2 &\equiv \left\| \xi - \sum_{i=1}^{n} a_i \eta_i \right\|^2 \\
&= \left( \xi - \sum_{i=1}^{n} a_i \eta_i, \xi - \sum_{i=1}^{n} a_i \eta_i \right) \\
&= (\xi, \xi) - 2\sum_{i=1}^{n} a_i (\xi, \eta_i) + \sum_{i=1}^{n} \sum_{j=1}^{n} a_i a_j (\eta_i, \eta_j) \\
&= \|\xi\|^2 - 2\sum_{i=1}^{n} a_i (\xi, \eta_i) + \sum_{i=1}^{n} a_i^2 \\
&= \|\xi\|^2 - \sum_{i=1}^{n} |(\xi, \eta_i)|^2 + \sum_{i=1}^{n} \left( a_i - (\xi, \eta_i) \right)^2,
\end{aligned}$$

where we have used the orthonormality condition $(\eta_i, \eta_j) = \delta_{ij}$.

The first two terms do not depend on the coefficients $a_i$, and the third term is a sum of squares, which is minimized when each square is zero, i.e., when

$$a_i = (\xi, \eta_i), \quad i = 1, \ldots, n.$$

Consequently the best (in the mean-square sense) linear estimator for $\xi$ in terms of $\eta_1, \ldots, \eta_n$ is

$$\hat{\xi} = \sum_{i=1}^{n} (\xi, \eta_i) \eta_i.$$

Here

$$\Delta = \inf E \left| \xi - \sum_{i=1}^{n} a_i \eta_i \right|^2 = E |\xi - \hat{\xi}|^2 = \|\xi\|^2 - \sum_{i=1}^{n} |(\xi, \eta_i)|^2,$$

which follows immediately from the expansion above.
