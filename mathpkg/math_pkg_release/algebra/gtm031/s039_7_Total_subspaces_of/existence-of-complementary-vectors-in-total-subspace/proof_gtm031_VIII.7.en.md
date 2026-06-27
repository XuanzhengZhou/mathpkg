---
role: proof
locale: en
of_concept: existence-of-complementary-vectors-in-total-subspace
source_book: gtm031
source_chapter: "Chapter VIII: The Ring of Linear Transformations"
source_section: "7. Total subspaces of R*"
---
**Proof.** If $m = 1$, we can find $f \in \mathfrak{R}'$ with $f(x_1) = \beta_1 \neq 0$. Then $x_1^* = f\beta_1^{-1}$ satisfies $x_1^*(x_1) = 1$.

Assume the result for $m-1$ vectors. Find $f_1, \ldots, f_{m-1}$ in $\mathfrak{R}'$ with $f_k(x_l) = \delta_{kl}$ for $k, l = 1, \ldots, m-1$. For any $f \in \mathfrak{R}'$ define

$$g(x) = f(x) - \sum_{k=1}^{m-1} f_k(x)f(x_k).$$

Then $g \in \mathfrak{R}'$ and $g(x_l) = 0$ for $l < m$. There exists $f$ such that $g(x_m) \neq 0$; otherwise for all $f$,
$$0 = g(x_m) = f(x_m) - \sum_{k=1}^{m-1} f_k(x_m)f(x_k),$$
contradicting totality. Let $g(x_m) = \gamma \neq 0$. Set $x_m^* = g\gamma^{-1}$. Then $x_m^*(x_m) = 1$ and $x_m^*(x_l) = 0$ for $l < m$. For $k < m$ set
$$x_k^* = f_k - f_k(x_m)x_m^*.$$
Then $x_i^*(x_j) = \delta_{ij}$ for all $i, j$, completing the induction.
