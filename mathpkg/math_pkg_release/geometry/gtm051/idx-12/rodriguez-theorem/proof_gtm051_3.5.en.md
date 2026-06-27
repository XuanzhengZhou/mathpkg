---
role: proof
locale: en
of_concept: rodriguez-theorem
source_book: gtm051
source_chapter: "3"
source_section: "3.5"
---

Suppose $\kappa$ is a principal curvature with associated principal direction $X_0$, $I(X_0, X_0) = 1$. Using the Lagrange multiplier rule, we may assert that $d(II - \kappa I) = 0$ at $X_0$, $I(X_0, X_0) = 1$. Since $II$ and $I$ are both quadratic forms and since the differential of any quadratic form $\beta$ at a point $X$ is given by $d\beta Y = 2\beta(X, Y)$, the above requirement is equivalent to

$$II(X_0, Y) - \kappa I(X_0, Y) = 0, \quad I(X_0, X_0) = 1, \quad \text{for all } Y,$$

which in turn is equivalent to

$$L_u X_0 = \kappa X_0, \quad I(X_0, X_0) = 1, \quad \kappa = II(X_0, X_0) = \kappa(X_0).$$

Therefore $X_0$ is an eigenvector of $L_u$ with eigenvalue equal to the principal curvature.
