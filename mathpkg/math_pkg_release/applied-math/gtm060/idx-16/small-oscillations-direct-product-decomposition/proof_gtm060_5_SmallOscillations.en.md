---
role: proof
locale: en
of_concept: small-oscillations-direct-product-decomposition
source_book: gtm060
source_chapter: "5"
source_section: "Small Oscillations"
---

From linear algebra, a pair of quadratic forms $(Aq, q)$ and $(Bq, q)$ with $A$ positive-definite can be simultaneously reduced to principal axes by a linear change of coordinates $Q = Cq$. Moreover, the coordinates $Q$ can be chosen so that the form $(Aq, q)$ decomposes into the sum of squares $(Q, Q) = \sum Q_i^2$. In such coordinates, since $\dot{Q} = C\dot{q}$, we obtain

$$T = \frac{1}{2} \sum_{i=1}^{n} \dot{Q}_i^2, \quad U = \frac{1}{2} \sum_{i=1}^{n} \lambda_i Q_i^2.$$

The numbers $\lambda_i$ are the eigenvalues of $B$ with respect to $A$, satisfying $\det|B - \lambda A| = 0$. All roots are real because $A$ and $B$ are symmetric. Lagrange's equations in the $Q$ coordinates become $\ddot{Q}_i = -\lambda_i Q_i$ for each $i$, which are $n$ uncoupled one-dimensional equations. Solving each yields the three cases stated. $\square$
